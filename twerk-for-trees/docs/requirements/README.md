# Twerk for Trees — requirements baseline v1

**Status: implementation-ready initial requirements, not a completed game.** This is the documented baseline for a first end-to-end implementation. The values are concrete enough to build and test; they are not asserted to have passed a real playtest or been approved as final balancing. The original [author pitch](../../README.md), [macro progression](../progression.md) and [research-backed design](../progression-design.md) remain the product context. Where those earlier proposals leave a decision open, this package defines the first-build behavior.

## Read in this order

1. [Product and actual progression requirements](01-progression.md) — scope, milestones, mandatory/optional path, repeatable economy, root through endgame, prestige.
2. [Content catalog](02-catalog.md) — every initial item, cultivar, unlock, upgrade, task, enemy, generator and endgame example in readable tables.
3. [Simulation, data and persistence requirements](03-simulation-and-state.md) — timing, scheduler, resource reservations, power, combat, save, offline and edge-case rules.
4. [Interface, accessibility and presentation](04-interface.md) — screens, interaction contract, states, notifications, touch/keyboard, art direction.
5. [Acceptance criteria and delivery roadmap](05-acceptance-and-roadmap.md) — test IDs, expected results, vertical-slice and full-release gates, explicit exclusions.
6. [Storage capacity progression](06-storage.md) — shared ceiling, six scalable module tiers, resource targets, overflow and reserved-input rules. This is required v1 functionality.

The source of truth for numerical content is [`data/progression-v1.json`](../../data/progression-v1.json), schemaVersion 1, balanceVersion v1.1-storage-candidate. The prose defines semantics not encoded in numerical data. Do not independently edit table values without updating the catalog and rerunning checks; do not change stable IDs once saves have shipped. [The design validator](../../tools/validate_progression.py) checks content references, existence of an unlock path, exact ingredient affordability and hard storage limits along a deterministic witness, and terminal steady-state material/power/storage capacity. It requires Python 3 and no dependencies:

```sh
cd twerk-for-trees
python3 tools/validate_progression.py
```

## Requirements precedence and scope

- The creative pitch remains the north star: silly wholesome animated twerkers, meaningful active input, dirt expansion, renewable resource trees, escalating automation, a singularity win. No copying Minecraft/third-party assets or data. [Research evidence](../sky-factory-4-research.md) is background, not game IP or a recipe source.
- This package deliberately specifies **one playable first release** with a complete path through Worldseed production; more species, enemy content, monetization, cloud accounts, multiplayer, and live-service events are excluded.
- Implementation work can begin on Rootwork and progressively enable features. First-run timing, fuel cost, combat success rates, artwork, text, worldseed threshold and prestige tuning are all candidates to validate with real traces. Any later product changes should update this package rather than silently diverge.
- No production app code or game build has been delivered by writing this spec. The Python script is a requirements/data check, not an engine or executable prototype.
