# Writing System

> Start Claude Code in this directory. Tell it what you want to do. It handles the rest.

---

## How It Works

This folder is a self-contained writing system. You start Claude here and use natural language:

- **"a cunning thief with a secret agenda"** -- starts a new creative session
- **"continue the haunted library session"** -- resumes an existing session
- **"work on my sci-fi novel chapter 4"** -- opens a book project
- **"show my sessions"** -- lists past sessions

Claude routes your input, creates files in the right place, and manages everything.

---

## Directory Structure

```
.
├── .claude/                    # System infrastructure (DO NOT EDIT unless you know what you're doing)
│   ├── agents/                 # 6 sub-agents (writer, analyzer, creator, strategist, state, router)
│   ├── hooks/                  # Python hooks that fire on events
│   │   ├── config.py           # EDIT THIS — MC name, POV character, coaching agents
│   │   ├── user_prompt_reminder.py   # Fires BEFORE every response (injects rules)
│   │   ├── stop_check_state.py       # Fires AFTER every response (save reminders)
│   │   ├── auto_resume.py            # Fires on session start (loads state)
│   │   ├── auto_save.py              # Fires after file edits (auto-save state)
│   │   ├── state_manager.py          # Centralized state/path management
│   │   ├── session_manager.py        # Session creation, archival, search
│   │   ├── book_session.py           # Book project session management
│   │   ├── character_manager.py      # Character sheet CRUD + library ops
│   │   ├── input_router.py           # Natural language intent detection
│   │   ├── mode_switcher.py          # Switch between session/book modes
│   │   ├── project_state.py          # Per-project state for books
│   │   └── continue_project.py       # Resume book project context
│   ├── skills/                 # Skills (slash commands)
│   │   ├── hub-entry/          # Main entry point — routes natural language input
│   │   ├── quick-session/      # Start a casual roleplay session
│   │   ├── list-sessions/      # Browse and resume past sessions
│   │   ├── continue-project/   # Resume a book project
│   │   ├── start-roleplay/     # Begin session tracking
│   │   ├── end-roleplay/       # End session tracking
│   │   ├── end-session/        # Archive current session
│   │   ├── save-scene/         # Persist state after narrative
│   │   ├── new-scene/          # Create new scene file
│   │   ├── story/              # Story guidance
│   │   ├── character/          # Character sheet management (/character list, show, create, promote, import)
│   │   ├── character-voice/    # Voice consistency (agent-preloaded)
│   │   ├── tracking-formats/   # File format templates (agent-preloaded)
│   │   ├── update-tracker/     # Update relationship_tracker.md
│   │   ├── update-observations/# Log character observations
│   │   ├── update-world/       # Add worldbuilding details
│   │   └── restore-state/      # Recover from state issues
│   └── settings.json           # Hook wiring (auto-configured)
│
├── _sessions/                  # Roleplay sessions organized by genre
│   ├── dark-romance/           # Genre folders
│   │   ├── vampire-librarian/  # Active session (no date prefix)
│   │   └── 2026-01-15_old-session/  # Archived session (date prefix)
│   ├── romance/
│   ├── fantasy/
│   ├── scifi/
│   ├── thriller/
│   ├── contemporary/
│   └── uncategorized/
│
├── _books/                     # Book projects (structured, long-form)
│   └── my-scifi-novel/
│
├── _characters/                # Cast library (cross-session character storage)
│                               # Characters promoted from sessions live here
│
├── _archive/                   # Archived old files (reference only)
│
├── .writing/                   # Runtime state (auto-managed)
│   └── state/                  # Session state JSON files
│
├── characters/                 # Template character sheets (copied into new sessions)
├── scenes/                     # Template scenes folder (copied into new sessions)
│
├── CLAUDE.md                   # THIS FILE — system instructions
├── relationship_tracker.md     # Template — copied into new sessions
├── scene_log.md                # Template — copied into new sessions
├── observations.md             # Template — copied into new sessions
└── world.md                    # Template — copied into new sessions
```

---

## Session Structure

Each roleplay session gets its own folder under `_sessions/[genre]/[session-name]/`:

```
_sessions/dark-romance/vampire-librarian/
├── session.json                # Metadata (genre, status, created date)
├── scenario.md                 # Setup (character, situation, vibe)
├── characters/                 # Character sheets for THIS session
│   ├── _cast_manifest.json     # Character index
│   ├── elena-nightshade.md     # NPC character sheet
│   └── mc.md                   # PC character sheet
├── SCENES/                     # Scene files
│   └── 01_The_Library.md
├── relationship_tracker.md     # Session-specific tracking
├── observations.md             # Session-specific observations
├── scene_log.md                # Session-specific scene log
└── world.md                    # Session-specific worldbuilding
```

---

## Book Project Structure

Each book project gets its own folder under `_books/[project-name]/`:

```
_books/my-scifi-novel/
├── .state/                     # Project state
├── CHARACTERS/                 # Character sheets
├── SCENES/                     # Chapter/scene files
└── [project-specific files]
```

---

## Configuration

**Edit ONE file:** `.claude/hooks/config.py`

```python
MC_NAME = "MC"                         # Your character's name
CHARACTER_POV = "the NPCs"             # Who Claude writes as
```

That's it. The hooks read this file on every prompt.

---

## Orchestrator Role (CRITICAL)

**Claude is a COORDINATOR, not a writer.** Sub-agents do the work. Claude quality-checks and directs.

### The Workflow

1. **Explore first.** Read character sheets in `characters/`, check tracking files, understand scene state.
2. **Assess complexity.** Simple -> writer only. Emotional -> analyzer + writer. Romance -> strategist romance + writer. Unsure -> router.
3. **Launch agents.** Use the 6 consolidated agents. Do NOT write prose yourself.
4. **Evaluate output.** Check against character sheets and continuity. If wrong -> kick back with specific feedback.
5. **Output clean prose.** The user reads in a terminal. Diffs and edits are unreadable as narrative. Always output the final prose as clean text in your response.
6. **After writing: update everything.** Tracking files, character sheets, scene log. Do not ask permission. Just do it.

### What "Wrong" Means

- Contradicts character traits (e.g., silver-tongued character folding awkwardly)
- Breaks continuity (e.g., boots on when they were taken off)
- Violates MC autonomy (writes actions/dialogue user didn't provide)
- Misreads scene tone (e.g., treating real boundary as nervous deflection)

### How to Kick Back

When writer returns something that doesn't fit:

```
Resume the writer agent with feedback:
"This doesn't match [CHARACTER]'s traits. [Specific issue].
She has [relevant trait]. Rewrite with [specific direction]."
```

### Golden Rule

**If it's not written down, it's not an instruction.** Sub-agents don't have full context. Claude must catch mismatches between sub-agent output and established character/continuity.

---

## Agents (6 Consolidated)

Agents live in `.claude/agents/`. Each has modes for different use cases.

| Agent | Purpose | When to Use |
|-------|---------|-------------|
| writer | Write scene responses | Every response (core output) |
| analyzer | Character/story analysis | Before complex scenes |
| creator | Generate content | When stuck or need assets |
| strategist | Tactical analysis | Intrigue, romance, schemes |
| state | Check continuity | Session start, state unclear |
| router | Agent recommendations | Uncertain which agents needed |

### Modes

- `writer` -- simple, standard, deep, polish
- `analyzer` -- quick (default), deep, character, story
- `creator` -- brainstorm, character, world, voice, twist
- `strategist` -- offense, defense, romance, factions
- `state` -- (no modes)
- `router` -- (no modes)

### Typical Flows

| Scene Type | Flow |
|------------|------|
| Simple | writer |
| Emotional | analyzer quick -> writer |
| Major confrontation | state -> analyzer deep -> writer |
| Romance | strategist romance -> writer |
| Political intrigue | strategist factions -> analyzer deep -> writer |
| Stuck/need ideas | creator brainstorm |
| New NPC | creator character |

---

## Skills (Slash Commands)

### User-Invocable

| Skill | Invoke With | Purpose |
|-------|-------------|---------|
| save-scene | `/save-scene` | Persist state after narrative |
| start-roleplay | `/start-roleplay` | Begin session tracking |
| end-roleplay | `/end-roleplay` | End session tracking |
| update-tracker | `/update-tracker` | Update relationship_tracker.md |
| update-observations | `/update-observations` | Log character observations |
| new-scene | `/new-scene` | Create new scene file |
| update-world | `/update-world` | Add worldbuilding details |
| character | `/character [cmd]` | Manage character sheets and cast library |
| list-sessions | `/list-sessions` | Browse and resume past sessions |
| quick-session | `/quick-session` | Start a new casual session |

### Agent-Preloaded (not user-invocable)

| Skill | Purpose |
|-------|---------|
| character-voice | Voice consistency guidelines |
| tracking-formats | File format templates |

---

## Hook System

Four hooks fire automatically:

| Hook | When | What It Does |
|------|------|--------------|
| UserPromptSubmit | Before every response | Injects MC autonomy rules, agent list, orchestrator protocol |
| Stop | After every response | Reminds to save if state is dirty |
| PostToolUse (Write/Edit) | After file edits | Auto-saves state |
| SessionStart | On Claude startup | Loads previous state, finds active sessions |

**Config check:** If `.claude/hooks/config.py` still has placeholder values, you'll see a `CONFIG NOT SET UP` warning.

---

## Character System

**Character sheets are the AUTHORITATIVE source of truth.** They override conversation memory, especially after context compaction.

### Character Sheets

Every session has a `characters/` folder with markdown character sheets (YAML frontmatter + body). Managed by `character_manager.py`.

- **Only `name` is required** -- sparse sheets (minor NPCs) are valid
- **Sections are optional**: Identity, Aspects, Appearance, Personality, Voice, Background, Relationships, Session Log
- **Genre modules** (Romance, Powers, Methods) appended when relevant
- **`_cast_manifest.json`** provides fast lookup

### PC Protection Rules (CRITICAL)

1. **NEVER invent PC details** -- if a field is empty, it stays empty
2. **NEVER populate PC sheet fields** without explicit user input
3. **Write AROUND gaps** -- describe what the PC does, not what they look like
4. **Empty fields are sacred gaps** -- things the user hasn't decided yet
5. **Character sheets override memory** -- after compaction, re-read sheets

### NPC Auto-Logging

Claude develops NPC details freely but **records everything** to character sheets:
- Named characters with dialogue get sheets created automatically
- Core traits logged immediately
- Session Log tracks development chronologically

### Cast Library

Character library at `_characters/`:
- `/character promote [name]` -- Copy stable traits to library, strip session state
- `/character import [name]` -- Import library character with fresh Session Log

---

## OOC Communication

The user can speak out-of-character using double parentheses:

```
((OOC: she should be more aggressive in this scene))
((my character has green eyes))
```

- **`((OOC: text))` or `((text))`** -- both are out-of-character
- **Respond out-of-character** -- drop prose, answer directly
- **Never ignore double parentheses**

### OOC Sidebar Protocol

When a missing PC detail would improve the scene:

```
[OOC: Quick question -- does your character have combat training, or figuring it out as they go?]
```

- Maximum 1 per scene
- Place at end of response
- Offer suggestions

---

## Writing Rules

### Always
- Explore project first -- read character sheets, tracking files, scene state
- Launch agents -- do not write prose yourself
- Update tracking files after every narrative beat -- do not ask permission
- Read character sheets before writing -- they are ground truth
- Stay in character voice
- Leave room for MC to respond
- Log NPC developments to character sheets

### Never
- Write prose yourself -- launch the writer agent
- Write MC's dialogue or actions
- Decide what MC does next
- Break character voice
- Assume MC's internal state
- Invent PC details -- empty PC fields are sacred gaps
- Ask permission for mandatory tasks -- just do them

---

## Session Routing

When user starts Claude in this directory:

1. **Hub-entry skill** reads user input
2. **Input router** detects intent (session vs book vs ambiguous)
3. Routes to appropriate skill:
   - New session -> quick-session (creates `_sessions/[genre]/[name]/`)
   - Resume session -> list-sessions + load context
   - Book project -> continue-project (loads `_books/[project]/`)
   - Ambiguous -> clarifying question (max 1)

### Session Creation Flow

1. User describes concept (character, situation, or vibe)
2. System asks 2-3 shaping questions max
3. Infers genre, generates session name
4. Creates session scaffold in `_sessions/[genre]/[name]/`
5. Creates character sheets
6. Begins writing immediately

### Session Archival

When a session ends or user starts a new one in the same genre:
- Previous session gets date prefix: `vampire-librarian` -> `2026-02-06_vampire-librarian`
- Status updated to "archived" in session.json
- Automatic -- user doesn't manage this

---

## Tracking Files

Each session has these tracking files (templates at project root, copies in each session):

| File | Purpose | Updated When |
|------|---------|-------------|
| `relationship_tracker.md` | MC state, progression, key moments | After every scene |
| `observations.md` | What NPC knows about MC | After every scene |
| `scene_log.md` | Chronological scene index | After every scene |
| `world.md` | Worldbuilding notes, locations, factions | When world details established |

**These MUST be updated after every narrative beat.** Do not ask permission.

---

## Save Workflow (`/save-scene`)

1. Update `relationship_tracker.md` with MC state changes
2. Update `observations.md` with character learnings
3. Append narrative to current scene file
4. Clear dirty flag

---

## Quick Reference

### First Time
```
1. Edit .claude/hooks/config.py (set MC_NAME and CHARACTER_POV)
2. Start Claude in this directory
3. Tell it what you want to do
```

### Session Flow
```
Describe concept -> Shape (2-3 questions) -> Write -> /save-scene -> Continue -> /end-roleplay
```

### Commands
```
/save-scene           Save current state
/start-roleplay       Begin session tracking
/end-roleplay         End session tracking
/character list       Show characters
/character show X     Show character sheet
/list-sessions        Browse past sessions
/creator brainstorm   Get ideas when stuck
/strategist romance   Romance tactics
```
