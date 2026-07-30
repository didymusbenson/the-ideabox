# Continue Project Skill

Resume a book project exactly where you left off.

## Trigger

User says any of:
- "continue [project-name]"
- "continue my-novel"
- "resume [project]"
- "back to [project]"
- "work on [project]"

## Usage

1. Run the continue_project command:
   ```bash
   python .claude/hooks/continue_project.py [project-identifier]
   ```

2. The command outputs resume context including:
   - Last scene and section
   - Open plot threads
   - Active characters
   - Key files to read

3. Read the key project files mentioned in the output:
   - CLAUDE.md (project instructions)
   - relationship_tracker.md (if exists)
   - scene_log.md (if exists)
   - characters/_cast_manifest.json (if exists) — load all character sheets
   - Any recent scene files

4. Read all character sheets in `characters/` — these are **ground truth** that survive compaction:
   ```python
   from character_manager import list_characters, read_character
   chars = list_characters(project_path / 'characters')
   for c in chars:
       meta, body = read_character(project_path / 'characters', c['file'].replace('.md', ''))
       # Character sheet values override conversation memory
   ```

4. You are now ready to continue writing!

## Project Identifiers

Projects can be found by partial name:
- "scifi" finds "my-scifi-novel"
- "dragon" finds "dragon-chronicles"

If ambiguous or not found, the command lists available projects.

## During Session

Update position when moving to new scene:
```python
from book_session import update_position
update_position(project_path, scene='04_New_Scene', section='opening')
```

Add plot threads as they emerge:
```python
from book_session import add_thread
add_thread(project_path, "Mysterious message from Atlas", characters=['Atlas', 'Aria'])
```

Update thread status when resolved:
```python
from book_session import update_thread
update_thread(project_path, 'mysterious-message-from-atlas', status='resolved', resolution_scene='04_2')
```

Track character focus changes:
```python
from book_session import update_character_focus
update_character_focus(project_path, ['Aria', 'Marcus', 'the Entity'])
```

Set current story arc:
```python
from book_session import update_current_arc
update_current_arc(project_path, 'The Betrayal Arc')
```

## End Session

When user ends writing session:
```python
from book_session import end_book_session
end_book_session(project_path, scenes_written=['04_1', '04_2'], word_count_delta=3500)
```

## Example

User: "continue my-novel"

1. Run: `python .claude/hooks/continue_project.py my-novel`
2. Read output (last scene, threads, files)
3. Read CLAUDE.md and tracking files
4. Ready to write!

User: "let's write the next scene"

1. Update position: `update_position(project, scene='04_1_NewScene')`
2. Write the scene
3. Auto-save handles persistence

User: "we're done for today"

1. End session: `end_book_session(project, scenes_written=['04_1_NewScene'], word_count_delta=2500)`
2. State preserved for next time

## Thread Status Values

- **active** - Thread is currently being developed
- **simmering** - Thread exists but not actively progressed
- **resolved** - Thread reached its conclusion
- **dropped** - Thread was abandoned (explain in notes)

## State Location

Project state lives in the project folder at `.state/project.json` for portability.
Hub tracks active project in `.writing/state/session.json`.
