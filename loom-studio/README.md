# Loom Studio — Project Spec
*A visualizer, project manager, and editing surface for Loom writing projects.*

**Status:** design spec, pre-implementation
**Upstream:** https://github.com/WintersRain/loom (MIT)
**Name:** "Loom Studio" is a placeholder. Any name is fine except one implying it is Claude Code or an Anthropic product — Anthropic's branding guidance permits "Powered by Claude" but not "Claude Code" or visual mimicry.

---

## 1. What this is

Loom is a creative-writing system for Claude Code: an orchestrator plus six subagents that write scenes, maintain character sheets, and track continuity across long-form projects. All of its state lives on disk as structured markdown.

Loom Studio is a **local web app that observes a running Loom session and renders its state**, plus an editor over the same files and a scaffolder for new projects.

The governing analogy is **React DevTools**. DevTools does not run your app. The app runs however it runs; DevTools attaches, shows the tree and live state, and lets you modify values in place.

### What it is NOT

- **Not a chat client.** There is no prompt box. The user prompts in their own tool — terminal Claude Code, an IDE, Cowork, whatever. This is a deliberate scope boundary, not a phase-one limitation.
- **Not a process manager.** It never spawns `claude`, never owns a PTY, never wraps a terminal.
- **Not an auth surface.** It never reads, stores, or transmits credentials. It has no model provider integration of any kind. All model traffic belongs to the user's own separately-authenticated Claude Code install. **This property must be preserved; it is what keeps the tool out of Anthropic's third-party authentication restrictions entirely.**
- **Not a SaaS.** Local-first, filesystem-native, single-user.

### Why the constraint is a feature

Because state is on disk and the agent re-reads it, **editing a file is a form of instruction**. Correcting `world.md` in the editor pane changes what the agent knows on its next read. No protocol is needed between the editor and the agent — they converge on the same bytes. The prompt box is redundant for most of what a writer actually needs to communicate.

---

## 2. Upstream state and required fixes

The fork starts from a repo that has been untouched since **2026-02-08** (6 commits, single author, `main` only, no tags or releases).

### Inventory

| Path | Contents |
|---|---|
| `.claude/agents/` | 6 subagents: `writer`, `analyzer`, `creator`, `strategist`, `state`, `router` |
| `.claude/hooks/` | 13 Python modules; `state_manager.py` is the de facto data layer (referenced in 15 places) |
| `.claude/skills/` | 18 slash commands |
| `_sessions/<genre>/<slug>/` | Per-session state: `session.json`, `scenario.md`, `characters/`, `SCENES/`, trackers |
| `_books/<name>/` | Long-form projects: `.state/`, `CHARACTERS/`, `SCENES/` |
| `_characters/` | Cross-session character library |
| Root templates | `scene_log.md`, `relationship_tracker.md`, `observations.md`, `world.md`, `scenes/Scene_001.md` |

### Blocking bugs — fix before building anything on top

1. **SessionStart hook hangs.** `auto_resume.py:97` calls `json.load(sys.stdin)`. A fix was committed (`9734b57`) then reverted (`cb7e429`) with no explanation, so the bug is live in HEAD. Reproducible: with an inherited-but-silent stdin the hook blocks indefinitely. The first-run setup prompt added in the final commit (`ba47c8d`) sits *downstream* of this read and may never fire.
2. **`python` vs `python3`.** All four wired hooks in `.claude/settings.json` invoke `python`, which does not exist on macOS or most current Linux distros. Silent total hook failure for many users.
3. **Bare relative paths in skills.** Skills write to `scenes/`, `scene_log.md`, `relationship_tracker.md` etc. with no session prefix, while the documented layout is `_sessions/<genre>/<slug>/`. Merely ambiguous with one terminal and one CWD; **immediately fatal** with two projects open in tabs. Refactoring to session-scoped path resolution touches most of the 18 skills and is a hard prerequisite.

### Structural refactor

Loom's hooks `print()` prose intended for a model to read (e.g. `FIRST TIME SETUP: ...`). They must additionally emit **structured events**. Do not replace the prose channel — multiple hooks on one event run in parallel, so the model-facing command hook and the UI-facing HTTP hook coexist.

---

## 3. Architecture

Single process. One HTTP server does both jobs:

```
localhost:PORT/            → the UI (static assets + websocket to browser)
localhost:PORT/hooks/*     → hook event ingestion (POST)
```

No Electron, no Tauri, no code signing, no per-platform packaging. Cross-platform falls out for free, and the UI is incidentally reachable from other devices on the LAN (draft on desktop, watch panels on a tablet).

### Three input feeds

**1. HTTP hooks — the live pulse.**
Claude Code hooks support an `http` handler type. The server receives the identical JSON payload that command hooks get on stdin, as the POST body, and replies with the same JSON output format.

```json
{
  "hooks": {
    "PreToolUse": [
      { "matcher": "Write|Edit|MultiEdit",
        "hooks": [{ "type": "http", "url": "http://localhost:8080/hooks/pre-tool-use", "timeout": 10 }] }
    ]
  }
}
```

Every event carries a common envelope: `session_id`, `transcript_path`, `cwd`, `hook_event_name`, and `permission_mode` on most events.

Events to consume:

| Event | Use |
|---|---|
| `SessionStart` / `SessionEnd` | Session registration / deregistration |
| `PreToolUse` | Pending-write preview, permission gating, inline rewrite |
| `PostToolUse` / `PostToolUseFailure` | Repaint trigger, error surfacing |
| `PostToolBatch` | **Preferred repaint trigger** — fires once after parallel tool calls resolve |
| `SubagentStop` | Subagent lifecycle; payload carries `agent_id` and `agent_type` |
| `Stop` | Turn boundary → autocommit point |
| `UserPromptSubmit` | Timeline marker (prompt originated elsewhere) |
| `PermissionRequest` / `PermissionDenied` | Permission flow visualization |
| `PreCompact` | Context-pressure warning in UI |

Hooks fire inside subagents. This is what makes loom's orchestrator visible — six named agents, and the UI knows which is live, what it is touching, and when it finishes. This is not obtainable from a terminal transcript.

**2. Transcript tailing — full fidelity.**
Every envelope supplies `transcript_path`, pointing at a session JSONL under `~/.claude/projects/<encoded-cwd>/<session-id>.jsonl`. Tail it for complete message content, tool results, and token usage. Hooks give the skeleton; the transcript gives the body. Purely passive read of a local file.

**3. Filesystem watching — the safety net.**
Hooks only cover agent-originated writes. Watching the project directory also catches vim, Obsidian, `git checkout`, and the user's own edits in the Studio editor.

### Session discovery

The app does not create sessions; it finds them.

- `SessionStart` POST registers a session (id, cwd, transcript path).
- `SessionEnd` deregisters.
- On cold start, scan `~/.claude/projects/` for recently-modified transcript JSONLs and backfill from disk.
- **Multiple concurrent sessions must be supported** — one window showing a book project and an RP session side by side. A terminal fundamentally cannot do this.

### Graceful degradation — non-negotiable

If Loom Studio is not running, the hooks fail. Loom **must remain fully usable headless**. Use short timeouts, fire-and-forget semantics for non-blocking events, and gate only genuinely interactive events on the server being reachable. A user who clones a Loom Project and never installs Studio must notice nothing.

---

## 4. Project format

### Manifest

A versioned manifest at the project root (`loom.json` or `loom.toml`) is the single source of truth.

```jsonc
{
  "loom_version": "1.0.0",        // REQUIRED from commit one — projects outlive formats
  "name": "Crimson Heart",
  "type": "book",                  // "book" | "session"
  "genre": "fantasy",
  "created": "2026-07-30T...",
  "agents":   { /* §5 */ },
  "tools":    { /* §5 */ },
  "schema":   { /* below */ },
  "ui":       { "default_panels": ["scene_log", "characters", "tracker"] }
}
```

Version it immediately. You will need to migrate an 80k-word manuscript without guessing which schema it was written under.

### Schema single-sourcing — build this first

`.claude/skills/tracking-formats/SKILL.md` currently documents the structure of `relationship_tracker.md`, `scene_log.md`, `observations.md`, and `world.md`. It is simultaneously:

- the **model's instruction** for how to write those files, and
- the **spec the UI parser needs** to read them.

If these are authored separately they will drift, and the failure is silent — the agent writes a section the panel cannot see. **Put the schema in the manifest, generate `tracking-formats/SKILL.md` from it, and validate incoming files against it.** One edit moves both sides.

### Metadata: frontmatter, not sidecars

YAML frontmatter on scene and tracker files — POV, chapter, status, tags, timestamps, `scene_number`, `characters_present`. Legible to the parser, hand-editable, git-diffable, readable by the model with no special tooling. A sidecar `.json` desynchronizes the first time the agent writes prose without updating it.

Rule: anything the UI **must** parse lives in frontmatter or a fenced block; free prose stays free prose. **Parse tolerantly** — show a "does not match schema" badge rather than throwing.

---

## 5. Agent & tool configuration

Per-project configuration, editable from the UI, materialized into the project's `.claude/` directory so that a user who just opens a terminal and runs `claude` gets their configured environment with no extra step.

### Configurable surface

**Subagents** — enable/disable each of the six independently.

| Agent | Role | Notes |
|---|---|---|
| `router` | Intent dispatch | Largely redundant when the UI provides explicit navigation; strong default-off candidate |
| `writer` | Prose generation | Core |
| `analyzer` | Continuity / consistency checking | Core |
| `creator` | Character & world generation | Optional |
| `strategist` | Pacing, plot structure | Optional |
| `state` | Tracker reconciliation | Core — this is loom's actual differentiator |

Disabling writes to `.claude/agents/` (move to a disabled subdirectory, or gate via frontmatter).

**Tools** — allow/deny lists mapped onto `.claude/settings.json` `permissions`. Reasonable defaults: `WebSearch` off for a closed-world fantasy project, on for research-heavy nonfiction.

**Plugins** — Claude Code plugins package skills, agents, hooks, and MCP servers and load by local path. Project-scoped plugin enablement belongs here.

**Genre presets** — a preset is a bundle of (agent set + tool policy + tracker schema + skill variants). Fantasy wants `world.md` with a magic-system section; thriller wants `observations.md` weighted toward information asymmetry; romance wants a denser `relationship_tracker.md`. Presets should be user-definable and exportable, not a fixed enum.

### Two settings files — important

- `.claude/settings.json` — **committed.** Loom's semantic hooks, agent config, tool permissions. Travels with the project.
- `.claude/settings.local.json` — **gitignored.** Loom Studio's HTTP hooks and chosen port.

If Studio's hooks land in the committed file, anyone who clones the project inherits hooks pointing at a localhost port on someone else's machine and their session degrades for no reason. Studio writes its own hook block on project load and should **select a free port at runtime**, updating `settings.local.json` accordingly.

---

## 6. New project flow

`Create New Project` → scaffold a directory → open it in Studio.

1. **Name, location, type** (book / session), genre.
2. **Agent configuration** — from a genre preset, with per-agent toggles exposed.
3. **Tool & plugin policy.**
4. **MC identity** — replaces loom's current `config.py` editing step and its `MC_NAME = "MC"` placeholder detection. Note loom's design rule that *the MC's sheet is sacred*: those fields must be user-editable only and visibly inert to the agent, enforced structurally (a `PreToolUse` deny on that path) rather than by trusting an instruction in prose.
5. **Scaffold**: copy `.claude/` (agents, hooks, skills) with the chosen config materialized; create the directory tree; write `loom.json`; generate `tracking-formats/SKILL.md` from schema; write `.gitignore` including `settings.local.json`.
6. **`git init` + initial commit.**
7. **Open**, and print the terminal command to start working (`cd <path> && claude`).

Also required: **Open Existing Project** — detect `loom.json`, offer migration if `loom_version` is behind, and offer to add Studio hooks to `settings.local.json` if absent.

---

## 7. Panels

| Panel | Source | Notes |
|---|---|---|
| **Activity** | Hook stream | Live: current tool, target file, active subagent (`agent_type`), elapsed time. The orchestrator made visible. |
| **Scene log** | `scene_log.md` | Sortable/filterable grid. Already a markdown table — a grid is the native rendering. |
| **Scene editor** | `SCENES/*.md` | Standard editor with frontmatter form. |
| **Characters** | `characters/`, `_characters/` | Sheet view; MC sheet visually distinguished as agent-inert. |
| **Relationship tracker** | `relationship_tracker.md` | Typed fields → structured view; graph over time is the ambitious version. |
| **Observations** | `observations.md` | **Highest-value panel.** Per-character models of what each character knows about another — information asymmetry as a first-class structure. This is the engine of mystery, thriller, and romance, and no story-bible tool models it because a static wiki cannot. |
| **World** | `world.md` | Section nav tree. |
| **Sessions** | `_sessions/`, `_books/` | Project explorer, multi-session switcher. |
| **Diff / pending write** | `PreToolUse` payload | See below. |

### Diff-gated writes — the interaction core

`PreToolUse` fires *before* the tool runs and its payload includes `tool_input` — meaning the full content of a pending `Write` is available before it lands. The hook response controls what happens next:

- `permissionDecision`: `"allow" | "deny" | "ask"` — the UI becomes the permission surface instead of a terminal y/n prompt.
- `updatedInput` (under `hookSpecificOutput`) — **replaces the tool's arguments before execution.** This is inline editing of the agent's output at the moment of writing: the agent proposes a scene, the user tightens a line in the editor pane, and the user's version is what hits disk. No round-trip through prose instructions.
- `additionalContext` alongside a `deny` — feeds a reason back to the model. (For command hooks, exit code 2 sends stderr back to Claude.)

That last mechanism is the **partial recovery of mid-turn steering** given up by having no prompt box. Rejecting a pending write with *"too florid, end the scene on the unanswered question"* is steering. It is narrow — reactive, one tool call at a time — but it is the difference between a viewer and a tool you can work through.

---

## 8. File watching & revisions

### Watching

- **Watch directories, not files.** Atomic saves rename, which breaks inode-based watchers.
- **Debounce 100–300ms.**
- **Prefer `PostToolBatch` over raw fs events during agent bursts** — one repaint instead of six.
- **Echo suppression will cost you a day if you skip it.** UI writes file → watcher fires → UI reloads → cursor jumps to top mid-sentence. Track write origin and ignore events for writes you initiated.
- Keep both feeds. Hooks are semantic but agent-only; fs watching is dumb but total.

### Revisions — use git, don't build a store

Loom is already a repo.

- **Autocommit on semantic boundaries** — `Stop` or `PostToolBatch`, never per keystroke. One commit ≈ one agent turn or one editing session.
- **Encode provenance in the commit message**: `agent_type`, `session_id`, scene number.
- Per-file history, diffs, and restore come free.
- **Do not stomp the user's own history.** Autosaves belong in a separate ref namespace (or shadow repo), with promotion to real commits as an explicit user action.

### Branches as plot lines — the feature worth building around

*"What if she doesn't take the deal"* is `git checkout -b`, write forward, then diff two versions of chapter nine side by side. No authoring tool offers this because none of them store prose as plain files in a repo. Loom accidentally does. Surface it as **Alternate Timelines** in the UI, not as git.

---

## 9. Build phases

**Phase 0 — Fork hygiene.** Fix the three blocking bugs (§2). Session-scoped path refactor. Verify loom works headless end-to-end before adding anything.

**Phase 1 — Read-only observer.** HTTP server, hook ingestion, transcript tail, session discovery, Activity panel. *Acceptance: run `claude` in a loom dir from a separate terminal and watch subagent activity render live in the browser.*

**Phase 2 — Panels + watching.** Parsers for the four tracker formats, fs watching with echo suppression, scene log / characters / world / observations panels. *Acceptance: agent writes a scene, all affected panels repaint within 500ms with no cursor disruption.*

**Phase 3 — Editing.** Scene editor, frontmatter forms, conflict handling for concurrent agent/user writes.

**Phase 4 — Project lifecycle.** Manifest, schema single-sourcing + SKILL.md generation, New Project wizard, agent/tool configuration UI, genre presets.

**Phase 5 — Interaction.** `PreToolUse` gating, diff preview, `updatedInput` inline rewrite, deny-with-reason steering.

**Phase 6 — Revisions.** Autocommit, history browser, Alternate Timelines.

Phases 1–2 are a working, useful tool. Everything after is additive.

---

## 10. Constraints checklist

- [ ] Never spawns `claude`; never touches credentials; no model provider integration.
- [ ] Loom remains fully functional with Studio not running.
- [ ] Studio hooks in `settings.local.json` only, gitignored, runtime port selection.
- [ ] Schema single-sourced; `tracking-formats/SKILL.md` is generated, never hand-edited.
- [ ] `loom_version` in the manifest from the first commit.
- [ ] Parsers tolerant; schema mismatch badges, never exceptions.
- [ ] MC sheet agent-inertness enforced structurally, not by prose instruction.
- [ ] Multi-session concurrent observation supported.
- [ ] Product name not "Claude Code"; no Claude Code visual mimicry.

---

## 11. Reference

- Loom upstream — https://github.com/WintersRain/loom
- Claude Code hooks reference — https://code.claude.com/docs/en/hooks
- Claude Code settings — https://code.claude.com/docs/en/settings
- Claude Code legal & compliance — https://code.claude.com/docs/en/legal-and-compliance

Hook event names, payload fields, and response schemas change between Claude Code releases. Treat the hooks reference as authoritative over this document and pin a minimum Claude Code version in the manifest.
