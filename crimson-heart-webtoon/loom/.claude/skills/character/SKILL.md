---
name: character
description: Manage character sheets — list, show, create, promote to library, import from library
user-invocable: true
---

# Character Management

Manage character sheets for the current session/project and the hub-level cast library.

## Commands

### `/character list` — List characters in current session
```python
import sys; sys.path.insert(0, '.claude/hooks')
from character_manager import list_characters
from pathlib import Path

# Find characters/ in current context (session or project)
# Check common locations:
chars = list_characters(Path('characters'))  # relative to current session/project
```

Display as a table:
```
| Name | Role | Status | Tags |
|------|------|--------|------|
| Elara Voss | npc | active | noble, love-interest |
| MC | pc | active | |
```

### `/character show [name]` — Show a character sheet
```python
from character_manager import read_character
meta, body = read_character(Path('characters'), 'elara-voss')
```

Display the full character sheet (frontmatter + body).

### `/character create [name]` — Create a new character sheet
Ask the user for:
1. Name (required)
2. Role (pc/npc/antagonist/supporting/minor) — default npc
3. Any initial details they want to include

```python
from character_manager import create_character
path = create_character(Path('characters'), name, role=role, sections=sections)
```

Confirm: "Created character sheet at `characters/[slug].md`"

### `/character promote [name]` — Promote to hub library
```python
from character_manager import promote_to_library
lib_path = promote_to_library(
    Path('characters'), 'elara-voss',
    source_session='current-session-name'
)
```

Confirm: "Promoted **Elara Voss** to library at `_characters/elara-voss.md`"

Explain: Stable traits are copied, session-specific state (Session Log) is cleared. The session copy remains unchanged.

### `/character import [name]` — Import from hub library
```python
from character_manager import import_from_library
path = import_from_library('elara-voss', Path('characters'), session_name='current-session')
```

Confirm: "Imported **Elara Voss** from library into `characters/elara-voss.md` with fresh Session Log"

### `/character library` — List hub library characters
```python
from character_manager import list_library
chars = list_library()
```

Display as a table:
```
| Name | Role | Source | Appearances |
|------|------|--------|-------------|
| Elara Voss | npc | dark-romance/noble-intrigue | 3 sessions |
```

## Context Detection

The skill needs to find the correct `characters/` folder:
1. If in a book project: `[project_path]/characters/`
2. If in a quick session: `[session_path]/characters/`
3. For library operations: `_characters/`

Read session state or check current directory context to determine which.

## Notes

- Character sheets use YAML frontmatter + markdown body (see tracking-formats skill)
- Only `name` is required — sparse sheets are valid
- Manifest is auto-rebuilt on every create/update/delete
- Library characters track their origin session and all appearances
- Promoted characters have session-specific state stripped
- Imported characters get a fresh Session Log
