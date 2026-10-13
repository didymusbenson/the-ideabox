# Engine evaluation

Research checked 2026-10-13. **Current decision: Unreal Engine, targeting PC**, selected explicitly by
the user. Windows is an initial-build assumption; the PC operating system was not explicitly chosen.
No exact Unreal version, minimum hardware, resolution, frame rate or enemy-count target is selected.
This is a design/target decision, not a measured capacity claim or approval to install or implement.
Documentation versions differ; pin and validate a released editor/toolchain combination before work.

## Decision record

- User: “unreal is the right target.”
- User: “pc as target”
- Confirmed: Unreal Engine and PC; Steam reference distribution; intended development on the user’s
  MacBook Pro, separate from the current secondary machine.
- Assumed, awaiting clarification when needed: Windows as the first build target.
- Still open: combat route, engine version, target PC specification, frame budget, keyboard/mouse and
  controller requirements, exact Steam game/build, Mac model/chip/RAM and asset workflow.
- Development-host availability is unverified. Do not equate a device-catalog entry with the intended
  MacBook Pro or assume a Mac development host establishes the final PC operating system.
- Confirm the Mac editor/tooling and eventual target-build workflow before setup; no cross-compilation
  or OpenKH GUI compatibility is assumed by this decision record.

The comparative research below is retained as historical rationale and alternatives, not an active
requirement to benchmark multiple engines before proceeding. Do not silently reopen the user's engine
choice because an implementation issue arises; first diagnose it within the selected Unreal path.

## Historical shortlist (superseded by the decision above)

The initial research compared Unreal's close-up animation/action-authoring strengths with Unity's
C#/data-oriented workflow, with Godot as an optional open-source/lightweight alternative. These were
engineering judgments rather than measured rankings. Unreal was already the proposed first candidate
when action feel and animation authoring dominate. Unity/Godot notes remain useful context only.

Simulation detail is separate from whether an enemy exists. Cheaper meshes, animation and decisions are acceptable. Identity, position, health, statuses, query participation and reachable combat existence persist. A draw instance can represent a real entity; a visual-only crowd member cannot count as an enemy. Never meet a density target by making visible enemies untargetable until the player crosses an activation radius.

## Unreal — selected engine

### Proposed first proof of concept

Start small: an Unreal Third Person foundation, authored movement/input and combo rules, Animation
Montages for attack playback, explicit gameplay hit queries, and one simple enemy. The ongoing
base-Sora movement/basic-attack discussion is a proposed initial slice, not a final choice between
Sora and the BBS Knights. Use original or appropriately licensed placeholders; no commercial imports
or implementation are performed by this documentation update.

Epic's Third Person template supplies a moving/jumping character and basic environment; it does not
supply KH combat feel. [Third Person template](https://dev.epicgames.com/documentation/en-us/unreal-engine/third-person-template-in-unreal-engine).
Montages combine animation sequences and support runtime section playback; buffering, branching,
cancels, movement, hit timing and damage rules remain authored gameplay.
[Animation Montages](https://dev.epicgames.com/documentation/en-us/unreal-engine/animation-montage-in-unreal-engine)

Prove movement, camera, basic attacks, hit reactions and enemy interaction before crowd engineering.
Do not begin with Mass. Add crowd systems only when profiling and correctness tests justify them;
the persistent-real-enemy contract still shapes the simple enemy's identity and hit handling.

### Later crowd and animation validation

Official MassGameplay documentation separates representation and simulation LOD. Representation can use high/low-resolution Actors, instanced static meshes or none; simulation LOD supports variable-frequency updates. Mass StateTree uses signals to arrange entity processing. The documentation labels Mass ISM animation experimental. These are useful building blocks, not a turnkey combat guarantee. [MassGameplay](https://dev.epicgames.com/documentation/en-us/unreal-engine/overview-of-mass-gameplay-in-unreal-engine)

Root motion can drive Character movement. The documented Walking/Falling behavior ignores root-motion Z and applies gravity, whereas Flying applies full root motion. Air combos need a deliberate movement policy. Enabling documented root-motion modes can also add game-thread work. [Root motion](https://dev.epicgames.com/documentation/en-us/unreal-engine/root-motion-in-unreal-engine)

Motion Warping modifies authored root motion around targets. It is relevant to gap closers, but selection, collision constraints, allowable warp distance and cancellation remain game work. [Motion Warping](https://dev.epicgames.com/documentation/en-us/unreal-engine/motion-warping-in-unreal-engine)

The Animation Budget Allocator throttles skeletal updates and can interpolate under a platform-specific time budget. Since ticks can stop or slow, authoritative hit windows cannot depend solely on throttled mesh updates. [Animation Budget Allocator](https://dev.epicgames.com/documentation/en-us/unreal-engine/animation-budget-allocator-in-unreal-engine)

Proposed path: conventional player and initial enemy character/animation tooling, with combat accessing stable enemy records from day one. Move measured crowd hot loops to Mass only when justified. StateTree handles intent/orchestration; explicitly ordered processors handle combat. Free battlefield navigation is a separate requirement from a lane-following crowd sample. Stock ISM/Actor promotion must be tested for state transfer and collision continuity; it does not automatically preserve custom damage.

Small-team/Codex judgment: C++, data definitions, tests and build scripts are reviewable text artifacts. Animation assets, retargeting and Blueprint graphs still need editor authoring and visual inspection. Binary assets require disciplined ownership/versioning. Compile time and editor footprint belong in the evaluation on the eventual desktop.

## Unity — historical alternative

Unity's ECS feature set includes Entities, Entities Graphics and Unity Physics. Rendering/LOD infrastructure does not by itself establish a finished crowd-combat animation stack. [ECS feature set](https://docs.unity.com/en-us/engine/6000.7/manual/packages-list/feature-sets/ecsfeature)

The checked Entities Graphics 1.4 mesh-deformation documentation labels that path experimental and lacking some SkinnedMeshRenderer features. This is a **version-specific caveat**, not a claim about every Unity animation option. Verify the production animation route in the exact candidate versions, including skinning, root motion, hit reactions and target builds. [Entities Graphics 1.4 deformation](https://docs.unity3d.com/Packages/com.unity.entities.graphics@1.4/manual/mesh_deformations.html)

Unity Physics world queries use a broadphase. Its docs warn that queries normally see the last built collision world; synchronizing it costs work. Deliberately order movement, collision-world construction and combat. [Collision queries](https://docs.unity3d.com/Packages/com.unity.physics@1.3/manual/collision-queries.html)

The documented NavMeshAgent is a Behaviour component. Adding Entities does not establish a scalable ECS navigation pipeline. Test a hybrid or data-oriented path including choke points and airborne/knockback transitions. [NavMeshAgent](https://docs.unity.com/en-us/engine/6000.0/script-reference/unityengine/ai/navmeshagent)

Proposed path: conventional player controller/Animator and modest interactive baseline, with explicit enemy gameplay records. Add jobs/ECS around measured simulation/query costs. Prove GameObject/ECS transform and animation handoffs before scaling. Avoid paying for duplicate full simulation stacks; native physics and a custom index must use one damage arbitration layer.

Small-team/Codex judgment: C# mechanics, tests, editor/import scripts and data tables fit text-based iteration. The hybrid boundary and package compatibility add work. Third-party animation packages could change the tradeoff but are not assumed, purchased or recommended here.

## Godot — historical alternative

AnimationTree supports root-motion extraction and blended control. Low-level rendering/physics/navigation servers offer alternatives to per-node overhead. NavigationServer changes synchronize rather than becoming immediately visible, so ordering matters. [AnimationTree](https://docs.godotengine.org/en/stable/tutorials/animation/animation_tree.html), [Servers](https://docs.godotengine.org/en/stable/tutorials/performance/using_servers.html), [NavigationServer](https://docs.godotengine.org/en/stable/tutorials/navigation/navigation_using_navigationservers.html)

MultiMesh is a render optimization, not enemy health, AI or collision. Official documentation describes whole-MultiMesh rather than individual-instance visibility culling. Spatially partition batches and verify the chosen release; the source page is flagged outdated, so this is explicitly a recheck item. [MultiMesh documentation source](https://github.com/godotengine/godot-docs/blob/master/tutorials/performance/using_multimesh.rst)

Godot's navigation guidance recommends staggering requests and simplifying navmesh complexity. [Navigation performance, 4.4](https://docs.godotengine.org/en/4.4/tutorials/navigation/navigation_optimizing_performance.html)

Proposed path: ordinary nodes for initial controller/animation; compact arrays/server-backed views only if profiling warrants them, potentially C# or native extensions for hot loops. Do not begin by writing a crowd renderer.

Small-team/Codex judgment: text scripts/scenes and engine source are attractive, but efficient skinned crowds, custom queries and asset tooling may consume the time saved by the smaller toolchain. Godot is not disqualified by genre; require the same real interaction benchmark.

## Official licensing snapshot

Checked 2026-10-13, not legal advice or a substitute for applicable terms before release.

- Unreal's public page states the standard game route is 5% royalty on attributable lifetime gross revenue above US$1 million, with Epic Games Store sales excluded there; distributed runtime games use royalties rather than non-game seats. Check the actual EULA, exclusions and any incentive programs before release. [Unreal licensing](https://www.unrealengine.com/license)
- Unity's 2026 page lists free Personal up to US$200,000 annual revenue/funding; Pro US$2,310/year per seat prepaid or US$210/month, with regional/tax variation. Runtime Fee is canceled. It also says first-party Havok entitlement/support does not continue into Unity 6.3; do not assume Havok is included. [Unity pricing updates](https://unity.com/products/pricing-updates)
- Godot is MIT-licensed with distribution copyright/license notice requirements; assets and third-party components have their own terms. [Godot license](https://godotengine.org/license/)

Engine licenses do not grant rights to Kingdom Hearts, Disney, Square Enix, Dynasty Warriors or Koei Tecmo assets/IP. Prototype with original/properly licensed content; engine choice does not resolve distribution rights.

## Unreal validation gate

Engine selection does not establish combat feel or crowd capacity. In the selected Unreal version,
validate the small controller/animation and real-entity encounter first. Record toolchain setup and
iteration cost, root-motion/air-combat behavior, navigation correctness, combat continuity and measured
performance on the intended PC hardware. Preserve the one-enemy baseline when later scaling up. Use the [prototype gates](prototype-plan.md) and
[interactive-horde matrix](interactive-horde.md). Reject an approach that requires distant enemies to
be untouchable even if its crowd rendering is impressive.

Profile packaged optimized builds as well as diagnostic builds. Keep import/shader warmup separate
from steady play and streaming. Track live, visible, animated, nearby-engaged and simulation-tier
counts separately. CPU and GPU can overlap; do not simply add their frame times. If 60 fps is chosen,
the complete frame envelope is 16.67 ms; if 30 fps, 33.33 ms. Neither target is selected here.

Useful official profiling references: [Unreal Insights](https://dev.epicgames.com/documentation/en-us/unreal-engine/unreal-insights-in-unreal-engine),
[Unity profiler markers](https://docs.unity.com/en-us/engine/6000.5/manual/analysis/profiler/markers),
and [Unity custom instrumentation](https://docs.unity.com/en-us/engine/6000.6/manual/analysis/profiler/customizing/adding-information-code/intro).

The Unreal validation record should report the tested versions/hardware/scenarios, three prototype gate
results, extra custom systems required, editor/asset workflow friction, license considerations and
remaining uncertainties. A vendor crowd demo does not establish this project's capacity.
