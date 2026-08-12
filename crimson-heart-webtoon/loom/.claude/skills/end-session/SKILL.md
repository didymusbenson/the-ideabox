---
name: end-session
description: End and archive current roleplay session
trigger: "end session|archive session|done with session|finish session|wrap up"
---

# End Session Skill

Archive the current session quickly and cleanly.

## When User Wants to End Session

### Step 1: Identify Current Session

Check for active session in state:

```python
import json
from pathlib import Path

state_file = Path('.writing/state/session.json')
if state_file.exists():
    state = json.loads(state_file.read_text())
    active_project = state.get('active_project')
```

If no active_project in state, ask user:
```
"Which session are you wrapping up?"
```

### Step 2: Brief Confirmation

Keep it quick - just name and genre:

```
"Archive [session-name] ([genre])? (yes/no)"
```

### Step 3: Archive the Session

```python
import sys
sys.path.insert(0, '.claude/hooks')
from session_manager import archive_session
from pathlib import Path

archived_path = archive_session(Path(session_path))
# Session folder renamed: {date}_{session_name}
# session.json updated: status='archived', archived_at=timestamp
```

### Step 4: Clear State

Update session.json to remove active_project:

```python
import json
from pathlib import Path

state_file = Path('.writing/state/session.json')
if state_file.exists():
    state = json.loads(state_file.read_text())
    state['active_project'] = None
    state_file.write_text(json.dumps(state, indent=2))
```

### Step 5: Confirm Completion

```
"Archived [session-name] to [genre]/[date]_[session-name]. Ready for next session anytime!"
```

## Example Flow

**User:** "let's wrap up this session"

**Claude:** "Archive vampire-librarian (dark-romance)? (yes/no)"

**User:** "yes"

**Claude:** "Archived vampire-librarian to dark-romance/2026-02-04_vampire-librarian. Ready for next session anytime!"

## Key Points

- **Quick and silent** - Don't make archival ceremonial
- **Content preserved** - Nothing deleted, just reorganized
- **Discoverable** - User can always find it via list-sessions skill
- **Date prefix** - Makes chronological browsing easy
- **Auto-archive** - When starting new session in same genre, old one auto-archives (via check_archive_needed)

## Auto-Archive Behavior

Note: Users don't always explicitly end sessions. The system handles this automatically:

When starting a new session in a genre that has an active session, `check_archive_needed()` auto-archives the old one first. This skill is for explicit endings when user wants to be intentional about wrapping up.
