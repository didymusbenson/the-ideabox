---
name: start-roleplay
description: Initialize a roleplay session. Reads state and prepares for play.
---

# Start Roleplay Session

This skill initializes state tracking for a roleplay session.

## What It Does

1. Reads character sheets in `characters/`
2. Reads tracking files (relationship_tracker.md, observations.md, scene_log.md, world.md)
3. Identifies the current scene state
4. Prepares Claude to write in-character

## When to Use

Run `/start-roleplay` at the beginning of any roleplay session, or when resuming.

## After Starting

During the session:
1. After ANY narrative response, update tracking files
2. Run `/save-scene` after each narrative beat
3. Character sheets are ground truth -- re-read after compaction

## Session Lifecycle

```
/start-roleplay          -> Read state, prepare context
     |
Write narrative          -> Launch writer agent
     |
Update tracking          -> Mandatory after every scene
     |
/save-scene              -> Persist everything
     |
/end-roleplay            -> Archive when done
```

## End Session

Run `/end-roleplay` when finished.
