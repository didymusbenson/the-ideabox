# Every visible enemy is real

## Required invariant

For every visible enemy representation, there is exactly one authoritative gameplay entity with a
stable identity, current position, relevant behavior/defense state, health and interaction history.
The representation does not substitute for the entity. The entity remains reachable within the
playable encounter and supports valid melee, ranged and area interactions. Visibility is not the
only interaction criterion: an enemy behind the camera, at range, or between simulation tiers can
still be affected by a valid attack.

Temporary invulnerability or defense is valid only when it is an authored, evidence-backed behavior
with appropriate feedback. Distance-based invulnerability is invalid. No visual-only horde impostors,
vanishing targets, untracked GPU-only enemies, or unreachable background armies count toward scale.

## Proposed architecture (to test, not engine commitment)

- **Authoritative registry:** stable IDs/generations; transforms; health; behavior state and elapsed
  time; defense/hit-reaction state; navigation intent; lifecycle and objective relevance.
- **Spatial query layer:** queries the complete relevant population, including reduced-frequency
  entities. Rendering membership is not the combat broadphase.
- **Simulation scheduler:** budgets decisions/pathfinding/animation separately. Nearby combat and
  imminent interactions receive high-detail processing. Distant entities can use cheaper decisions
  and locomotion, provided their observable motion/state remains correct.
- **Presentation layer:** mesh/animation/shadow LOD derives from entity state. Swapping representation
  never resets identity, health, animation phase relevant to a hit window, or behavior timers.
- **Interaction resolver:** projectiles, raycasts, swept attacks and explosions resolve against
  current authoritative state, not a stale collider frozen until the player arrives.

### Correctness-first baseline

Initially keep compact movement integration and query bounds current each combat tick; throttle AI
decisions and visual updates first. If movement itself is later coarse, define its trajectory at any
interaction time and prove conservative candidate gathering plus exact refinement. A large stale
broadphase box is not sufficient evidence of a hit. Include vertical extent, terrain obstruction and
line of sight in the appropriate narrowphase rules.

Attack-instance IDs and per-target rules prevent duplicate damage across cells, frames and adapters.
A gameplay action clock and event ledger keep attack/defense windows correct while skeleton updates
are throttled; do not apply damage independently from both animation notifies and timeline events.

### Adapter handoff and overload

Only one system writes an entity's authoritative transform at a time. Hydrate a richer adapter from
the current health, statuses, action clock, velocity and reaction; commit state before demotion. Use
hysteresis and a speed/latency-based approach horizon to prewarm presentation. Teleports and long-range
hits still work without that preparation. Damage cannot wait for a rich actor to become available.
Pool exhaustion may reduce visual detail or planning frequency; it must never create invulnerability.
Test exhausted pools, homing/reflected attacks, sudden mass promotion and pending-promotion hits.

### Distant interaction procedure

1. Predict or advance the relevant entities to the query/impact time under the same authoritative
   time model; conservatively gather candidates across their possible movement envelopes.
2. Resolve exact position and gameplay-relevant defense/attack state before accepting/rejecting hits.
3. Apply damage, hit reaction, aggro and objective events once to stable IDs.
4. Promote affected entities if continuing interactions require it; reconcile presentation without
   teleportation, resurrected health or duplicate hits.

This can use analytic/simple locomotion or temporary promotion, but neither technique is assumed to
be free or automatically correct. Fast projectiles and moving targets need swept/time-aware tests.
Long-range attacks must not rely only on a radius around the player to activate targets. Multiple
attacks hitting during promotion/demotion need ordered events and exactly-once damage semantics.

## Optimization order

Profile first. Reduce redundant AI decisions, share navigation queries, use spatial partitioning,
batch simple work, limit avoidable skeletal updates, and use visual LOD. Keep combat collision and
state semantics independently valid. Attack coordination may limit how many enemies attack at once
for readability, but all still exist, can be approached/hit, and react correctly. If performance
fails, reduce actual concurrent enemy count or battlefield scope; never swap in fake enemies.

## Correctness test matrix

Run at multiple population levels and on both sides of every tier threshold. Each test records
entity IDs, timestamps, positions/states, hit events and expected outcomes.

| Test | Pass condition |
|---|---|
| Walk toward one distant visible enemy | Same ID, health and evolving state; no pop/spawn substitute; reachable encounter |
| Fire long-range magic while standing still | Hit/miss follows actual path and state before player proximity activates anything |
| Fast projectile crosses multiple tiers | Swept collision catches valid targets; no tunneling from coarse ticks |
| Large area attack overlaps several tiers | Same target set and one damage event per target as the high-detail reference |
| Defense window begins/ends between coarse updates | Hit accepted/rejected at impact time by defense rule, not stale state |
| Enemy moves behind camera or becomes occluded | Existing projectile and objective interactions still resolve correctly |
| Repeated boundary crossings | No duplicated entity, position discontinuity, health reset or timer restart |
| Launch/knockback across boundary | Trajectory and recovery continue; no lost airborne collision |
| Kill during promotion/demotion | One death/reward/objective event; no resurrection or orphaned renderer |
| Many simultaneous ranged hits | No missing hits under load; promotion storm measured rather than hidden |
| Ally fights distant visible enemies | Authoritative outcomes reflect combat; player approach does not rewrite history |
| Obstacles, narrow passage, airborne player | Reachability/route failure handled explicitly; no permanently decorative stranded crowd |

Use a full-detail reference mode for controlled equivalent scenarios, with deterministic seeds where
practical. Exact cross-engine physics determinism is not assumed. Compare gameplay events and bounded
trajectory/state tolerances, recording divergences. Screenshots alone cannot prove interactivity.

## Performance test matrix

Proposed sweep: 32, 64, 128, 256, 512 entities, continuing only while useful. These are experimental
steps, **not promised shipping counts**. Vary nearby attackers, visible count, projectiles, spell area,
path updates, obstacle density, animation complexity and ally load separately. Include worst-case
all-visible/all-in-range, mass promotion, effects-heavy combat, and long sustained runs.

Record hardware, OS, engine/build/settings, revision, scenario/seed, resolution, entity counts,
CPU/GPU frame time distributions (median/p95/p99), spike causes, AI/nav/animation/collision time,
memory and allocations. Agree the target frame budget and acceptable tail latency before declaring a
pass. Report correctness alongside timings; performance measured with dropped interactions fails.
