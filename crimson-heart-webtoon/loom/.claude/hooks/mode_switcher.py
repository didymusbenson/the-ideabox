#!/usr/bin/env python3
"""
Mode Switcher - Hub-level mode transition management.

This module enables clean switching between quick sessions and book projects
without session restarts. It's the core Python module for hub-entry routing.

Usage:
    from mode_switcher import detect_intent, switch_mode, get_hub_context, validate_hub_state

Functions:
    get_known_projects() - Get list of project directory names
    detect_intent(user_input) - Determine quick vs book intent from natural language
    switch_mode(new_mode, target) - Clean mode transition with state management
    get_hub_context() - Current hub state summary for routing decisions
    validate_hub_state() - Check hub state integrity
"""
import json
import re
import sys
from datetime import datetime
from pathlib import Path

# Add hooks directory to path for local imports
hooks_dir = Path(__file__).resolve().parent
if str(hooks_dir) not in sys.path:
    sys.path.insert(0, str(hooks_dir))

from state_manager import read_state, atomic_write_state, BOOKS_DIR, SESSIONS_DIR
from project_state import find_project, initialize_project_state
from session_manager import archive_session, list_sessions

# Pattern matching for book mode detection
BOOK_PATTERNS = [
    r'\bcontinue\b',           # "continue halcyon"
    r'\bresume\b',             # "resume the verge"
    r'\bback to\b',            # "back to halcyon"
    r'\bwork on\b',            # "work on my book"
    r'\bproject\b',            # "halcyon project"
    r'\bchapter\b',            # "chapter 4 of verge"
    r'\bbook\b',               # "continue my book"
]

# Pattern matching for quick session detection
QUICK_PATTERNS = [
    r'\bquick\b',              # "quick session"
    r'\btonight\b',            # "vampire romance tonight"
    r'\bsomething\b',          # "something dark"
    r'\bjust want\b',          # "just want to write"
    r'\bcasual\b',             # "casual session"
    r'\broleplay\b',           # "roleplay"
]


def get_known_projects() -> list:
    """
    Get list of known project directory names.

    Returns lowercase project names, skipping directories that start
    with '.' or '_'.

    Returns:
        list: List of project names (lowercase)
    """
    if not BOOKS_DIR.exists():
        return []
    return [
        p.name.lower() for p in BOOKS_DIR.iterdir()
        if p.is_dir() and not p.name.startswith('.') and not p.name.startswith('_')
    ]


def detect_intent(user_input: str) -> dict:
    """
    Detect whether user wants quick session or book project.

    Matching priority:
    1. Known project name in input (high confidence book mode)
    2. BOOK_PATTERNS vs QUICK_PATTERNS scoring
    3. Default to quick with low confidence if no patterns match

    Args:
        user_input: User's natural language input

    Returns:
        dict: {
            'mode': 'quick' | 'book' | 'ambiguous',
            'confidence': 'high' | 'medium' | 'low',
            'target': str | None,
            'reason': str
        }
    """
    if not user_input:
        return {
            'mode': 'ambiguous',
            'confidence': 'low',
            'target': None,
            'reason': 'No input provided'
        }

    input_lower = user_input.lower()
    known_projects = get_known_projects()

    # Check for known project name in input
    for project in known_projects:
        # Extract significant words from project name (split on - and _)
        project_words = project.replace('-', ' ').replace('_', ' ').split()
        for word in project_words:
            # Only match words longer than 3 chars to avoid false positives
            if len(word) > 3 and word in input_lower:
                return {
                    'mode': 'book',
                    'confidence': 'high',
                    'target': project,
                    'reason': f'Project identifier "{word}" detected'
                }

    # Score book vs quick patterns
    book_score = sum(1 for p in BOOK_PATTERNS if re.search(p, input_lower))
    quick_score = sum(1 for p in QUICK_PATTERNS if re.search(p, input_lower))

    # Book mode if book_score > quick_score AND book_score >= 2
    if book_score > quick_score and book_score >= 2:
        return {
            'mode': 'book',
            'confidence': 'medium',
            'target': None,
            'reason': f'Book patterns matched ({book_score} vs {quick_score})'
        }

    # Quick mode if quick_score > book_score
    if quick_score > book_score:
        return {
            'mode': 'quick',
            'confidence': 'medium',
            'target': None,
            'reason': f'Quick patterns matched ({quick_score} vs {book_score})'
        }

    # Default to quick with low confidence if no patterns match
    if book_score == 0 and quick_score == 0:
        return {
            'mode': 'quick',
            'confidence': 'low',
            'target': None,
            'reason': 'No clear indicators, defaulting to quick session'
        }

    # Ambiguous if equal and both > 0
    if book_score == quick_score and book_score > 0:
        return {
            'mode': 'ambiguous',
            'confidence': 'low',
            'target': None,
            'reason': f'Mixed signals (book: {book_score}, quick: {quick_score})'
        }

    # Fallback: quick mode
    return {
        'mode': 'quick',
        'confidence': 'low',
        'target': None,
        'reason': f'Unclear intent (book: {book_score}, quick: {quick_score})'
    }


def switch_mode(new_mode: str, target: str = None) -> dict:
    """
    Clean mode transition with state management.

    Handles:
    - Archiving active quick session if switching away from quick mode
    - Recording switch history (switch_from info)
    - Loading new mode's context

    Args:
        new_mode: 'quick' or 'book'
        target: Project identifier for book mode (required for book)

    Returns:
        dict: New hub state after switch, or {'error': message} on failure
    """
    current_state = read_state('session.json')
    current_mode = current_state.get('mode')

    # Archive quick session if switching away from quick
    if current_mode == 'quick' and current_state.get('session_path'):
        session_path = Path(current_state['session_path'])
        if session_path.exists():
            try:
                archive_session(session_path)
            except Exception as e:
                print(f"Warning: Could not archive session: {e}", file=sys.stderr)

    # Record what we're switching from
    switch_from = {
        'mode': current_mode,
        'name': current_state.get('active_project') or current_state.get('active_session'),
        'timestamp': datetime.now().isoformat()
    }

    # Build new state based on new_mode
    new_state = {
        'mode': new_mode,
        'last_saved': datetime.now().isoformat(),
        'unsaved_changes': False,
        'last_mode_switch': datetime.now().isoformat(),
        'switch_from': switch_from
    }

    if new_mode == 'book':
        if not target:
            return {'error': 'Book mode requires project target'}

        project_path = find_project(target)
        if not project_path:
            available = get_known_projects()
            return {
                'error': f'Project not found: {target}',
                'available': available
            }

        # Initialize project state if needed
        initialize_project_state(project_path)

        new_state['active_project'] = project_path.name
        new_state['project_path'] = str(project_path)
        new_state['active_session'] = None
        new_state['session_path'] = None

    elif new_mode == 'quick':
        # For quick mode, clear project fields; session fields populated by quick-session skill
        new_state['active_project'] = None
        new_state['project_path'] = None
        new_state['active_session'] = None
        new_state['session_path'] = None

    else:
        return {'error': f'Unknown mode: {new_mode}'}

    # Atomically write new state
    if atomic_write_state('session.json', new_state):
        return new_state
    else:
        return {'error': 'Failed to save hub state'}


def get_hub_context() -> dict:
    """
    Get current hub context summary for Claude.

    Returns:
        dict: {
            'current_mode': str | None,
            'active': str | None (project or session name),
            'unsaved': bool,
            'path': str | None (project or session path),
            'books': list (available book projects),
            'recent_sessions': list (last 5 sessions)
        }
    """
    state = read_state('session.json')

    context = {
        'current_mode': state.get('mode'),
        'active': state.get('active_project') or state.get('active_session'),
        'unsaved': state.get('unsaved_changes', False),
        'path': state.get('project_path') or state.get('session_path')
    }

    # Add navigation options - available books
    context['books'] = get_known_projects()

    # Recent sessions (last 5)
    if SESSIONS_DIR.exists():
        recent = list_sessions(SESSIONS_DIR)[:5]
        context['recent_sessions'] = [
            {'name': s['name'], 'genre': s['genre']} for s in recent
        ]
    else:
        context['recent_sessions'] = []

    return context


def validate_hub_state() -> dict:
    """
    Check hub state integrity and identify issues.

    Validates:
    - project_path exists if set
    - session_path exists if set
    - mode/active_project consistency

    Returns:
        dict: {
            'valid': bool,
            'issues': list,
            'suggested_repairs': list
        }
    """
    state = read_state('session.json')
    issues = []
    repairs = []

    # Check project path validity
    if state.get('project_path'):
        path = Path(state['project_path'])
        if not path.exists():
            issues.append(f"Project path does not exist: {path}")
            repairs.append("Clear active_project and project_path")

    # Check session path validity
    if state.get('session_path'):
        path = Path(state['session_path'])
        if not path.exists():
            issues.append(f"Session path does not exist: {path}")
            repairs.append("Clear active_session and session_path")

    # Check mode consistency
    if state.get('mode') == 'book' and not state.get('active_project'):
        issues.append("Mode is 'book' but no active_project set")
        repairs.append("Clear mode or set active_project")

    if state.get('mode') == 'quick' and state.get('active_project'):
        issues.append("Mode is 'quick' but active_project is set")
        repairs.append("Clear active_project or change mode to 'book'")

    return {
        'valid': len(issues) == 0,
        'issues': issues,
        'suggested_repairs': repairs
    }


# CLI testing interface
if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("Usage:")
        print("  mode_switcher.py detect <input>     - Detect intent from input")
        print("  mode_switcher.py switch <mode> [target] - Switch to mode")
        print("  mode_switcher.py context            - Get hub context")
        print("  mode_switcher.py validate           - Validate hub state")
        sys.exit(1)

    cmd = sys.argv[1]

    if cmd == 'detect':
        user_input = ' '.join(sys.argv[2:]) if len(sys.argv) > 2 else ''
        result = detect_intent(user_input)
        print(json.dumps(result, indent=2))

    elif cmd == 'switch':
        mode = sys.argv[2] if len(sys.argv) > 2 else 'quick'
        target = sys.argv[3] if len(sys.argv) > 3 else None
        result = switch_mode(mode, target)
        print(json.dumps(result, indent=2))

    elif cmd == 'context':
        result = get_hub_context()
        print(json.dumps(result, indent=2))

    elif cmd == 'validate':
        result = validate_hub_state()
        print(json.dumps(result, indent=2))

    else:
        print(f"Unknown command: {cmd}")
        sys.exit(1)
