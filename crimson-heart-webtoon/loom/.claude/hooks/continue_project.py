#!/usr/bin/env python3
"""
Continue project command - loads book project state for resumption.

Usage: python continue_project.py <project-identifier>
Output: Resume context message for Claude

This command:
1. Finds project by partial name match
2. Loads or initializes project state
3. Updates hub session.json with active project
4. Outputs context for Claude to resume writing
"""
import json
import sys
from datetime import datetime
from pathlib import Path

# Import from local hooks directory
hooks_dir = Path(__file__).resolve().parent
sys.path.insert(0, str(hooks_dir))

from project_state import find_project, initialize_project_state, read_project_state, BOOKS_DIR
from state_manager import atomic_write_state, get_state_dir


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


def update_hub_session(project_path: Path) -> None:
    """
    Update hub session.json with active project info.

    The hub tracks which project is currently active - state lives
    in .writing/state/session.json at the hub level.

    Args:
        project_path: Path to the book project directory
    """
    session_data = {
        'active_project': project_path.name,
        'project_path': str(project_path),
        'mode': 'book',
        'last_saved': datetime.now().isoformat(),
        'unsaved_changes': False
    }
    atomic_write_state('session.json', session_data)


def build_resume_context(project_path: Path, state: dict) -> str:
    """
    Build human-readable markdown context for Claude to resume writing.

    Args:
        project_path: Path to the book project directory
        state: Project state dictionary

    Returns:
        str: Markdown-formatted resume context
    """
    display_name = state.get('display_name', project_path.name)
    last_position = state.get('last_position', {})
    open_threads = state.get('open_threads', [])
    character_focus = state.get('character_focus', [])
    current_arc = state.get('current_arc')
    session_history = state.get('session_history', [])

    lines = [f"# Resuming: {display_name}", ""]

    # Position info
    scene = last_position.get('scene')
    section = last_position.get('section')
    chapter = last_position.get('chapter')

    if scene:
        lines.append(f"**Last scene:** {scene}")
    if section:
        lines.append(f"**Section:** {section}")
    if chapter:
        lines.append(f"**Chapter:** {chapter}")
    if current_arc:
        lines.append(f"**Arc:** {current_arc}")

    if scene or section or chapter or current_arc:
        lines.append("")

    # Open threads
    active_threads = [t for t in open_threads if t.get('status') in ('active', 'simmering')]
    if active_threads:
        lines.append(f"**Open threads ({len(active_threads)}):**")
        for thread in active_threads[:5]:  # Max 5
            desc = thread.get('description', 'Unknown thread')
            status = thread.get('status', 'active')
            lines.append(f"- {desc} ({status})")
        if len(active_threads) > 5:
            lines.append(f"- ...and {len(active_threads) - 5} more")
        lines.append("")

    # Active characters
    if character_focus:
        lines.append(f"**Active characters:** {', '.join(character_focus)}")
        lines.append("")

    # Last session
    if session_history:
        last_session = session_history[-1]
        started = last_session.get('started')
        if started:
            time_ago = format_time_ago(started)
            lines.append(f"**Last session:** {time_ago}")
            lines.append("")

    # Key project files
    lines.append("**Key project files:**")

    # Always mention CLAUDE.md
    claude_md = project_path / 'CLAUDE.md'
    if claude_md.exists():
        lines.append(f"- {project_path}/CLAUDE.md - Project instructions")
    else:
        lines.append(f"- {project_path}/CLAUDE.md - (not found, consider creating)")

    # Optional tracking files
    tracking_files = [
        ('relationship_tracker.md', 'Character relationships'),
        ('scene_log.md', 'Scene history'),
        ('observations.md', 'Story observations'),
        ('worldbuilding.md', 'World details'),
    ]

    for filename, description in tracking_files:
        filepath = project_path / filename
        if filepath.exists():
            lines.append(f"- {project_path}/{filename} - {description}")

    lines.append("")
    lines.append("Read these files for full context before continuing.")

    return "\n".join(lines)


def continue_project(identifier: str) -> dict:
    """
    Load a book project for continuation.

    Args:
        identifier: Full or partial project name

    Returns:
        dict: Result with project info and context, or error
    """
    # Find project
    project_path = find_project(identifier)

    if not project_path:
        # Get list of available projects
        available = []
        if BOOKS_DIR.exists():
            available = sorted([
                p.name for p in BOOKS_DIR.iterdir()
                if p.is_dir() and not p.name.startswith('.') and not p.name.startswith('_')
            ])

        return {
            'error': f"Project not found: '{identifier}'",
            'available': available
        }

    # Initialize project state (creates if needed)
    state = initialize_project_state(project_path)

    # Update hub session with active project
    update_hub_session(project_path)

    # Build resume context
    context = build_resume_context(project_path, state)

    return {
        'project': project_path.name,
        'path': str(project_path),
        'context': context,
        'state': state
    }


def list_projects() -> list:
    """List all available book projects."""
    if not BOOKS_DIR.exists():
        return []

    return sorted([
        p.name for p in BOOKS_DIR.iterdir()
        if p.is_dir() and not p.name.startswith('.') and not p.name.startswith('_')
    ])


def main() -> int:
    """CLI entry point. Returns exit code."""
    # No argument - list projects
    if len(sys.argv) < 2:
        projects = list_projects()
        if projects:
            print("Available book projects:")
            for p in projects:
                print(f"  - {p}")
            print(f"\nUsage: python continue_project.py <project-name>")
        else:
            print(f"No projects found in {BOOKS_DIR}")
        return 0

    # Get identifier from arguments
    identifier = ' '.join(sys.argv[1:])

    # Continue project
    result = continue_project(identifier)

    if 'error' in result:
        print(f"Error: {result['error']}", file=sys.stderr)
        if result.get('available'):
            print("\nAvailable projects:", file=sys.stderr)
            for p in result['available']:
                print(f"  - {p}", file=sys.stderr)
        return 1

    # Success - output context for Claude
    print(result['context'])
    return 0


if __name__ == '__main__':
    sys.exit(main())
