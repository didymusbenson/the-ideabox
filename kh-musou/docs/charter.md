# Project charter

## Original brief

The following is the user's supplied specification, preserved verbatim (including the compact layout):

> PROJECT: Standalone Kingdom Hearts–style musou action game  GOAL Create our own interpretation of a Kingdom Hearts × Dynasty Warriors crossover—not a mod of either existing game.  The player controls a Keyblade wielder with KH-inspired movement, ground/air attacks, magic, and defensive actions. A musou-style combo/input system maps button sequences to these moves.  Heartless retain recognizable behavior from their KH counterparts: movement, attacks, defensive states, vulnerabilities, and hit reactions. Battles place them within a DW-style campaign structure with objectives, allied forces, and shifting battlefield pressure.  HORDE REQUIREMENT Every visible enemy must be a real, reachable, fightable entity. No decorative, untouchable Heartless standing in for the horde.  Distance-based processing reductions are acceptable only if enemies retain identity, position, and state. Approaching or attacking them must produce correct interaction, including attacks at long range.  TECHNOLOGY / TOOLCHAIN • Standalone game engine — not selected yet. Needs animation-driven   combat, character movement, collision, navigation, and scalable   crowd simulation. • OpenKH — primary research toolkit for KH2/Birth by Sleep formats,   assets, and documented systems; KH2 AI-script tools are especially   relevant. Verify support for the exact source-game edition. • Ghidra — investigate native executable behavior where existing   documentation and data tools are insufficient. • AI coding assistant — help interpret findings, implement systems,   and write tests. Generated interpretations require verification. • Unreal asset tooling, such as UAssetGUI — conditional research   tools if KH3 or DW3 Remastered becomes a source of investigation;   not required for the initial KH2-focused route.  APPROACH Study selected KH behaviors, then implement them in the new engine. Do not assume recovered code can be transplanted directly.
>
> Dynasty Warriors executable decompilation is not a prerequisite.  FIRST PROTOTYPE A Keyblade controller, contrasting Heartless types, one battlefield objective, and a genuinely interactive horde. Validate enemy fidelity, combat feel, and crowd performance before expanding into a campaign.

## Later user direction — 2026-10-13

Two combat routes are now under consideration: three playable Keyblade Knights inspired by the
Terra/Ventus/Aqua archetypes, translating BBS command attacks into musou combos; or Sora's KH2-inspired
moveset with longer-combo finishers and a possible timed Drive Form ultimate. Shotlocks in the
three-Knight route may remain distinct, become combo enders with reaction follow-ups, or become
charged ultimates. These are alternatives, not a route selection. See [combat routes](combat-routes.md).

The initial brief's KH2-focused research wording remains historical context. KH2 tool maturity does
not decide the combat design. At that point no engine or exact source edition had been selected;
the later Unreal/PC decision below supersedes the engine uncertainty. Both routes
retain the original interactive-horde and standalone-implementation requirements.

## Later engine and platform decisions — 2026-10-13

The user explicitly selected **Unreal Engine** (“unreal is the right target.”) and **PC** (“pc as
target”). Windows is a planning assumption for an initial build, not an explicit operating-system
choice. Engine version, hardware/frame budget and final combat route remain unresolved. The original
brief above is historical and remains verbatim; its “not selected yet” sentence is superseded here.

The user also selected **Steam** for the reference distribution and identified their **MacBook Pro**
as the intended development machine, available later. It is not the current secondary computer.
Exact source game/build and Mac model/chip/RAM are unknown; no connection to that specific Mac is
assumed. The development host does not change the PC target or settle its operating system.

These choices do not authorize installation, asset extraction, code, builds or deployment. The current
smaller proof-of-concept discussion concerns base-Sora-inspired movement, basic attacks and one enemy;
it is a proposed first experiment, not selection of the full Sora route or approval to implement it.

## What this documentation adds

The brief is authoritative. Suggested enemy candidates, engine shortlist, data contracts, objective,
benchmark tiers and work packages are proposals to test, not additional user decisions. Research
findings carry sources; an inferred implementation approach is labeled as such. An unverified detail
must remain an open question rather than silently becoming a requirement.

## Deliverable boundaries

This pass adds a new project to The Ideabox and supplies a later implementation handoff. It does not
build the game, install the selected engine, extract commercial assets, decompile executables, or
deploy a site. It records the user’s engine/platform decisions without treating them as implementation
authorization.
A locally owned game copy is not treated as a redistribution license. Tool licenses and game-content
rights are separate; keep commercial source files outside this public repository and use original or
appropriately licensed assets for a distributable prototype. Before any later extraction or sharing,
review the applicable rights, license terms and intended use rather than assuming permission.

The first prototype uses placeholder geometry and original animations sufficient to evaluate feel
and behavior. The KH references guide research and design; release branding and asset provenance
remain decisions to resolve before publication.

## Repository placement

`kh-musou/` is an additive idea following this repository's `main` branch README: a top-level project
folder, README entry point, docs, and notes.md; the root project index links here. On 2026-10-13,
GitHub's default branch still pointed to an older psychic-game branch. Work follows the multi-project
`main` convention and does not change the repository default setting or existing project directions.
