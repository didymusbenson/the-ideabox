---
name: end-roleplay
description: End a roleplay session. Saves final state and archives if needed.
---

# End Roleplay Session

This skill cleanly ends a roleplay session.

## What It Does

1. Runs `/save-scene` for any unsaved narrative
2. Confirms session ended
3. Optionally archives the session

## When to Use

Run `/end-roleplay` when:
- Finished playing for the day
- Switching to a different session or project
- Before closing Claude

## Before Ending

**IMPORTANT**: Make sure all narrative has been saved. This skill will run `/save-scene` automatically if needed.

## Resuming Later

To continue the roleplay in a new session:
1. Start Claude in this directory
2. Say "continue [session name]" or use `/list-sessions` to find it
3. Claude loads the session context and picks up where you left off
