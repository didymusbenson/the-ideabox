---
name: restore-state
description: Manually restore session state from a backup
---

# Restore State

When the user invokes `/restore-state`, help them recover from a previous backup.

## Steps

1. **List available backups** in `.writing/state/backups/`:
   - session.json.1 (most recent)
   - session.json.2
   - session.json.3 (oldest)

   For each backup, show:
   - Whether it exists
   - File size (as sanity check)
   - Whether JSON is valid

2. **Ask which backup to restore** (default: most recent valid)

3. **Perform restoration**:
   - Copy selected backup to `.writing/state/session.json`
   - Confirm restoration with backup timestamp

4. **Show restored state summary**:
   - Active project (if any)
   - Last position
   - When it was saved

## Example Output

```
Available backups:
  1. session.json.1 - 2.3 KB, valid JSON
  2. session.json.2 - 2.1 KB, valid JSON
  3. session.json.3 - does not exist

Which backup to restore? (1-3, or 'cancel'): 1

Restored from session.json.1
  Project: My Novel
  Position: Chapter 4, Scene 2
  Saved: 2026-02-03 14:30:00
```

## When to Use

- Auto-save captured unwanted state changes
- Corruption recovery didn't pick the right backup
- User wants to roll back to earlier point
- Debugging state issues
