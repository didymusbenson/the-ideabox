---
name: story
description: Quick Story Starter - Begin a new scene with minimal setup.
---

# Quick Story Starter

Start a new scene quickly with just a prompt.

## When to Use

- Beginning a new session
- Jumping to a new scene mid-session
- User says `/story [setup]`

## Process

1. Parse the user's setup prompt
2. Check scene_log.md for current scene number
3. Create new scene file with basic header
4. Write an opening 2-3 paragraphs establishing:
   - Setting (where/when)
   - Character's current state
   - A hook or moment of interest
5. End with an opening for MC to respond

## Input Format

User provides: `/story [brief setup description]`

Examples:
- `/story morning after the party`
- `/story confrontation in the garden`
- `/story first meeting at the market`

## Output

Write the opening directly. No meta-commentary.

### Scene File Header
```markdown
# Scene [NUMBER]: [Title from setup]

**Location**: [Inferred from setup]
**Time**: [Inferred from setup]
**Characters Present**: the NPC character, MC

---
```

### Opening Prose
2-3 paragraphs that:
- Ground the reader in the moment
- Show the NPC character doing something
- Create a natural entry point for MC

## After Writing

1. Update scene_log.md with new scene
2. Mark state as dirty
3. Run `/save-scene` to persist

## Quality

- Match the character's established voice from the first line
- Use sensory details to establish mood
- Don't over-explain - let the scene breathe
- End on something that invites MC response
