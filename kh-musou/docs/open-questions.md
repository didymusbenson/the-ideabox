# Open questions and decision log

## Confirmed direction

Standalone KH-inspired musou; Keyblade movement and ground/air combat; magic and defense; recognizable
Heartless; musou input sequences and battlefield pressure; every visible enemy real and fightable.
Research precedes implementation. OpenKH is the first research route; native disassembly is conditional.

## Decisions needed before an implementation spike

1. **Source edition:** exact KH2/BBS edition, region, platform and build to study; do not blend data.
2. **Target machine and frame budget:** minimum CPU/GPU/RAM, resolution, and desired frame rate. No
   hardware or fixed 60 fps commitment has been supplied.
3. **Crowd objective:** target simultaneous visible enemies, active attackers, map dimensions and
   attack ranges. Investigate scaling curves rather than announcing a speculative thousands count.
4. **Player reference:** which KH movement/combat reference is authoritative, and which deviations
   make the musou version more playable?
5. **Engine:** shortlist and spike criteria, not an inherited choice from another Ideabox project.
6. **Asset route:** original placeholders initially; what source materials can later be lawfully
   inspected locally, and what independently licensed/original assets can actually ship?
7. **Scope and resources:** team size, time budget, intended audience/platform and release intent.
8. **Enemy candidates:** approve contrasting types after their evidence is sufficient.

## Resolve during the first slice

Root motion vs hybrid movement; airborne navigation/avoidance; crowd attack-slot policy; combo buffer
and cancel rules; guard/evade semantics; battle scale and truthful reinforcement presentation;
retargeting or original animation workflow; acceptable visual LOD; test replay strategy.

## Deferred

Full campaign structure, large roster, progression economy, elaborate story, online multiplayer,
commercial asset pipeline, and additional KH3/DW edition research. A later question is not approval
to extract or distribute those games' content.

## Recorded 2026-10-13

Engine remains unselected. No benchmark, asset import, behavior reproduction, or native reverse
engineering has been performed. Research documentation does not establish performance feasibility.
