# Sources and evidence register

Public primary documentation/source checked 2026-10-13. Links below support tool or engine
capabilities, not claims that a particular Heartless behavior has been reproduced or that a target
crowd size has been achieved. Detailed qualifications appear beside citations in the research docs.
Mutable documentation may change; pin release/commit and archive relevant evidence references when
a later implementation begins. No commercial game data was inspected in this pass.

## Combat-route reference supplement — 2026-10-13

[Combat routes](combat-routes.md#source-provenance-and-named-move-candidates) carries direct citations
and the source-fact versus proposed-mapping distinction for each move:
- Primary: [Piggyback's official KH2 guide sample](https://www.piggyback.com/en/kh2_e_samplepages/),
  printed pp. 28–29, for normal attacks and finishers.
- Secondary: KHWiki's individual BBS command entries, Shotlock, Valor Form, Limit Form, Stun Impact,
  Finishing Leap and Magnet Burst, linked beside the relevant claims in the route document.

The secondary entries support reference identification and edition cautions, not exact-build timing
or runtime verification. Stun Impact is KH1 Final Mix-origin inspiration; it must not be relabeled
as a canonical KH2 base-Sora move. No command conversion or gameplay experiment was performed.

## Public primary sources

- [Object Editor](https://openkh.dev/tool/GUI.Kh2ObjectEditor/) — used in [toolchain-research.md](toolchain-research.md)
- [MSET](https://openkh.dev/kh2/file/anb/mset.html) — used in [toolchain-research.md](toolchain-research.md)
- [ANB](https://openkh.dev/kh2/file/anb/anb.html) — used in [toolchain-research.md](toolchain-research.md)
- [Bdxio](https://openkh.dev/tool/CLI.Bdxio/) — used in [toolchain-research.md](toolchain-research.md)
- [AI](https://openkh.dev/kh2/file/ai/) — used in [toolchain-research.md](toolchain-research.md)
- [ISA](https://openkh.dev/kh2/file/ai/kh2ai.html) — used in [toolchain-research.md](toolchain-research.md)
- [BdxTraps.cs](https://github.com/OpenKH/OpenKh/blob/master/OpenKh.Command.Bdxio/Models/BdxTraps.cs) — used in [toolchain-research.md](toolchain-research.md)
- [Atkp.cs](https://github.com/OpenKH/OpenKh/blob/master/OpenKh.Kh2/Battle/Atkp.cs) — used in [toolchain-research.md](toolchain-research.md)
- [Mod creation](https://openkh.dev/tool/GUI.ModsManager/creatingMods.html) — used in [toolchain-research.md](toolchain-research.md)
- [PMO](https://openkh.dev/bbs/file/type/pmo.html) — used in [toolchain-research.md](toolchain-research.md)
- [PAM](https://openkh.dev/bbs/file/type/pam.html) — used in [toolchain-research.md](toolchain-research.md)
- [BBS library](https://github.com/OpenKH/OpenKh/tree/master/OpenKh.Bbs) — used in [toolchain-research.md](toolchain-research.md)
- [PAM converter](https://github.com/OpenKH/OpenKh/tree/master/OpenKh.Command.PAMtoFBXConverter) — used in [toolchain-research.md](toolchain-research.md)
- [PMO converter](https://github.com/OpenKH/OpenKh/tree/master/OpenKh.Command.PmoConverter) — used in [toolchain-research.md](toolchain-research.md)
- [Repository](https://github.com/OpenKH/OpenKh) — used in [toolchain-research.md](toolchain-research.md)
- [KH2 builds](https://openkh.dev/kh2/builds.html) — used in [toolchain-research.md](toolchain-research.md)
- [Editions](https://openkh.dev/kh2/editions.html) — used in [toolchain-research.md](toolchain-research.md)
- [BAR](https://openkh.dev/kh2/file/type/bar.html) — used in [toolchain-research.md](toolchain-research.md)
- [Mod Manager](https://openkh.dev/tool/GUI.ModsManager/) — used in [toolchain-research.md](toolchain-research.md)
- [File types](https://openkh.dev/kh2/file-type.html) — used in [toolchain-research.md](toolchain-research.md)
- [BBS builds](https://openkh.dev/bbs/builds.html) — used in [toolchain-research.md](toolchain-research.md)
- [Object dictionary](https://openkh.dev/kh2/dictionary/obj.html) — used in [toolchain-research.md](toolchain-research.md)
- [Language specifications](https://ghidra.re/ghidra_docs/languages/index.html) — used in [toolchain-research.md](toolchain-research.md)
- [P-code reference](https://ghidra.re/ghidra_docs/languages/html/pcoderef.html) — used in [toolchain-research.md](toolchain-research.md)
- [Introductory guide](https://ghidra.re/ghidra_docs/GhidraClass/Beginner/Introduction_to_Ghidra_Student_Guide.html) — used in [toolchain-research.md](toolchain-research.md)
- [LICENSE](https://github.com/OpenKH/OpenKh/blob/master/LICENSE) — used in [toolchain-research.md](toolchain-research.md)
- [MassGameplay](https://dev.epicgames.com/documentation/en-us/unreal-engine/overview-of-mass-gameplay-in-unreal-engine) — used in [engine-evaluation.md](engine-evaluation.md)
- [Root motion](https://dev.epicgames.com/documentation/en-us/unreal-engine/root-motion-in-unreal-engine) — used in [engine-evaluation.md](engine-evaluation.md)
- [Motion Warping](https://dev.epicgames.com/documentation/en-us/unreal-engine/motion-warping-in-unreal-engine) — used in [engine-evaluation.md](engine-evaluation.md)
- [Animation Budget Allocator](https://dev.epicgames.com/documentation/en-us/unreal-engine/animation-budget-allocator-in-unreal-engine) — used in [engine-evaluation.md](engine-evaluation.md)
- [ECS feature set](https://docs.unity.com/en-us/engine/6000.7/manual/packages-list/feature-sets/ecsfeature) — used in [engine-evaluation.md](engine-evaluation.md)
- [Entities Graphics 1.4 deformation](https://docs.unity3d.com/Packages/com.unity.entities.graphics@1.4/manual/mesh_deformations.html) — used in [engine-evaluation.md](engine-evaluation.md)
- [Collision queries](https://docs.unity3d.com/Packages/com.unity.physics@1.3/manual/collision-queries.html) — used in [engine-evaluation.md](engine-evaluation.md)
- [NavMeshAgent](https://docs.unity.com/en-us/engine/6000.0/script-reference/unityengine/ai/navmeshagent) — used in [engine-evaluation.md](engine-evaluation.md)
- [AnimationTree](https://docs.godotengine.org/en/stable/tutorials/animation/animation_tree.html) — used in [engine-evaluation.md](engine-evaluation.md)
- [Servers](https://docs.godotengine.org/en/stable/tutorials/performance/using_servers.html) — used in [engine-evaluation.md](engine-evaluation.md)
- [NavigationServer](https://docs.godotengine.org/en/stable/tutorials/navigation/navigation_using_navigationservers.html) — used in [engine-evaluation.md](engine-evaluation.md)
- [MultiMesh documentation source](https://github.com/godotengine/godot-docs/blob/master/tutorials/performance/using_multimesh.rst) — used in [engine-evaluation.md](engine-evaluation.md)
- [Navigation performance, 4.4](https://docs.godotengine.org/en/4.4/tutorials/navigation/navigation_optimizing_performance.html) — used in [engine-evaluation.md](engine-evaluation.md)
- [Unreal licensing](https://www.unrealengine.com/license) — used in [engine-evaluation.md](engine-evaluation.md)
- [Unity pricing updates](https://unity.com/products/pricing-updates) — used in [engine-evaluation.md](engine-evaluation.md)
- [Godot license](https://godotengine.org/license/) — used in [engine-evaluation.md](engine-evaluation.md)
- [Unreal Insights](https://dev.epicgames.com/documentation/en-us/unreal-engine/unreal-insights-in-unreal-engine) — used in [engine-evaluation.md](engine-evaluation.md)
- [Unity profiler markers](https://docs.unity.com/en-us/engine/6000.5/manual/analysis/profiler/markers) — used in [engine-evaluation.md](engine-evaluation.md)
- [Unity custom instrumentation](https://docs.unity.com/en-us/engine/6000.6/manual/analysis/profiler/customizing/adding-information-code/intro) — used in [engine-evaluation.md](engine-evaluation.md)

- [UAssetGUI](https://github.com/atenfyr/UAssetGUI) — conditional scope in [toolchain-research.md](toolchain-research.md)

## Implementation evidence record template

- Claim ID and plain-language claim
- Confidence: verified exact-build test / documented field or script / observation / hypothesis / adaptation
- Game edition, platform/store, region/build, relevant hashes, loadout and encounter setup
- Tool/editor/package release and source commit
- Source URL or lawful private-local input reference; file/object/motion/script offsets as relevant
- Reproduction steps, input trace, capture timebase, units and uncertainty
- Expected and observed outcomes, repeated samples, contradictions and remaining unknowns
- New implementation rule and intentional deviations
- Regression fixture plus measured pass/fail result

Keep proprietary binaries and raw extracted assets out of this public repository. A source-code
parser, field name, named host call or AI explanation is not by itself verified gameplay semantics.

## This pass's verification boundary

Verified repository layout and contribution convention, public tool/engine documentation and relevant
source presence, completeness/local links of these planning documents, and publication commit hashes.
No engine benchmark, asset conversion, extraction, game behavior measurement, executable analysis,
controller playtest or deployed game is claimed.
