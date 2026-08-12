# Loom

A self-contained creative writing system for [Claude Code](https://docs.anthropic.com/en/docs/claude-code). Start Claude in this directory, describe what you want to write, and it handles the rest — routing, file management, character tracking, and scene continuity.

## Requirements

- [Claude Code](https://docs.anthropic.com/en/docs/claude-code) (Anthropic's CLI tool)
- An Anthropic API key or Claude Pro/Max subscription

## Quick Start

1. **Clone this repo** (or download and extract):
   ```
   git clone https://github.com/WintersRain/loom.git
   cd loom
   ```

2. **Set your character name** in `.claude/hooks/config.py`:
   ```python
   MC_NAME = "Alex"              # Your character's name (or "MC" to stay anonymous)
   CHARACTER_POV = "the NPCs"    # Who Claude writes as (leave default unless you know what you're doing)
   ```

3. **Start Claude Code** in the loom directory:
   ```
   claude
   ```

4. **Tell it what you want to do.** That's it. Examples:
   - `a cunning thief with a secret agenda` — starts a new creative session
   - `something dark and mysterious` — starts from a vibe
   - `trapped in a castle with a stranger` — starts from a situation
   - `continue the vampire librarian session` — resumes a past session
   - `work on my sci-fi novel chapter 4` — opens a book project
   - `show my sessions` — lists everything you've done

## How It Works

When you type something, Loom figures out what you mean:

- **New session?** It asks 2-3 quick shaping questions (character, situation, vibe), creates a session folder, builds character sheets, and starts writing.
- **Resume session?** It finds your past session, loads the context, and picks up where you left off.
- **Book project?** It loads your project state, open plot threads, and active characters.

Claude coordinates a team of 6 specialized sub-agents (writer, analyzer, creator, strategist, state, router) — it doesn't write prose directly, it orchestrates and quality-checks.

## Session Structure

Sessions are auto-organized by genre under `_sessions/`:

```
_sessions/
  fantasy/
    vampire-librarian/        # Active session
      session.json            # Metadata
      scenario.md             # Setup (character, situation, vibe)
      characters/             # Character sheets (auto-created)
      SCENES/                 # Your scene files
      relationship_tracker.md # Tracks progression
      observations.md         # What characters know about each other
      scene_log.md            # Scene index
      world.md                # Worldbuilding notes
  thriller/
  romance/
  dark-romance/
  scifi/
  contemporary/
  uncategorized/
```

When you start a new session in a genre that already has one, the old session is automatically archived with a date prefix. Nothing is ever deleted.

## Book Projects

For longer, structured work, book projects live in `_books/`:

```
_books/my-novel/
  .state/        # Project state (auto-managed)
  CHARACTERS/    # Character sheets
  SCENES/        # Chapter/scene files
```

## Commands

Use these during a session:

| Command | What it does |
|---------|-------------|
| `/save-scene` | Save current state |
| `/new-scene` | Start a new scene file |
| `/character list` | Show all characters |
| `/character show [name]` | View a character sheet |
| `/character create [name]` | Create a new character |
| `/list-sessions` | Browse past sessions |
| `/end-roleplay` | End session tracking |
| `/update-tracker` | Update relationship tracker |
| `/update-world` | Add worldbuilding details |

## Character System

- Every named character with dialogue gets a character sheet automatically
- NPC details are developed freely by Claude and logged to sheets
- **Your character's sheet is sacred** — Claude never invents details about your character. Empty fields stay empty until you fill them.
- Characters can be promoted to a cross-session library (`/character promote [name]`) and imported into new sessions (`/character import [name]`)

## Out-of-Character Communication

Use double parentheses to speak out of character:

```
((she should be more aggressive in this scene))
((my character has green eyes))
((OOC: let's skip ahead to the next morning))
```

Claude will drop out of prose and respond directly.

## What's in the Box

| Directory | Purpose |
|-----------|---------|
| `.claude/agents/` | 6 sub-agents (writer, analyzer, creator, strategist, state, router) |
| `.claude/hooks/` | Python hooks that fire on events (auto-save, state tracking, prompt injection) |
| `.claude/skills/` | Slash commands (listed above) |
| `_sessions/` | Your creative sessions, organized by genre |
| `_books/` | Book projects |
| `_characters/` | Cross-session character library |

## Configuration

The only file you need to edit is `.claude/hooks/config.py`. Everything else is managed automatically.

## License

MIT
