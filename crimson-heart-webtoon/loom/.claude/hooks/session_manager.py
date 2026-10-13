#!/usr/bin/env python3
"""
Session Manager - Quick session creation and management.

This module provides session operations for the quick-session workflow:
- Entry type detection (character/situation/vibe)
- Genre inference from scenario elements
- Session scaffolding creation
- Session name generation
- Session archival and listing
- Session search and resume

Usage:
    from session_manager import (
        detect_entry_type,
        infer_genre,
        generate_session_name,
        create_session_scaffold,
        archive_session,
        check_archive_needed,
        list_sessions,
        get_session_path
    )

Functions:
    detect_entry_type(user_input) - Identify entry type from user's initial input
    infer_genre(character, situation, vibe) - Infer genre from scenario elements
    generate_session_name(scenario) - Generate kebab-case session name
    create_session_scaffold(sessions_dir, genre, session_name, scenario) - Create session directory structure
    archive_session(session_dir) - Archive a session with date prefix
    check_archive_needed(sessions_dir, genre) - Check for and archive active sessions in genre
    list_sessions(sessions_dir, genre) - List sessions, optionally filtered by genre
    get_session_path(sessions_dir, name_or_path) - Find session by name or path
"""
import json
import os
import re
import shutil
import sys
from datetime import datetime
from pathlib import Path

# Add hooks directory to path for local imports
_hooks_dir = Path(__file__).resolve().parent
if str(_hooks_dir) not in sys.path:
    sys.path.insert(0, str(_hooks_dir))

from character_manager import create_characters_folder


# Entry point patterns for classification
ENTRY_PATTERNS = {
    'character': [
        r'\b(maid|butler|assassin|vampire|demon|angel|neighbor|boss|teacher)\b',
        r'\b(cunning|shy|cold|obsessive|gentle|stern|fierce)\b',
        r'\b(she|he|they)\s+(is|are|has|wants)\b',
        r'\bcharacter\b',
    ],
    'situation': [
        r'\b(trapped|stuck|forced|arranged|hired|found|discovered)\b',
        r'\b(meet|meeting|encounter|confrontation)\b',
        r'\b(elevator|room|house|office|island|castle|prison|dungeon)\b',
        r'\bscenario|situation\b',
    ],
    'vibe': [
        r'\b(dark|light|fun|intense|slow|cozy|spicy)\b',
        r'\b(romance|thriller|mystery|fantasy)\b',
        r'\bsomething\s+(like|with|that)\b',
        r'\b(feel|mood|vibe|tone)\b',
    ]
}


# Genre keywords for classification
GENRE_KEYWORDS = {
    'dark-romance': ['dark', 'obsess', 'yandere', 'forced', 'captive', 'villain', 'evil'],
    'romance': ['gentle', 'sweet', 'slow burn', 'enemies to lovers', 'fake dating'],
    'fantasy': ['demon', 'angel', 'mage', 'kingdom', 'magic', 'dragon', 'isekai'],
    'scifi': ['space', 'alien', 'future', 'android', 'superhero', 'powers'],
    'thriller': ['spy', 'assassin', 'revenge', 'mystery', 'dangerous'],
    'contemporary': ['neighbor', 'coworker', 'college', 'roommate', 'modern'],
    'uncategorized': []  # Fallback
}


def detect_entry_type(user_input: str) -> str:
    """
    Detect entry point type from user's initial message.

    Pattern match against ENTRY_PATTERNS dict, scoring each type.
    Returns highest scoring type, defaults to 'vibe' if tie or unclear.

    Args:
        user_input: User's initial session description

    Returns:
        str: 'character', 'situation', or 'vibe'
    """
    if not user_input:
        return 'vibe'

    input_lower = user_input.lower()
    scores = {'character': 0, 'situation': 0, 'vibe': 0}

    for entry_type, patterns in ENTRY_PATTERNS.items():
        for pattern in patterns:
            if re.search(pattern, input_lower):
                scores[entry_type] += 1

    # Return highest scoring, default to 'vibe' if tie/unclear
    if max(scores.values()) == 0:
        return 'vibe'

    # Get max score
    max_score = max(scores.values())

    # If there's a tie, default to 'vibe'
    tied = [k for k, v in scores.items() if v == max_score]
    if len(tied) > 1:
        return 'vibe'

    return max(scores, key=scores.get)


def infer_genre(character: str, situation: str, vibe: str) -> str:
    """
    Infer genre from scenario elements.

    Combines inputs, lowercases, and matches against GENRE_KEYWORDS.
    Returns highest scoring genre, or 'uncategorized' if no matches.

    Args:
        character: Character description
        situation: Situation description
        vibe: Vibe/mood description

    Returns:
        str: Genre name (dark-romance, romance, fantasy, scifi, thriller, contemporary, or uncategorized)
    """
    # Combine and normalize inputs
    combined = f"{character or ''} {situation or ''} {vibe or ''}".lower()

    if not combined.strip():
        return 'uncategorized'

    scores = {genre: 0 for genre in GENRE_KEYWORDS}

    for genre, keywords in GENRE_KEYWORDS.items():
        for keyword in keywords:
            if keyword in combined:
                scores[genre] += 1

    # Return highest scoring, or 'uncategorized' if no matches
    best = max(scores, key=scores.get)
    return best if scores[best] > 0 else 'uncategorized'


def generate_session_name(scenario: dict) -> str:
    """
    Generate a kebab-case session name from scenario elements.

    Takes first 2-3 significant words from character/situation/vibe.
    Returns kebab-case name (max 30 chars).

    Args:
        scenario: Dict with 'character', 'situation', 'vibe' keys

    Returns:
        str: Kebab-case session name (e.g., 'shy-librarian-trapped')
    """
    # Gather words from scenario elements
    words = []

    # Stop words to filter out
    stop_words = {
        'a', 'an', 'the', 'is', 'are', 'was', 'were', 'be', 'been',
        'being', 'have', 'has', 'had', 'do', 'does', 'did', 'will',
        'would', 'could', 'should', 'may', 'might', 'must', 'shall',
        'in', 'on', 'at', 'to', 'for', 'of', 'with', 'by', 'from',
        'and', 'or', 'but', 'not', 'so', 'yet', 'just', 'only',
        'something', 'like', 'that', 'this', 'it', 'i', 'you', 'we',
        'they', 'he', 'she', 'my', 'your', 'our', 'their', 'his', 'her'
    }

    # Extract significant words from each element
    for key in ['character', 'situation', 'vibe']:
        value = scenario.get(key, '')
        if value:
            # Split on whitespace and non-alphanumeric
            element_words = re.findall(r'\b[a-zA-Z]+\b', value.lower())
            # Filter stop words and short words
            significant = [w for w in element_words if w not in stop_words and len(w) > 2]
            words.extend(significant[:2])  # Take up to 2 from each element

    # If no words extracted, use fallback
    if not words:
        words = ['quick', 'session']

    # Take first 3 significant words
    name_words = words[:3]

    # Join with hyphen
    name = '-'.join(name_words)

    # Truncate to max 30 chars (at word boundary if possible)
    if len(name) > 30:
        truncated = name[:30]
        # Cut at last hyphen if possible
        last_hyphen = truncated.rfind('-')
        if last_hyphen > 10:  # Keep at least something meaningful
            name = truncated[:last_hyphen]
        else:
            name = truncated

    return name


def create_session_scaffold(
    sessions_dir: Path,
    genre: str,
    session_name: str,
    scenario: dict
) -> Path:
    """
    Create session directory structure with minimal scaffolding.

    Creates:
    - {sessions_dir}/{genre}/{session_name}/ directory
    - session.json with metadata
    - scenario.md with setup section
    - SCENES/ subdirectory

    Args:
        sessions_dir: Path to _sessions/ directory
        genre: Genre/mood category (dark-romance, fantasy, etc.)
        session_name: Kebab-case session name
        scenario: Dict with entry_type, character, situation, vibe

    Returns:
        Path: Path to created session directory
    """
    # Ensure sessions_dir is a Path
    sessions_dir = Path(sessions_dir)

    # Create session directory (no date prefix for active sessions)
    session_dir = sessions_dir / genre / session_name
    session_dir.mkdir(parents=True, exist_ok=True)

    # Create session metadata
    session_json = {
        'name': session_name,
        'genre': genre,
        'status': 'active',
        'created': datetime.now().isoformat(),
        'entry_type': scenario.get('entry_type', 'vibe'),
        'character': scenario.get('character', ''),
        'situation': scenario.get('situation', ''),
        'vibe': scenario.get('vibe', ''),
    }

    # Write session.json
    session_file = session_dir / 'session.json'
    session_file.write_text(
        json.dumps(session_json, indent=2, ensure_ascii=False),
        encoding='utf-8'
    )

    # Format session name for display
    display_name = session_name.replace('-', ' ').title()

    # Write scenario.md with essential details only
    scenario_md = f"""# {display_name}

## Setup
**Character:** {scenario.get('character', 'TBD')}
**Situation:** {scenario.get('situation', 'TBD')}
**Vibe:** {scenario.get('vibe', 'TBD')}

## Summary
{scenario.get('summary', 'Scenario to be developed.')}
"""
    scenario_file = session_dir / 'scenario.md'
    scenario_file.write_text(scenario_md, encoding='utf-8')

    # Create empty SCENES directory
    scenes_dir = session_dir / 'SCENES'
    scenes_dir.mkdir(exist_ok=True)

    # Create characters/ folder with empty manifest
    create_characters_folder(session_dir)

    return session_dir


def archive_session(session_dir: Path) -> Path:
    """
    Archive a session by adding date prefix to folder name.

    Reads session.json to get created timestamp, extracts date,
    renames folder to {date}_{session_name}, updates status to 'archived'.

    Args:
        session_dir: Path to session directory to archive

    Returns:
        Path: Path to archived session directory

    Raises:
        FileNotFoundError: If session_dir doesn't exist
    """
    session_dir = Path(session_dir)

    if not session_dir.exists():
        raise FileNotFoundError(f"Session directory not found: {session_dir}")

    # Read session.json for created timestamp
    session_file = session_dir / 'session.json'
    if session_file.exists():
        try:
            session_data = json.loads(session_file.read_text(encoding='utf-8'))
            created = session_data.get('created', '')
        except (json.JSONDecodeError, UnicodeDecodeError):
            created = ''
            session_data = {}
    else:
        # No session.json - use current date and create minimal metadata
        created = ''
        session_data = {'name': session_dir.name, 'status': 'active'}

    # Extract date from created timestamp or use current date
    if created:
        try:
            # Parse ISO format timestamp
            date_str = created.split('T')[0]  # Get YYYY-MM-DD part
        except (ValueError, IndexError):
            date_str = datetime.now().strftime('%Y-%m-%d')
    else:
        date_str = datetime.now().strftime('%Y-%m-%d')

    # Build archived name: {date}_{session_name}
    session_name = session_dir.name
    archived_name = f"{date_str}_{session_name}"

    # Target path is in same parent directory (same genre folder)
    archived_dir = session_dir.parent / archived_name

    # Move the directory
    shutil.move(str(session_dir), str(archived_dir))

    # Update session.json with archived status
    session_file = archived_dir / 'session.json'
    session_data['status'] = 'archived'
    session_data['archived_at'] = datetime.now().isoformat()
    session_data['name'] = session_name  # Keep original name

    session_file.write_text(
        json.dumps(session_data, indent=2, ensure_ascii=False),
        encoding='utf-8'
    )

    return archived_dir


def check_archive_needed(sessions_dir: Path, genre: str) -> Path | None:
    """
    Check for and archive any active session in the specified genre.

    Scans {sessions_dir}/{genre}/ for active sessions (no date prefix,
    status='active'). If found, archives it.

    Args:
        sessions_dir: Path to _sessions/ directory
        genre: Genre folder to check

    Returns:
        Path | None: Path to archived session, or None if nothing to archive
    """
    sessions_dir = Path(sessions_dir)
    genre_dir = sessions_dir / genre

    if not genre_dir.exists():
        return None

    # Date prefix pattern: YYYY-MM-DD_
    date_prefix_pattern = re.compile(r'^\d{4}-\d{2}-\d{2}_')

    for item in genre_dir.iterdir():
        if not item.is_dir():
            continue

        # Skip if already has date prefix (already archived)
        if date_prefix_pattern.match(item.name):
            continue

        # Check session.json for status
        session_file = item / 'session.json'
        if session_file.exists():
            try:
                session_data = json.loads(session_file.read_text(encoding='utf-8'))
                status = session_data.get('status', 'active')
            except (json.JSONDecodeError, UnicodeDecodeError):
                status = 'active'  # Assume active if can't read
        else:
            # No session.json - treat as legacy active session
            status = 'active'

        if status == 'active':
            # Found an active session - archive it
            return archive_session(item)

    return None


def list_sessions(sessions_dir: Path, genre: str = None) -> list[dict]:
    """
    List sessions, optionally filtered by genre.

    Scans genre folders for session directories, reads their metadata,
    and returns sorted list of session info dicts.

    Args:
        sessions_dir: Path to _sessions/ directory
        genre: Optional genre to filter by (None = all genres)

    Returns:
        list[dict]: List of session dicts with keys:
            - name: Session name (without date prefix)
            - genre: Genre category
            - status: 'active' or 'archived'
            - created: ISO timestamp or None
            - path: Full path to session directory
            - scene_count: Number of .md files in SCENES/
    """
    sessions_dir = Path(sessions_dir)
    results = []

    # Determine which genres to scan
    if genre:
        genres_to_scan = [genre]
    else:
        # Scan all genre directories
        genres_to_scan = []
        if sessions_dir.exists():
            for item in sessions_dir.iterdir():
                if item.is_dir() and not item.name.startswith('.'):
                    genres_to_scan.append(item.name)

    # Date prefix pattern for extracting original name
    date_prefix_pattern = re.compile(r'^(\d{4}-\d{2}-\d{2})_(.+)$')

    for g in genres_to_scan:
        genre_dir = sessions_dir / g
        if not genre_dir.exists():
            continue

        for item in genre_dir.iterdir():
            if not item.is_dir():
                continue

            # Parse session name (remove date prefix if present)
            match = date_prefix_pattern.match(item.name)
            if match:
                name = match.group(2)
                is_archived = True
            else:
                name = item.name
                is_archived = False

            # Read session.json if exists
            session_file = item / 'session.json'
            if session_file.exists():
                try:
                    session_data = json.loads(session_file.read_text(encoding='utf-8'))
                    status = session_data.get('status', 'archived' if is_archived else 'active')
                    created = session_data.get('created')
                except (json.JSONDecodeError, UnicodeDecodeError):
                    status = 'archived' if is_archived else 'active'
                    created = None
            else:
                # No session.json - infer from folder structure
                status = 'archived' if is_archived else 'active'
                created = None

            # Count scenes (check SCENES/ first, then lowercase scenes/)
            scene_count = 0
            scenes_dir = item / 'SCENES'
            if not scenes_dir.exists():
                scenes_dir = item / 'scenes'
            if scenes_dir.exists():
                scene_count = len([f for f in scenes_dir.iterdir() if f.suffix == '.md'])

            results.append({
                'name': name,
                'genre': g,
                'status': status,
                'created': created,
                'path': str(item),
                'scene_count': scene_count
            })

    # Sort by created date descending (newest first), None dates at end
    results.sort(key=lambda x: (x['created'] is None, x['created'] or ''), reverse=True)

    return results


def get_session_path(sessions_dir: Path, name_or_path: str) -> Path | None:
    """
    Find session by name or path.

    If name_or_path is a full path that exists, returns it.
    Otherwise, searches all genre folders for matching session name.
    Supports partial/fuzzy matching (session name contains search term).

    Args:
        sessions_dir: Path to _sessions/ directory
        name_or_path: Session name to search for, or full path

    Returns:
        Path | None: Path to matching session, or None if not found
    """
    # Check if it's already a valid path
    path = Path(name_or_path)
    if path.exists() and path.is_dir():
        return path

    sessions_dir = Path(sessions_dir)
    search_term = name_or_path.lower()

    # Date prefix pattern for extracting original name
    date_prefix_pattern = re.compile(r'^\d{4}-\d{2}-\d{2}_(.+)$')

    if not sessions_dir.exists():
        return None

    # Search all genre folders
    for genre_dir in sessions_dir.iterdir():
        if not genre_dir.is_dir() or genre_dir.name.startswith('.'):
            continue

        for item in genre_dir.iterdir():
            if not item.is_dir():
                continue

            # Get session name (without date prefix)
            match = date_prefix_pattern.match(item.name)
            if match:
                session_name = match.group(1)
            else:
                session_name = item.name

            # Fuzzy match: session name contains search term
            if search_term in session_name.lower():
                return item

    return None


# Allow running as script for testing
if __name__ == '__main__':
    print("Session Manager - Quick Session Operations")
    print("-" * 40)

    # Test detect_entry_type
    test_inputs = [
        ("cunning thief with attitude", "character"),
        ("trapped in elevator with my boss", "situation"),
        ("something dark and obsessive", "vibe"),
        ("", "vibe"),
    ]

    print("\nEntry Type Detection:")
    for test_input, expected in test_inputs:
        result = detect_entry_type(test_input)
        status = "PASS" if result == expected else f"FAIL (got {result})"
        print(f"  '{test_input}' -> {result} [{status}]")

    # Test infer_genre
    print("\nGenre Inference:")
    genre_tests = [
        (("vampire lord", "captured", "dark obsessive"), "dark-romance"),
        (("shy neighbor", "moving in", "sweet"), "romance"),
        (("demon", "summoned", "fantasy"), "fantasy"),
    ]

    for (char, sit, vibe), expected in genre_tests:
        result = infer_genre(char, sit, vibe)
        status = "PASS" if result == expected else f"FAIL (got {result})"
        print(f"  ({char}, {sit}, {vibe}) -> {result} [{status}]")

    # Test generate_session_name
    print("\nSession Name Generation:")
    name_tests = [
        ({'character': 'shy librarian', 'situation': 'trapped elevator'}, "shy-librarian-trapped"),
        ({'character': '', 'situation': '', 'vibe': ''}, "quick-session"),
    ]

    for scenario, expected in name_tests:
        result = generate_session_name(scenario)
        print(f"  {scenario} -> {result}")

    # Test list_sessions and get_session_path (if _sessions exists)
    from state_manager import SESSIONS_DIR
    sessions_dir = SESSIONS_DIR
    if sessions_dir.exists():
        print("\nSession Listing (dark-romance):")
        sessions = list_sessions(sessions_dir, 'dark-romance')
        print(f"  Found {len(sessions)} sessions")
        for s in sessions[:3]:
            print(f"    - {s['name']} ({s['status']}, {s['scene_count']} scenes)")

        print("\nSession Search:")
        found = get_session_path(sessions_dir, 'evil')
        print(f"  Search 'evil': {found}")
        found = get_session_path(sessions_dir, 'nonexistent-xyz')
        print(f"  Search 'nonexistent-xyz': {found}")
