---
name: tracking-formats
description: File format templates for roleplay tracking files. Preload when updating state.
user-invocable: false
---

# Tracking File Formats

## relationship_tracker.md Structure

```markdown
# Relationship Tracker: [NPC Name] & MC

## Current Status

**MC State**: [Level/Description]
**Resistance Level**: [High/Medium/Low/None]
**Physical Comfort**: [Description]
**Emotional State**: [Current feeling]

## Progression Tracking

### Key Moments

| Scene | Event | Impact | Category |
|-------|-------|--------|----------|
| 001 | [What happened] | [Effect] | Connection/Resistance/Comfort |

### Resistance Moments
| Scene | What MC Resisted | Outcome |
|-------|-----------------|---------|

### Connection Moments
| Scene | What Happened | Significance |
|-------|---------------|--------------|

## MC's State Tracking

### Current Concerns
- [Active worry]

### Things MC Has Accepted
- [Accepted element]

### Things MC Has Asked For
- [Request]

## Notes
[Additional observations]
```

## scene_log.md Structure

```markdown
# Scene Log

## Current Scene
**Number**: [XXX]
**Title**: [Name]
**Status**: Active

## Scene Index

| # | Title | Summary | Key Events | Status |
|---|-------|---------|------------|--------|
| 001 | [Title] | [Brief summary] | [Major events] | Complete |
| 002 | [Title] | - | - | Active |

## Timeline

### [Date/Time Period]
- Scene [X]: [What happened]
- Scene [Y]: [What happened]
```

## observations.md Structure

```markdown
# [NPC Name]'s Observations About MC

## Physical Details
- [Observed physical trait]

## Behavioral Patterns
- [Pattern noticed]

## Preferences
- [Like/dislike identified]

## Tells
- [Signal when lying/nervous/comfortable]

## Scene-by-Scene Log

### Scene 001 - [Context]
- [Observation]
- [What it means to character]

### Scene 002 - [Context]
- [Observation]
```

## world.md Structure

```markdown
# World of [Session Name]

## Locations

### [Location Name]
[Description]
*Established: Scene X*

## Factions & Groups

### [Group Name]
[Description, structure, goals]
*Established: Scene X*

## Characters (NPCs)

### [NPC Name]
[Brief description, role]
*Established: Scene X*

## History & Lore

### [Topic]
[Content]
*Established: worldbuild agent*

## World Rules

### [System/Rule]
[How it works]

## Miscellaneous
[Other details]
```

## Update Rules

1. **APPEND, never overwrite** - History matters
2. **Include scene references** - Track where details came from
3. **Be specific** - Vague entries are useless
4. **Cross-reference** - Link related entries
5. **Maintain formatting** - Consistency aids readability

## Character Sheet Format

### YAML Frontmatter (machine-queryable)

```yaml
---
name: [Character Name]          # REQUIRED — only required field
role: pc | npc | antagonist | supporting | minor
status: active | inactive | deceased | unknown
tags: [tag1, tag2]
created: YYYY-MM-DD
updated: YYYY-MM-DD
---
```

### Sections (all optional)

| Section | Content | Notes |
|---------|---------|-------|
| Identity | Full name, age, occupation, first appearance | Structured fields |
| Aspects | FATE-style evocative phrases | High Concept, Trouble, Relationship |
| Appearance | Physical description, style | Freeform prose |
| Personality | Core traits, quirks, values, fears | Structured fields |
| Voice | Speech pattern, vocabulary, signature phrases | Includes examples |
| Background | Backstory relevant to current story | Freeform prose |
| Relationships | Connections to other characters | Table format |
| Session Log | Chronological development tracker | Auto-populated by Claude |

### Genre Modules (optional, appended when relevant)

| Module | When Used | Key Fields |
|--------|-----------|------------|
| Romance | Romance/dark-romance sessions | Attraction, love language, boundaries |
| Powers & Abilities | Fantasy/sci-fi sessions | Type, abilities, limitations, source |
| Methods & Resources | Thriller/intrigue sessions | Skills, resources, network, weaknesses |

### Cast Manifest (_cast_manifest.json)

```json
{
  "version": 1,
  "generated": "ISO-timestamp",
  "characters": {
    "slug-name": {
      "name": "Display Name",
      "role": "npc",
      "status": "active",
      "tags": ["tag1"],
      "file": "slug-name.md",
      "created": "YYYY-MM-DD",
      "updated": "YYYY-MM-DD"
    }
  }
}
```

### Character Update Rules

1. **Only `name` is required** — a character sheet with just frontmatter name is valid
2. **Sections are optional** — omit sections that have no content yet
3. **Manifest is auto-rebuilt** — never edit _cast_manifest.json directly
4. **Use character_manager.py** — all CRUD goes through the module, not direct file edits
5. **Include scene references** — log where character details were established
