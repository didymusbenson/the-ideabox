---
name: new-book
description: Create a new book project with scaffolding. Use when user wants to start a new book, novel, or long-form writing project.
---

# New Book Project

Create a new book project with full scaffolding.

## Trigger

User wants to start a new book, novel, or long-form writing project.

## Steps

1. Gather from user (through conversation, NOT a form):
   - Working title or concept
   - Genre

2. Generate a kebab-case project name from the title/concept.

3. Create the project using the book_session helper:

```python
import sys; sys.path.insert(0, '.claude/hooks')
from book_session import create_book_project

project_path = create_book_project(
    project_name="kebab-case-name",
    working_title="The Working Title",
    genre="sci-fi"
)
```

This creates the full directory structure:

```
_books/[project-name]/
  .state/
    project.json
  CHARACTERS/
  SCENES/
  CLAUDE.md          # Project-specific instructions
  world.md           # Worldbuilding bible
```

4. Update `.writing/state/session.json` to set `active_project` to the new project name:

```python
from state_manager import read_state, write_state

session = read_state('session.json')
session['active_project'] = "kebab-case-name"
session['mode'] = 'book'
write_state('session.json', session)
```

5. Begin worldbuilding conversation or writing - whatever the user wants to do next.

## Notes

- Project name should be short, descriptive, kebab-case
- Don't over-scaffold - the user will build out content through conversation
- If the user has already been discussing worldbuilding, capture that into world.md immediately
- After creation, route to the continue-project skill to load resume context

## Examples

**User:** "I want to start a new sci-fi book about a colony ship"

**Action:**
1. Ask for working title (or suggest one from the concept)
2. Confirm genre (sci-fi, from context)
3. Create project: `create_book_project("colony-ship", "Colony Ship", "sci-fi")`
4. Set active project in session state
5. Begin worldbuilding: "Let's build this world. Tell me about the colony ship..."

**User:** "new book"

**Action:**
1. Ask: "What's the concept? Give me a title, genre, or just a vibe."
2. User responds with details
3. Create project from their response
4. Begin writing flow

## Related Skills

- **hub-entry** - Routes "start a book" inputs here
- **continue-project** - Resume an existing book project
- **end-session** - Archive session when done writing
