---
name: hub-entry
description: Natural language entry point for Writing Hub
---

# Hub Entry

Accept any natural language input and route to the appropriate writing mode.

## Trigger

This skill activates for ANY initial user input, including:
- "vampire romance tonight" (quick session)
- "continue my-novel chapter 4" (book project)
- "something dark and obsessive" (quick session)
- "back to my novel" (book project)
- "quick session with a demon" (quick session)
- "dark romance" (ambiguous - clarify)

## Flow

### 1. Route the Input

```python
import sys; sys.path.insert(0, '.claude/hooks')
from input_router import route_input

result = route_input(user_input)
# Returns: RoutingResult with mode, confidence, project_name, entry_type, clarification
```

### 2. Handle by Mode

**If result.mode == 'book' and result.project_name is None:**
- No project yet - user wants to CREATE a new book
- Route to **new-book** skill (`/new-book`)
- Gather title, genre through conversation
- Create project scaffolding, then begin writing

**If result.mode == 'book' and result.project_name is set:**
- Project identified: follow continue-project skill
- Run continue_project.py with result.project_name
- Read project files, resume context
- Ready to write

```python
from mode_switcher import switch_mode

# Switch to book mode and load project
switch_result = switch_mode('book', result.project_name)
if 'error' not in switch_result:
    # Route to continue-project skill
    # Run: python .claude/hooks/continue_project.py {result.project_name}
    pass
```

Then follow the **continue-project** skill to load resume context.

**If result.mode == 'session':**
- Follow quick-session skill
- Use result.entry_type and result.initial_concept
- Begin conversational shaping (2-3 questions max)
- Create scaffold and start writing

Route to **quick-session** skill with the user's input for character/situation/vibe detection.

**If result.mode == 'ambiguous':**
- Present result.clarification['message'] to user
- Wait for user to pick option (1, 2) or provide more detail
- Re-route based on clarification
- Never guess - always clarify when uncertain

Show the clarification message directly:

```
{result.clarification['message']}
```

### 3. Handle Clarification Response

When user responds to clarification:

**If user says "1" or "2":**
- Look up corresponding option in result.clarification['options']
- Route directly to that mode

**If user provides more detail:**
- Re-run route_input() with new input
- Continue from step 2

## Mode Switching Mid-Session

When user is already in a mode and wants to switch:

```python
from mode_switcher import switch_mode

# This handles:
# - Archiving quick session if leaving quick mode
# - Updating hub state
# - Recording switch history
switch_result = switch_mode(new_mode, target)

if 'error' in switch_result:
    # Report error (e.g., project not found)
    print(f"Error: {switch_result['error']}")
    if 'available' in switch_result:
        print(f"Available: {', '.join(switch_result['available'])}")
else:
    # Proceed with new mode
    # Route to appropriate skill (quick-session or continue-project)
    pass
```

## Rules

1. **Speed over ceremony** - Get to writing fast
2. **Never guess wrong** - Clarify if uncertain (confidence < 0.6)
3. **Accept deferrals** - "you decide" is valid input
4. **One clarification max** - If still unclear after one question, default to session

## Disambiguation Patterns

When clarification needed, use this format:
> I'm not sure what you'd like to do. Did you mean to:
>
> 1. **Continue your book project** "[project-name]"?
> 2. **Start a quick session** with "[concept]" as the starting idea?
>
> Just say "1" or "2", or tell me more!

## Session vs Project Heuristics

**Signals pointing to BOOK:**
- Project name mentioned (even partial)
- "continue", "resume", "back to", "work on"
- Chapter/scene reference
- Specific character names from existing projects

**Signals pointing to SESSION:**
- "tonight", "quick", "something"
- Mood/vibe words without project context
- Character archetypes (vampire, maid, demon)
- Situation descriptions (trapped, arranged, fake)

**When signals conflict:** Ask clarifying question

## Examples

### Example 1: Clear Book Project (with project name)

**User:** "continue my-novel chapter 4"

**Routing:**
```python
result = route_input("continue my-novel chapter 4")
# result.mode = 'book'
# result.confidence = 0.9
# result.project_name = 'my-scifi-novel'
# result.chapter = '4'
```

**Action:**
1. `switch_mode('book', 'my-scifi-novel')`
2. Route to continue-project skill with chapter 4 context

---

### Example 2: Clear Quick Session (character-first)

**User:** "vampire romance tonight"

**Routing:**
```python
result = route_input("vampire romance tonight")
# result.mode = 'session'
# result.confidence = 0.9
# result.entry_type = 'character'
# result.initial_concept = 'vampire romance tonight'
```

**Action:** Route to quick-session skill - character-first entry

---

### Example 3: Clear Quick Session (situation-first)

**User:** "trapped in elevator with my boss"

**Routing:**
```python
result = route_input("trapped in elevator with my boss")
# result.mode = 'session'
# result.confidence = 0.75
# result.entry_type = 'situation'
# result.initial_concept = 'trapped in elevator with my boss'
```

**Action:** Route to quick-session skill - situation-first entry

---

### Example 4: Ambiguous Input (shows clarification)

**User:** "dark romance"

**Routing:**
```python
result = route_input("dark romance")
# result.mode = 'ambiguous'
# result.confidence = 0.4
# result.clarification = {
#     'message': "I'm not sure what you'd like to do. Did you mean to:\n\n1. ..."
# }
```

**Action:** Show result.clarification['message'] and wait for user choice

---

### Example 5: Implicit Continue (uses last active project)

**User:** "continue"

**Routing:**
```python
result = route_input("continue")
# result.mode = 'book'
# result.project_name = 'my-scifi-novel'  # from session.json active_project
# result.reasoning = "Keyword 'continue' + implicit continue of last project"
```

**Action:** Route to continue-project skill with last active project

---

### Example 6: Rich Input (skips questions)

**User:** "shy librarian trapped in the library after hours with a mysterious stranger who might be a ghost"

**Routing:**
```python
result = route_input("shy librarian trapped...")
# result.mode = 'session'
# result.entry_type = 'situation'
# result.initial_concept = full input
```

**Action:** Route to quick-session skill - input is rich enough to skip shaping questions

## Notes

- This skill is the **MAIN entry point** for the writing system
- Quick sessions go to `_sessions/[genre]/[session-name]/`
- Book projects live in `_books/[project-name]/`
- Hub state tracked in `.writing/state/session.json`
- Per-project state tracked in `[project]/.state/project.json`

## Related Skills

- **new-book** - Create a new book project with scaffolding
- **quick-session** - Conversational flow for starting casual sessions
- **continue-project** - Resume context loading for book projects
- **list-sessions** - Browse and search past sessions
- **end-session** - Explicit session archive (quick sessions auto-archive on mode switch)
