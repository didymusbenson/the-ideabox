---
name: new-scene
description: Create a new scene file with proper header and update scene_log.md.
---

# New Scene

Create a new scene file and update the scene log.

## When to Use

- Starting a new scene
- User says "new scene" / "next scene"
- Scene naturally ends and new one begins

## Process

1. Check scene_log.md for current scene number
2. Create new scene file: `scenes/Scene_XXX.md`
3. Add header to new scene file
4. Update scene_log.md with new entry

## New Scene File Format

```markdown
# Scene [NUMBER]: [TITLE]

**Location**: [Where]
**Time**: [When]
**Characters Present**: [Who]

---

**Setup**: [1-2 sentences of initial situation]

---

[Scene content will be appended here]
```

## Scene Log Entry Format

Add to the Scene Index table:

```markdown
| [#] | [Title] | [Summary - fill later] | - | Active |
```

## Scene Numbering

- Use 3-digit format: 001, 002, 003...
- Check existing files to avoid duplicates

## Rules

- Always update both the new file AND scene_log.md
- Set previous scene status to "Complete"
- Leave Summary as "-" initially (fill when scene ends)
