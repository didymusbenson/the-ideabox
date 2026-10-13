#!/usr/bin/env python3
"""
Auto-resume hook - restores state when session starts.
Event: SessionStart
Output: Context message for Claude about resumed state
"""
import json
import sys
from datetime import datetime
from pathlib import Path

# Import from state_manager (same directory)
hooks_dir = Path(__file__).resolve().parent
sys.path.insert(0, str(hooks_dir))

try:
    from state_manager import read_state_with_recovery, get_project_root
except ImportError as e:
    print(f"Auto-resume: Could not import state_manager: {e}", file=sys.stderr)
    sys.exit(0)


def format_time_ago(iso_timestamp: str) -> str:
    """Format timestamp as human-readable 'X ago' string."""
    try:
        last_dt = datetime.fromisoformat(iso_timestamp)
        delta = datetime.now() - last_dt

        if delta.days > 0:
            return f"{delta.days} day{'s' if delta.days > 1 else ''} ago"
        elif delta.seconds > 3600:
            hours = delta.seconds // 3600
            return f"{hours} hour{'s' if hours > 1 else ''} ago"
        elif delta.seconds > 60:
            minutes = delta.seconds // 60
            return f"{minutes} minute{'s' if minutes > 1 else ''} ago"
        else:
            return "just now"
    except (ValueError, TypeError):
        return "unknown time"


def _report_character_sheets():
    """Detect and report character sheet locations for current session/project."""
    try:
        project_root = get_project_root()

        # Check for characters/ folders in common locations
        locations = []

        # Direct characters/ at project root (book projects)
        chars_root = project_root / 'characters'
        if chars_root.exists():
            manifest = chars_root / '_cast_manifest.json'
            if manifest.exists():
                data = json.loads(manifest.read_text(encoding='utf-8'))
                count = len(data.get('characters', {}))
                locations.append((str(chars_root), count))

        # Check _sessions/ for active session characters
        sessions_dir = project_root / '_sessions'
        if sessions_dir.exists():
            for genre_dir in sessions_dir.iterdir():
                if not genre_dir.is_dir() or genre_dir.name.startswith('.'):
                    continue
                for session_dir in genre_dir.iterdir():
                    if not session_dir.is_dir():
                        continue
                    # Skip archived sessions (date-prefixed)
                    if session_dir.name[:4].isdigit():
                        continue
                    chars_dir = session_dir / 'characters'
                    if chars_dir.exists():
                        manifest = chars_dir / '_cast_manifest.json'
                        if manifest.exists():
                            data = json.loads(manifest.read_text(encoding='utf-8'))
                            count = len(data.get('characters', {}))
                            if count > 0:
                                locations.append((str(chars_dir), count))

        if locations:
            print()
            print("CHARACTER SHEETS LOADED:")
            for path, count in locations:
                print(f"  {path} ({count} character{'s' if count != 1 else ''})")
            print("  Sheets are GROUND TRUTH  - override conversation memory.")

    except Exception as e:
        # Non-fatal  - don't block session start
        pass


def main() -> int:
    """Main hook function. Returns exit code."""
    try:
        # Read SessionStart input (may be empty object)
        input_data = json.load(sys.stdin)

        # Load session state with recovery
        session, was_recovered = read_state_with_recovery('session.json')

        # Build resume message if there's an active project
        if session.get('active_project'):
            project = session.get('active_project', 'Unknown')
            last_position = session.get('last_position', {})
            chapter = last_position.get('chapter', '') if last_position else ''
            scene = last_position.get('scene', '') if last_position else ''
            last_saved = session.get('last_saved', '')

            # Build position string
            position_parts = []
            if chapter:
                position_parts.append(f"Chapter {chapter}")
            if scene:
                position_parts.append(f"Scene {scene}")
            position_str = ", ".join(position_parts) if position_parts else "start"

            # Build time string
            time_str = format_time_ago(last_saved) if last_saved else "unknown time"

            # Recovery notice if we recovered from backup
            recovery_note = " (recovered from backup)" if was_recovered else ""

            # Output resume context
            print(f"Resuming: {project} - {position_str}, last edit {time_str}{recovery_note}")

        elif was_recovered:
            # No active project but we recovered - note it
            print("Session state recovered from backup. No active project.")

        # If no active project and no recovery, check for first-time setup
        if not session.get('active_project') and not was_recovered:
            try:
                from config import MC_NAME
                if MC_NAME == "MC":
                    print("FIRST TIME SETUP: The user has not configured their character name yet.")
                    print("Ask them: \"What name do you want to use for your main character?\"")
                    print("Then tell them to edit .claude/hooks/config.py and set MC_NAME to their chosen name.")
                    print("Also ask about CHARACTER_POV (who Claude writes as, e.g. 'the NPCs', 'Elena').")
            except ImportError:
                pass

        # Detect character sheets in current context
        _report_character_sheets()

        return 0

    except json.JSONDecodeError:
        # No input - just exit cleanly
        return 0
    except Exception as e:
        print(f"Auto-resume hook error: {e}", file=sys.stderr)
        return 0


if __name__ == '__main__':
    sys.exit(main())
