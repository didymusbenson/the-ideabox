#!/usr/bin/env python3
"""
Character Manager - Character sheet CRUD and manifest management.

This module provides the data layer for the character profile system.
Character sheets are markdown files with YAML frontmatter, stored in
per-session or per-project characters/ folders with a JSON manifest index.

Usage:
    from character_manager import (
        create_characters_folder,
        create_character,
        read_character,
        update_character,
        delete_character,
        rebuild_manifest,
        list_characters,
        find_character,
        parse_frontmatter,
        render_frontmatter,
        generate_sheet,
        slugify
    )

Functions:
    slugify(name) - Convert name to kebab-case filename slug
    parse_frontmatter(content) - Parse YAML frontmatter from markdown
    render_frontmatter(metadata) - Render dict to YAML frontmatter string
    generate_sheet(name, role, status, tags, sections, genre_modules) - Render character sheet markdown
    create_characters_folder(parent_dir) - Create characters/ folder with empty manifest
    create_character(characters_dir, name, ...) - Create character sheet file
    read_character(characters_dir, identifier) - Read character sheet
    update_character(characters_dir, identifier, ...) - Update character sheet
    delete_character(characters_dir, identifier) - Delete character sheet
    rebuild_manifest(characters_dir) - Regenerate _cast_manifest.json from .md files
    list_characters(characters_dir, role, status, tag) - List characters with optional filters
    find_character(characters_dir, query) - Fuzzy search for character file
    create_library_folder() - Create hub-level _characters/ library
    promote_to_library(characters_dir, identifier, source_session) - Promote to library
    import_from_library(identifier, characters_dir, session_name) - Import from library
    rebuild_library_index() - Regenerate _library_index.json
    list_library(role, tag) - List library characters

Constants:
    VALID_ROLES - Allowed character roles
    VALID_STATUSES - Allowed character statuses
    MAX_SLUG_LENGTH - Maximum filename slug length
    TEMPLATE_SECTIONS - Ordered list of standard sections
    GENRE_MODULES - Genre-specific optional section definitions
"""
import json
import os
import re
import sys
import tempfile
from datetime import datetime
from pathlib import Path

# Add hooks directory to path for cross-module imports
_hooks_dir = Path(__file__).resolve().parent
if str(_hooks_dir) not in sys.path:
    sys.path.insert(0, str(_hooks_dir))


# --- Constants ---

VALID_ROLES = ['pc', 'npc', 'antagonist', 'supporting', 'minor']
VALID_STATUSES = ['active', 'inactive', 'deceased', 'unknown']
MAX_SLUG_LENGTH = 50

TEMPLATE_SECTIONS = [
    'Identity',
    'Aspects',
    'Appearance',
    'Personality',
    'Voice',
    'Background',
    'Relationships',
    'Session Log',
]

GENRE_MODULES = {
    'romance': ('Romance', {
        'Attraction Type': '[emotional, physical, intellectual, power]',
        'Love Language': '[words, touch, acts, gifts, time]',
        'Boundaries': '',
        'Turn-Ons': '',
        'Vulnerabilities': '',
    }),
    'fantasy': ('Powers & Abilities', {
        'Type': '[magic, physical, divine, psionic]',
        'Abilities': '',
        'Limitations': '',
        'Source': '',
    }),
    'thriller': ('Methods & Resources', {
        'Skills': '',
        'Resources': '',
        'Network': '',
        'Weaknesses': '',
    }),
}

# Default content for structured sections (used when section is included but has no content)
_IDENTITY_DEFAULT = (
    "**Full Name:** \n"
    "**Age:** \n"
    "**Occupation/Role:** \n"
    "**First Appearance:** Scene XXX"
)

_ASPECTS_DEFAULT = (
    "<!-- FATE-style aspects: 3-5 evocative phrases that capture the character's essence -->\n"
    "<!-- Each aspect should have both positive and negative potential -->\n"
    "- **High Concept:** [Who they fundamentally are]\n"
    "- **Trouble:** [What complicates their existence]\n"
    "- **Relationship:** [Their defining connection to another character]"
)

_RELATIONSHIPS_HEADER = (
    "<!-- Connections to other characters -->\n"
    "| Character | Relationship | Dynamic |\n"
    "|-----------|-------------|---------|"
)

_SESSION_LOG_HEADER = (
    "<!-- Chronological development tracker -- auto-populated by Claude -->\n"
    "| Session | Event | Development |\n"
    "|---------|-------|-------------|"
)


# --- Utility Functions ---

def slugify(name: str) -> str:
    """
    Convert a character name to a kebab-case filename slug.

    Args:
        name: Character name (e.g., "Elara Voss", "Dr. James O'Brien")

    Returns:
        str: Kebab-case slug (e.g., "elara-voss", "dr-james-o-brien")
    """
    if not name or not name.strip():
        return 'unnamed'
    slug = re.sub(r'[^a-z0-9]+', '-', name.lower()).strip('-')
    if not slug:
        return 'unnamed'
    return slug[:MAX_SLUG_LENGTH]


# --- Frontmatter Parser ---

def parse_frontmatter(content: str) -> tuple:
    """
    Parse YAML frontmatter from markdown content.

    Handles flat key-value pairs only (no nesting). Supports:
    - String values
    - Flow-style lists: [a, b, c]
    - Booleans: true/false
    - Empty values (returned as None)
    - Quoted strings
    - Colons in values (uses partition, not split)

    Args:
        content: Full markdown file content

    Returns:
        tuple: (metadata_dict, body_string)
    """
    if not content.startswith('---'):
        return {}, content

    # Find closing ---
    end_match = re.search(r'\n---\s*\n', content[3:])
    if not end_match:
        # Try end of string (file ends right after frontmatter)
        end_match = re.search(r'\n---\s*$', content[3:])
        if not end_match:
            return {}, content

    yaml_block = content[4:end_match.start() + 3]
    body = content[end_match.end() + 3:]

    metadata = {}
    for line in yaml_block.strip().split('\n'):
        line = line.strip()
        if not line or line.startswith('#'):
            continue
        if ':' not in line:
            continue

        key, _, value = line.partition(':')
        key = key.strip()
        value = value.strip()

        # Parse value types
        if value.startswith('[') and value.endswith(']'):
            # Flow-style list: [a, b, c]
            inner = value[1:-1]
            if inner.strip():
                items = [item.strip().strip('"').strip("'")
                         for item in inner.split(',') if item.strip()]
            else:
                items = []
            metadata[key] = items
        elif value.lower() in ('true', 'false'):
            metadata[key] = value.lower() == 'true'
        elif value == '':
            metadata[key] = None
        else:
            # Strip quotes if present
            if (value.startswith('"') and value.endswith('"')) or \
               (value.startswith("'") and value.endswith("'")):
                value = value[1:-1]
            metadata[key] = value

    return metadata, body


def render_frontmatter(metadata: dict) -> str:
    """
    Render a metadata dict back to YAML frontmatter string.

    Inverse of parse_frontmatter. Lists are rendered as flow-style [a, b, c].
    None values are rendered as empty strings.

    Args:
        metadata: Dict of frontmatter key-value pairs

    Returns:
        str: YAML frontmatter string with --- delimiters
    """
    lines = ['---']
    for key, value in metadata.items():
        if isinstance(value, list):
            items = ', '.join(str(v) for v in value)
            lines.append(f'{key}: [{items}]')
        elif isinstance(value, bool):
            lines.append(f'{key}: {"true" if value else "false"}')
        elif value is None:
            lines.append(f'{key}:')
        else:
            lines.append(f'{key}: {value}')
    lines.append('---')
    return '\n'.join(lines)


# --- Template Rendering ---

def generate_sheet(
    name: str,
    role: str = 'npc',
    status: str = 'active',
    tags: list = None,
    sections: dict = None,
    genre_modules: list = None
) -> str:
    """
    Render a complete character sheet as a markdown string.

    Sections are optional — only sections with content in the sections dict
    are included. A call with only a name produces a minimal valid sheet
    (frontmatter + heading, no body sections).

    Args:
        name: Character name (required)
        role: Character role (pc, npc, antagonist, supporting, minor)
        status: Character status (active, inactive, deceased, unknown)
        tags: List of tags (default [])
        sections: Dict mapping section names to content strings
        genre_modules: List of genre keys to append (e.g., ['romance', 'fantasy'])

    Returns:
        str: Complete character sheet markdown
    """
    # Validate role and status
    if role not in VALID_ROLES:
        role = 'npc'
    if status not in VALID_STATUSES:
        status = 'active'

    tags = tags or []
    sections = sections or {}

    now = datetime.now().strftime('%Y-%m-%d')

    # Build frontmatter
    frontmatter = render_frontmatter({
        'name': name,
        'role': role,
        'status': status,
        'tags': tags,
        'created': now,
        'updated': now,
    })

    # Start with frontmatter + heading
    parts = [frontmatter, '', f'# {name}']

    # Render standard sections (only those provided or with defaults for key sections)
    for section_name in TEMPLATE_SECTIONS:
        content = sections.get(section_name)

        if content:
            # Section has user-provided content
            parts.append(f'\n## {section_name}\n{content}')
        elif section_name in sections:
            # Section key exists but content is empty/None — use defaults for structured sections
            if section_name == 'Identity':
                parts.append(f'\n## {section_name}\n{_IDENTITY_DEFAULT}')
            elif section_name == 'Aspects':
                parts.append(f'\n## {section_name}\n{_ASPECTS_DEFAULT}')
            elif section_name == 'Relationships':
                parts.append(f'\n## {section_name}\n{_RELATIONSHIPS_HEADER}')
            elif section_name == 'Session Log':
                parts.append(f'\n## {section_name}\n{_SESSION_LOG_HEADER}')
            else:
                parts.append(f'\n## {section_name}')
        # If section_name not in sections at all, omit entirely (sparse profiles)

    # Append genre modules
    if genre_modules:
        for genre_key in genre_modules:
            if genre_key in GENRE_MODULES:
                section_title, fields = GENRE_MODULES[genre_key]
                genre_lines = [f'\n## {section_title}']
                for field_name, field_default in fields.items():
                    genre_lines.append(f'**{field_name}:** {field_default}')
                parts.append('\n'.join(genre_lines))

    # Ensure trailing newline
    return '\n'.join(parts) + '\n'


# --- Scaffolding ---

def create_characters_folder(parent_dir: Path) -> Path:
    """
    Create characters/ subdirectory with empty _cast_manifest.json.

    Idempotent — safe to call on every initialization.

    Args:
        parent_dir: Parent directory (session dir or project dir)

    Returns:
        Path: Path to characters/ directory
    """
    parent_dir = Path(parent_dir)
    characters_dir = parent_dir / 'characters'
    characters_dir.mkdir(parents=True, exist_ok=True)

    manifest_path = characters_dir / '_cast_manifest.json'
    if not manifest_path.exists():
        empty_manifest = {
            'version': 1,
            'generated': datetime.now().isoformat(),
            'characters': {}
        }
        manifest_path.write_text(
            json.dumps(empty_manifest, indent=2, ensure_ascii=False),
            encoding='utf-8'
        )

    return characters_dir


# --- CRUD Operations ---

def create_character(
    characters_dir: Path,
    name: str,
    role: str = 'npc',
    status: str = 'active',
    tags: list = None,
    sections: dict = None,
    genre_modules: list = None
) -> Path:
    """
    Create a new character sheet file and update manifest.

    Args:
        characters_dir: Path to characters/ directory
        name: Character name
        role: Character role (default 'npc')
        status: Character status (default 'active')
        tags: List of tags
        sections: Dict of section name -> content
        genre_modules: List of genre keys to include

    Returns:
        Path: Path to created character sheet file
    """
    characters_dir = Path(characters_dir)
    characters_dir.mkdir(parents=True, exist_ok=True)

    slug = slugify(name)
    filepath = characters_dir / f'{slug}.md'

    # Handle filename collision
    if filepath.exists():
        counter = 2
        while (characters_dir / f'{slug}-{counter}.md').exists():
            counter += 1
        filepath = characters_dir / f'{slug}-{counter}.md'

    # Generate sheet content
    content = generate_sheet(
        name=name,
        role=role,
        status=status,
        tags=tags,
        sections=sections,
        genre_modules=genre_modules
    )

    filepath.write_text(content, encoding='utf-8')

    # Update manifest
    rebuild_manifest(characters_dir)

    return filepath


def read_character(characters_dir: Path, identifier: str) -> tuple:
    """
    Read a character sheet by slug or name.

    Args:
        characters_dir: Path to characters/ directory
        identifier: Slug (exact filename stem) or character name

    Returns:
        tuple: (metadata_dict, body_string)

    Raises:
        FileNotFoundError: If character not found
    """
    characters_dir = Path(characters_dir)

    # Try exact slug match first
    filepath = characters_dir / f'{identifier}.md'
    if not filepath.exists():
        # Try slugifying the identifier
        slug = slugify(identifier)
        filepath = characters_dir / f'{slug}.md'

    if not filepath.exists():
        # Try fuzzy find
        found = find_character(characters_dir, identifier)
        if found:
            filepath = found
        else:
            raise FileNotFoundError(f"Character not found: {identifier}")

    content = filepath.read_text(encoding='utf-8')
    return parse_frontmatter(content)


def update_character(
    characters_dir: Path,
    identifier: str,
    metadata: dict = None,
    body: str = None
) -> bool:
    """
    Update a character sheet.

    Merges metadata (new keys override, existing preserved).
    Always updates the 'updated' timestamp.

    Args:
        characters_dir: Path to characters/ directory
        identifier: Slug or character name
        metadata: Dict of frontmatter fields to merge
        body: New markdown body (replaces entire body if provided)

    Returns:
        bool: True on success
    """
    characters_dir = Path(characters_dir)

    # Find the file
    filepath = characters_dir / f'{identifier}.md'
    if not filepath.exists():
        slug = slugify(identifier)
        filepath = characters_dir / f'{slug}.md'
    if not filepath.exists():
        found = find_character(characters_dir, identifier)
        if found:
            filepath = found
        else:
            return False

    content = filepath.read_text(encoding='utf-8')
    existing_meta, existing_body = parse_frontmatter(content)

    # Merge metadata
    if metadata:
        existing_meta.update(metadata)

    # Always update timestamp
    existing_meta['updated'] = datetime.now().strftime('%Y-%m-%d')

    # Use new body or keep existing
    final_body = body if body is not None else existing_body

    # Rewrite file
    new_content = render_frontmatter(existing_meta) + '\n' + final_body
    filepath.write_text(new_content, encoding='utf-8')

    # Update manifest
    rebuild_manifest(characters_dir)

    return True


def delete_character(characters_dir: Path, identifier: str) -> bool:
    """
    Delete a character sheet file and update manifest.

    Args:
        characters_dir: Path to characters/ directory
        identifier: Slug or character name

    Returns:
        bool: True if deleted, False if not found
    """
    characters_dir = Path(characters_dir)

    filepath = characters_dir / f'{identifier}.md'
    if not filepath.exists():
        slug = slugify(identifier)
        filepath = characters_dir / f'{slug}.md'
    if not filepath.exists():
        found = find_character(characters_dir, identifier)
        if found:
            filepath = found
        else:
            return False

    filepath.unlink()
    rebuild_manifest(characters_dir)
    return True


# --- Manifest Management ---

def rebuild_manifest(characters_dir: Path) -> dict:
    """
    Scan all .md files and regenerate _cast_manifest.json.

    Source of truth is the .md files. Manifest is a denormalized cache
    for fast lookups. Written atomically (temp file + os.replace).

    Args:
        characters_dir: Path to characters/ directory

    Returns:
        dict: The rebuilt manifest
    """
    characters_dir = Path(characters_dir)
    manifest = {
        'version': 1,
        'generated': datetime.now().isoformat(),
        'characters': {}
    }

    for md_file in sorted(characters_dir.glob('*.md')):
        if md_file.name.startswith('_'):
            continue

        try:
            content = md_file.read_text(encoding='utf-8')
        except Exception:
            continue

        meta, _ = parse_frontmatter(content)
        if not meta.get('name'):
            continue

        slug = md_file.stem
        tags = meta.get('tags', [])
        if tags is None:
            tags = []

        manifest['characters'][slug] = {
            'name': meta.get('name', slug),
            'role': meta.get('role', 'npc'),
            'status': meta.get('status', 'active'),
            'tags': tags,
            'file': md_file.name,
            'created': meta.get('created', ''),
            'updated': meta.get('updated', ''),
        }

    # Atomic write
    manifest_path = characters_dir / '_cast_manifest.json'
    try:
        fd, temp_path_str = tempfile.mkstemp(
            dir=str(characters_dir),
            prefix='.tmp_',
            suffix='.json'
        )
        temp_path = Path(temp_path_str)
        with os.fdopen(fd, 'w', encoding='utf-8') as f:
            json.dump(manifest, f, indent=2, ensure_ascii=False)
            f.flush()
            os.fsync(f.fileno())
        os.replace(str(temp_path), str(manifest_path))
    except Exception:
        # Fallback: direct write
        manifest_path.write_text(
            json.dumps(manifest, indent=2, ensure_ascii=False),
            encoding='utf-8'
        )

    return manifest


def list_characters(
    characters_dir: Path,
    role: str = None,
    status: str = None,
    tag: str = None
) -> list:
    """
    List characters from manifest with optional filters.

    Args:
        characters_dir: Path to characters/ directory
        role: Filter by role (e.g., 'npc', 'pc')
        status: Filter by status (e.g., 'active')
        tag: Filter by tag (characters must have this tag)

    Returns:
        list: List of character entry dicts
    """
    characters_dir = Path(characters_dir)
    manifest_path = characters_dir / '_cast_manifest.json'

    if not manifest_path.exists():
        manifest = rebuild_manifest(characters_dir)
    else:
        try:
            manifest = json.loads(manifest_path.read_text(encoding='utf-8'))
        except (json.JSONDecodeError, Exception):
            manifest = rebuild_manifest(characters_dir)

    characters = list(manifest.get('characters', {}).values())

    # Apply filters
    if role:
        characters = [c for c in characters if c.get('role') == role]
    if status:
        characters = [c for c in characters if c.get('status') == status]
    if tag:
        characters = [c for c in characters if tag in c.get('tags', [])]

    return characters


def find_character(characters_dir: Path, query: str) -> Path:
    """
    Fuzzy search for a character file.

    Priority: exact slug match > starts-with > contains.
    Searches both slugs and names.

    Args:
        characters_dir: Path to characters/ directory
        query: Search query (name or partial slug)

    Returns:
        Path | None: Path to matching file, or None
    """
    characters_dir = Path(characters_dir)
    query_lower = query.lower()
    query_slug = slugify(query)

    md_files = [f for f in characters_dir.glob('*.md') if not f.name.startswith('_')]

    # Priority 1: Exact slug match
    for f in md_files:
        if f.stem == query_slug:
            return f

    # Priority 2: Starts-with match on slug
    for f in md_files:
        if f.stem.startswith(query_slug):
            return f

    # Priority 3: Contains match on slug or name
    for f in md_files:
        if query_slug in f.stem:
            return f

    # Priority 4: Search by name in frontmatter
    for f in md_files:
        try:
            content = f.read_text(encoding='utf-8')
            meta, _ = parse_frontmatter(content)
            name = meta.get('name', '')
            if name and query_lower in name.lower():
                return f
        except Exception:
            continue

    return None


# --- Cast Library Operations ---

# Hub-level library directory - relative to project root
from state_manager import CHARACTERS_DIR
LIBRARY_DIR = CHARACTERS_DIR


def create_library_folder() -> Path:
    """
    Create hub-level _characters/ library folder with index.

    Returns:
        Path: Path to _characters/ directory
    """
    LIBRARY_DIR.mkdir(parents=True, exist_ok=True)

    index_path = LIBRARY_DIR / '_library_index.json'
    if not index_path.exists():
        empty_index = {
            'version': 1,
            'generated': datetime.now().isoformat(),
            'characters': {}
        }
        index_path.write_text(
            json.dumps(empty_index, indent=2, ensure_ascii=False),
            encoding='utf-8'
        )

    return LIBRARY_DIR


def promote_to_library(
    characters_dir: Path,
    identifier: str,
    source_session: str = ''
) -> Path:
    """
    Promote a session character to the hub-level library.

    Copies stable traits, strips session-specific state (Session Log entries).
    Adds origin tracking metadata.

    Args:
        characters_dir: Path to session's characters/ directory
        identifier: Character slug or name
        source_session: Name/path of source session for tracking

    Returns:
        Path: Path to library character file

    Raises:
        FileNotFoundError: If character not found in session
    """
    import shutil

    # Read from session
    meta, body = read_character(characters_dir, identifier)

    # Strip session-specific state
    # Remove Session Log content (keep header)
    lines = body.split('\n')
    cleaned_lines = []
    in_session_log = False
    session_log_table_started = False

    for line in lines:
        if line.strip().startswith('## Session Log'):
            in_session_log = True
            cleaned_lines.append(line)
            continue

        if in_session_log:
            # Keep the header row and separator, skip data rows
            if line.strip().startswith('|') and not session_log_table_started:
                cleaned_lines.append(line)
                if '---' in line:
                    session_log_table_started = True
                continue
            elif line.strip().startswith('## '):
                # New section starts — end of session log
                in_session_log = False
                session_log_table_started = False
                cleaned_lines.append(line)
                continue
            elif line.strip().startswith('|') and session_log_table_started:
                # Skip data rows
                continue
            elif not line.strip():
                cleaned_lines.append(line)
                continue
            else:
                cleaned_lines.append(line)
                continue
        else:
            cleaned_lines.append(line)

    cleaned_body = '\n'.join(cleaned_lines)

    # Add library metadata
    meta['source_session'] = source_session
    meta['promoted'] = datetime.now().strftime('%Y-%m-%d')
    meta['appearances'] = [source_session] if source_session else []
    meta['updated'] = datetime.now().strftime('%Y-%m-%d')

    # Ensure library directory exists
    library_dir = create_library_folder()

    # Write to library
    slug = slugify(meta.get('name', 'unnamed'))
    filepath = library_dir / f'{slug}.md'

    # Handle collision
    if filepath.exists():
        counter = 2
        while (library_dir / f'{slug}-{counter}.md').exists():
            counter += 1
        filepath = library_dir / f'{slug}-{counter}.md'

    content = render_frontmatter(meta) + '\n' + cleaned_body
    filepath.write_text(content, encoding='utf-8')

    # Rebuild library index
    rebuild_library_index()

    return filepath


def import_from_library(
    identifier: str,
    characters_dir: Path,
    session_name: str = ''
) -> Path:
    """
    Import a library character into a session.

    Creates a session-local copy with a fresh Session Log.
    Tracks the appearance in the library character's metadata.

    Args:
        identifier: Character slug or name in library
        characters_dir: Target session's characters/ directory
        session_name: Name of importing session for tracking

    Returns:
        Path: Path to session-local character file

    Raises:
        FileNotFoundError: If character not found in library
    """
    library_dir = create_library_folder()

    # Read from library
    meta, body = read_character(library_dir, identifier)

    # Strip library-only metadata for the session copy
    session_meta = {k: v for k, v in meta.items()
                    if k not in ('source_session', 'promoted', 'appearances')}
    session_meta['imported_from'] = 'library'
    session_meta['updated'] = datetime.now().strftime('%Y-%m-%d')

    # Reset Session Log to empty (fresh for this session)
    if '## Session Log' in body:
        lines = body.split('\n')
        new_lines = []
        in_session_log = False
        for line in lines:
            if line.strip().startswith('## Session Log'):
                in_session_log = True
                new_lines.append(line)
                new_lines.append(_SESSION_LOG_HEADER)
                new_lines.append('')
                continue
            if in_session_log:
                if line.strip().startswith('## '):
                    in_session_log = False
                    new_lines.append(line)
                continue
            new_lines.append(line)
        body = '\n'.join(new_lines)

    # Write to session
    characters_dir = Path(characters_dir)
    characters_dir.mkdir(parents=True, exist_ok=True)

    slug = slugify(meta.get('name', 'unnamed'))
    filepath = characters_dir / f'{slug}.md'

    if filepath.exists():
        counter = 2
        while (characters_dir / f'{slug}-{counter}.md').exists():
            counter += 1
        filepath = characters_dir / f'{slug}-{counter}.md'

    content = render_frontmatter(session_meta) + '\n' + body
    filepath.write_text(content, encoding='utf-8')

    # Update session manifest
    rebuild_manifest(characters_dir)

    # Track appearance in library copy
    if session_name:
        _track_library_appearance(identifier, session_name)

    return filepath


def _track_library_appearance(identifier: str, session_name: str):
    """Track that a library character appeared in a session."""
    library_dir = create_library_folder()
    try:
        meta, body = read_character(library_dir, identifier)
        appearances = meta.get('appearances', [])
        if isinstance(appearances, str):
            appearances = [appearances]
        if session_name not in appearances:
            appearances.append(session_name)
        update_character(library_dir, identifier,
                         metadata={'appearances': appearances})
    except Exception:
        pass  # Non-fatal


def rebuild_library_index() -> dict:
    """
    Rebuild the hub-level library index from .md files.

    Returns:
        dict: The rebuilt library index
    """
    library_dir = create_library_folder()

    index = {
        'version': 1,
        'generated': datetime.now().isoformat(),
        'characters': {}
    }

    for md_file in sorted(library_dir.glob('*.md')):
        if md_file.name.startswith('_'):
            continue

        try:
            content = md_file.read_text(encoding='utf-8')
        except Exception:
            continue

        meta, _ = parse_frontmatter(content)
        if not meta.get('name'):
            continue

        slug = md_file.stem
        tags = meta.get('tags', [])
        if tags is None:
            tags = []
        appearances = meta.get('appearances', [])
        if appearances is None:
            appearances = []

        index['characters'][slug] = {
            'name': meta.get('name', slug),
            'role': meta.get('role', 'npc'),
            'status': meta.get('status', 'active'),
            'tags': tags,
            'file': md_file.name,
            'source_session': meta.get('source_session', ''),
            'promoted': meta.get('promoted', ''),
            'appearances': appearances,
        }

    # Write index
    index_path = library_dir / '_library_index.json'
    try:
        fd, temp_path_str = tempfile.mkstemp(
            dir=str(library_dir),
            prefix='.tmp_',
            suffix='.json'
        )
        temp_path = Path(temp_path_str)
        with os.fdopen(fd, 'w', encoding='utf-8') as f:
            json.dump(index, f, indent=2, ensure_ascii=False)
            f.flush()
            os.fsync(f.fileno())
        os.replace(str(temp_path), str(index_path))
    except Exception:
        index_path.write_text(
            json.dumps(index, indent=2, ensure_ascii=False),
            encoding='utf-8'
        )

    return index


def list_library(role: str = None, tag: str = None) -> list:
    """
    List all characters in the hub-level library.

    Args:
        role: Filter by role
        tag: Filter by tag

    Returns:
        list: List of library character dicts
    """
    library_dir = create_library_folder()
    index_path = library_dir / '_library_index.json'

    if not index_path.exists():
        index = rebuild_library_index()
    else:
        try:
            index = json.loads(index_path.read_text(encoding='utf-8'))
        except Exception:
            index = rebuild_library_index()

    characters = list(index.get('characters', {}).values())

    if role:
        characters = [c for c in characters if c.get('role') == role]
    if tag:
        characters = [c for c in characters if tag in c.get('tags', [])]

    return characters


# Allow running as script for testing
if __name__ == '__main__':
    print("Character Manager - Character Sheet CRUD Operations")
    print("-" * 50)
    print(f"Valid roles: {VALID_ROLES}")
    print(f"Valid statuses: {VALID_STATUSES}")
    print(f"Template sections: {TEMPLATE_SECTIONS}")
    print(f"Genre modules: {list(GENRE_MODULES.keys())}")
    print(f"Max slug length: {MAX_SLUG_LENGTH}")

    # Test slugify
    test_names = ['Elara Voss', "Dr. James O'Brien", '', 'A' * 100]
    print("\nSlugify tests:")
    for name in test_names:
        print(f"  '{name}' -> '{slugify(name)}'")
