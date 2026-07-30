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

### Target scenario & the lightweight-pull goal (owner-confirmed)
The owner's primary workflow, and the case this must optimize:

1. The owner prompts the agent to write a chapter; the agent works through a long turn.
2. During or after that turn, the owner makes human edits in the Studio editor. Studio **saves** them — persists the edit to the project file on disk *and* records it as a human-originated delta in the change-log (coalesced per editing session, not per keystroke; echo-suppressed from the agent's own writes).
3. When the owner returns and prompts again, the accumulated deltas are injected at `UserPromptSubmit`, and the agent picks up where the human left it.

**Turn-gated delivery is acceptable here by design.** The owner does not expect, or want, mid-turn interruption; edits made while the agent writes simply wait for the next prompt. So `UserPromptSubmit` injection (§5) is the primary path for this workflow; §7's `PreToolUse` / autonomous-run handling stays a recorded edge case, not the target.

**The win is content-level, not just scoping.** The goal is not merely "re-read fewer files" but "**do not re-read the lengthy files at all**." Two grades of light:
- *Lighter:* inject "world.md changed" → the agent re-reads world.md (skips unchanged files, but still re-reads the lengthy changed one).
- *Lightest (the goal):* inject the **diff itself** → the agent patches its understanding from those few lines and does not re-open the file.

So change-log entries must carry the **changed content** (a diff / the edited region), and the injection inlines that diff — not just a "these files changed" pointer.

**Why inlining the diff is sound:** the agent already holds the pre-edit version of the file in context (it read it when it started the chapter), so the diff is meaningful against that baseline and no full re-read is needed.

**Fallback:** if the baseline is not in context — after a compaction, or for a file the agent never read this session — a bare diff has nothing to anchor to. Rule: **diff-first, fall back to a targeted file-read only when the baseline is missing.**

## 6. One backbone, many features (architectural observation)
*(Forward-looking observation, to validate in design — not a locked decision.)*

The §5 change-log/injection pattern is not a one-off. Most of Studio's features are combinations of **two primitives** — a read side and a write side — so the "Studio watches → writes a delta → injects at turn start" pipe is really the first end-to-end use of a backbone that powers much more.

**Primitive A — the change-feed (read / observe).** One normalized timeline of everything Studio can observe about a session, merged from the three input feeds:
- agent tool events (HTTP hooks — `PreToolUse`, `PostToolBatch`, `SubagentStop`, …),
- transcript deltas (tailing the session JSONL),
- human / external filesystem edits (fs-watch, echo-suppressed).

**Primitive B — the control surface (write / inject).** The hook-response points where Studio can talk *back* to the agent:
- `UserPromptSubmit` — inject context at turn start (the §5 delta; reminders),
- `PreToolUse` — `permissionDecision` (allow / deny / ask), `updatedInput` (replace the pending tool args), `additionalContext` (feed a reason back on deny).

Nearly every Studio feature is A, B, or A+B:

| Feature | A: change-feed (read) | B: control surface (write) |
|---|---|---|
| Activity panel | ✓ agent events + transcript | — |
| Panel repaints (scene log, characters, world, observations) | ✓ fs-watch + `PostToolBatch` | — |
| Human-edit awareness (§5) | ✓ fs-watch human edits → log | ✓ `UserPromptSubmit` injects the delta |
| Pending-write preview / diff | ✓ `PreToolUse.tool_input` | ✓ `permissionDecision` allow/deny/ask |
| Inline rewrite of agent output | ✓ `PreToolUse.tool_input` | ✓ `updatedInput` replaces args before write |
| Deny-with-reason steering | — | ✓ `deny` + `additionalContext` |
| Autocommit / revisions | ✓ `Stop` / `PostToolBatch` triggers | — (git side-effect) |
| Alternate timelines | downstream of revisions (git) | — |

**Why this matters:**
- **Build order.** Ship the read side first (Primitive A → Activity panel, live repaints) — that is already a useful, read-only tool. Add the write side later (Primitive B → gating, rewrite, deny-with-reason, and the §5 injection). This matches the README's phase plan (observer in Phases 1–2, interaction in Phase 5).
- **§5 is the natural vertical slice.** It is the first feature that threads both primitives end-to-end (fs-watch → log → inject), so building it proves the whole architecture rather than a corner of it.
- **Cross-assistant (§4).** Both primitives are, today, plumbed through Claude Code's hook/transcript model. The *concepts* (observe a session; inject at defined control points) should carry to ChatGPT/Codex/Gemini, but the *channels* will differ per assistant. Claude-first now; treat A and B as the portable abstractions and re-implement their transports later.

## 7. Considered & set aside — an in-session "log-watcher" agent
*(Evaluated during requirements capture; not adopted. Recorded so it is not re-proposed. Includes the refinement it motivates.)*

**The idea:** run a background subagent inside the session that polls the change-log for hash changes and pipes detected human edits back to the primary agent — giving mid-run awareness without waiting for the user's next prompt.

**Why it does not beat the §5 hook approach:**
- **Same turn-gating.** A subagent cannot inject into the primary agent's *active* context. Its findings reach the primary only as a returned result / background-task notification, which the primary absorbs at a step boundary — never mid-generation. (Directly observable: background helper agents report back at turn boundaries, not mid-response.) The watcher relocates *where* watching happens, not *when* the primary can absorb it — and `UserPromptSubmit` / `PreToolUse` already provide that boundary for free.
- **Worse detector than Studio.** Detection belongs in Studio, which watches the filesystem mechanically (real OS events, no polling) and knows write-origin for echo suppression. An in-session polling loop re-implements this less accurately, cannot cleanly tell human writes from agent writes, and burns tokens every iteration.
- **Breaks the core separation.** The design keeps Studio observing and the agent writing, converging on the same bytes with no protocol between them. Putting a watcher *inside* the agent runtime couples the two and loses that.
- **No better cross-assistant story.** A Claude subagent poller is as Claude-specific as a hook, and more fragile.

**The kernel worth keeping — inject at `PreToolUse`, not only `UserPromptSubmit`.** The real gap the watcher idea chases is *long autonomous runs*: the agent works many internal turns with no user prompts, so `UserPromptSubmit` never fires and human edits pile up unseen. The platform-native fix is not a polling agent but an additional injection point — a Studio `PreToolUse` hook that, before each Write/Edit, drains unconsumed human deltas from the §5 log and returns them as `additionalContext`. It is deterministic, fires at every tool call, costs nothing when the log is empty, and needs no background process. Detection stays in Studio; the trigger stays in hooks; the §5 log is the shared state. Net rule: inject at **both** `UserPromptSubmit` (turn start) **and** `PreToolUse` (each tool call) to close the autonomous-run hole.

## Open tensions (to revisit during gap analysis)
- The README's observability mechanism (HTTP hooks, transcript tailing, subagent visibility) is Claude Code-specific, but the multi-assistant scaffolding want (§3) is broader. How "observe a running session" generalizes beyond Claude is unresolved and deferred.
- §5 human-edit awareness is only softly handled upstream (best-effort re-read on the next prompt, scoped to named files, at full re-read cost) and bounded by Claude Code's hook events; carrying it to other assistants (§4) compounds it.
