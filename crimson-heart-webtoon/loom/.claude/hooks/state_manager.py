#!/usr/bin/env python3
"""
State Manager - Centralized state file operations for Writing Hub.

This module provides cross-platform path handling and state management
for all hooks. State is stored in project-local .writing/state/ folder.

Usage:
    from state_manager import read_state, write_state, get_state_dir

Functions:
    get_project_root() - Get project root directory
    get_state_dir() - Get state directory (creates if needed)
    get_backup_dir() - Get backup directory (creates if needed)
    read_state(filename) - Read JSON state file
    write_state(filename, data) - Write JSON state file
    atomic_write_state(filename, data) - Write with atomic replace and backup
    rotate_backups(filename, max_backups) - Rotate backup files
    read_state_with_recovery(filename) - Read with corruption recovery
    save_with_retry(filename, data, max_retries) - Save with retry and backoff
    get_platform() - Detect platform (defaults to Windows)
    migrate_global_state() - Migrate from ~/.claude/ if found

Constants:
    BOOKS_DIR - Path to book projects directory (_books/ under project root)
    SESSIONS_DIR - Path to roleplay sessions directory (_sessions/ under project root)
    CHARACTERS_DIR - Path to character library directory (_characters/ under project root)
"""
import json
import os
import platform
import shutil
import sys
import tempfile
import time
from datetime import datetime
from pathlib import Path


def _get_root():
    """Internal helper to get project root before get_project_root is defined."""
    try:
        return Path(__file__).resolve().parent.parent.parent
    except Exception:
        return Path.cwd()


# All content directories are relative to project root
BOOKS_DIR = _get_root() / '_books'
SESSIONS_DIR = _get_root() / '_sessions'
CHARACTERS_DIR = _get_root() / '_characters'


def get_project_root() -> Path:
    """
    Get the project root directory.

    Navigates from hook location (.claude/hooks/) up to project root.
    Uses Path(__file__).resolve() for reliable cross-platform resolution.

    Returns:
        Path: Absolute path to project root directory.
    """
    try:
        hook_dir = Path(__file__).resolve().parent
        # Hook is at: project/.claude/hooks/state_manager.py
        # Project root is 2 levels up: .claude/hooks -> .claude -> project
        project_root = hook_dir.parent.parent
        return project_root
    except Exception as e:
        print(f"Path issue: Cannot determine project root from {__file__}. "
              f"Try: Ensure state_manager.py is in .claude/hooks/ folder.",
              file=sys.stderr)
        # Return current directory as fallback
        return Path.cwd()


def get_state_dir() -> Path:
    """
    Get the project-local state directory, creating if needed.

    State is stored in {project_root}/.writing/state/ to keep it
    portable and visible (not hidden in user home directory).

    Returns:
        Path: Absolute path to state directory.
    """
    try:
        project_root = get_project_root()
        state_dir = project_root / ".writing" / "state"
        state_dir.mkdir(parents=True, exist_ok=True)
        return state_dir
    except PermissionError as e:
        print(f"Path issue: Cannot create .writing/state/ directory. "
              f"Try: Check folder permissions or run as administrator.",
              file=sys.stderr)
        return Path.cwd() / ".writing" / "state"
    except Exception as e:
        print(f"Path issue: {e}. Try: Delete .writing/state/ and restart.",
              file=sys.stderr)
        return Path.cwd() / ".writing" / "state"


def read_state(filename: str) -> dict:
    """
    Read a JSON state file, returning empty dict if not found or on error.

    Args:
        filename: Name of state file (e.g., 'session.json')

    Returns:
        dict: Parsed JSON content, or empty dict on any error.
    """
    try:
        state_file = get_state_dir() / filename
        if state_file.exists():
            return json.loads(state_file.read_text(encoding='utf-8'))
        return {}
    except json.JSONDecodeError as e:
        print(f"Path issue: {filename} contains invalid JSON. "
              f"Try: Delete the file or fix the JSON syntax.",
              file=sys.stderr)
        return {}
    except PermissionError as e:
        print(f"Path issue: Cannot read {filename}. "
              f"Try: Check if file is locked by another program.",
              file=sys.stderr)
        return {}
    except Exception as e:
        print(f"Path issue: Error reading {filename}: {e}. "
              f"Try: Delete .writing/state/{filename} and restart.",
              file=sys.stderr)
        return {}


def write_state(filename: str, data: dict) -> None:
    """
    Write data to a JSON state file with proper formatting.

    Creates parent directories if needed. Uses indent=2 for readability.
    Always specifies UTF-8 encoding for Windows compatibility.

    Args:
        filename: Name of state file (e.g., 'session.json')
        data: Dictionary to serialize as JSON
    """
    try:
        state_file = get_state_dir() / filename
        state_file.write_text(
            json.dumps(data, indent=2, ensure_ascii=False),
            encoding='utf-8'
        )
    except PermissionError as e:
        print(f"Path issue: Cannot write to {filename}. "
              f"Try: Check if file is locked or folder is read-only.",
              file=sys.stderr)
    except TypeError as e:
        print(f"Path issue: Data for {filename} is not JSON-serializable. "
              f"Try: Ensure all values are strings, numbers, lists, or dicts.",
              file=sys.stderr)
    except Exception as e:
        print(f"Path issue: Error writing {filename}: {e}. "
              f"Try: Check disk space and folder permissions.",
              file=sys.stderr)


def get_backup_dir() -> Path:
    """
    Get the backup directory for state files, creating if needed.

    Backups are stored in {state_dir}/backups/ to keep them
    separate from active state files.

    Returns:
        Path: Absolute path to backup directory.
    """
    backup_dir = get_state_dir() / "backups"
    backup_dir.mkdir(parents=True, exist_ok=True)
    return backup_dir


def rotate_backups(filename: str, max_backups: int = 3) -> None:
    """
    Rotate backup files, keeping up to max_backups versions.

    Naming pattern: {filename}.1 (newest) to {filename}.{max_backups} (oldest)
    Before rotation: current -> .1, .1 -> .2, .2 -> .3, .3 deleted

    Args:
        filename: Name of state file (e.g., 'session.json')
        max_backups: Maximum number of backups to keep (default 3)
    """
    state_dir = get_state_dir()
    backup_dir = get_backup_dir()
    current_file = state_dir / filename

    # Skip rotation if current file doesn't exist
    if not current_file.exists():
        return

    try:
        # Delete oldest backup if exists
        oldest_backup = backup_dir / f"{filename}.{max_backups}"
        if oldest_backup.exists():
            oldest_backup.unlink()

        # Shift backups up: .2 -> .3, .1 -> .2
        for i in range(max_backups - 1, 0, -1):
            older = backup_dir / f"{filename}.{i}"
            newer = backup_dir / f"{filename}.{i + 1}"
            if older.exists():
                shutil.move(str(older), str(newer))

        # Copy current to .1
        newest_backup = backup_dir / f"{filename}.1"
        shutil.copy2(str(current_file), str(newest_backup))

    except Exception as e:
        print(f"Path issue: Backup rotation failed for {filename}: {e}. "
              f"Try: Check permissions on .writing/state/backups/ folder.",
              file=sys.stderr)


def atomic_write_state(filename: str, data: dict) -> bool:
    """
    Write state atomically with backup rotation.

    Uses temp file + os.replace pattern for crash safety.
    Creates a backup of the current file before overwriting.

    Args:
        filename: Name of state file (e.g., 'session.json')
        data: Dictionary to serialize as JSON

    Returns:
        bool: True on success, False on failure
    """
    state_dir = get_state_dir()
    state_file = state_dir / filename
    temp_path = None
    fd = None

    try:
        # Rotate backups before writing (preserves current state)
        rotate_backups(filename)

        # Create temp file in same directory for atomic replace
        fd, temp_path_str = tempfile.mkstemp(
            dir=str(state_dir),
            prefix='.tmp_',
            suffix='.json'
        )
        temp_path = Path(temp_path_str)

        # Write JSON to temp file
        with os.fdopen(fd, 'w', encoding='utf-8') as f:
            fd = None  # fdopen takes ownership of fd
            json.dump(data, f, indent=2, ensure_ascii=False)
            f.flush()
            os.fsync(f.fileno())

        # Atomically replace current file with temp file
        os.replace(str(temp_path), str(state_file))
        return True

    except Exception as e:
        print(f"Path issue: Atomic write failed for {filename}: {e}. "
              f"Try: Check disk space and folder permissions.",
              file=sys.stderr)
        return False

    finally:
        # Clean up temp file on failure
        if temp_path and temp_path.exists():
            try:
                temp_path.unlink()
            except Exception:
                pass
        # Close fd if fdopen didn't take ownership
        if fd is not None:
            try:
                os.close(fd)
            except Exception:
                pass


def read_state_with_recovery(filename: str) -> tuple:
    """
    Read state file with automatic corruption recovery from backups.

    Tries current file first, then backups in order (.1, .2, .3).
    Restores first valid backup as current file if recovery needed.

    Args:
        filename: Name of state file (e.g., 'session.json')

    Returns:
        tuple: (state_dict, was_recovered)
            - state_dict: Parsed JSON content, or empty dict if all failed
            - was_recovered: True if recovery from backup was needed
    """
    state_dir = get_state_dir()
    backup_dir = get_backup_dir()
    state_file = state_dir / filename

    # Try current file first
    try:
        if state_file.exists():
            content = state_file.read_text(encoding='utf-8')
            data = json.loads(content)
            return (data, False)  # No recovery needed
        else:
            # File doesn't exist — fresh start, not an error
            return ({}, False)
    except (json.JSONDecodeError, PermissionError) as e:
        print(f"Path issue: {filename} is corrupted or locked, attempting recovery...",
              file=sys.stderr)
    except FileNotFoundError:
        return ({}, False)  # File doesn't exist — fresh start

    # Try backups in order (only reached if current file was corrupted)
    for i in range(1, 4):  # .1, .2, .3
        backup_file = backup_dir / f"{filename}.{i}"
        try:
            if backup_file.exists():
                content = backup_file.read_text(encoding='utf-8')
                data = json.loads(content)

                # Valid backup found - restore it as current file
                try:
                    state_file.write_text(content, encoding='utf-8')
                    print(f"Recovered {filename} from backup .{i}",
                          file=sys.stderr)
                except Exception as restore_err:
                    print(f"Path issue: Could not restore backup: {restore_err}",
                          file=sys.stderr)

                return (data, True)  # Recovery successful
        except (json.JSONDecodeError, PermissionError, FileNotFoundError):
            continue  # Try next backup

    # All recovery attempts failed — corrupted with no valid backups
    print(f"Path issue: No valid state found for {filename}. Starting fresh.",
          file=sys.stderr)
    return ({}, True)


def save_with_retry(filename: str, data: dict, max_retries: int = 3) -> tuple:
    """
    Save state with retry and exponential backoff.

    Wraps atomic_write_state with retry logic for transient failures
    like file locks or permission issues.

    Args:
        filename: Name of state file (e.g., 'session.json')
        data: Dictionary to serialize as JSON
        max_retries: Maximum number of attempts (default 3)

    Returns:
        tuple: (success, error_message)
            - success: True if save succeeded
            - error_message: Error string if failed, None if succeeded
    """
    last_error = None

    for attempt in range(max_retries):
        try:
            if atomic_write_state(filename, data):
                return (True, None)
            else:
                last_error = "atomic_write_state returned False"
        except Exception as e:
            last_error = str(e)

        # Exponential backoff: 0.1s, 0.2s, 0.4s
        if attempt < max_retries - 1:
            delay = 0.1 * (2 ** attempt)
            time.sleep(delay)

    return (False, last_error)


def get_platform() -> str:
    """
    Detect the current platform, defaulting to Windows on any failure.

    Per user decision: assume Windows if detection fails, since user
    is on Windows and this is the safe default.

    Returns:
        str: 'Windows', 'Linux', or 'Darwin' (macOS)
    """
    try:
        system = platform.system()
        if system in ('Windows', 'Linux', 'Darwin'):
            return system
        # Unknown platform - default to Windows per user decision
        return 'Windows'
    except Exception:
        return 'Windows'


def migrate_global_state() -> bool:
    """
    Migrate state from global ~/.claude/ to project-local .writing/state/.

    Checks for old global state files and migrates them to the new
    project-local location. Only migrates if destination doesn't exist.

    Returns:
        bool: True if any migration occurred, False otherwise.
    """
    migrated = False

    try:
        global_dir = Path.home() / ".claude"
        local_dir = get_state_dir()

        # Mapping of old files to new files
        # Format: (old_name, new_name, transform_function or None)
        migrate_map = [
            ("roleplay_session_active", "session.json", _transform_session_marker),
            ("roleplay_dirty", None, None),  # Just note it existed, don't migrate
        ]

        for old_name, new_name, transform in migrate_map:
            old_file = global_dir / old_name
            if old_file.exists():
                if new_name and transform:
                    new_file = local_dir / new_name
                    if not new_file.exists():
                        # Transform and write new format
                        new_data = transform(old_file)
                        write_state(new_name, new_data)
                        migrated = True
                        print(f"Migrated: {old_file} -> {new_file}", file=sys.stderr)

                # Clean up old file (optional - leave for now for safety)
                # old_file.unlink()

    except Exception as e:
        print(f"Path issue: Migration check failed: {e}. "
              f"Try: Manually check ~/.claude/ for old state files.",
              file=sys.stderr)

    return migrated


def _transform_session_marker(old_file: Path) -> dict:
    """
    Transform old session marker file to new session.json format.

    Old format: Empty marker file (existence = session active)
    New format: JSON with session details

    Args:
        old_file: Path to old roleplay_session_active file

    Returns:
        dict: New session.json structure
    """
    return {
        "active_project": None,
        "mode": None,
        "last_position": None,
        "started_at": datetime.now().isoformat(),
        "_migrated_from": str(old_file),
        "_migrated_at": datetime.now().isoformat()
    }


# Allow running as script for testing
if __name__ == '__main__':
    # When run directly, just verify module loads and print state dir
    print(f"Platform: {get_platform()}")
    print(f"Project root: {get_project_root()}")
    print(f"State dir: {get_state_dir()}")
