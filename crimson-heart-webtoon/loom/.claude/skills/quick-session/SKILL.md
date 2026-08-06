---
name: quick-session
description: Start a casual creative session in under 60 seconds
---

# Quick Session

Start a quick, casual creative session with minimal setup. Accept any starting point and guide to writing within 60 seconds.

## Entry Points

Works with any initial input:

- **Character-first:** "cunning thief", "cold vampire lord", "shy neighbor"
- **Situation-first:** "trapped in elevator", "fake dating", "arranged marriage"
- **Vibe-first:** "something dark", "light and fun", "slow burn romance"

## Flow

### 1. Accept Initial Input

User provides starting idea in any format. Run entry detection:

```python
import sys; sys.path.insert(0, '.claude/hooks')
from session_manager import detect_entry_type

entry_type = detect_entry_type(user_input)
# Returns: 'character', 'situation', or 'vibe'
```

### 2. Conversational Shaping (2-3 questions max)

Based on entry type, ask follow-up questions to fill gaps:

**Entry: Character-first**
> "What situation brings you together?"
> "What's the vibe - slow burn, intense, playful?"

**Entry: Situation-first**
> "Who are you with - any character ideas?"
> "What's the vibe - awkward comedy, building tension, or...?"

**Entry: Vibe-first**
> "Any character type in mind, or should I suggest?"
> "Any particular situation, or want me to create one?"

### 3. Generate and Scaffold

Once elements gathered (character + situation + vibe):

```python
from session_manager import infer_genre, generate_session_name, create_session_scaffold
from pathlib import Path

# Infer genre from combined elements
genre = infer_genre(character, situation, vibe)

# Generate session name
scenario = {
    'entry_type': entry_type,
    'character': character,
    'situation': situation,
    'vibe': vibe,
    'summary': brief_summary  # Optional, generated if not provided
}
session_name = generate_session_name(scenario)

# Create scaffold
sessions_dir = Path('.') / '_sessions'  # Relative to project root
session_dir = create_session_scaffold(sessions_dir, genre, session_name, scenario)
```

### 4. Character Profiling (Quick Tier)

After scaffolding, create initial character sheets. This is **lightweight** — 1-2 questions woven into the shaping conversation.

```python
from character_manager import create_character
from pathlib import Path

characters_dir = session_dir / 'characters'

# Create NPC sheet from scenario description
create_character(characters_dir, npc_name, role='npc', tags=[genre],
                 sections={'Identity': f'**Full Name:** {npc_name}\n**Occupation/Role:** {npc_role}'})

# Create PC sheet with just what the user provided — NEVER invent details
# Only include what the user explicitly stated
create_character(characters_dir, pc_name or 'MC', role='pc',
                 sections={})  # Empty until user provides details
```

**Quick Tier Rules:**
- Ask **1-2 character questions** max, woven into shaping ("Who are you in this — name, or should I just call you MC?")
- **Immediately flush** user answers to the PC character sheet file
- Create NPC sheets from the scenario description (Claude can invent NPC details freely)
- If user defers ("you decide" for their character), create a bare PC sheet with just `role: pc`

### 5. Start Writing

Begin first scene immediately after profiling.

Show brief confirmation:
> "Starting **[Session Name]** in `_sessions/[genre]/[name]/`"
>
> [Begin opening scene...]

## Rules

### Question Limits
- **Maximum 2-3 questions** before writing starts
- Skip questions if user provides rich enough input
- Combine questions where natural ("Who and what's the vibe?")

### Accept Deferrals
- "you decide" - Claude fills element creatively
- "surprise me" - Claude generates interesting option
- "whatever" - Claude picks reasonable default
- No pushback, just generate and continue

### Minimal Tracking
Quick sessions use lightweight structure:
- `scenario.md` - Setup and summary
- `SCENES/` - Scene content
- `characters/` - Character sheets (auto-created by scaffold)
- `characters/_cast_manifest.json` - Character index

### Genre Override
User can override inferred genre at any point:
- "put this in dark-romance"
- "actually, file under fantasy"
- "move to contemporary"

## Examples

### Example 1: Character-first Entry

**User:** cunning thief with a hidden agenda

**Claude:** (detects character entry)
> A scheming rogue - I like it. What situation brings you into their orbit?

**User:** I'm the merchant lord whose vault they're targeting

**Claude:**
> Perfect setup. What's the vibe - cat and mouse, tense standoff, or pure chaos?

**User:** dark, they're definitely planning something

**Claude:**
> Starting **Cunning Thief Agenda** in `_sessions/thriller/cunning-thief-agenda/`
>
> [Opens with the thief's first day casing the estate...]

### Example 2: Situation-first Entry

**User:** trapped in a broken elevator together

**Claude:** (detects situation entry)
> Classic setup. Who's trapped with you - stranger, coworker, nemesis?

**User:** my boss, we don't get along

**Claude:**
> Boss enemies locked in close quarters. Awkward comedy or building tension?

**User:** tension, definitely tension

**Claude:**
> Starting **Elevator Boss Tension** in `_sessions/contemporary/elevator-boss-tension/`
>
> [Opens with elevator doors closing...]

### Example 3: Vibe-first Entry

**User:** something dark and obsessive, like a villain romance

**Claude:** (detects vibe entry)
> Dark obsession - my favorite flavor. Any character type calling to you? Vampire lord, demon, morally gray human?

**User:** surprise me

**Claude:** (generates character)
> How about a fallen angel who's been watching you? Any particular situation, or want me to set the scene?

**User:** you decide

**Claude:**
> Starting **Fallen Angel Obsession** in `_sessions/dark-romance/fallen-angel-obsession/`
>
> [Opens with protagonist sensing they're being watched...]

### Example 4: Rich Input (Skip Questions)

**User:** I want a shy librarian who gets trapped in the library after hours with a mysterious stranger who might be a ghost

**Claude:** (detects situation entry, but input is rich enough)
> Starting **Shy Librarian Ghost** in `_sessions/fantasy/shy-librarian-ghost/`
>
> [Opens with librarian realizing she's locked in...]

## Session Location

All quick sessions go to:
```
_sessions/[genre]/[session-name]/
  session.json      # Metadata
  scenario.md       # Setup document
  SCENES/           # Scene content
  characters/       # Character sheets (auto-created)
    _cast_manifest.json
```

Genres: dark-romance, romance, fantasy, scifi, thriller, contemporary, uncategorized

## Auto-Archive

When a session ends (user says done, or starts new session in same genre), previous sessions are archived with date prefix:

```
_sessions/dark-romance/
  2026-02-04_old-session/    # Archived (date prefix)
  vampire-librarian/         # Active (no prefix)
```

Archive happens automatically. User doesn't need to manage it.

## Notes

- This skill is for **casual creative sessions**, not structured book projects
- Use `/book` command for projects needing full tracking infrastructure
- Sessions can be promoted to book projects later if they grow
- Previous sessions can be listed and resumed (see list-sessions skill)
