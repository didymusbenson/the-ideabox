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

**Project creation also initializes version control.** Scaffolding runs `git init` and makes an initial commit as part of setting up the project, so the repo exists from commit one. This is a hard prerequisite, not an optional step: every version-control-backed capability — named snapshots, the Track-Changes-style review flow, and Alternate Timelines (§9) — depends on the project being a git repo from the start. Scaffolding also writes a `.gitignore` covering Studio's `settings.local.json` and the ephemeral session change-log, so local and ephemeral state never enters the project's history. For **Open Existing Project**, if the folder is not already a git repo, Studio offers to initialize one — version-control-backed features stay unavailable until it is.

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

## 8. Interface layout & the manuscript centerpiece (owner sketch)
*(From an owner-provided wireframe; an initial approximation, to refine. Transcribed here as ASCII + prose since the source image is not stored in-repo.)*

Tabs and pages organized by **content category**, with the **manuscript as the primary centerpiece** and reference material kept visually available alongside it.

```
+-------------+------------------+--------------------------+----------------+
| LEFT RAIL   | REFERENCE PANEL  | MANUSCRIPT (centerpiece) | RIGHT RAIL     |
|             |                  |                          |                |
| Worldbuild- | Open worldbuild- | Open manuscript page,    | Story Pages /  |
| ing tabs    | ing file, shown  | navigated by PAGE-TURN   | Table of       |
| ----------- | in full and kept | (prev / next chapter or  | Contents       |
| Project /   | visible alongside | file)                   | directory      |
| Meta files  | the manuscript   |                          |                |
| tab         |                  | [ Editing toolbar, nav,  |                |
|             |                  |   controls ]             |                |
+-------------+------------------+--------------------------+----------------+
```

### Regions
1. **Left rail — category navigation (tabbed).** Content grouped by category: a **Worldbuilding tabs** group and a **Project / Meta files** group. Selecting an entry opens it in the reference panel. Navigation is organized by category, not one flat file tree.
2. **Reference panel — an open info / wiki / worldbuilding file, in full.** These files open here and **stay visually available** next to the manuscript, so lore is on-screen while reading or writing. A persistent companion pane — not a modal or a transient popover. It is a **file-preview zone for non-story content**, **read-only by default** (it opens a read-only copy of the file). An **Edit** button toggles inline edit mode; changes **save on exiting edit mode** or via manual save (button / shortcut). This read-first-by-default posture guards non-story files against accidental edits, and it stands in deliberate contrast to the manuscript centerpiece, which is edit-capable with an always-present toolbar — two intentional editing postures. Two payoffs: (a) the enter-edit → exit-edit (or manual-save) boundary is exactly the "editing session" §5 coalesces one human-edit delta around; (b) edits made here (e.g. `world.md`) are human edits that feed the same §5 change-log and next-turn inline-diff pull as the manuscript, just on non-story files.
3. **Manuscript — the centerpiece.** Its own **special view**, distinct from the other panels, with the prose as the focus. Navigated by **page-turning** — previous / next loads the adjacent chapter or file rather than scrolling one long document or clicking through a tree. An **editing toolbar + nav + controls** anchors the bottom of this view. The manuscript is editable here, and owner edits made in this pane are exactly the human edits §5 logs and pulls — the centerpiece view and the change-log/inline-diff loop are the same surface.
4. **Right rail — story structure.** A **Story Pages / Table of Contents** directory of the manuscript (chapters / scenes / files), used to jump within the book.

### Notes & things to pin down later
- **Manuscript vs. reference are deliberately different surfaces** — a book-like page-turning reader/editor for prose, versus persistent reference panes for worldbuilding/meta. Not one generic file viewer.
- **Page-turn order needs a source of truth.** "Previous / next chapter" implies a defined sequence — resolve it from the manifest and/or frontmatter (`scene_number`, chapter) per §4, not filename sort alone.
- **Maps onto the README §7 panels, re-arranged:** manuscript ≈ Scene editor (promoted to centerpiece); reference panel ≈ World / Characters / Observations; right rail ≈ Scene log / project explorer.
- **Not yet placed in this sketch:** the Activity panel (live agent observer) and the pending-write / diff surface from README §7 — where they live (a collapsible strip, a toggled mode, etc.) is an open layout question.
- Whether multiple reference files can be open at once is also open.

## 9. Alternate Timelines — parallel story versions (core value proposition)
*(Owner-elevated to a headline value prop. Surfaces git branches as writer-facing "timelines"; the word "branch" never appears in the UI.)*

**The pitch:** a writer can keep **more than one version of their story alive at once** and **hop freely between them**. "What if she takes the deal" and "what if she doesn't" are two timelines the writer maintains in parallel — switches between, compares side by side, and carries work forward in whichever they prefer — without copying files, renaming folders, or losing either version. No other authoring tool offers this, because none store prose as plain files in a repo; Loom does, so Studio gets it almost for free. This is one of the two headline capabilities that *are* git, and a core reason git is the chosen substrate rather than a bespoke store — not a nice-to-have.

**Core interactions (writer vocabulary; git stays hidden):**
- **New timeline from here** — fork a parallel version from any snapshot or point in the story (git: branch).
- **Switch / hop** — jump between timelines; the manuscript centerpiece shows the active one (git: checkout).
- **Compare** — view two timelines side by side and diff them (e.g. chapter 9 in "Darker ending" vs "Original"), using the prose-aware diff from the version-control layer.
- **Bring across** — pull a scene / chapter from one timeline into another, or merge a whole timeline back into the main one (git: cherry-pick / merge), through the same accept / review flow used for agent proposed-revisions.
- **Name & curate** — timelines carry writer names ("Darker ending," "Romance subplot"), never ref names.

**Relationship to agent "proposed revisions":** both are git branches underneath, but different lifecycles and UX — *proposed revisions* are short-lived agent drafts you accept or discard; *alternate timelines* are long-lived parallel versions you deliberately maintain and hop between. Keep them visually distinct so they do not blur. (The proposed-revisions / Track-Changes review model is discussed and pending its own section.)

**Design notes to pin down later:**
- **Divergence point matters.** A timeline forks from a specific snapshot; that anchor is what makes "compare timelines" meaningful. Track it and show it.
- **The agent writes into whatever timeline is checked out.** Switching timeline swaps the files on disk, which the agent re-reads (ties to §5). Studio must make the active timeline unmissable, so an agent never writes prose into the wrong version — a mis-scoped write here is costly. First-class UX concern, not a detail.
- **Autosave / shadow history and snapshots resolve against the active timeline** and must not leak across timelines.

## 10. Loom View — the branch visualizer (git history as a woven loom)
*(Owner want. The signature visual, and the payoff of a loom-themed name: the git commit graph rendered as an actual loom.)*

**The picture:** the project's git history drawn as a **weave** — timelines are the threads running through the project, **bookmarks** (commits) are the knots along each thread, and fork / merge points are where threads split off and weave back together. The git DAG is a loom; Loom View simply draws it as one. This is the home base for managing the §9 alternate timelines, and the concrete reason a loom-themed name fits.

**What it shows:** the story's development over time — every timeline, where each forked, where any merged back, which timeline is active now, and *what happened* along the way: human vs. agent edits and which agent (the provenance already written into commit trailers, per README §8).

**Interactive, in author language (git primitives, zero git words):**
- **Hop** — click a thread to switch to that timeline (git: checkout).
- **Go back to a bookmark** — return to an earlier save point (see the safety rule below).
- **New timeline from here** — fork a parallel version from any bookmark (git: branch); the §9 "new timeline from here."
- **Compare** — select two bookmarks or timelines to diff, via the prose-aware diff layer.

**Bookmarks = commits, with a message.** A deliberate save prompts the author for a **bookmark message** (the writer-facing commit message). Loom View surfaces those messages — hover a knot to read one, or toggle labels on to see them along the threads. ("Bookmark" is the same concept the version-control model calls a curated snapshot / save point; the term will be unified when that section is written.)

**Only bookmarks and timelines are woven.** Deliberate saves (bookmarks) and named timelines are the only things drawn on the loom. Autosaves stay in the silent background shadow layer and are never rendered as threads — otherwise thousands of keystroke-commits bury the weave and it stops being readable.

**Design constraints to honor:**
- **"Go back to a bookmark" must be non-destructive.** A naive rollback (git hard reset) silently discards everything after that point — catastrophic for a writer. Going back must restore *forward-safely* — fork a new timeline from the bookmark, or restore it into a new save — and never discard later work unless the author explicitly chooses to.
- **The weave must stay legible.** Real git graphs get tangled; Loom View renders only named timelines + bookmarks, with collapsing / filtering so a long project does not become spaghetti. (Reinforces the shadow-autosave separation above.)
- **Provenance markers.** Indicate on threads / knots whether a change was human- or agent-authored (and which agent), so "what happened throughout the project" is legible at a glance.

## 11. First-time setup — git readiness (detect first, prompt only if needed)
*(Owner want. A one-time onboarding check that Loom's git substrate is usable, run before it matters.)*

Every version-control-backed capability (§3 git init, §9 timelines, §10 Loom View, bookmarks, autosave) needs a working, identity-configured git. Most users arrive already set up — anyone who has used Cowork, Codex, or Claude Code almost certainly has git and an identity — so this must be **silent when things are fine, and surface only when something is actually missing.**

**Detection first (the default is: do nothing).** On first launch, Studio probes:
- `git` is present and runnable (`git --version`).
- A committer identity exists (`git config user.name` and `user.email` both resolve to non-empty values).

If both hold, git is usable — **Studio says nothing and never shows the setup UI.** No nag, no wizard. (Owner requirement.)

**Prompt only for what is missing:**
- **No git →** a plain explainer ("Loom uses git to track your progress and power your timelines") plus per-platform install guidance. A hard blocker — git is the substrate — so it is explained, not glossed. Studio cannot silently install git; it points the user and re-checks.
- **No identity →** a two-field in-app form (name, email) that Studio applies via `git config`. "What name should we sign your saves with?" No account, no signup, no server — a local identity is all local commits need. This is the simplest path and the default.

**Optional: connect GitHub.** The prompt may offer to connect a GitHub account for backup / sharing / pushing timelines off-machine. Clearly optional and skippable; local-only is fully functional without it.

**Three kinds of "credential" — keep them straight (important):**
- **Git identity** (name + email) — not a secret, just commit authorship. Studio sets this. Required for commits.
- **GitHub auth** (optional) — a real credential, but only for git *remote* push, never for model access. To preserve the "Studio never stores or transmits credentials" property (README §1), Studio must **delegate to the system git credential helper / `gh` / OS keychain and never store or transmit the token itself.**
- **Model-provider credentials** (Anthropic / OpenAI keys, Claude auth) — Studio **never** touches these. This is the §1 constraint that keeps Loom out of third-party authentication restrictions, and nothing in first-run setup changes it. Git identity and optional GitHub auth are unrelated to model auth.

**Notes to pin down later:**
- Whether to support the optional GitHub connect **in the POC** or defer it — it adds credential-helper plumbing and platform variance for a non-essential (local git is enough). Candidate defer.
- The identity Studio sets here tags **human** commits on the Loom View; agent (Claude Code) commits carry their own identity — the human-vs-agent provenance §10 draws depends on these being separate.
- Re-probe on each launch (cheap), so a later-broken setup (e.g. identity cleared) is caught — still silent when fine.

## Open tensions (to revisit during gap analysis)
- The README's observability mechanism (HTTP hooks, transcript tailing, subagent visibility) is Claude Code-specific, but the multi-assistant scaffolding want (§3) is broader. How "observe a running session" generalizes beyond Claude is unresolved and deferred.
- §5 human-edit awareness is only softly handled upstream (best-effort re-read on the next prompt, scoped to named files, at full re-read cost) and bounded by Claude Code's hook events; carrying it to other assistants (§4) compounds it.
