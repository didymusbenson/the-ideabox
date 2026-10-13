# KH2-first toolchain and combat fidelity research

Research date: 2026-10-13. Public documentation/source inspection only. No commercial executable, disc image, asset or extracted game script was downloaded or processed. No engine is selected here. Proposed behaviors and numerical fidelity targets are not measured findings.

## Research starting point, not a combat-route decision

This document began as a KH2-first tooling investigation. The user's later [BBS three-Knight and
Sora alternatives](combat-routes.md) remain equally open as design routes. The verified KH2 tool
coverage below can reduce research uncertainty; it does not select the playable roster or invalidate
BBS. Audit exact-build BBS command/Shotlock behavior separately if that route is explored.

For a KH2 research slice, select one exact Kingdom Hearts II edition/build, one player configuration
and two contrasting enemies. Kingdom Hearts II Final Mix is a research candidate, not a confirmed edition choice. Use OpenKH for format knowledge/inspection and appropriately licensed tooling. Write a new standalone combat implementation from evidence-backed specifications: reading BDX or importing animations does not import the combat runtime. Dynasty Warriors decompilation is not a prerequisite.

Choose the lawful reference copy actually available to the user and matching footage. PS2 KH2FM has explicit legacy executable references; HD PC may be more convenient locally. Asset compatibility and gameplay equivalence require separate tests.

## Verified OpenKH capabilities and limits

- **KH2 objects:** Object Editor documents MDLX model/textures/collisions/AI, MSET motions and APDX effects/UI. Frame-by-frame playback, collision overlays and trigger editing are available. It notes incomplete effect understanding and limits on in-game memory testing. This is inspection support, not a complete portable runtime or verified converter for the user's build. [Object Editor](https://openkh.dev/tool/GUI.Kh2ObjectEditor/)
- **Moveset selection:** MSET has default/player/raw slot mappings and player-state fallback rules. The debug motion-name table is explicitly incomplete for Final Mix. Names alone are not an action graph. [MSET](https://openkh.dev/kh2/file/anb/mset.html)
- **Animation/combat events:** ANB documents RAW/interpolated motion, local/global timing and frame/range triggers. Attack triggers reference ATKP/collision groups; other entries concern combo permission, movement/gravity state and magic casting. Unknown entries remain. [ANB](https://openkh.dev/kh2/file/anb/anb.html)
- **AI:** Bdxio documents BDX decoding into bdscript and reverse encoding. The AI format is a VM script with engine syscalls, not the native executable. [Bdxio](https://openkh.dev/tool/CLI.Bdxio/), [AI](https://openkh.dev/kh2/file/ai/)
- **Important documentation conflict:** The older ISA chapter warns about unknown instructions/functions and claims syscalls are undocumented. Do not repeat that as a current blanket claim: current source has a substantial named trap registry with table/index/flags. Names still do not prove complete semantics. Check current source before declaring a reverse-engineering gap. [ISA](https://openkh.dev/kh2/file/ai/kh2ai.html), [BdxTraps.cs](https://github.com/OpenKH/OpenKh/blob/master/OpenKh.Command.Bdxio/Models/BdxTraps.cs)
- **Attack parameters:** Atkp.cs contains attack type, power/element, reaction, knockback, reflection-related, interval, revenge-damage and combo-classification fields; it is explicitly marked unfinished. Field names do not establish formulas, units or ordering. [Atkp.cs](https://github.com/OpenKH/OpenKh/blob/master/OpenKh.Kh2/Battle/Atkp.cs)
- **Tables/encounters:** Mod creation docs expose listpatch support including atkp, enmp, magc, objentry and cmd plus spawn/area scripts. These tables are inputs, not the engine's damage/movement implementation. [Mod creation](https://openkh.dev/tool/GUI.ModsManager/creatingMods.html)
- **BBS formats:** PMO models and PAM animations are documented. PAM describes channel/keyframe layouts, interpolation/loops and a 30 FPS animation-header value; do not infer universal gameplay tick rate or remaster equivalence from it. [PMO](https://openkh.dev/bbs/file/type/pmo.html), [PAM](https://openkh.dev/bbs/file/type/pam.html)
- **BBS source exists beyond the tool index:** Pam.cs, Pmo.cs, PAtk.cs and battle/event classes exist, as do PAMtoFBXConverter and PmoConverter projects. Source existence was verified; successful conversion, exact-build support and equivalent AI/runtime coverage were not. [BBS library](https://github.com/OpenKH/OpenKh/tree/master/OpenKh.Bbs), [PAM converter](https://github.com/OpenKH/OpenKh/tree/master/OpenKh.Command.PAMtoFBXConverter), [PMO converter](https://github.com/OpenKH/OpenKh/tree/master/OpenKh.Command.PmoConverter)

Keep four separate statuses: documented, source inspected, tool run, output validated. This study establishes the first two selectively. The README requests .NET 8, describes Windows-oriented UI tools and cross-platform CLI with testing primarily on Windows, and still lists compatible-engine development among future plans. Pin a release/commit, not `latest`; do not characterize OpenKH as a complete recovered KH2/BBS runtime. [Repository](https://github.com/OpenKH/OpenKh)

## Exact-edition gate

1. **PS2 KH2FM:** OpenKH identifies Japanese Final Mix as SLPM 66675, timestamp 2007-02-16. Vanilla JP SLPM 66233 and US SLUS 21005 are separate builds; do not interchange executable offsets. [KH2 builds](https://openkh.dev/kh2/builds.html)
2. **Edition versus platform:** Edition IDs affect file selection, save identifiers, confirm buttons and text spacing. JP/US/FM executable locations differ; FM uses SYSTEM.CNF to establish edition. [Editions](https://openkh.dev/kh2/editions.html)
3. **PS3 versus PS4/PS2:** The build table lists distinct regional remaster codes. BAR documentation explicitly says PS2/PS4 are little-endian, PS3 big-endian. The Object Editor's broad all-version sameness claim cannot establish universal raw-byte equality. [BAR](https://openkh.dev/kh2/file/type/bar.html)
4. **HD PC:** Current Mod Manager documentation supports Steam and Epic. This establishes supported modding workflows, not identical executables, patches or timing. Record storefront, collection, patch/build ID and executable hash. [Mod Manager](https://openkh.dev/tool/GUI.ModsManager/)
5. **Concrete PC asset differences:** File-type docs identify PC SEB as references to remastered SCD audio, WD as unused on PC, and HD a.us as based on a.fm while PS2 a.us is based on a.jp. [File types](https://openkh.dev/kh2/file-type.html)
6. **BBS is separate:** Its build list distinguishes original PSP editions and Japanese Final Mix ULJM-05775. The checked build list does not establish a PSP-to-PC equivalence map. [BBS builds](https://openkh.dev/bbs/builds.html)

Reference manifest: title/version; platform/store; region/language; edition ID if known; executable/relevant-data SHA-256; patch/build; mods; difficulty; player stats, equipment, form and abilities; party state; capture FPS; measured simulation/animation timebase; OpenKH release/commit/tool versions. Exact numerical fidelity is blocked until this exists; a graybox prototype is not.

## Evidence model

Classify each claim, not each whole enemy:
- V: exact-build data interpretation corroborated by controlled tests.
- D: identified data/script/trigger whose runtime meaning remains partly unconfirmed.
- O: repeatable controlled observation without implementation confirmation.
- H: hypothesis, inferred label, recollection or desired behavior.
- A: intentional adaptation with reason and acceptance test.

A documented tool feature is not V-grade gameplay evidence. Each evidence record needs ID, source/provenance, edition/hash, relative file and BAR entry index/type, motion slot/script offset/trap identifier, capture time/frame range, measurement/unit/error, test setup, sample count and contradictions. Do not upload commercial research inputs to the documentation repository.

Portable output: original action/state specifications, timing/displacement curves, transition guards, target rules and test cases. Preserve the distinction between measured observations and tuning choices. Decompiled output is not a portable source project.

## Enemy verification workflow

The object dictionary verifies Soldier M_EX010 (301), Shadow M_EX020 (302), Large Body M_EX050 (303), Rapid Thruster M_EX660 (304) and Surveillance Robot M_EX770 (306). It also lists world-specific and RAW/CROWD variants: choose the actual combat variant in the pinned copy. [Object dictionary](https://openkh.dev/kh2/dictionary/obj.html)

The first proposed pair is Shadow and Large Body; Soldier is an alternative if the evidence or prototype needs favor it. Candidate labels such as surface-state evasion, directional defense and mobile melee are H-grade hypotheses here, not findings from inspected game scripts. Select two after evidence review; a third enemy is a later expansion.

For each:
1. Match object ID to MDLX/MSET/APDX and encounter parameters; hash and record variant.
2. Inventory motion slots, collision groups and trigger timelines, including unknowns.
3. When authorized locally, decode BDX and map perception, state guards, timers/random draws, motion calls, damage/revenge transitions and attack spawning. Record which host calls lack proven semantics.
4. Join attack references to ATKP/collision groups/stats; record missing joins.
5. Observe at near/mid/far distances, front/side/rear angles, player ground/air state and hit/miss/guard conditions, both alone and grouped. Repeat random cases; one clip cannot establish a probability.
6. Implement an original specification using placeholders; validate isolated behavior before horde integration.

Falsifiable experiments: Soldier speed/attack-choice distribution by distance; Shadow candidate surface-state transition timing and hit acceptance around its boundaries; Large Body front/rear damage/stagger outcomes by attack class. These discover rules rather than assume them.

## Practical fidelity matrix

These are provisional measurement examples, not selected acceptance thresholds or measured KH values. Calibrate tolerances to source uncertainty and intended fidelity before implementing tests. Compare source-time seconds with stated uncertainty, not raw video frames from different editions.

| System | Evidence starting point | Main unknown | Test target |
|---|---|---|---|
| Movement/jump/landing | Slots, root/position tracks, movement triggers | Input acceleration, camera mapping, gravity, world collision | Fixed input trace; speed/apex/time/heading/recovery curves within 5% after coordinate calibration |
| Ground/air Keyblade chains | Motions, attack links, combo intervals | Buffering, action selection, launch pursuit, cancellation priority | Input sweep across transitions; startup/active/recovery/chain boundaries within one verified source tick, or explicit capture uncertainty |
| Weapon hits | Attachment, collision groups, ATKP interval | Swept collision, deduplication, hitstop order | Edge-of-arc fixtures; matching target set and configured damage-event count per attack/target |
| Magic | Cast triggers, MAG-related scripts/data, magc/atkp | Projectile speed/homing/range, AOE shape, MP/cancel rules | Single/multiple targets; timing/radius/range/recovery within 5%; particles never create damage independently |
| Defense | Defensive motions/triggers, reflection flags | Invulnerability edges, cone, failure/counter rules | Attack timing swept around boundaries and angles; matching outcome matrix |
| Enemy decisions | BDX branches/constants plus host-call evidence | Scheduling, randomness, encounter overrides | Deterministic guard fixtures; distribution comparisons for randomness; all gaps tagged |
| Horde adaptation | Original per-enemy state specification | Deliberate new scale behavior | Same ID/HP/status/position/action continuity across distance/visibility; long-range hits affect the target before approach |

Pin one loadout before measuring combos. Start the prototype with one ranged spell and one defense; a close-area spell is a useful later coverage case. Never conflate a spell's behavior between KH2 and BBS because its name matches.

Hard constraint: every visible enemy is a real, reachable, fightable persistent entity. A genuine temporary hidden/invulnerable combat state is different from a fake distant entity. Reduced update frequency must not erase hits, teleport identity, replace a target or suppress long-range interaction. Engine architecture/performance is a separate study.

## Ghidra's narrow role

Use only for a consequential named gap that data and controlled observations cannot resolve, such as a host-call condition that changes a guard outcome. Record executable hash, processor/loader, function/address, callsites and interpretation, then validate against disassembly and experiments. Native PS2 code and BDX use different instruction sets.

Ghidra translates instructions through p-code for analysis; its C-like output does not restore original types, build environment or engine services. Verify processor/loader support rather than assuming generic MIPS handles every platform-specific feature. [Language specifications](https://ghidra.re/ghidra_docs/languages/index.html), [P-code reference](https://ghidra.re/ghidra_docs/languages/html/pcoderef.html), [Introductory guide](https://ghidra.re/ghidra_docs/GhidraClass/Beginner/Introduction_to_Ghidra_Student_Guide.html)

Stopping rule: investigate one stated blocker with an observable result. If unresolved, document a bounded adaptation and continue; full-game decompilation is not a gate.

## Conditional Unreal-asset tooling

[UAssetGUI](https://github.com/atenfyr/UAssetGUI) supports low-level inspection/editing of Unreal
assets and JSON conversion with explicit engine-version and optional mapping inputs. It is not a
KH2/BBS parser or a recovered combat runtime. Consider it only if KH3 or DW3 Remastered later becomes
a selected research source; this pass does not verify either game's exact package compatibility.
Confirm source-game build, cooked engine version, mappings and applicable access/asset permissions
before using it. It is unnecessary for the initial KH2/OpenKH route and does not determine the engine
of this new standalone game. No such assets were opened in this research.

## Provenance and distribution

The checked OpenKH LICENSE is Apache-2.0. Reused tool code needs applicable license/attribution/notices and change notices; inspect dependency/submodule licenses separately. This does not grant rights to commercial models, animation, audio, scripts, executables or branding acquired elsewhere. Tool availability and owning a game do not by themselves establish redistribution permission. [LICENSE](https://github.com/OpenKH/OpenKh/blob/master/LICENSE)

Use original/appropriately licensed placeholders and original implementation for the standalone prototype. Keep commercial binaries, extracted content and decompiler output outside public commits/builds. Record private-local provenance with hashes. Resolve permissions/applicable legal questions before distributing protected material; this technical plan does not establish authorization.

## Exact first desktop tasks and gates

1. Confirm available lawful reference copy and exact desired baseline; no extraction is included in this completed research task.
2. Pin OpenKH release/commit, OS and runtime; verify selected tool help/about output.
3. Create reference manifest/evidence ledger and separate private research inputs from public source/output.
4. With authorized local inputs, prove one object/motion/trigger timeline is readable and internally consistent. Record bone counts, slots, tool version and frame comparison. This is the compatibility gate.
5. Establish capture timebase and fixed loadout; measure movement, one ground chain, one air chain, one ranged magic configuration and one defense matrix; add a close-area case when useful.
6. Produce two enemy evidence packets; implement isolated placeholder tests before mixed encounters.
7. Scale those same persistent entities; prove continuity and long-range interaction before judging visual crowd size.
8. Escalate only unresolved consequential fidelity gaps to narrow executable analysis; label approximations instead of hiding them.

Gating unknowns: exact source build, reference availability, local tool compatibility, player loadout, capture timing, format support and unknown trigger/trap semantics. None requires a Dynasty Warriors decompilation.
