# Loom Studio — Requirements (living document)

**Status:** requirements capture, in progress.
**Purpose:** The evolving ground truth for what Loom Studio must do — the owner's wants, captured as they are spec'd, ahead of gap analysis and design decisions.
**Relationship to [`../README.md`](../README.md):** The README is an early, opinionated design spec. This document captures the owner's stated wants; where the two diverge, the divergence is flagged here for reconciliation during gap analysis rather than silently resolved.

## 1. What Loom Studio is
A local **viewer and editor** for the files that make up a Loom project.

## 2. Core capabilities
The user can:
- **Open** an existing project.
- **Configure** a project.
- **Create** a new project — which instantiates a new project directory pre-populated with all the boilerplate AI documentation/config an assistant needs to work with the project.

## 3. Project scaffolding — multi-assistant boilerplate
Creating a new project stands up a fresh project directory containing the boilerplate "AI docs" that AI tools require to operate on the project — targeting the broader assistant ecosystem (Claude, ChatGPT/Codex, Gemini, etc.), not a single vendor.

## 4. Scope & phasing
- **Claude-first.** Design and build against Claude tooling first.
- **OpenAI (and others) next.** Expand to the OpenAI spec after a working proof of concept; other assistants follow.

## 5. Human-in-the-loop consistency — PROBLEM TO SOLVE
**Want:** when a human edits a project file out-of-band (in vim / Obsidian / the Studio editor / etc.), the agent should be made aware and kept consistent — *without* the agent having to re-read edited files on every turn.

**Upstream reality (verified against `WintersRain/loom` @ HEAD, 2026-07):** loom does **not** do this, and its design is the inverse.
- Wired hooks: `UserPromptSubmit`, `Stop`, `PostToolUse(Write|Edit)`, `SessionStart`.
- `PostToolUse(Write|Edit)` → `auto_save.py` fires only on the **agent's own** Write/Edit tool calls (it stamps session state); a human edit fires no tool event, so nothing detects it.
- There is **no filesystem watcher** — no watchdog/inotify/mtime/hash/diff logic anywhere in the hooks.
- loom's consistency strategy is exactly the "re-read every time" behavior this want tries to avoid: `UserPromptSubmit` reminds the model to "READ character sheets before writing," and `CLAUDE.md` declares the on-disk sheets "the AUTHORITATIVE source of truth… after compaction, re-read sheets."

**Root cause:** Claude Code's hook model has no event that fires on an external/human file change — hooks fire on session lifecycle and on the agent's own tool use — so upstream loom cannot notify the agent of a human edit when it happens; the earliest it re-reads is the next `UserPromptSubmit` (or `SessionStart`).

**Therefore:** mid-conversation "agent stays consistent with human edits without constant re-reads" is an **open problem Loom Studio must solve**, not something inherited. (This aligns with the README's own §3 note that filesystem watching is the "safety net" because "hooks only cover agent-originated writes," including "the user's own edits.") Solution directions are deferred to the design phase.

## Open tensions (to revisit during gap analysis)
- The README's observability mechanism (HTTP hooks, transcript tailing, subagent visibility) is Claude Code-specific, but the multi-assistant scaffolding want (§3) is broader. How "observe a running session" generalizes beyond Claude is unresolved and deferred.
- §5 human-edit awareness is unsolved upstream and bounded by Claude Code's hook events; carrying it to other assistants (§4) compounds it.
