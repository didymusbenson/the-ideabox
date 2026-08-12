#!/usr/bin/env python3
"""
Book session lifecycle - manages session start/end for book projects.

Functions:
- start_book_session(project_path) - Record session start in project state
- end_book_session(project_path) - Record session end with statistics
- update_position(project_path, scene, section) - Update last position
- add_thread(project_path, thread_data) - Add new plot thread
- update_thread(project_path, thread_id, updates) - Update thread status
- update_character_focus(project_path, characters) - Set active characters
- update_current_arc(project_path, arc) - Set current story arc
"""
import json
import re
import sys
from datetime import datetime
from pathlib import Path

# Import from local hooks directory
hooks_dir = Path(__file__).resolve().parent
sys.path.insert(0, str(hooks_dir))

from project_state import read_project_state, write_project_state
from state_manager import BOOKS_DIR


def create_book_project(project_name: str, working_title: str, genre: str = "uncategorized") -> Path:
    """
    Create a new book project with full scaffolding.

    Args:
        project_name: Kebab-case directory name
        working_title: Human-readable title
        genre: Genre classification

    Returns:
        Path to the created project directory
    """
    project_path = BOOKS_DIR / project_name

    # Create directory structure
    (project_path / '.state').mkdir(parents=True, exist_ok=True)
    (project_path / 'CHARACTERS').mkdir(exist_ok=True)
    (project_path / 'SCENES').mkdir(exist_ok=True)

    # Initialize project state
    state = {
        'project_name': project_name,
        'working_title': working_title,
        'genre': genre,
        'status': 'worldbuilding',
        'created': datetime.now().isoformat(),
        'last_edited': datetime.now().isoformat(),
        'total_sessions': 0,
        'last_position': None,
        'open_threads': [],
        'character_focus': [],
        'current_arc': None,
        'session_history': []
    }

    write_project_state(project_path, state)

    # Create empty world.md
    world_file = project_path / 'world.md'
    if not world_file.exists():
        world_file.write_text(
            f'# {working_title} - Worldbuilding\n\n',
            encoding='utf-8'
        )

    # Create project CLAUDE.md
    claude_file = project_path / 'CLAUDE.md'
    if not claude_file.exists():
        claude_file.write_text(
            f'# {working_title} - Project Instructions\n\n'
            f'## Status\nNew project. Worldbuilding phase.\n\n'
            f'## Genre\n{genre}\n',
            encoding='utf-8'
        )

    return project_path


def generate_thread_id(description: str) -> str:
    """
    Generate kebab-case ID from description (first 5 words).

    Args:
        description: Thread description text

    Returns:
        str: Kebab-case identifier
    """
    # Remove non-word characters, lowercase, split into words
    words = re.sub(r'[^\w\s]', '', description.lower()).split()[:5]
    return '-'.join(words)


def start_book_session(project_path: Path) -> dict:
    """
    Record session start in project state.

    Adds a new entry to session_history with started timestamp.
    Keeps only last 20 sessions (trims oldest).

    Args:
        project_path: Path to the book project directory

    Returns:
        dict: Updated project state
    """
    state = read_project_state(project_path)

    # Create new session entry
    new_session = {
        'started': datetime.now().isoformat(),
        'ended': None,
        'scenes_written': [],
        'word_count_delta': 0
    }

    # Get or create session_history
    session_history = state.get('session_history', [])

    # Add new session
    session_history.append(new_session)

    # Keep only last 20 sessions
    if len(session_history) > 20:
        session_history = session_history[-20:]

    state['session_history'] = session_history
    state['last_edited'] = datetime.now().isoformat()

    write_project_state(project_path, state)
    return state


def end_book_session(project_path: Path, scenes_written: list = None, word_count_delta: int = 0) -> dict:
    """
    Record session end with statistics.

    Updates the last session_history entry with end time and statistics.
    Increments total_sessions counter.

    Args:
        project_path: Path to the book project directory
        scenes_written: List of scene identifiers written this session
        word_count_delta: Net words added/removed this session

    Returns:
        dict: Updated project state
    """
    state = read_project_state(project_path)

    # Get session history
    session_history = state.get('session_history', [])

    if session_history:
        # Update last session entry
        last_session = session_history[-1]
        last_session['ended'] = datetime.now().isoformat()
        last_session['scenes_written'] = scenes_written or []
        last_session['word_count_delta'] = word_count_delta

    # Increment total sessions
    state['total_sessions'] = state.get('total_sessions', 0) + 1
    state['last_edited'] = datetime.now().isoformat()

    write_project_state(project_path, state)
    return state


def update_position(project_path: Path, scene: str = None, section: str = None, chapter: int = None) -> dict:
    """
    Update last position in project.

    Only updates fields that are provided (not None).
    Preserves existing values for fields not specified.

    Args:
        project_path: Path to the book project directory
        scene: Scene identifier (e.g., '04_New_Scene')
        section: Section within scene (e.g., 'opening', 'middle', 'climax')
        chapter: Chapter number

    Returns:
        dict: Updated project state
    """
    state = read_project_state(project_path)

    # Get or create last_position
    last_position = state.get('last_position', {})
    if last_position is None:
        last_position = {}

    # Update only provided fields
    if scene is not None:
        last_position['scene'] = scene
        # Also update scene_file path
        last_position['scene_file'] = f'SCENES/{scene}.md'
    if section is not None:
        last_position['section'] = section
    if chapter is not None:
        last_position['chapter'] = chapter

    state['last_position'] = last_position
    state['last_edited'] = datetime.now().isoformat()

    write_project_state(project_path, state)
    return state


def add_thread(project_path: Path, description: str, opened_scene: str = None, characters: list = None) -> dict:
    """
    Add a new plot thread to track.

    Generates thread ID from description. Thread starts as 'active'.

    Args:
        project_path: Path to the book project directory
        description: What the thread is about
        opened_scene: Scene where thread was introduced (defaults to current scene)
        characters: List of character names involved

    Returns:
        dict: The new thread that was created
    """
    state = read_project_state(project_path)

    # Generate thread ID
    thread_id = generate_thread_id(description)

    # Get current scene for default
    last_position = state.get('last_position', {})
    current_scene = last_position.get('scene') if last_position else None

    # Create thread
    new_thread = {
        'id': thread_id,
        'description': description,
        'opened_scene': opened_scene or current_scene,
        'opened_at': datetime.now().isoformat(),
        'characters': characters or [],
        'status': 'active',
        'resolution_scene': None,
        'notes': None
    }

    # Get or create open_threads list
    open_threads = state.get('open_threads', [])
    open_threads.append(new_thread)

    state['open_threads'] = open_threads
    state['last_edited'] = datetime.now().isoformat()

    write_project_state(project_path, state)
    return new_thread


def update_thread(project_path: Path, thread_id: str, status: str = None, resolution_scene: str = None, notes: str = None) -> dict | None:
    """
    Update an existing plot thread.

    Finds thread by ID and updates provided fields.

    Args:
        project_path: Path to the book project directory
        thread_id: Thread identifier
        status: New status ('active', 'simmering', 'resolved', 'dropped')
        resolution_scene: Scene where thread was resolved
        notes: Additional notes about the thread

    Returns:
        dict: Updated thread, or None if not found
    """
    state = read_project_state(project_path)

    # Find thread
    open_threads = state.get('open_threads', [])
    thread = None

    for t in open_threads:
        if t.get('id') == thread_id:
            thread = t
            break

    if thread is None:
        return None

    # Update provided fields
    if status is not None:
        thread['status'] = status
    if resolution_scene is not None:
        thread['resolution_scene'] = resolution_scene
    if notes is not None:
        thread['notes'] = notes

    state['last_edited'] = datetime.now().isoformat()

    write_project_state(project_path, state)
    return thread


def update_character_focus(project_path: Path, characters: list) -> dict:
    """
    Set active characters for current writing focus.

    Replaces the entire character_focus list.

    Args:
        project_path: Path to the book project directory
        characters: List of character names currently in focus

    Returns:
        dict: Updated project state
    """
    state = read_project_state(project_path)

    state['character_focus'] = characters
    state['last_edited'] = datetime.now().isoformat()

    write_project_state(project_path, state)
    return state


def update_current_arc(project_path: Path, arc: str) -> dict:
    """
    Set the current story arc being written.

    Args:
        project_path: Path to the book project directory
        arc: Name or description of current arc

    Returns:
        dict: Updated project state
    """
    state = read_project_state(project_path)

    state['current_arc'] = arc
    state['last_edited'] = datetime.now().isoformat()

    write_project_state(project_path, state)
    return state


# Allow running as script for testing
if __name__ == '__main__':
    print("book_session.py - Book project session lifecycle functions")
    print("\nFunctions:")
    print("  start_book_session(project_path)")
    print("  end_book_session(project_path, scenes_written, word_count_delta)")
    print("  update_position(project_path, scene, section, chapter)")
    print("  add_thread(project_path, description, opened_scene, characters)")
    print("  update_thread(project_path, thread_id, status, resolution_scene, notes)")
    print("  update_character_focus(project_path, characters)")
    print("  update_current_arc(project_path, arc)")
