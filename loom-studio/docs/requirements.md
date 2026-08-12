# Loom Studio — Requirements (living document)

**Status:** direction set. Author-first (Course A) is the agreed spine; the per-item resolutions and the engine-as-dependency boundary below are accepted. Individual mechanics still get refined in design, but the shape is no longer open.
**Purpose:** The ground truth for what Loom Studio must do and the direction it is built in.
**Relationship to [`../README.md`](../README.md):** The README is the original, observer-first design spec (its core is "React DevTools for a running Loom session"). This document records the agreed direction and **governs where the two diverge** — most importantly, it demotes the live observer from the product's spine to a layered, Claude-first enhancement (see §3). The README stays useful for detail on hooks, panels, and the git-revision model.
**Relationship to the Loom engine:** Loom (upstream, MIT) is treated as a **finished piece of software**. Studio is a *host/manager* that stands up and configures engine instances; it edits the engine only minimally, at the contract level (§4).

---

## 1. What Loom Studio is
A local, non-developer **writing environment** for Loom projects — a viewer and editor for a project's files, and a **host/manager** that stands up new project engine instances and configures them. It is not a rewrite of the Loom engine and not, at its core, a live session monitor (that is a later layer — §3).

## 2. Who it's for & design principles
The primary user is a **non-developer author.** Every principle follows from that:
- **Hide the machinery.** Powerful tools (git especially) are presented in author vocabulary — "bookmarks," "timelines," "go back," "accept changes" — never git nouns. The user should never see a commit hash, a branch ref, or a conflict marker.
- **The manuscript is the centerpiece.** The whole interface orbits the prose; everything else is in service of writing.
- **Local-first & credential-clean.** Single-user, filesystem-native, no account required to be fully functional. Studio never touches model-provider credentials (§4, §5).
- **Useful headless.** The tool is valuable with **no AI session running at all** — a git-backed writing app on its own. AI features enhance it; they are not a precondition for it.
- **Parse tolerantly.** When reading engine output, show a "doesn't match schema" badge rather than throwing.

## 3. Direction & scope — Course A (author-first)
The product, and the POC, is the **author's writing environment**: create/open/configure projects, the manuscript-centerpiece editor with reference panels, and the writer-facing version-control suite (bookmarks, Alternate Timelines, Loom View). This spine is **assistant-agnostic** and works standalone.

The **live-observer + mechanical human↔agent consistency** capabilities (watching a running session, injecting deltas at turn boundaries) are a **layered, Claude-first enhancement**, delivered through a thin internal **session-adapter** interface — not part of the spine and never a blocker.

- **Claude-first, multi-assistant via adapters.** Ship a Claude adapter first. The spine runs with **zero adapters** connected. Other assistants (ChatGPT/Codex, Gemini) get their own adapters later, or none — the app stays fully usable either way. This is the resolution to the old cross-assistant tension: it is graceful degradation by design, not a parity problem.
- **Durable-first.** The spine builds on git (stable for decades); the fragile, release-sensitive hook plumbing is touched only in the adapter layer, after the valuable core exists.

## 4. Studio ↔ the Loom engine — the contract boundary
Loom is a **finished engine.** Studio never forks-and-hacks its internals; it interacts through **contracts** and edits the engine only for *consistency* and *frontend consumability*.

**The contract surfaces (the only places Studio meets the engine):**
1. **Scaffold contract** — the `.claude/` boilerplate (agents, hooks, skills, settings) + project layout (`loom.json` manifest, directory tree, `.gitignore`) Studio materializes to **create** an instance.
2. **Config contract** — subagent enable/disable, tool permissions, plugins, genre presets, MC identity → written into that instance's `.claude/`. This is how Studio **configures** an engine.
3. **Data/schema contract** — the tracker + frontmatter formats Studio parses for its panels and both sides write. Single-source the schema from the manifest and **generate `tracking-formats/SKILL.md` from it**. This is what "frontend consumability" means.
4. **Events contract (later)** — the additive HTTP hook the Claude adapter consumes. Additive, coexists with the engine's existing prose channel, and deferred under Course A.

**The only edits Studio makes to the engine (everything else is left alone):**
- **Emit `python3` (resolve the interpreter) in generated `settings.json` — in scope.** A scaffolder that ships the `python`-vs-`python3` bug stands up broken instances. Studio owns the boilerplate, so it emits correct boilerplate regardless of upstream state.
- **Schema single-sourcing / stable frontmatter — in scope.** Contract #3; panels need parseable files.
- **Path/session-scoping — conditional.** Only needed when Studio manages *multiple* projects at once; a single-active-project POC can leave it.
- **Structured-events hook — deferred + additive.** The adapter layer, not a rewrite.
- **Engine internals (e.g. the SessionStart stdin edge case) — out of scope.** Studio never spawns `claude` and never invokes hooks, so it never hits them. The engine's own concern.

> Note: the README §2 lists these as live "blocking bugs." Under Course A + this boundary they reduce to the small in-scope set above; the rest is the engine's business.

## 5. Project lifecycle — create, configure, open
Maps directly onto standing up and configuring engine instances.

**Create a new project** stands up a fresh engine instance:
1. Name, location, type (book/session), genre.
2. Materialize `.claude/` from the scaffold + config contracts, with the chosen configuration (agents, tools, plugins, preset, MC identity) baked in — so a user who just opens a terminal and runs `claude` gets their configured environment with no extra step.
3. Write `loom.json` (with `loom_version` from commit one) and generate `tracking-formats/SKILL.md` from its schema.
4. **`git init` + initial commit.** Hard prerequisite: every version-control-backed capability (bookmarks, Track-Changes review, Alternate Timelines, Loom View) depends on the repo existing from the start.
5. Write `.gitignore` covering Studio's `settings.local.json` and the ephemeral session change-log — local/ephemeral state never enters project history.

**Configure a project** — the config contract surfaced as UI (subagent toggles, tool policy, plugins, genre presets, MC identity), materialized back into `.claude/`.

**Open an existing project** — detect `loom.json`, offer migration if `loom_version` is behind, and if the folder is not yet a git repo, offer to initialize one (VC features stay unavailable until it is).

**First-time git readiness (detect first, prompt only if needed).** On first launch Studio probes that `git` is present and runnable and that a committer identity exists (`user.name` + `user.email`). **If both hold, Studio says nothing — no wizard, no nag.** It prompts *only* for what is missing:
- **No git →** plain explainer ("Loom uses git to track your progress and power your timelines") + per-platform install guidance. Hard blocker; Studio can't silently install it, so it points and re-checks.
- **No identity →** a two-field form (name, email) applied via `git config`. No account, no server — a local identity is all local commits need. This tags **human** commits on the Loom View (distinct from the agent's own commit identity).

**Three kinds of "credential" — kept strictly separate:**
- **Git identity** (name + email) — not a secret; Studio sets it; required for commits.
- **GitHub auth** (optional, **deferred past POC**) — a real credential but only for remote push (backup/sharing), never model access. When built, Studio **delegates to the system git credential helper / `gh` / OS keychain and never stores or transmits the token itself.** Local git fully powers the spine, so this is not needed to prove the concept and is skipped for now.
- **Model-provider credentials** (Anthropic/OpenAI keys, Claude auth) — Studio **never** touches these. This is what keeps Loom out of third-party authentication restrictions; nothing in setup goes near it.

## 6. Interface layout & the manuscript centerpiece
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

1. **Left rail — category navigation (tabbed).** Content grouped by category (Worldbuilding tabs; Project/Meta files), not one flat file tree. Selecting an entry opens it in the reference panel.
2. **Reference panel — non-story file preview, read-first.** Info/wiki/worldbuilding files open here and **stay visually available** beside the manuscript — a persistent companion pane, not a modal. **Read-only by default** (opens a read-only copy); an **Edit** button toggles inline edit mode; changes **save on exiting edit mode** or manual save. Two intentional editing postures: reference = read-first (guards non-story files against accidental edits), manuscript = edit-capable with a permanent toolbar. The enter-edit → exit-edit boundary is exactly the "editing session" the change-log coalesces one human-edit delta around (§10). **Resolved: multiple reference files may be open as tabs; one visible at a time for the POC** (split panes are post-POC polish).
3. **Manuscript — the centerpiece.** Its own special view, prose-focused, navigated by **page-turning** (prev/next loads the adjacent chapter or file). Editing toolbar + nav + controls anchor the bottom. Owner edits made here are the human edits the change-log captures (§10) — the centerpiece and the edit-capture loop are the same surface. **Resolved: the diff/review surface is a *mode of this centerpiece*** — reviewing a proposed revision or comparing timelines takes over the center in "review mode," then returns to writing. It is not a separate always-on panel.
4. **Right rail — story structure.** A **Table of Contents** of the manuscript (chapters/scenes/files) for jumping around. **Resolved: page-turn order is authored here** — order resolves from frontmatter (`scene_number`/chapter) → manifest → filename, and the author **reorders by dragging in the TOC**, which writes back to frontmatter/manifest. Nobody hand-edits YAML.

**Resolved: the Activity/observer panel is not prime real estate.** Because the observer is a deferred, adapter-gated layer (§3), it appears only as a collapsible/slide-in surface when a live Claude session is connected, and never competes with the manuscript.

## 7. Version control for writers — the model
Git is the storage engine, **fully hidden** behind author vocabulary. This section is the owed VC model + the git-substrate decision.

**Why git (decision, locked).** Not merely ubiquity: (a) Loom is already a git repo and the agent already autocommits to it; (b) the two headline features — Alternate Timelines and prose-as-plain-files — *are* the git model; (c) it fits local-first/offline/single-user/zero-server exactly; (d) durability aligns with the manifest's "projects outlive formats." The one weakness (line-oriented diff/merge on reflowing prose) is a **presentation/merge-layer** problem to solve on top — a layer you'd build under *any* backend — not a reason to switch. Ideas from alternatives are borrowed, not adopted: **conflict-as-data** (from jujutsu) for how we record/resolve conflicts; **CRDTs** only if a narrow real-time same-paragraph collision ever appears (our target flow is turn-gated, so not now).

**The three tiers (author-facing → git primitive):**
1. **Autosave — the safety net.** Every file save and turn boundary is captured automatically in a **silent shadow layer** (separate ref namespace). "You never lose work." Never prompts, never drawn on the Loom View.
2. **Bookmarks — save points.** A deliberate save prompts the author for a **bookmark message** and creates a named commit on the current timeline. This is the curated history the author browses, names, and returns to. (Standard term: **"bookmark."** "Snapshot" is retired as a synonym.)
3. **Proposed revisions & timelines — branches.** Agent revision *waves* and parallel story versions live on branches (§8, §9).

**Track-Changes review.** When an agent does a revision *wave* to existing prose, it lands as a **proposed revision** (a branch), shown to the author as **tracked changes with before/after**, to **Accept** (merge), **Discard**, or later **Accept some**. New content may write direct (autosave/bookmarks undo it); revisions to existing prose are review-gated — matching how authors feel about generated-new vs. someone-editing-mine.

**Sharp edges, resolved author-first:**
- **Conflicts are shown as "pick or blend," never raw markers.** Prefer to avoid them by construction (branch from a known point, review before diverging further).
- **Prose-aware, word/sentence-level diff** — not git's line diff. This is the layer referenced throughout (timeline compare, review mode).
- **Partial-accept is deferred** — POC ships **all-or-nothing per draft**; hunk-level granularity comes later.

## 8. Alternate Timelines — parallel story versions (core value proposition)
A writer keeps **more than one version of their story alive at once** and **hops freely between them.** "What if she takes the deal" vs "what if she doesn't" are two timelines maintained in parallel — switched between, compared side by side, carried forward in whichever is preferred — without copying files or losing either. No other authoring tool offers this, because none store prose as plain files in a repo. A headline differentiator, not a nice-to-have.

**Interactions (writer vocabulary; git hidden):**
- **New timeline from here** — fork a parallel version from any bookmark (git: branch).
- **Switch / hop** — jump between timelines; the manuscript centerpiece shows the active one (git: checkout).
- **Compare** — two timelines side by side via the §7 prose-aware diff.
- **Bring across** — pull a scene from one timeline into another, or merge one back, through the §7 accept/review flow.
- **Name & curate** — writer names ("Darker ending," "Romance subplot"), never refs.

**Timelines vs. proposed revisions:** both are branches underneath, different lifecycles — timelines are *long-lived parallel versions you maintain*; proposed revisions are *short-lived agent drafts you accept or discard*. Kept visually distinct.

**Resolved: active-timeline safety.** The agent writes into whatever timeline is checked out, so a mis-scoped write is costly. Mitigations: a **persistent, prominent active-timeline indicator** in the manuscript chrome ("You're writing in: *Darker Ending*"); **switching is explicit and confirmed**, and **blocked/hard-warned while the agent is mid-turn** (fits the turn-gated model). Later: tag agent writes with the timeline active at turn start so Studio can flag a mismatch. Autosave/bookmarks resolve against the active timeline and never leak across.

## 9. Loom View — the branch visualizer (git history as a woven loom)
The signature visual, and the payoff of a loom-themed name: the git history drawn as a **weave** — timelines are threads, **bookmarks** are knots along them, forks/merges are where threads split and rejoin. It is the home base for managing §8 timelines, and shows the story's development: every timeline, where each forked/merged, which is active, and *what happened* (human vs. agent edits, which agent — from commit-trailer provenance).

**Interactions (author language):** **hop** (switch timeline), **go back to a bookmark**, **new timeline from here** (fork), **compare** (diff two bookmarks/timelines).

**Bookmarks carry messages,** surfaced here — hover a knot to read one, or toggle labels along the threads.

**Resolved constraints:**
- **"Go back to a bookmark" is non-destructive — two safe modes only.** (a) **Restore into a new timeline** (fork from that bookmark; current work untouched — *default*), or (b) **Reset this timeline to here**, which first auto-bookmarks the current tip so nothing is unrecoverable. No path ever does a bare `reset --hard`.
- **The weave stays legible.** Only **bookmarks + named timelines** are drawn; autosaves stay in the silent shadow layer. Long linear runs collapse ("+12 saves," expandable); the active timeline is highlighted. Filters (timeline/date/human-vs-agent) are post-POC.
- **Provenance markers** distinguish human- vs. agent-authored (and which agent) at a glance.

## 10. The Claude-connected layer (deferred enhancement, adapter-gated)
Everything here rides the **Claude adapter** (§3) and is layered on *after* the spine. It is not required for a usable POC.

**Human-edit consistency — the goal.** When a human edits a project file, the agent should stay consistent with that edit **without re-reading every file every turn.**

**Split by build phase (Course A):**
- **Built early (serves the spine regardless of AI):** Studio's **filesystem watcher** + an append-only **session change-log** (`.loom/session-log.jsonl`), with **echo suppression** (agent/Studio writes excluded). This already earns its place — it powers editor echo-suppression, autosave, and Loom View provenance. Human edits are **coalesced per editing session** (the reference-panel edit-mode boundary, §6), carrying the changed content (a diff), not just a path.
- **Deferred to the Claude adapter (the enhancement):** a Studio-owned hook that **injects unconsumed deltas** at turn boundaries — at **both `UserPromptSubmit`** (turn start) **and `PreToolUse`** (each tool call, to cover long autonomous runs). Delivery is **content-level**: inline the diff so the agent *patches* its in-context understanding rather than re-reading the lengthy file (sound because the agent already holds the pre-edit baseline). **Fallback: diff-first, targeted file-read only when the baseline is missing** (post-compaction, or a file never read this session). Consume/ack marks deltas seen so they aren't re-injected.
- **POC consistency = the soft re-read fallback.** Until the injection ships, the engine's existing behavior (the `UserPromptSubmit` prose reminder to re-read files) carries consistency — acceptable, since the target flow is turn-gated and this already works, just at re-read cost. The injection is the *upgrade*.

**Verified upstream facts (why this is a real gap, not free):** loom wires `UserPromptSubmit`, `Stop`, `PostToolUse(Write|Edit)`, `SessionStart`. `PostToolUse(Write|Edit)` fires only on the agent's **own** writes; a human edit fires no tool event; there is **no filesystem watcher**. Claude Code has no event for an external file change — so nothing notifies the agent at the moment a human edits. This is precisely what Studio's watcher + injection supplies.

**The backbone underneath (adapter internals).** Two primitives compose most connected features:
- **A — change-feed (read):** one normalized timeline of agent tool events (hooks), transcript deltas, and human fs-edits.
- **B — control surface (write):** hook-response points — `UserPromptSubmit` injection; `PreToolUse` `permissionDecision`/`updatedInput`/`additionalContext`.

Human-edit consistency is A+B; the Activity panel is A-only; pending-write preview, inline rewrite, and deny-with-reason steering are B (with A for the pending content). The Activity/observer panel and these steering features are **adapter-layer, deferred**, and surfaced only when a live session is connected (§6).

**Cross-assistant:** the change-log and both primitives are *concepts* that carry to other assistants; the *channels* are Claude-specific. Each new assistant needs its own adapter (or falls back to soft re-read). Claude-first now.

## 11. Build order (Course A)
1. **Project lifecycle + git readiness** (§5) — create/open/configure, `git init`, first-run detection.
2. **The writing surfaces** (§6) — manuscript centerpiece, reference panels, category nav, TOC.
3. **Writer version control** (§7–§9) — autosave, bookmarks, Track-Changes review, Alternate Timelines, Loom View, non-destructive rollback.
4. **Change-log + echo-suppression** (§10, spine-serving half) — fs-watch, session-log, provenance.
5. **Claude adapter** (§10, enhancement half) — delta injection at `UserPromptSubmit`/`PreToolUse`, then the Activity/observer panel and steering features.
6. **Other-assistant adapters** — after a working Claude-first POC.

Steps 1–3 are the usable, standalone POC. Everything after is additive.

## 12. Resolved decisions & still-open items
**Resolved (this pass):** Course A author-first spine; engine treated as a finished dependency touched only via contracts (§4); git chosen and hidden (§7); three-tier VC model + Track-Changes (§7); "bookmark" as the standard term; cross-assistant handled via adapters (not parity); human-edit injection deferred, change-log built early (§10); Activity panel deferred/collapsible; diff as a review-*mode* of the centerpiece; multiple reference files as tabs (one visible, POC); page-turn order authored via TOC drag; active-timeline safety via prominent indicator + confirmed switching; non-destructive rollback (two safe modes); Loom View legibility (bookmarks+timelines only); GitHub connect deferred past POC.

**Still genuinely open (for design):**
- Exact prose-diff/merge library and the "pick or blend" conflict UX.
- Migration mechanics when `loom_version` is behind.
- The precise session-adapter interface (what a non-Claude adapter must provide).
- Whether/when path/session-scoping in the engine is needed (tied to concurrent multi-project).
- MC-sheet agent-inertness enforced structurally (a `PreToolUse` deny on that path) — carried from the README, not yet specced here.

---

## Appendix A — Considered & set aside: an in-session "log-watcher" agent
*Idea:* a background subagent that polls the change-log and pipes human edits back to the primary agent for mid-run awareness. *Not adopted:* a subagent cannot inject into the primary's active context — its findings land only at a step boundary, the same turn-gating a hook already gives for free; it is a worse detector than Studio's fs-watch (no clean human/agent origin, burns tokens); and it couples watching into the agent runtime, breaking the observe/write separation. **The kernel worth keeping** became the §10 rule: inject at both `UserPromptSubmit` and `PreToolUse` to cover long autonomous runs — deterministic, no polling, the change-log as shared state.
