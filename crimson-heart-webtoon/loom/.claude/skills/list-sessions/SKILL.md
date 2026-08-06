---
name: list-sessions
description: Browse and resume past roleplay sessions
trigger: "show sessions|list sessions|past sessions|find session|my sessions"
---

# List Sessions Skill

Show user their past sessions and help them resume one.

## When User Asks for Past Sessions

### Step 1: Ask for Genre Filter (Optional)

Available genres:
- dark-romance
- romance
- fantasy
- scifi
- thriller
- contemporary
- uncategorized
- **all** (show everything)

```
"Which genre? Or 'all' to see everything."
```

If user seems to want specific genre, use it. If unclear, show all.

### Step 2: Call list_sessions

```python
import sys
sys.path.insert(0, '.claude/hooks')
from session_manager import list_sessions
from pathlib import Path

sessions = list_sessions(Path('_sessions'), genre='dark-romance')  # or None for all
```

### Step 3: Display as Table

Format results:

| Name | Genre | Status | Created | Scenes |
|------|-------|--------|---------|--------|
| vampire-librarian | dark-romance | active | 2026-01-15 | 5 |
| shy-librarian-trapped | romance | archived | 2026-01-10 | 3 |

**Notes:**
- Show name without date prefix (more readable)
- Status: "active" or "archived"
- Created: just the date, not full timestamp (or "unknown" if missing)
- Scenes: number of .md files in SCENES/ folder

### Step 4: Offer to Resume

```
"Want to continue one of these? Just tell me which."
```

Wait for user to pick. Accept partial names like "vampire" or "librarian".

## Resume Flow

When user picks a session:

### Step 1: Find Session Path

```python
from session_manager import get_session_path
from pathlib import Path

session_path = get_session_path(Path('_sessions'), 'vampire')
# Returns: _sessions/dark-romance/vampire-librarian
```

### Step 2: Load Context

Read these files from the session:

1. **scenario.md** - The setup (character, situation, vibe)
2. **Highest-numbered scene** - Where they left off

```python
from pathlib import Path

session_dir = Path(session_path)

# Read scenario
scenario_file = session_dir / 'scenario.md'
scenario = scenario_file.read_text() if scenario_file.exists() else None

# Find last scene (highest number)
scenes_dir = session_dir / 'SCENES'
if not scenes_dir.exists():
    scenes_dir = session_dir / 'scenes'

scenes = sorted(scenes_dir.glob('*.md'))
last_scene = scenes[-1].read_text() if scenes else None
```

### Step 3: Summarize and Continue

Tell user where they left off:

```
"Found it! In [session-name], you were:
[Brief summary from scenario.md]

Your last scene was [scene-name]:
[2-3 sentence summary of what was happening]

Ready to continue? Pick up where we left off or start a new scene?"
```

Then continue writing from that point.

## Example Output

**User:** "Show me my sessions"

**Claude:** "Which genre? Or 'all' to see everything."

**User:** "dark romance"

**Claude:**

| Name | Genre | Status | Created | Scenes |
|------|-------|--------|---------|--------|
| vampire-librarian | dark-romance | active | - | 5 |
| fallen-angel | dark-romance | archived | - | 8 |
| trapped-elevator | dark-romance | archived | - | 12 |

"Want to continue one of these? Just tell me which."

**User:** "vampire"

**Claude:** "Found it! In vampire-librarian, you had a shy vampire scenario at the library. Your last scene was THE_AFTER_HOURS where [summary]. Ready to continue?"

## Key Points

- Use _sessions as the sessions directory
- Partial name matching works (user says "vampire", finds "vampire-librarian")
- Sessions without session.json are legacy - infer status from folder name
- Don't make this feel formal - keep it conversational
