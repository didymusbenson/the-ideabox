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

## 5. Human-in-the-loop consistency
**Want:** when a human edits a project file out-of-band (in vim / Obsidian / the Studio editor / etc.), the agent should stay consistent with that edit — ideally *without* paying to re-read every file on every turn.

**Does the edit-then-prompt flow already work upstream? Mostly yes.** If the user edits a file and *then* sends a prompt, loom's `UserPromptSubmit` hook re-injects an orchestrator protocol that instructs the agent to "EXPLORE FIRST: Read characters/, tracking files, scene state" before writing (and `CLAUDE.md` declares the on-disk files the authoritative source of truth). So the agent is told to re-read those files on the next turn and generally picks up the human's edit. Consistency is maintained for that flow.

**But the guarantee is soft, and it is exactly the re-read cost the want tries to avoid:**
- **Prose-instructed, not mechanical.** Nothing *detects* the edit; the agent only re-reads because a reminder tells it to. Compliance is best-effort — under context pressure, or when the model "remembers" a file from earlier in the conversation, it can answer from stale in-context content and miss the edit.
- **Scoped to the files loom names.** The protocol covers `characters/`, tracking files, and scene state. An edit to a file outside those classes is not guaranteed to be re-read.
- **Costs a full re-read every turn.** Consistency is bought by re-reading everything each response — the token/latency tax the want explicitly wants to shed.
- **Nothing mid-turn.** The earliest re-read is the next `UserPromptSubmit`; an edit made while the agent is working is not seen until the user prompts again. (Fine for edit-then-prompt; a gap for edit-during-turn.)

**Verified upstream facts:** loom wires `UserPromptSubmit`, `Stop`, `PostToolUse(Write|Edit)`, `SessionStart`. `PostToolUse(Write|Edit)` → `auto_save.py` fires only on the agent's **own** Write/Edit calls; a human edit fires no tool event. There is **no filesystem watcher** anywhere in the hooks. Root cause: Claude Code's hook model has no event for an external/human file change, so nothing can notify the agent at the moment a human edits a file.

**Loom Studio's opportunity:** make edit-awareness *mechanical and cheap* instead of *blanket and prose-driven* — e.g. Studio watches the filesystem, knows exactly which file a human changed, and can surface or target just that delta — rather than relying on the agent re-reading everything every turn and hoping it complies. A leading candidate direction is captured below.

### Candidate approach — Studio-watched change-log, injected at turn start
*(Proposal, owner-proposed. Not a locked decision — to confirm during the design phase.)*

**Key correction:** AI tools do not "watch" or subscribe to files — they *pull* (read on their own turn). So the watcher is **Studio**, not the agent; Studio hands the agent a delta at the next turn boundary.

**Shape (reuses two things Studio must build anyway — fs-watching and hooks):**
1. Studio's filesystem watcher (a core feature) detects human-originated edits, **echo-suppressed** so agent-originated and Studio-originated writes are excluded — only human edits are logged.
2. Studio appends each human edit to a small, append-only **session change-log** (e.g. `.loom/session-log.jsonl`) — bite-sized entries: file path, changed section, timestamp, optional diff.
3. A Studio-owned `UserPromptSubmit` hook injects the **unconsumed** entries into the agent's context at the start of each turn ("since your last turn, the human edited `world.md` → Magic System"), then marks them consumed. The agent reads only those files — or none, if the diff is inlined.

**Why it fits "bite-sized + consistent":**
- **Bite-sized** — a few delta lines per turn, not a full re-read of every tracker.
- **Consistent** — mechanical detection (fs-watch) replaces prose-hoping; the agent is *handed* the change, not reminded to go look for it.
- **Targeted** — only the files that actually changed.

**Constraints to honor:**
- **Still turn-gated.** Delivery is at `UserPromptSubmit`/`SessionStart` only; a human edit made mid-turn waits for the next prompt. Inherent to Claude Code's hook model.
- **Consume/ack semantics.** The log needs a "seen" marker so the same edit is not re-injected every turn.
- **Echo suppression is load-bearing.** Never feed the agent its own (or Studio's) writes.
- **Placement.** The hook is Studio's → `settings.local.json` (gitignored); the log is ephemeral session state → gitignored, never committed project content.
- **Cross-assistant (§4).** The log file is portable; the injection channel is Claude-specific (`UserPromptSubmit`). ChatGPT/Codex/Gemini need their own equivalent (system-prompt / context-file injection). Claude-first now, generalize later.

**Simpler-but-softer alternative:** have Studio write a single `RECENT_CHANGES.md` and instruct the agent (via `CLAUDE.md`) to read it each turn. Less plumbing (no consume-tracking hook), but it reverts to best-effort compliance — the exact softness §5 is trying to eliminate. Injection is preferred.

## Open tensions (to revisit during gap analysis)
- The README's observability mechanism (HTTP hooks, transcript tailing, subagent visibility) is Claude Code-specific, but the multi-assistant scaffolding want (§3) is broader. How "observe a running session" generalizes beyond Claude is unresolved and deferred.
- §5 human-edit awareness is only softly handled upstream (best-effort re-read on the next prompt, scoped to named files, at full re-read cost) and bounded by Claude Code's hook events; carrying it to other assistants (§4) compounds it.
