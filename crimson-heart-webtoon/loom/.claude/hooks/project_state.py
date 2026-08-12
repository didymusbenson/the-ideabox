#!/usr/bin/env python3
"""
Project State - Per-project state operations for book projects.

This module provides state management for individual book projects,
keeping each project's continuity state isolated in its own .state/ folder.

Usage:
    from project_state import find_project, read_project_state, write_project_state

Functions:
    get_project_state_dir(project_path) - Get/create .state/ folder for project
    read_project_state(project_path) - Read project.json for a project
    write_project_state(project_path, data) - Write project.json atomically
    initialize_project_state(project_path) - Create initial state for project
    find_project(identifier) - Find project by partial name match

Constants:
    BOOKS_DIR - Path to book projects directory (_books/ under project root)
"""
import json
import os
import sys
import tempfile
from datetime import datetime
from pathlib import Path

# Import rotate_backups from state_manager for backup rotation
hooks_dir = Path(__file__).resolve().parent
sys.path.insert(0, str(hooks_dir))
from state_manager import rotate_backups, BOOKS_DIR
from character_manager import create_characters_folder


def get_project_state_dir(project_path: Path) -> Path:
    """
    Get the state directory for a specific project, creating if needed.

    State lives INSIDE the project folder at .state/ for portability.
    Also creates .state/backups/ subfolder for backup rotation.

    Args:
        project_path: Path to the book project directory

    Returns:
        Path: Absolute path to project's .state/ directory
    """
    state_dir = project_path / '.state'
    state_dir.mkdir(parents=True, exist_ok=True)

    # Create backups subfolder
    backup_dir = state_dir / 'backups'
    backup_dir.mkdir(parents=True, exist_ok=True)

    return state_dir


def read_project_state(project_path: Path) -> dict:
    """
    Read project.json for a specific project.

    Args:
        project_path: Path to the book project directory

    Returns:
        dict: Parsed JSON content, or empty dict if not found or invalid
    """
    try:
        state_file = get_project_state_dir(project_path) / 'project.json'
        if state_file.exists():
            return json.loads(state_file.read_text(encoding='utf-8'))
        return {}
    except json.JSONDecodeError as e:
        print(f"Path issue: project.json contains invalid JSON: {e}. "
              f"Try: Delete the file or fix the JSON syntax.",
              file=sys.stderr)
        return {}
    except PermissionError as e:
        print(f"Path issue: Cannot read project.json: {e}. "
              f"Try: Check if file is locked by another program.",
              file=sys.stderr)
        return {}
    except Exception as e:
        print(f"Path issue: Error reading project.json: {e}",
              file=sys.stderr)
        return {}


def _rotate_project_backups(project_path: Path, filename: str = 'project.json', max_backups: int = 3) -> None:
    """
    Rotate backup files for a project's state file.

    Naming pattern: {filename}.1 (newest) to {filename}.{max_backups} (oldest)

    Args:
        project_path: Path to the book project directory
        filename: Name of state file (default 'project.json')
        max_backups: Maximum number of backups to keep (default 3)
    """
    state_dir = get_project_state_dir(project_path)
    backup_dir = state_dir / 'backups'
    current_file = state_dir / filename

    # Skip rotation if current file doesn't exist
    if not current_file.exists():
        return

    try:
        import shutil

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
              f"Try: Check permissions on .state/backups/ folder.",
              file=sys.stderr)


def write_project_state(project_path: Path, data: dict) -> bool:
    """
    Write project.json atomically with backup rotation.

    Uses temp file + os.replace pattern for crash safety.
    Creates a backup of the current file before overwriting.

    Args:
        project_path: Path to the book project directory
        data: Dictionary to serialize as JSON

    Returns:
        bool: True on success, False on failure
    """
    state_dir = get_project_state_dir(project_path)
    state_file = state_dir / 'project.json'
    temp_path = None
    fd = None

    try:
        # Rotate backups before writing (preserves current state)
        _rotate_project_backups(project_path)

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
        print(f"Path issue: Atomic write failed for project.json: {e}. "
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


def initialize_project_state(project_path: Path) -> dict:
    """
    Initialize state for a book project.

    Creates .state/ folder and project.json if they don't exist.
    Scans project for existing tracking files to populate initial state.

    Args:
        project_path: Path to the book project directory

    Returns:
        dict: The project state (existing or newly created)
    """
    state_dir = get_project_state_dir(project_path)
    state_file = state_dir / 'project.json'

    # If state already exists, return it
    if state_file.exists():
        return read_project_state(project_path)

    # Scan for existing content to populate initial state
    last_scene = None
    last_scene_file = None

    # Check for SCENES/ or scenes/ folder
    scenes_dir = project_path / 'SCENES'
    if not scenes_dir.exists():
        scenes_dir = project_path / 'scenes'

    if scenes_dir.exists():
        # Get scene files sorted by name (most recent is typically last)
        scenes = sorted(scenes_dir.glob('*.md'))
        if scenes:
            last_scene = scenes[-1].stem  # Most recent by name sort
            last_scene_file = f'SCENES/{scenes[-1].name}'

    # Check for character folder
    has_characters = (project_path / 'CHARACTERS').exists() or (project_path / 'characters').exists()

    # Check for tracking files
    has_relationship_tracker = (project_path / 'relationship_tracker.md').exists()
    has_scene_log = (project_path / 'scene_log.md').exists()
    has_observations = (project_path / 'observations.md').exists()

    # Create characters/ folder with empty manifest if not already present
    create_characters_folder(project_path)

    # Create initial state
    initial_state = {
        'project_name': project_path.name,
        'display_name': project_path.name.replace('-', ' ').replace('_', ' ').title(),
        'last_position': {
            'chapter': None,
            'scene': last_scene,
            'scene_file': last_scene_file,
            'section': None
        },
        'open_threads': [],
        'character_focus': [],
        'current_arc': None,
        'session_history': [],
        'last_edited': datetime.now().isoformat(),
        'total_sessions': 0
    }

    # Write initial state
    write_project_state(project_path, initial_state)

    return initial_state


def find_project(identifier: str) -> Path | None:
    """
    Find project by name, supporting fuzzy matching.

    Matching priority:
    1. Exact match (case-insensitive, normalizes spaces/underscores to hyphens)
    2. Starts-with match
    3. Contains match (only if single match)

    Skips directories starting with '.' or '_'.

    Args:
        identifier: Full or partial project name

    Returns:
        Path: Path to found project, or None if not found or ambiguous
    """
    # Normalize identifier: lowercase, spaces/underscores to hyphens
    identifier_normalized = identifier.lower().replace(' ', '-').replace('_', '-')

    # Get all project directories (skip hidden and underscore-prefixed)
    projects = [
        p for p in BOOKS_DIR.iterdir()
        if p.is_dir() and not p.name.startswith('.') and not p.name.startswith('_')
    ]

    # Priority 1: Exact match (case-insensitive)
    for p in projects:
        if p.name.lower() == identifier_normalized:
            return p

    # Priority 2: Starts-with match
    for p in projects:
        if p.name.lower().startswith(identifier_normalized):
            return p

    # Priority 3: Contains match (only if single match)
    matches = [p for p in projects if identifier_normalized in p.name.lower()]
    if len(matches) == 1:
        return matches[0]

    # Ambiguous or not found
    return None


# Allow running as script for testing
if __name__ == '__main__':
    print(f"BOOKS_DIR: {BOOKS_DIR}")

    # Test find_project
    test_ids = ['halcyon', 'fire', 'nonexistent', 'verge']
    for test_id in test_ids:
        result = find_project(test_id)
        print(f"find_project('{test_id}'): {result}")
