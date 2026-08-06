---
name: save-scene
description: Persist current roleplay state. MUST be called after every narrative scene.
---

# Save Scene - State Persistence Workflow

This skill ensures roleplay events are persisted to source-of-truth files.

## When to Use

**MANDATORY after:**
- Any scene with dialogue or action
- Any state change (relationship, location, time)
- Any character observation about MC
- Before ending a session

**The user can invoke with:** `/save-scene`

## Workflow

Execute these agents/updates in sequence:

### 1. Update Tracker
Update `relationship_tracker.md` with any MC state changes:
- Emotional/physical state
- Relationship progression
- New key moments

### 2. Update Observations
Append to `observations.md` what the character learned about MC:
- New details observed
- Patterns noticed
- Preferences revealed

### 3. Append to Scene File
Append the narrative to the current scene file in `scenes/`.

### 4. Update Scene Log
Update `scene_log.md` with the scene entry.

### 5. Update Character Sheets
Log any NPC developments to their character sheets in `characters/`.

## Output

After completion, confirm:
```
Scene saved:
- Tracker: [changes or "no changes"]
- Observations: [X] new entries
- Scene file: [lines] appended
- State: cleared
```

## Critical Rule

**If this workflow is not run, events exist only in conversation and WILL BE LOST on session end or context compaction.**
