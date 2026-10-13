# Open questions and decision log

## Confirmed direction

Standalone KH-inspired musou; Keyblade movement and ground/air combat; magic and defense; recognizable
Heartless; musou input sequences and battlefield pressure; every visible enemy real and fightable.
Research precedes implementation. OpenKH is the first research route; native disassembly is conditional.
**Unreal Engine and PC are selected.** Windows is an initial-build assumption, not a confirmed OS.
**Steam** is the selected reference distribution. The intended development host is the user's
**MacBook Pro**, available later, not the current secondary computer. Its exact identity/connection,
model/chip/RAM and installed toolchain are unverified.

## Combat alternatives: user direction, open selection

The [side-by-side route document](combat-routes.md) records two live alternatives:
- Three playable Knights based on Terra (heavy Strikes), Ventus (Raids/throws) and Aqua (magic-enhanced
  attacks), translating iconic BBS commands into musou combos.
- Sora's KH2-inspired moveset, longer-chain finishers and a possible timed Drive Form ultimate
  (Valor is the user's example).

Still open:
1. Which route should lead, or should a bounded comparison precede the choice?
2. Are the Knights original characters or Terra, Ventus and Aqua themselves? How is character
   selection/switching handled, if switching is wanted at all?
3. Which specific commands/finishers define each kit, and which imported inspirations are allowed?
4. Does any command-deck equipping/cooldown/progression system survive the combo translation?
5. Shotlocks: preserve targeting/follow-ups, combo ender plus reaction follow-ups, or charged ultimate?
   What governs target selection, costs, safety windows, interruption and follow-up timing?
6. Sora: which forms, duration/charge rules, altered moves and entry/expiry behavior? Are source
   party/resource restrictions useful here or intentionally omitted?
7. What input grammar exposes these moves without locking in a layout before testing?

Research evidence can inform these choices; it does not make the creative decisions for the user.

## Decisions needed before an implementation spike

1. **Source edition:** Steam is selected; verify the exact KH2/BBS title, edition, region and installed
   build/patch before studying files. Do not blend data between editions.
2. **Target machine and frame budget:** minimum CPU/GPU/RAM, resolution, and desired frame rate. No
   hardware or fixed 60 fps commitment has been supplied.
3. **Crowd objective:** target simultaneous visible enemies, active attackers, map dimensions and
   attack ranges. Investigate scaling curves rather than announcing a speculative thousands count.
4. **Player reference:** which KH movement/combat reference is authoritative, and which deviations
   make the musou version more playable?
5. **Unreal setup:** exact released version, MacBook Pro model/chip/RAM, editor/build toolchain and
   PC operating system. Verify the intended development Mac when it becomes available. Engine
   choice is settled; no installations are authorized by that choice alone.
6. **Asset route:** original placeholders initially; what source materials can later be lawfully
   inspected locally, and what independently licensed/original assets can actually ship?
7. **Scope and resources:** team size, time budget, intended audience and release intent; PC is the
   selected platform. Keyboard/mouse and controller requirements remain open.
8. **Enemy candidates:** approve contrasting types after their evidence is sufficient.

## BBS pipeline questions after source inspection

[OpenKH source inspection](toolchain-research.md#bbs-feasibility-serious-head-start-not-a-complete-combat-pipeline)
confirms implemented model export and PAM → ANB conversion; project existence is no longer the only
evidence. Still unresolved: actual edition compatibility, downstream animated playback, attack-event
reconstruction, command-ID joins, collision/projectile semantics and Shotlock runtime. EPD parameters
do not answer the BBS enemy-AI question. No export or source test was run in this research pass.

## Resolve during the first slice

Root motion vs hybrid movement; airborne navigation/avoidance; crowd attack-slot policy; combo buffer
and cancel rules; guard/evade semantics; battle scale and truthful reinforcement presentation;
retargeting or original animation workflow; acceptable visual LOD; test replay strategy.

## Deferred

Full campaign structure, roster expansion beyond a selected route, progression economy, elaborate
story, online multiplayer, commercial asset pipeline, and additional KH3/DW edition research. A later question is not approval
to extract or distribute those games' content.

## Recorded 2026-10-13

The user explicitly selected Unreal Engine and PC. The proposed initial base-Sora movement/basic-
attack/one-enemy experiment does not settle the full combat route or authorize implementation.
Windows remains an assumption; no exact Unreal release, hardware specification or frame target is
selected. No benchmark, asset import, behavior reproduction or native reverse engineering has been
performed. Research documentation does not establish performance feasibility.
