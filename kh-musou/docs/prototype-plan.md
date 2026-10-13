# Prototype plan and later desktop handoff

These are next work packages, not work performed during this research pass. Complete the correctness
and feel gates before growing the campaign. Select tools/versions only when the implementation
environment is available; the engine is not preselected by this plan.

## P0a — Choose the combat experiment, not a default winner

Confirm whether the next authorized implementation should explore one route or compare both. The
[route comparison](combat-routes.md) proposes one representative Knight against Sora with a temporary
form sketch as a bounded experiment; it is not an approved reduction of the three-Knight vision.
Select representative commands, Sora finishers and exact source editions with provenance. Explicitly
choose which Shotlock variant an experiment tests, or stage separate variants. Do not implement
command-deck equipping/cooldowns or full KH systems by implication.

**Exit:** a written experiment scope, remaining route decisions and comparison criteria are agreed.
A tool-support advantage is recorded as evidence, not treated as the user's combat-design choice.

## P0 — Establish evidence and budgets

**Inputs:** exact source edition/build, legal local source availability, target hardware, target frame
budget, desired starting crowd count and prototype controls.

**Deliverables:** source/provenance manifest; two enemy evidence records; engine comparison decision;
small reproducible benchmark scenarios; explicit unknowns. Pin tool versions and cite source commits.

**Exit:** there is enough verified behavior to implement two contrasting enemies, and the team knows
what constitutes a performance pass. If source access is absent, use clearly labeled original behavior
proxies for engine experiments and do not claim enemy fidelity has passed.

## P1 — Controller and animation spike

Use original placeholders. Implement travel/jump/landing, short ground and air chains, one ranged
spell, guard and evasion. Make input buffering, cancel windows, animation events and hit regions
observable. Test root-driven and/or hybrid movement without premature general frameworks.

**Exit:** a reviewer can perform the intended transitions repeatedly; animation-driven attacks collide
correctly; fast movement does not tunnel; misses and defense give readable feedback; controls remain
consistent under simulated load. Record playtest findings, not just a video of a successful combo.

**Route extension:** test the selected command-derived branches or longer Sora finishers and the
agreed Shotlock/form payoff. If comparing, use matched enemy/arena conditions and record content-cost
and evidence differences. If selecting the Knight route, schedule all three identity slices before
claiming roster distinctness; a single representative cannot establish it.

## P2 — Two enemy behavior slices

Implement independent state machines from the verified evidence records. Include telegraph, attack,
recovery, defensive/vulnerable states, hit reactions and death. Mark every intentional adaptation.

**Exit:** the [enemy regression checklist](enemy-fidelity.md) passes one-on-one and in small groups.
Unexplained behavior differences block a fidelity claim even if the combat is enjoyable.

## P3 — Interactive horde and profiling

Add stable entities, complete spatial queries, visual LOD and budgeted simulation only as required by
measurement. Start full-detail and preserve it as the reference. Exercise player approach **and
long-range attacks** before optimizing density. Run the [correctness/performance matrix](interactive-horde.md).

**Exit:** no invisible interaction cutoff, duplicate entities, health resets, missed valid hits or
state discontinuities; the measured target count meets the agreed frame budget on the target machine.
If it fails, profile and reduce scope or revise scheduling. Never hide failure behind decorative crowds.

## P4 — One battlefield objective

Add one ally/control-point objective with one meaningful pressure change. Expose win/fail state,
objective contributions, ally/enemy combat events and spawn/despawn history.

**Exit:** the player can influence the ally and objective through actual combat; distant events remain
consistent on approach; the slice is replayable and reports its correctness/performance metrics.

## P5 — Review before campaign

Review three separate gates: **enemy fidelity**, **combat feel**, **crowd performance/correctness**.
All must pass; aggregate frame rate does not excuse invalid interactions, and fidelity does not excuse
unresponsive controls. Record known deviations and failures. Then decide whether to expand, simplify,
change engine/architecture, or stop. A campaign plan is justified only by that evidence.

## Copyable implementation assignment

Read `kh-musou/README.md`, the charter, combat-routes, enemy-fidelity, interactive-horde, toolchain-research,
engine-evaluation and open-questions docs. Inspect repository instructions and the selected local
workspace before editing. Confirm exact source edition and provenance; do not import commercial
assets into the public repository. Establish target hardware/frame budget and engine spike choice.
Confirm the chosen route or bounded comparison and payoff experiment. Implement only the approved
next milestone using original placeholders and reproducible tests.
Preserve the every-visible-enemy invariant, including attacks at long range. Record source evidence,
unknowns, benchmark settings/results and adaptation decisions. Do not grow the campaign before all
three prototype gates pass. Follow The Ideabox's additive-work and remote-checkpoint conventions.

## Required handoff artifacts for each future milestone

- Engine/tool versions and reproducible launch/test commands
- Source manifest plus derived behavior specification, without proprietary binaries
- Scenario definitions, baseline/optimized results and unresolved failures
- Short captured evidence for combat feel, backed by entity/event logs for correctness
- Commit and verified remote branch; explicit description of what was and was not tested
