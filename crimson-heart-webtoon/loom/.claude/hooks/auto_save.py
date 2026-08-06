#!/usr/bin/env python3
"""
Auto-save hook - saves state after every file modification.
Event: PostToolUse (matches Write|Edit)
Mode: Async (non-blocking)
"""
import json
import sys
from datetime import datetime
from pathlib import Path

# Import from state_manager (same directory)
hooks_dir = Path(__file__).resolve().parent
sys.path.insert(0, str(hooks_dir))

try:
    from state_manager import read_state, save_with_retry
except ImportError as e:
    # If import fails, hook should still not block
    print(f"Auto-save: Could not import state_manager: {e}", file=sys.stderr)
    sys.exit(0)


def main() -> int:
    """Main hook function. Returns exit code."""
    try:
        # Read PostToolUse input from stdin
        input_data = json.load(sys.stdin)

        # Extract tool info (available but we don't filter - matcher does that)
        tool_name = input_data.get('tool_name', 'Unknown')

        # Read current session state
        session = read_state('session.json')

        # Update last_saved timestamp
        session['last_saved'] = datetime.now().isoformat()

        # If there's an active project, mark it was saved
        if session.get('active_project'):
            session['unsaved_changes'] = False

        # Save with retry (handles atomic write + backup rotation)
        success, error = save_with_retry('session.json', session)

        if not success:
            # Return systemMessage for async hook output
            # This will appear on the NEXT conversation turn
            print(json.dumps({
                "systemMessage": f"[Auto-save failed: {error}]"
            }))

        return 0  # Always exit 0 for async hooks

    except json.JSONDecodeError:
        # No input or invalid input - just exit cleanly
        return 0
    except Exception as e:
        print(f"Auto-save hook error: {e}", file=sys.stderr)
        return 0  # Don't block on error


if __name__ == '__main__':
    sys.exit(main())
