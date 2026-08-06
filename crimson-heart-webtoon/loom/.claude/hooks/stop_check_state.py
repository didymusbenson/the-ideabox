#!/usr/bin/env python3
"""
Stop Hook: Check if roleplay state needs saving before session ends.

Fires on Stop event. Checks session.json for:
1. Active session (started_at is set)
2. Unsaved changes (unsaved_changes flag is true)

If state needs saving, outputs instruction for Claude to fire save workflow.
Uses state_manager.py for all state operations (pathlib-based).
"""
import json
import sys
from pathlib import Path

# Add hooks directory to path for local imports
hooks_dir = Path(__file__).resolve().parent
if str(hooks_dir) not in sys.path:
    sys.path.insert(0, str(hooks_dir))

# Import from state_manager for state operations
try:
    from state_manager import get_state_dir, read_state, get_project_root
except ImportError as e:
    print(f"Hook error: Cannot import state_manager: {e}", file=sys.stderr)
    # Define minimal fallbacks
    def get_state_dir():
        return Path(__file__).resolve().parent.parent.parent / ".writing" / "state"
    def read_state(filename):
        return {}
    def get_project_root():
        return Path(__file__).resolve().parent.parent.parent


def check_state_needs_saving() -> tuple[bool, str]:
    """
    Check if state needs saving based on session.json.

    Returns:
        tuple: (needs_save: bool, reason: str)
    """
    try:
        session = read_state("session.json")

        # Check for unsaved changes flag
        if session.get("unsaved_changes", False):
            return True, "Unsaved changes flagged in session"

        # Check if there's an active session that might have content
        if session.get("started_at") and session.get("active_project"):
            # Active session exists - might need saving
            mode = session.get("mode", "unknown")
            return True, f"Active {mode} session detected"

        return False, "No active session or unsaved changes"

    except Exception as e:
        print(f"Hook error checking state: {e}", file=sys.stderr)
        return False, f"Error checking state: {e}"


def get_project_name() -> str:
    """
    Get the project name from project root directory.

    Returns:
        str: Project directory name
    """
    try:
        project_root = get_project_root()
        return project_root.name
    except Exception:
        return "Unknown project"


def main():
    """
    Main hook function - checks state and outputs reminder if needed.

    Reads JSON from stdin (Claude Code input), outputs save reminder if needed.
    Always exits 0 (never blocks).
    """
    try:
        # Read Stop event data from stdin
        try:
            input_data = json.load(sys.stdin)
        except (json.JSONDecodeError, EOFError):
            input_data = {}

        # Check if state needs saving
        needs_save, reason = check_state_needs_saving()

        if needs_save:
            project = get_project_name()

            print()
            print("=" * 60)
            print("ROLEPLAY STATE CHECK - ACTION REQUIRED")
            print("=" * 60)
            print()
            print(f"Project: {project}")
            print(f"Reason: {reason}")
            print()
            print("You MUST run the save-scene workflow now:")
            print()
            print("1. Run /save-scene to persist state")
            print("   - Updates relationship_tracker.md")
            print("   - Updates observations.md")
            print("   - Appends to scene file")
            print("   - Clears unsaved_changes flag")
            print()
            print("=" * 60)

    except Exception as e:
        # Log error but don't block
        print(f"Stop hook error: {e}", file=sys.stderr)

    sys.exit(0)


if __name__ == '__main__':
    main()
