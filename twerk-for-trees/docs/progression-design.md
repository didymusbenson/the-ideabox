# TFT — detailed progression design (proposal)

> Implementation now follows the [v1 requirements package](requirements/README.md), including the
> exact [content catalog](../data/progression-v1.json), engine semantics and acceptance tests. This
> research-backed proposal is retained as rationale and context; where values differ, use the v1
> requirements baseline for implementation.

**Status:** research-backed design, not implemented or playtested. This extends [progression & tech branches](progression.md), [zones & interface](zones-and-interface.md), and the author's [pitch](../README.md). It preserves the clay automation gate, seed-drop Farm, resource-tree trunk, Quarry, critical-path Arena, shared Power Grid, and Universal Paperclips-inspired singularity. See the [SF4 research](sky-factory-4-research.md) for evidence. All names, recipes, values and age labels below are TFT proposals; nothing imports Minecraft assets, recipes, proprietary naming or mods.

## 1. Player experience and hard constraints

The player should go through five distinct feelings, not five equivalent rows of bigger numbers:

1. **I have nothing.** One ordinary tree, one plot, one twerker; finish a harvest by tapping the mascot.
2. **I can build more trees.** Make dirt from leaf litter, expand capacity, discover a new species and choose which plot to accelerate.
3. **The orchard works without me.** Clay unlocks the first collection automation. Farming becomes a second resource engine; tool and soil investment make familiar trees more useful.
4. **I am running an industry.** Quarry increases bulk materials; Factory processes them; generators are a real shared production constraint; Arena materials enable more machines.
5. **I am making something impossibly large.** Many automated lines feed one terminal product, then a deliberate choice to keep optimizing or build a faster new world.

**Do not make a tap directly mint wood, clay, etc.** Taps accelerate the selected plot's timer; the output is a completed action. Every improvement gives a meaningful new action, new ingredient, new resource route, or new control lever. The UI always explains the next unlock in material terms rather than a mystery progress bar. No tier requires a future tier's input, no permanent first-run loss of a last seed, and no reliance on an unbounded rare drop to open required content.

## 2. Proposed dependency spine

Arrows are capabilities and resources, not a linear quest checklist. Parallel activities may interleave. The Workshop buys/builds unlocks, but the relevant zone performs production.

```text
Starter tree -> litter -> dirt -> more plots
                    |         |
                    |         +-> screen -> grit -> stone tree
                    |                             -> clay tree -> mechanical collector
                    +-> field seed -> Farm -> compost, fibre, oil
Stone + clay -> kiln -> charcoal / fired parts -> copper + iron cultivation
                          |                         |
                          +-> fuelwood/coal tree     +-> pick -> Quarry
                                                    +-> tin -> bronze / iron tools
                                                    +-> basic generator -> Power Grid
Farm fibre + iron/bronze -> Arena -> creature catalysts
Quarry + Farm + Orchard + metal tools -> Factory -> powered processing/routing
Copper + quartz + resin -> control systems; Arena catalyst -> safe automatic combat
Factory + Grid + upgraded Farm/Quarry -> advanced alloy, polymer, crystal
Advanced alloy + crystal + polymer + catalysts -> convergence core
Convergence core + all-zone sustained inputs + surplus power -> Worldseed Press
Worldseed quantity threshold -> Singularity -> Endless OR Replant
```

The Farm can open earlier than Clay, and the Quarry and Arena can open before a full Factory build. Factory and Grid are separate: basic power is buildable from the metal phase, before the first electric processor. Bronze is useful but not required to construct the first generator. First-run paths may choose to improve plots, Farm, or mining first; all converge in industrial and terminal recipes. Arena progression is required for some machine families, but basic power and material inputs must be obtainable without Arena.

### Milestone tiers

| Phase | What the player builds and does | New bottleneck | First visible payoff |
|---|---|---|---|
| Roots (MVP) | Starter wood → dirt expansion → screen → stone and clay trees → mechanical collection | Plots, timer, buffer | Leave the game and return to harvested materials |
| Cultivation | Farm, improved soil, charcoal/fuel, fiber, crop products; unlock more tree species | Capacity vs quality | Farm waste turns into orchard upgrades |
| Foundry | Kiln, concentrate preparation, basic metals, cast tools, tin & bronze, Quarry | Raw materials and fuel | A bulk ore source and faster metal processing |
| Workshop-to-Factory | Power Grid, small generators, batteries, routing, powered machines, Arena | Watts and input shortages | Run a complete raw-to-refined chain hands-off |
| Industrial | Deeper strata, better soils, polymers, precision parts, mobile drop simulation, efficient energy | Competing chains and resource ratios | Each earlier activity becomes an input supplier |
| Convergence | Terminal press, network throughput, bulk compression and repeated core fabrication | Sustained bottleneck rate | Visible ETA to Singularity |
| After the win | Endless or new world | Optional records or faster rerun | A persistent achievement and meaningful new run |

## 3. Root economy — testable vertical slice

### Inventory, plot and timer rules

- The initial Workshop tab is available at start. It has a basic crafting bench; no paid unlock to access dirt/crafting. Starter tree is planted in one existing plot, inventory empty.
- A tree is a permanent cultivar for this run after first discovery; planting/switching a free plot to a **known** cultivar is free, resetting that plot's growth timer only after confirming any lost partial growth. Replanting the starter on an empty plot always works. Never let the player consume the only seed required to restart. Use cuttings as an early crafting material, not as a consumable permission to use a known tree.
- Base cycle times below include growth and harvest cooldown. A completed unautomated cycle accrues one harvest in a local buffer (capacity three cycles initially); player can collect all ready cycles. A full buffer pauses growth, no lost output. An unautomated plot can accrue three cycles offline then stops. Clay-gated mechanical collectors move finished output into the shared inventory and clear the local buffer, including during offline simulation. The slice's second clay upgrade is a mechanical auto-twerker, which accelerates a single plot's timer independently of collection, preserving the pitch's first auto-twerker payoff.
- One tap subtracts 0.25 seconds from the focused timer during a valid active cycle. Prototype limit: no more than eight accepted taps per rolling second, so natural time plus accepted input is at most 3× base growth. At four valid taps/sec, theoretical 2× effective growth. No tap banking, no time subtracted below zero, no double harvest on concurrent completion; tapping full buffers does nothing and exposes collect control. Taps on other plots split the **one** active attention budget. No auto-clicking required to achieve comfortable pacing.
- A harvest always produces the baseline bundle; optional bonus drops are separately rolled. First Farm seed appears on a starter harvest (chance possible on cycles 1–2, guaranteed by cycle 3 even offline). Farm remains a purchase in the Workshop, not a popup forced on the player. A bonus never replaces baseline resources.
- Early starter materials have no global inventory cap; manual/local buffers are the first deliberate capacity lesson. Industrial storage later limits only machine buffers/queues, not the player's ability to recover a running world.

### Initial recipe and producer baseline (numbers explicitly for prototype)

| ID / recipe | Inputs | Output / effect | Cost/time notes |
|---|---|---|---|
| `starter` | None | 3 timber + 2 litter + 1 cutting / harvest | 12 s cycle |
| `dirt` | 2 litter | 1 dirt | Instant at bench; repeatable |
| `plot` | 3 dirt + 2 timber | +1 empty plot (first expansion); known species free to plant | Later plots grow cost; see below |
| `screen` | 4 timber + 2 dirt | Screen station | One-time Workshop upgrade |
| `grit` | 1 dirt | 2 grit | Screen recipe; deterministic, instant in slice |
| `stone_cultivar` | 2 grit + 1 cutting | Permanent stone cultivar | No target-tree output required |
| `stone` | Known cultivar in a plot | 2 stone + 1 litter + 1 cutting / harvest | 18 s cycle |
| `clay_cultivar` | 2 stone + 1 dirt + 1 cutting | Permanent clay cultivar | A recipe, not a random discovery |
| `clay` | Known cultivar in a plot | 2 clay + 1 litter + 1 cutting / harvest | 20 s cycle |
| `collector` | 4 clay + 4 timber + 2 stone | One mechanical collection attachment per plot | No Grid needed, no acceleration; can be reassigned freely |
| `clockwork_twerker` | 2 clay + 2 timber + 1 stone | One reusable mechanical auto-twerker attachment, 0.8× base cycle duration | After first collector; no electric Grid; later powered models replace rather than stack with it |
| `field` | Field seed + 2 dirt + 3 timber | Farm tab with one field | Seed discovery is guaranteed by harvest 3; optional alongside slice |
| `root_trial` | 3 known species, at least 2 plots, one collector, one clockwork auto-twerker and 10 clay collected after collector install | Slice capstone | Test proxy for endgame; not the live full-world win threshold |

The screen is kept because the pitch calls for it, but is brief and deterministic. It teaches the same combine-to-unlock pattern immediately and is not a loot-dice casino. In the full game, screens/presses remain minor processing devices, not the central source of metal. Prototype may use simple instant conversion; longer processing times become meaningful after multiple producers are active.

**Width vs depth.** Subsequent plots cost dirt and timber. Starting proposal: for the next new plot when there are `p ≥ 1` existing plots, cost `3 + floor((p-1)*1.5)` dirt and `2 + floor((p-1)*1.0)` timber; first expansion exactly 3/2. Test progressively rather than committing to this formula at endgame. Proposed upgrades give distinct value: plot expansion parallelizes separate tree families, compost soil reduces growth time, tool upgrade increases materials per harvest, collector removes collection friction. Make production visible so buying a second collector versus a third plot is a real decision.

### Starter walkthrough (one reproducible deterministic idle schedule)

Conservative check using no taps, collection at scheduled harvests and no Farm bonus. Do not model this as measured playtest.
1. Harvest starter three times (36s) → 9 timber, 6 litter, 3 cuttings; craft 3 dirt and spend 3 dirt/2 timber on plot 2. Plant starter twice.
2. Harvest both starters twice (24s) → gain 12 timber, 8 litter, 4 cuttings. Craft 4 dirt; buy screen (4 timber, 2 dirt), then screen 1 dirt → 2 grit; buy stone cultivar using grit and a cutting. Switch plot 2 to stone.
3. Collect one stone harvest (18s), starter continues in parallel. Spend 2 stone + 1 dirt + cutting to discover clay. Use any available starter litter for further dirt. Keep starter active; collect necessary timber/litter to build plot 3 when affordable (next plot costs 4 dirt, 3 timber). Plant clay on plot 3 (or rotate plot 2 temporarily). Preserve a stone source for collector cost.
4. Collect 2 clay harvests (40s) and at least one more stone harvest; spend 4 clay, 4 timber, 2 stone to build collector. The original two plots may continue while the third grows. Target first collector in roughly 2–5 minutes without tapping, 1–3 minutes with comfortable active rhythm; manual timing and resource decisions are additional. A deterministic event-ledger check reached plot 2 at 36s, stone discovery at 60s, clay discovery at 78s, plot 3 at 96s and the collector at 136s (2m16s), with no negative ingredient counts. Five additional clay cycles bring the clay counter to 10 at 236s (3m56s). It assumed instant crafting and prompt collection and did not model tap input, offline buffers or runtime automation. **Validate those behaviors with a real slice**, not this arithmetic check.
5. Assign collector to clay, leave/simulate elapsed time, and collect the first automatic batch. Build the clockwork auto-twerker after the first two automatically collected clay (20s after installation), spending 2 clay, 2 timber and 1 stone. Then the four remaining required automatic clay cycles take 16s each, giving 10 cumulative collected clay at 220s under the same arithmetic assumptions (8 remaining clay in inventory after the attachment purchase). This extra step demonstrates automatic timer acceleration as distinct from collection. Show a locked next tier teaser and a scaled prestige proxy for the MVP only.

This route demonstrates all gate inputs are possible from current-tier producers. The first collector is an observable payoff, not just a faster animation. Prototype targets are hypotheses; if passive feels slow, adjust cycle time and recipe costs rather than rewarding raw tapping disproportionately.

## 4. Tree roster and production graph (after roots)

The material families below are a starting roster, not a mandatory final catalog. Earlier trees keep producing support ingredients after Quarry unlock. Each first-time discovery uses preexisting inputs; cultivars remain available for the run. Standard growth provides a guaranteed raw bundle, bonus yields can add spice but not gate progression. Ordinary raw ores are processed rather than harvested as finished ingots.

| Family | First discovery inputs / station | Recurring output | Why it matters |
|---|---|---|---|
| Wood | Starter | Timber, litter, cuttings | Dirt, tools, basic fuel, fiber |
| Stone | Screen grit + wood cutting | Stone, litter | Clay, tools, kiln, aggregate |
| Clay | Stone + dirt + cutting | Clay | Collectors, fired parts, kiln |
| Coal | Fired part + charcoal + stone + cutting (kiln) | Coal fragments, litter | Higher density fuel, furnace, generator |
| Copper | Copper concentrate made from clay + stone + charcoal at kiln; graft using one refined copper | Copper raw material | Conductors, circuits, basic generator |
| Iron | Iron concentrate made from coal + stone + fired clay, smelted and grafted | Iron ore | Tools, Quarry, machinery, reinforcement |
| Tin | Stone + fired clay + refined copper sample, kiln → first tin concentrate then graft | Tin ore | Bronze and solder |
| Silica | Stone grit + clay, kiln → glass-grade silica; graft | Silica | Glass, lenses, circuitry |
| Quartz | Silica + iron tool capability, deposit unlocked in Quarry → quartz sample; graft | Quartz | Precision control and late crystals |
| Resinwood | Farm fiber + compost + copper tool capability | Resin, litter | Adhesive, oil/polymer substitutes and upgrade reagents |
| Gem | Quartz + refined iron + Arena mineral core, precision graft station | Gem fragments | Advanced tool and crystal recipes |
| Heavy metal | Deep Quarry ore sample + alloy tool | Heavy ore | Durable high-tier machinery and advanced energy |
| Rare crystal | Gem fragments + quartz + stabilized catalyst, advanced graft station | Crystal shards | Convergence recipes; may grow slowly versus powered processing |

A material recipe may have both a one-time discovery route and a bulk production route; show both in recipe details. Example: copper's initial concentrate comes from pre-metal ingredients, and a smelted first copper unlocks the tree; repeated copper is generated by that tree or mined later, not by repeatedly spending stone/clay/charcoal in the discovery recipe. The first metal concentrate recipes intentionally yield enough for the first ingot/graft; the first graft never consumes the only available source since the bootstrap recipe remains unlocked. No repeated mandatory combustion lottery. No need for 20 distinct ore trees just because SF4 has them.

### Mid-game suggested recipes (quantities illustrative for first economy spreadsheet)

The table uses ordinary resources, not locked numerical balancing. All machine build costs are one-time unless stated; crafting batches may be queued, and recipes show actual input rates. Active Workshop work can finish a queued batch faster but never bypass inputs.

| Upgrade / task | Example build or batch requirement | Produces / unlocks |
|---|---|---|
| Kiln (manual) | 6 clay + 6 stone + 4 timber | Fired parts (2 clay → 1 fired part, heat) and smelting access |
| Charcoal | 2 timber, kiln | 1 charcoal, self-start with timber as fuel; later coal alternative |
| Copper concentrate | 2 clay + 2 stone + 1 charcoal | 2 copper raw; smelt 2 raw + 1 charcoal → 1 copper |
| Iron concentrate | 2 coal fragments + 2 stone + 1 fired part | 2 iron raw; smelt 2 raw + 1 fuel → 1 iron |
| Tin concentrate | 2 stone + 1 fired part + 1 copper | 2 tin raw; need one refined tin for graft, not reciprocal tin input |
| Bronze alloy | 2 copper + 1 tin (kiln with heat upgrade) | 3 bronze; Workshop alloy line |
| Iron pick | 3 iron + 2 timber | Quarry tab and shallow ore beds |
| Dairy/animal pen | Farm crop surplus + timber + fired parts | Livestock food and animal products; no animal required for first metal |
| Quartz stratum | Iron pick + fired parts + stone production | Quartz samples; unlock quartz cultivar |
| Arena gate | Timber + shaped iron/bronze + Farm fiber | First opponent and basic protective gear |
| Basic generator | 4 copper + 3 iron + 2 fired parts | Grid tab; consumes fuel only while operating |
| Factory bench | 4 iron + 3 copper + 2 fired parts, access to Grid | Powered processor bays |
| Powered processor | 3 iron + 2 copper + fired part | Crush/press raw ore batches more efficiently |
| Alloy furnace | 4 iron + 2 bronze + silica glass | Automated metal/alloy processing; no advanced alloy required to build |
| Sorting router | Copper + silica glass + iron | Recipe-input reservation and output collection upgrades |
| Circuit bench | Copper + quartz + resin + iron shell | Control parts; uses manual first batch before automated circuit line |
| Ward motor | Iron/bronze + control parts + first Arena core | Automatic combat and higher machine tier |
| Deep drill | Advanced-grade alloy + control parts + Arena shell | Deeper Quartz/rare-heavy ore, faster than early trees |
| Advanced alloy | Iron + bronze + heavy ore sample (deep stratum unlocked with normal alloy-grade tools first; optional faster drill later) | Durable material for high-tier Factory and generators |
| Polymer line | Farm oil + Resinwood resin + fired catalyst | Polymer, not an imported oil chemistry chain |
| Precision crystal line | Quartz + gem fragments + control parts, powered | Crystal for convergence and efficient generator upgrades |
| Convergence core | Advanced alloy + polymer + crystal + stabilized Arena catalyst | Terminal Press construction and repeatable terminal reagent |

Build recipes for each capability should use at least two families where it makes sense, but avoid forcing every minor recipe to touch all zones. The deep stratum is accessible at slower rates using iron/bronze and quartz-era tools; the deep drill multiplies it, never gates its own heavy ore. A guaranteed heavy-ore sample supports the first tree or advanced alloy. Gem tree is optional if Quarry can supply gem fragments after the required Arena core; precision line needs gem fragments, not specifically tree-produced ones.

The milestone table is not an implementation data file. Final quantities, durations, batch sizes and power requirements need an economy pass, including a route feasibility simulator.

## 5. Zone progression (the seven existing tabs)

### Orchard
- **Roots:** hand-collected buffered production; focused tap speed for one plot; dirt expansion.
- **Clay:** mechanical collector allows unattended transfer. It requires no electric Grid and only automates collection, reconciling the clay-before-metal timing with the shared Grid. The clockwork auto-twerker is the next clay-era upgrade, a small passive timer speedup independent of collection.
- **Farm upgrades:** composted soil, irrigation and fertilizer; soil choices improve duration or yield. A speed upgrade must not double-dip into output. Collector remains useful, not obsoleted.
- **Grid era:** powered auto-twerkers actively accelerate a plot without taps (while consuming watts), powered replant settings for multi-plant plots, production scheduling and bulk collection/routing.
- **Advanced:** nursery specialization increases multiple plants per plot or supports higher-tier cultivars with explicit soil requirements; old trees stay available at lower cost.

### Farm
- Seed unlock by an observed drop, guaranteed by the third ordinary harvest. First field produces crop, fiber and organic waste on a timer. Active watering hastens only the focused field (same attention budget).
- Waste + litter → soil compost (repeated growth improvements). Crops → feed; pen → animal products. Oil crops unlock with iron tools → renewable fuel and Resinwood/polymer input. Irrigation reduces cycle time; animal feed consumed per batch after livestock unlock. First field grows free baseline crop without feed/fuel.
- Later fermenter consumes crops/waste → biofuel for Grid. Oil/refined polymer remain useful after mineral producer scaling. Automated fields and pens use power from Grid; manual harvesting always possible.
- Farms have a clear non-combat route to basic feed; no random seed bottleneck. Farm does not become the only possible fuel source (coal fallback).

### Quarry
- Manual iron pick opens shallow stone/coal/copper/iron beds (guaranteed repeatable tasks). Choosing a bed determines the output, not a generic loot pool. Active mining reduces cycle time.
- Iron tools → silica/quartz/gem-bearing strata; metal/bronze upgrades open slow heavy-ore beds before an advanced drill exists. Quarry throughput should beat comparable raw-resource trees (initial target 2–4× per comparable investment tier), but Orchard still supplies base material unpowered.
- Powered drill/hauler upgrades add throughput and collection. Separate drill and transport costs reduce the incentive to simply multiply drills without expanding power/buffer. Late automated drill supplies bulk metal and slow rare ore fallback.

### Arena
- Simplified HP/success-rate system as specified: first basic opponent offers one guaranteed core on first win and a repeatable common drop. Show win chance, expected health loss, food consumption and payout; no full combat triangle. First fight must be achievable with baseline iron/bronze armor and ordinary crop food. On defeat, cooldown and HP recovery; do not delete equipment or essential materials.
- Prototype enemy lanes: **Burrower** → fiber-binding core (ward motor), **Stoneback** → hard shell (deep drill), **Glowbug** → stabilized catalyst ingredient (crystal/refining), harder creature → rare core for terminal machine. Names pending original art/tone design. Drops only from combat or its later automated descendants; basic first-run path guarantees each required specimen by a fixed number of wins (recommend first win or visible token pity).
- Manual battles use no electricity; ward motor + already demonstrated successful encounter → auto-battle consumes power and food. It can be disabled or restricted to safe opponents. Later mob-grinder produces the known opponent's drops on a deterministic powered timer with an explicit operation cost; original manual route remains accessible.
- Required terminal catalyst is derived from arena loot with a stable repeatable recipe; avoid making the endgame hostage to a low-probability drop.

### Workshop
- Initial crafting, discovery screen and clay collector; use blueprint status as distinct from purchase, availability and queued production.
- From metal phase unlock batch jobs, quick recipes and optional active processing; later routing reservations/automatic repeating jobs for inputs and finished products. There is one resource ledger shared across tabs, separate local task buffers and one active attention budget.
- A purchased upgrade must communicate its effect on average production rates, additional required inputs, watts, and eventual payoff. The next obtainable blueprint and material deficits are visible.
- Don't replicate spatial block layouts or inventory grids. Tools and upgrades are applied to specific producer groups, not all resources at once.

### Power Grid
- One shared Grid; early mechanical collectors and clockwork auto-twerkers explicitly exempt. Start with no electricity and zero powered load. All later powered automation (Orchard twerkers, Farm harvesters, Quarry drills, Arena auto-work, Factory machines) uses watts. Manual or mechanical tasks continue regardless of outage.
- Initial combustion generator uses timber/charcoal/coal, output scales with fuel type and upgrade. Biofuel generator later competes with polymer feedstock; upgraded generators/renewable wind-like option use advanced parts for steady baseline output. No need to build real-world generator mechanics. Energy storage buffers temporary shortages; manual priority overrides automatic scheduling.
- Define supply = fueled/running generator output, demand = sum of enabled *runnable* machine requirements; blocked/no-input machines draw zero except explicit standby if later added. If demand exceeds instantaneous supply, first consume stored energy and then pause lower-priority tasks in stable order, preserving their partial progress. Allow player to pin a priority and toggle machines; display which machine is waiting and why. No random tripping or input loss.
- Energy unit: watt-second (or abstract `power·s`); watt capacity is rate, battery capacity is energy. Example 20 W supplied, 12 + 10 W desired: battery at 20 energy units covers 2 W excess for 10 s; once empty, lower-priority 10 W job pauses and active load becomes 12 W. Do not allocate fractional power unless a specific machine explicitly supports throttling. Energy never goes negative.
- Grid cannot deadlock from empty fuel: hand harvest, starter manual charcoal kiln, fuel generator start with hand-fed fuel. Reserve generator fuel from unrelated recipes on demand. If the entire grid goes dark, display three next recoverable actions, preserve all inventory, and resume correctly once supply is restored.

### Factory
- Machine families progress from processor and smelter → alloy furnace, glass and shaping → automatic routing and batch queues → motor, circuit and polymer lines → precision crystal, high-grade alloys → convergence and terminal press.
- One machine performs one defined recipe at a time. Before work, atomically reserve inputs; finish consumes reservation and commits output, retiring timer exactly once. Full buffer pauses before work or holds completed output, not losses. Recipe switch returns unconsumed reservations only; completed materials are never duplicated.
- Scaling choice: add more machines vs faster machines vs energy-efficient ones vs improved supply. Speed fixes one bottleneck but costs watts and more ingredients per minute. Demonstrate in UI net flow = production/min − required consumption/min. A stopped machine lists missing resources or power rather than counting fictional output.
- Give output storage and recipe routing an industrial payoff while keeping simple global inventory useful. Introduce optional queue/routing controls only when multiple machines are unlocked. Never require the player to micromanage acorns or place a cable.

## 6. Automation and economy rules

### Four layers of automation

| Layer | When | Effect |
|---|---|---|
| Buffer and collect | Start | Natural growth can happen while away; player retrieves up to buffer capacity. |
| Mechanical collection and clockwork | Clay | Collector automates pickup, no Grid. A distinct clockwork auto-twerker trims cycle duration without electricity. |
| Electrified production | Metals/Grid | Powered acceleration, automatic repeated processing, mining/harvesting/auto-battle. |
| Integrated network | Factory/industrial | Automatic routing, input reservation, improved machine efficiency, load priorities, demand-limited queues and passive loot fabrication. |

Avoid conflating **yield**, **speed**, **collection**, and **routing**: upgrading one must solve a visible problem. Use soil tiers (e.g. base / compost / mineral-rich / precision medium) as one category. Illustrative growth multipliers 1.00, 0.80, 0.65, 0.50 and yield upgrade multipliers 1.00, 1.25, 1.50; combined at most 3× under these candidate tiers, before active input; tune costs with real simulation. Speed boosts change completion rate only, yield boosts change bundle only, and collectors never mint material. Use fractional carry for deterministic fractional yield if applicable (e.g. 1.25 of four units = five; no hidden drop chance). SF4's steep 35× soil index is a lesson in long-term reinvestment, not TFT's initial curve.

### Overflow, offline and basic accounting

- Use integer resource quantities / explicit remainder; nonnegative counts and energy. Producers advance via elapsed time events rather than UI frames. Manual buffered tasks stop at their cap; automatic tasks run while there are inputs, output capacity and power. Offline catch-up processes exactly the same completions/reservations/fuel use and storage constraints as online; no independent multiplication of each producer assuming fictional unlimited downstream inputs.
- For recurring processes, batch only while current constraints remain valid. Evaluate output availability → dependent jobs → generation/consumption at event boundaries in deterministic order; tie-break by stable machine ID/priority. Persist clock and pending jobs after each atomic state transition. Offline time capped initially at a generous, disclosed 12 hours for prototype; assess whether 24+ hours is better after profiling. Backward wall clock clamps elapsed to zero rather than subtracting progress; do not award extra time on repeated resume.
- Manual starter harvest should never depend on fuel, energy, defeating an enemy or a scroll. Dirt expansion and collector repair cannot permanently consume a capability. Retain starter tool and known cultivars. A missed seed roll cannot block progress. Use explicit reclaim/repair costs with preview if later added.
- The summary on resume shows resources produced, consumed, time elapsed/capped, and the first reason each stalled chain stopped. The game never secretly simulates impossible input or ignores fuel. Show currently achievable rates separately from theoretical max if all machines were supplied.

## 7. Advancement / mastery boards (guidance, not hard gates)

Keep links to actual gate recipes, not another separate set of chores. Every board lists three to six real milestones at a time, auto-completes based on actions or owned capability, and offers optional mastery badges. A core gate uses a material recipe and not an unrelated board achievement. Proposed first seven boards:

| Board | Representative milestones | Core capstone / optional mastery |
|---|---|---|
| Rootwork | Collect first harvest, craft first dirt, plant second plot, discover stone & clay, collect automatically | First unattended clay batch |
| Cultivation | First Farm seed/field, compost upgrade, first livestock, irrigation | Stable compost supply; optional all cultivar catalog |
| Metallurgy | First kiln, coal, copper/iron/tin, alloy, Quarry | First automated alloy batch |
| Supply lines | First buffer pause/resume, routing, reserve fuel, full raw-to-refined loop | Keep a line running for a measured duration without input deficit |
| Spark | First generator, battery, one overdraw recovery, renewable fuel, efficiency upgrade | Power several zones sustainably |
| Fieldwork | First Quarry deeper bed, first Arena win, first known auto-battle, repeatable catalyst supply | All required specimens automated; optional opponent collection |
| Convergence | Precision crystal, advanced alloy, polymer, core, terminal Press, threshold | Singularity; optional world's production record |

No mandatory board order; display unlocked tasks and next prerequisites together. Avoid paying out unlimited prestige for multiple easy boards during one run. Completion rewards may be cosmetics or reasonable one-time local rewards if later chosen; do not require prestige to access advanced machinery in world one.

## 8. Endgame: terminal resource and prestige design

**Proposed resource name: Worldseed.** A crystalline seed capable of producing a new world, combining the tree theme with the existing Universal Paperclips-style industrial obsession. Name is provisional. The Factory's terminal **Worldseed Press** initially produces one Worldseed per batch after the player builds a Convergence Core as a machine ingredient. The repeated recipe consumes actual ongoing output from all branches, for example: alloy + crystal + polymer + stabilized Arena catalyst + nutrient/compost substrate and surplus energy. The recipe does not consume a Worldseed to make its first one. Inputs are inventory debits, not accomplishment flags.

Illustrative endgame chain: Orchard supplies resin/litter; Farm supplies oil/compost; Quarry supplies bulk ores and quartz; Factory refines metal/alloy, polymer, crystal; Arena supplies catalyst material; Grid supplies production energy. Build rate multipliers only by investment in these suppliers. Display net terminal rate over a rolling period and ETA to threshold; amount produced is cumulative per run, not current inventory if future spending is allowed. Threshold should be established by balance simulation: e.g. aim for a sustained production interval of several hours at minimum viable endgame and significantly shorter with investment, not an arbitrary astronomical count with no progression. Endgame test must verify all branch inputs can be made with independent first-run recipes at finite rates; no infinite self-feed/negative stock.

At target, declare Singularity once per run and present two explicit choices:
- **Endless:** keep world intact, pursue optional mastery goals and production-rate records. No new mandatory unlocks; can choose Replant later. No forced reset.
- **Replant:** preview which state resets (plots, materials, machine unlocks, production state) and what persists (records/achievements/cosmetics, prestige upgrades), then confirm. Grant one nonrepeatable reward at first Singularity for the world, not every repeated view of the threshold. Candidate permanent upgrades: starting extra dirt/plot, starter timer acceleration, more manual buffer slots, or a production efficiency bonus. Start with a single meaningful reward for the MVP; in full design choose from a small capped tree of upgrades. A new run must visibly accelerate the starter loop without skipping its entire identity. No prestige locked basic collector or required first-run technology. No Parabox-like rollback exploit. Keep early replant *out of full design by default*; optional prototype capstone uses a clearly labeled scaled-down proxy of singularity/restart. Consider partial reset only if later playtesting proves a stall problem, not a required treadmill.

## 9. Prototype validation and remaining design decisions

**Vertical-slice success criteria** (no implementation claimed):
- Fresh zero-inventory run obtains dirt, a second plot, screen, stone & clay, collector without lucky drops. A designer can reproduce this path idle and with active tapping. Farming seed guaranteed by cycle three and optional at slice scope.
- Test active vs idle elapsed time, tap cap, and first collector payoff. A focus switch cannot create two concurrent multipliers. Full buffer/overflow/clock-boundary test; off-by-one at exactly completed cycle; fast taps can't duplicate harvest.
- First collector and clockwork auto-twerker work before electricity; collector produces through a simulated absence until its allowed storage cap, never consumes nonexistent power. Switching plots/recipe cannot lose a last seed or duplicate output.
- After full metal/energy feature, test finite fuel, overdraw and battery depletion, higher-priority machines, zero-input and full-output buffers, recovery from completely unpowered world, and online/offline replay parity.
- A coarse paper-graph fixed-point check on 48 named core capabilities/materials (excluding the clockwork attachment, whose inputs are all available) reached the Worldseed recipe from starter outputs in 19 dependency layers, with no unreachable nodes. This validates qualitative reachability only, not fuel, rates, quantities or implementation. Before adding a new phase: repeat that dependency check from actual recipe definitions, verify each target unlock has at least one noncircular path and no hard gate depends on undiscovered output; simulate producer net flows and bottleneck under active and idle schedules, including a player who buys width before depth and vice versa.
- Full run: obtain repeatable Worldseed inputs with each branch, sustain positive output, threshold triggers one win/reward, endless retains state, replant preserves exactly promised state and saves/cancels correctly. Balance for multiple runs, not only best-case arithmetic.

**Open design decisions**: final art/resource naming; combat probabilities, drops, cooldown and equipment schema; exact tree and Quarry material catalog and output ratios; time/yield/machine and generator cost curves; storage/queue capacity after roots; offline cap and multi-plot attention accessibility; first-run duration and terminal count; size/shape of prestige tree; accessibility alternate input (hold/timed assist without exceeding active cap); number notation/caps and optional mastery rewards. All proposed quantities in this doc are initial candidates, not production-ready values. A small deterministic simulator and first-tree interaction spike come before implementing the entire industrial roster.

The central invariant is still the original pitch: the player earns the right to stop tapping, but can always return and accelerate the next interesting bottleneck.
