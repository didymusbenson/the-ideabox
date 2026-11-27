# Content catalog v1 (human-readable reference)

This view summarizes the authoritative [machine-readable catalog](../../data/progression-v1.json). The initial candidate values are exact targets for the first implementation, not a claim of balanced production pacing. IDs are stable save/schema identifiers; displayed names may change without changing IDs. All quantities are integer items, seconds are real simulation seconds, and watts are abstract in-game power units. See [progression requirements](01-progression.md) and [engine rules](03-simulation-and-state.md) for behavioral semantics.

**Inventory resource IDs (45)**

| ID | Display name | Acquisition/zone family |
|---|---|---|
| `timber` | Timber | orchard |
| `litter` | Leaf litter | orchard |
| `cutting` | Cutting | orchard |
| `dirt` | Dirt | workshop |
| `grit` | Grit | workshop |
| `stone` | Stone | orchard/quarry |
| `clay` | Clay | orchard |
| `field_seed` | Field seed | orchard |
| `crop` | Crop | farm |
| `fiber` | Fiber | farm |
| `waste` | Organic waste | farm |
| `compost` | Compost | farm/workshop |
| `feed` | Feed | farm/workshop |
| `animal_product` | Animal produce | farm |
| `oil` | Plant oil | farm |
| `food` | Rations | workshop |
| `charcoal` | Charcoal | workshop/factory |
| `fired_part` | Fired part | workshop/factory |
| `coal` | Coal | orchard/quarry |
| `copper_raw` | Copper concentrate | orchard/quarry/workshop |
| `copper` | Copper ingot | workshop/factory |
| `iron_raw` | Iron ore | orchard/quarry/workshop |
| `iron` | Iron ingot | workshop/factory |
| `tin_raw` | Tin ore | orchard/quarry/workshop |
| `tin` | Tin ingot | workshop/factory |
| `bronze` | Bronze | workshop/factory |
| `silica` | Silica | orchard/quarry/workshop |
| `glass` | Glass | workshop/factory |
| `quartz` | Quartz | orchard/quarry |
| `resin` | Resin | orchard |
| `gem` | Gem fragments | orchard/quarry |
| `heavy_ore` | Heavy ore | quarry/orchard |
| `alloy` | Advanced alloy | factory |
| `core` | Burrower core | arena |
| `shell` | Stoneback shell | arena |
| `glow` | Glowbug dust | arena |
| `rare_core` | Titan core | arena |
| `catalyst` | Stabilized catalyst | factory |
| `biofuel` | Biofuel | farm/factory |
| `control` | Control parts | factory |
| `polymer` | Polymer | factory |
| `crystal` | Precision crystal | factory |
| `convergence_core` | Convergence core | factory |
| `worldseed` | Worldseed | factory |
| `crystal_shard` | Crystal shard | orchard/factory |

## Cultivars (13)

All are guaranteed base bundles. A known cultivar can be replanted freely on an available plot. The starter also gives a one-time Farm seed on one of the first three completed harvests.

| Cultivar ID | Display name | Cycle s | Output per cycle | Technology |
|---|---|---:|---|---|
| `starter` | Starter tree | 12 | 3 timber, 2 litter, 1 cutting | — |
| `stone` | Stonewood | 18 | 2 stone, 1 litter, 1 cutting | `stone_cultivar` |
| `clay` | Claywood | 20 | 2 clay, 1 litter, 1 cutting | `clay_cultivar` |
| `coal` | Fuelwood | 24 | 2 coal, 1 litter, 1 cutting | `coal_cultivar` |
| `copper` | Copperwood | 28 | 3 copper_raw, 1 litter, 1 cutting | `copper_cultivar` |
| `iron` | Ironwood | 30 | 3 iron_raw, 1 litter, 1 cutting | `iron_cultivar` |
| `tin` | Tinwood | 32 | 3 tin_raw, 1 litter, 1 cutting | `tin_cultivar` |
| `silica` | Sandwood | 24 | 3 silica, 1 litter, 1 cutting | `silica_cultivar` |
| `quartz` | Quartzwood | 36 | 2 quartz, 1 litter, 1 cutting | `quartz_cultivar` |
| `resin` | Resinwood | 30 | 3 resin, 2 litter, 1 cutting | `resin_cultivar` |
| `gem` | Gemwood | 42 | 2 gem, 1 litter, 1 cutting | `gem_cultivar` |
| `heavy_ore` | Heavywood | 44 | 2 heavy_ore, 1 litter, 1 cutting | `heavy_cultivar` |
| `crystal_shard` | Crystalwood | 60 | 1 crystal_shard, 1 litter, 1 cutting | `crystal_cultivar` |

## Technology / one-time purchases (45)

Requires column is all-of; additionally check the material cost. Machine/producer/generator effects create the first corresponding slot as part of purchase; repeatable construction is listed separately. No advancement board prerequisites beyond the listed technology/material gate.

| Tech ID | Name | Cost | Requires | Effect |
|---|---|---|---|---|
| `screen` | Screen station | 4 timber, 2 dirt | — | recipe: screen_grit |
| `stone_cultivar` | Stone cultivar | 2 grit, 1 cutting | `screen` | cultivar: stone |
| `clay_cultivar` | Clay cultivar | 2 stone, 1 dirt, 1 cutting | `stone_cultivar` | cultivar: clay |
| `field` | Farm | 1 field_seed, 2 dirt, 3 timber | — | zone: farm; producer: field; initialSlots: 1 |
| `kiln` | Kiln | 6 clay, 6 stone, 4 timber | `clay_cultivar` | machine: kiln; initialSlots: 1 |
| `coal_cultivar` | Coal cultivar | 1 fired_part, 1 charcoal, 2 stone, 1 cutting | `kiln` | cultivar: coal |
| `copper_cultivar` | Copper cultivar | 1 copper, 1 cutting | `kiln` | cultivar: copper |
| `iron_cultivar` | Iron cultivar | 1 iron, 1 cutting | `coal_cultivar`, `kiln` | cultivar: iron |
| `tin_cultivar` | Tin cultivar | 1 tin, 1 cutting | `kiln`, `copper_cultivar` | cultivar: tin |
| `silica_cultivar` | Silica cultivar | 2 silica, 1 cutting | `kiln`, `stone_cultivar` | cultivar: silica |
| `alloy_heat` | Alloy heat lining | 3 fired_part, 2 copper, 2 charcoal | `kiln`, `copper_cultivar` | recipe: bronze_manual |
| `iron_pick` | Iron pick and Quarry | 3 iron, 2 timber | `kiln` | zone: quarry; producer: quarry; initialSlots: 1 |
| `quartz_bed` | Quartz bed | 3 fired_part, 6 stone, 2 iron | `iron_pick` | quarryBed: quartz |
| `quartz_cultivar` | Quartz cultivar | 2 quartz, 1 cutting | `quartz_bed` | cultivar: quartz |
| `compost_soil` | Compost soil | 3 compost, 2 dirt | `field` | upgrade: soil_compost |
| `animal_pen` | Animal pen | 6 timber, 2 fired_part, 5 crop | `field`, `kiln` | producer: animal; initialSlots: 1 |
| `oil_field` | Oil crop | 4 fiber, 2 iron, 3 compost | `field`, `kiln` | farmTask: oil |
| `resin_cultivar` | Resinwood cultivar | 4 fiber, 2 compost, 1 copper, 1 cutting | `field`, `copper_cultivar` | cultivar: resin |
| `arena` | Arena | 5 timber, 4 iron, 4 fiber, 4 food | `field`, `kiln` | zone: arena; enemy: burrower; hp: 100 |
| `reinforced_armor` | Reinforced armor | 5 iron, 3 bronze, 4 food | `arena`, `alloy_heat` | enemy: stoneback; hp: 130 |
| `glowbug_trial` | Glowbug trial | 3 quartz, 3 bronze, 5 food | `arena`, `quartz_bed`, `reinforced_armor` | enemy: glowbug; hp: 160 |
| `titan_trial` | Titan trial | 4 alloy, 2 crystal, 8 food | `glowbug_trial`, `precision_line`, `deep_bed`, `alloy_furnace` | enemy: titan; hp: 200 |
| `grid` | Power Grid | 4 copper, 3 iron, 2 fired_part | `kiln` | zone: grid; generator: combustion; initialSlots: 1 |
| `factory` | Factory | 4 iron, 3 copper, 2 fired_part | `grid` | zone: factory; machine: processor; initialSlots: 1 |
| `alloy_furnace` | Powered alloy furnace | 4 iron, 2 bronze, 2 glass | `factory`, `alloy_heat` | machine: alloy_furnace; initialSlots: 1 |
| `router` | Sorting network | 3 copper, 2 glass, 3 iron | `factory`, `silica_cultivar` | automation: repeat_queues |
| `circuit_bench` | Circuit bench | 3 copper, 2 quartz, 2 resin, 2 iron | `factory`, `quartz_bed`, `resin_cultivar` | machine: circuit_bench; initialSlots: 1 |
| `ward_motor` | Ward motor | 3 iron, 2 control, 1 core | `circuit_bench`, `arena` | automation: arena_auto |
| `deep_bed` | Deep ore bed | 4 bronze, 3 quartz, 3 iron | `quartz_bed`, `alloy_heat` | quarryBed: heavy_ore |
| `heavy_cultivar` | Heavywood cultivar | 2 heavy_ore, 2 bronze, 1 cutting | `deep_bed` | cultivar: heavy_ore |
| `gem_bed` | Gem bed | 4 quartz, 3 iron, 1 core | `quartz_bed`, `arena` | quarryBed: gem |
| `gem_cultivar` | Gemwood cultivar | 2 gem, 1 quartz, 1 cutting | `gem_bed` | cultivar: gem |
| `deep_drill` | Deep drill | 4 alloy, 3 control, 2 shell | `alloy_furnace`, `deep_bed`, `ward_motor`, `reinforced_armor` | automation: deep_drill |
| `polymer_line` | Polymer line | 4 iron, 3 copper, 4 resin, 2 fired_part | `factory`, `oil_field`, `resin_cultivar` | machine: polymer_line; initialSlots: 1 |
| `precision_line` | Precision line | 4 glass, 3 control, 4 quartz, 2 gem | `circuit_bench`, `gem_bed`, `factory` | machine: precision_line; initialSlots: 1 |
| `stabilizer` | Catalyst stabilizer | 4 iron, 2 control, 1 glow | `glowbug_trial`, `circuit_bench` | machine: stabilizer; initialSlots: 1 |
| `biofuel_line` | Fermenter and biofuel generator | 3 iron, 2 bronze, 3 oil | `field`, `grid`, `oil_field` | machine: fermenter; initialSlots: 1; generator: biofuel |
| `advanced_grid` | High-capacity generator | 4 alloy, 2 crystal, 3 control | `precision_line`, `alloy_furnace`, `grid`, `deep_bed` | generator: advanced |
| `precision_soil` | Precision soil | 6 compost, 2 alloy, 1 crystal | `compost_soil`, `precision_line`, `alloy_furnace`, `deep_bed` | upgrade: soil_precision |
| `mineral_soil` | Mineral soil | 4 compost, 4 stone, 1 bronze | `compost_soil`, `alloy_heat` | upgrade: soil_mineral |
| `forge_tools` | Shaped tools | 3 bronze, 3 timber | `alloy_heat` | upgrade: yield_shaped |
| `precision_tools` | Precision tools | 3 alloy, 2 crystal | `precision_line`, `forge_tools`, `alloy_furnace`, `deep_bed` | upgrade: yield_precision |
| `crystal_cultivar` | Crystalwood cultivar | 3 gem, 3 quartz, 1 catalyst, 1 cutting | `stabilizer`, `gem_bed` | cultivar: crystal_shard |
| `convergence` | Convergence station | 8 alloy, 5 polymer, 4 crystal, 3 catalyst, 1 rare_core | `polymer_line`, `precision_line`, `stabilizer`, `titan_trial` | machine: convergence; initialSlots: 1 |
| `worldseed_press` | Worldseed Press | 1 convergence_core, 8 alloy, 4 control, 4 crystal | `convergence`, `advanced_grid` | machine: worldseed_press; initialSlots: 1 |

## Repeatable constructions (28)

Costs and maximum additional purchases, subject also to total slot/attachment caps and available target. The plot formula overrides the literal first-plot price, and caps include awarded prestige slots. Generator/machine caps include the initial free slot. Every other listed price is flat in v1.

| Build ID | Name | Cost | Requires | Effect | Max additional |
|---|---|---|---|---|---:|
| `plot` | Additional plot | 3 dirt, 2 timber | — | plots: 1 | 63 |
| `collector` | Mechanical collector | 4 clay, 4 timber, 2 stone | `clay_cultivar` | attachment: collector | 64 |
| `clockwork_twerker` | Clockwork auto-twerker | 2 clay, 2 timber, 1 stone | `clay_cultivar` | attachment: clockwork; requiresBuild: collector | 64 |
| `field_slot` | Additional field | 3 dirt, 3 timber, 1 compost | `field` | fields: 1 | 31 |
| `pen_slot` | Additional animal pen | 6 timber, 2 fired_part, 4 feed | `animal_pen` | pens: 1 | 15 |
| `quarry_slot` | Additional quarry work gang | 3 iron, 2 timber | `iron_pick` | quarrySlots: 1 | 31 |
| `auto_twerker` | Powered auto-twerker | 2 iron, 2 copper, 1 control | `grid`, `circuit_bench` | attachment: powered_twerker | 64 |
| `farm_harvester` | Field harvester | 2 iron, 1 copper, 1 control | `field`, `router`, `circuit_bench` | attachment: farm_auto | 32 |
| `pen_harvester` | Pen feeder | 2 iron, 2 copper, 1 control | `animal_pen`, `router`, `circuit_bench` | attachment: pen_auto | 16 |
| `quarry_drill` | Quarry drill | 3 iron, 2 bronze, 1 control | `iron_pick`, `router`, `circuit_bench` | attachment: quarry_auto | 32 |
| `mob_grinder` | Mob grinder | 3 alloy, 2 control, 1 shell | `ward_motor`, `alloy_furnace`, `reinforced_armor` | machine: grinder; requiresEnemyMastery: true | 16 |
| `battery` | Battery | 3 copper, 2 iron, 1 glass | `grid`, `silica_cultivar` | energyCapacity: 600 | 16 |
| `combustion_generator` | Combustion generator | 4 copper, 3 iron, 2 fired_part | `grid` | generator: combustion | 31 |
| `biofuel_generator` | Biofuel generator | 4 iron, 3 bronze, 1 control | `biofuel_line`, `circuit_bench` | generator: biofuel | 31 |
| `advanced_generator` | High-capacity generator | 4 alloy, 2 crystal, 3 control | `advanced_grid` | generator: advanced | 31 |
| `extra_kiln` | Additional kiln | 6 clay, 6 stone, 4 timber | `kiln` | machine: kiln | 15 |
| `extra_processor` | Additional processor | 3 iron, 2 copper, 1 fired_part | `factory` | machine: processor | 15 |
| `extra_alloy_furnace` | Additional alloy furnace | 4 iron, 2 bronze, 2 glass | `alloy_furnace` | machine: alloy_furnace | 15 |
| `extra_circuit_bench` | Additional circuit bench | 3 copper, 2 quartz, 2 resin, 2 iron | `circuit_bench` | machine: circuit_bench | 15 |
| `extra_polymer_line` | Additional polymer line | 4 iron, 3 copper, 4 resin, 2 fired_part | `polymer_line` | machine: polymer_line | 15 |
| `extra_precision_line` | Additional precision line | 4 glass, 3 control, 4 quartz, 2 gem | `precision_line` | machine: precision_line | 15 |
| `extra_stabilizer` | Additional stabilizer | 4 iron, 2 control, 1 glow | `stabilizer` | machine: stabilizer | 15 |
| `extra_fermenter` | Additional fermenter | 3 iron, 2 bronze, 3 oil | `biofuel_line` | machine: fermenter | 15 |
| `extra_convergence` | Additional convergence | 8 alloy, 5 polymer, 4 crystal, 3 catalyst, 1 rare_core | `convergence` | machine: convergence | 15 |
| `extra_worldseed_press` | Additional worldseed press | 1 convergence_core, 8 alloy, 4 control, 4 crystal | `worldseed_press` | machine: worldseed_press | 15 |
| `buffer_upgrade` | Storage upgrade | 5 timber, 2 iron | `iron_pick` | bufferCycles: 3 | 32 |
| `efficiency_upgrade` | Machine efficiency kit | 2 control, 2 bronze, 1 glass | `circuit_bench` | machineUpgrade: efficiency | 64 |
| `speed_upgrade` | Machine speed kit | 2 control, 2 bronze, 2 copper | `circuit_bench` | machineUpgrade: speed | 64 |

## Tasks and recipes (48)

The listed station or producer slot is required, in addition to technology and ingredient stock. Manual bench recipes execute atomically, manually started kiln tasks are timed, buffered tasks naturally repeat until full after assignment, powered tasks execute once unless repeat is unlocked/enabled. The active UI does not generate materials directly; active boosts and upgrades are in the engine requirements. Power shown is base consumption. Automated Farm/Quarry attachment watts are additive and listed in the config.

| Task ID | Zone / slot | Duration s | Input | Output | Requires | Base W | Repeat kind |
|---|---|---:|---|---|---|---:|---|
| `make_dirt` | workshop/bench | 0 | 2 litter | 1 dirt | — | 0 | manual |
| `screen_grit` | workshop/bench | 0 | 1 dirt | 2 grit | `screen` | 0 | manual |
| `compost` | workshop/bench | 0 | 2 litter, 2 waste | 1 compost | `field` | 0 | manual |
| `ration` | workshop/bench | 0 | 2 crop | 1 food | `field` | 0 | manual |
| `feed` | workshop/bench | 0 | 2 crop | 1 feed | `field` | 0 | manual |
| `ration_rich` | workshop/bench | 0 | 1 animal_product, 1 crop | 3 food | `animal_pen` | 0 | manual |
| `field_crop` | farm/field | 18 | None | 3 crop, 2 fiber, 2 waste | `field` | 0 | buffered |
| `field_oil` | farm/field | 24 | None | 3 oil, 1 waste, 1 fiber | `oil_field` | 0 | buffered |
| `pen_product` | farm/animal | 30 | 1 feed | 2 animal_product, 2 waste | `animal_pen` | 0 | buffered |
| `charcoal` | workshop/kiln | 8 | 2 timber | 1 charcoal | `kiln` | 0 | manual |
| `fired_part` | workshop/kiln | 8 | 2 clay, 1 charcoal | 1 fired_part | `kiln` | 0 | manual |
| `copper_concentrate` | workshop/kiln | 10 | 2 clay, 2 stone, 1 charcoal | 2 copper_raw | `kiln` | 0 | manual |
| `iron_concentrate` | workshop/kiln | 12 | 2 coal, 2 stone, 1 fired_part | 2 iron_raw | `coal_cultivar`, `kiln` | 0 | manual |
| `tin_concentrate` | workshop/kiln | 12 | 2 stone, 1 fired_part, 1 copper | 2 tin_raw | `kiln`, `copper_cultivar` | 0 | manual |
| `silica_bootstrap` | workshop/kiln | 8 | 2 grit, 1 clay | 2 silica | `kiln` | 0 | manual |
| `smelt_copper` | workshop/kiln | 10 | 2 copper_raw, 1 charcoal | 1 copper | `kiln` | 0 | manual |
| `smelt_copper_coal` | workshop/kiln | 10 | 2 copper_raw, 1 coal | 1 copper | `kiln`, `coal_cultivar` | 0 | manual |
| `electric_copper` | factory/processor | 8 | 2 copper_raw | 2 copper | `factory` | 8 | powered |
| `smelt_iron` | workshop/kiln | 10 | 2 iron_raw, 1 charcoal | 1 iron | `kiln` | 0 | manual |
| `smelt_iron_coal` | workshop/kiln | 10 | 2 iron_raw, 1 coal | 1 iron | `kiln`, `coal_cultivar` | 0 | manual |
| `electric_iron` | factory/processor | 8 | 2 iron_raw | 2 iron | `factory` | 8 | powered |
| `smelt_tin` | workshop/kiln | 10 | 2 tin_raw, 1 charcoal | 1 tin | `kiln` | 0 | manual |
| `smelt_tin_coal` | workshop/kiln | 10 | 2 tin_raw, 1 coal | 1 tin | `kiln`, `coal_cultivar` | 0 | manual |
| `electric_tin` | factory/processor | 8 | 2 tin_raw | 2 tin | `factory` | 8 | powered |
| `glass_manual` | workshop/kiln | 10 | 2 silica, 1 charcoal | 2 glass | `kiln` | 0 | manual |
| `bronze_manual` | workshop/kiln | 12 | 2 copper, 1 tin, 1 charcoal | 3 bronze | `alloy_heat` | 0 | manual |
| `bronze_powered` | factory/alloy_furnace | 10 | 2 copper, 1 tin | 4 bronze | `alloy_furnace` | 10 | powered |
| `advanced_alloy` | factory/alloy_furnace | 16 | 2 iron, 2 bronze, 2 heavy_ore | 4 alloy | `alloy_furnace`, `deep_bed` | 12 | powered |
| `glass_powered` | factory/processor | 8 | 2 silica | 3 glass | `factory` | 6 | powered |
| `fired_powered` | factory/processor | 8 | 2 clay | 2 fired_part | `factory` | 6 | powered |
| `charcoal_powered` | factory/processor | 8 | 3 timber | 2 charcoal | `factory` | 5 | powered |
| `mine_stone` | quarry/quarry | 15 | None | 6 stone | `iron_pick` | 0 | buffered |
| `mine_coal` | quarry/quarry | 18 | None | 6 coal | `iron_pick` | 0 | buffered |
| `mine_copper_raw` | quarry/quarry | 20 | None | 8 copper_raw | `iron_pick` | 0 | buffered |
| `mine_iron_raw` | quarry/quarry | 22 | None | 8 iron_raw | `iron_pick` | 0 | buffered |
| `mine_tin_raw` | quarry/quarry | 24 | None | 8 tin_raw | `iron_pick` | 0 | buffered |
| `mine_silica` | quarry/quarry | 15 | None | 8 silica | `iron_pick` | 0 | buffered |
| `mine_quartz` | quarry/quarry | 26 | None | 6 quartz | `quartz_bed` | 0 | buffered |
| `mine_gem` | quarry/quarry | 32 | None | 5 gem | `gem_bed` | 0 | buffered |
| `mine_heavy_ore` | quarry/quarry | 36 | None | 5 heavy_ore | `deep_bed` | 0 | buffered |
| `make_control` | factory/circuit_bench | 12 | 2 copper, 1 quartz, 1 resin | 2 control | `circuit_bench` | 8 | powered |
| `make_polymer` | factory/polymer_line | 12 | 2 oil, 2 resin, 1 fired_part | 3 polymer | `polymer_line` | 8 | powered |
| `make_crystal` | factory/precision_line | 16 | 2 quartz, 2 gem, 1 control | 3 crystal | `precision_line` | 12 | powered |
| `make_crystal_shard` | factory/precision_line | 12 | 2 crystal_shard, 1 control | 3 crystal | `precision_line`, `crystal_cultivar` | 10 | powered |
| `stabilize` | factory/stabilizer | 14 | 2 glow, 1 shell, 1 compost | 3 catalyst | `stabilizer` | 10 | powered |
| `ferment` | farm/fermenter | 10 | 3 crop, 2 waste | 3 biofuel | `biofuel_line` | 5 | powered |
| `make_convergence_core` | factory/convergence | 30 | 3 alloy, 3 polymer, 3 crystal, 2 catalyst, 1 rare_core | 1 convergence_core | `convergence` | 18 | powered |
| `press_worldseed` | factory/worldseed_press | 30 | 2 alloy, 2 polymer, 2 crystal, 1 catalyst, 1 compost | 1 worldseed | `worldseed_press` | 20 | powered |

## Arena (4)

| Enemy | Unlock | Fight duration (s) | Base win chance | Win/loss damage | Normal victory | First-win bonus | Grinder period (s) / W |
|---|---|---:|---:|---:|---|---|---|
| `burrower` | `arena` | 12 | 85% | 12/25 | 2 core | 1 core | 16 / 8 |
| `stoneback` | `reinforced_armor` | 18 | 80% | 20/35 | 2 shell | 1 shell | 22 / 10 |
| `glowbug` | `glowbug_trial` | 22 | 78% | 25/40 | 3 glow | 1 glow | 26 / 12 |
| `titan` | `titan_trial` | 30 | 72% | 30/50 | 1 rare_core | 1 rare_core | 36 / 16 |

Each fight costs one ration (heals 40 HP on start), manual fights 0 W, automated fights 6 W. After 2 losses against an enemy, the next valid resolved attempt wins (pity), except canceled fights consume the reserved ration and do not count. Defeat cooldown 60s; no gear loss. Mastery at 5 completed wins per enemy allows its grinder assignment. Grinder is deterministic, costs one ration per cycle, grants normal output only, no HP damage or mastery progress.

## Generators (3)

| ID | Output | Input options: burn duration per unit |
|---|---:|---|
| `combustion` | 20 W | timber: 15s; charcoal: 35s; coal: 45s |
| `biofuel` | 45 W | biofuel: 45s |
| `advanced` | 100 W | coal: 60s; biofuel: 90s |

Batteries hold 600 watt-seconds each; charging/discharging details are in engine rules. For the terminal example, two advanced generators on coal supply 200 W at at most 2 coal/min.

## Initial constants

| Rule | Candidate |
|---|---|
| Initial state | 1 planted starter plot, Orchard+Workshop, empty inventory, 100 HP |
| Tap | 250 ms per accepted tap, at most 8 per rolling second across all active tasks |
| Buffer | 3 completed cycles/slot; storage kit +3, max 12 cycles |
| Plot price | For current plot count p, 3 + floor(1.5(p−1)) dirt, 2 + (p−1) timber |
| Soil duration | base 1, compost 0.8, mineral 0.65, precision 0.5 |
| Orchard/Quarry yield | base 1, shaped 1.25, precision 1.5 |
| Clockwork/powered auto-twerker | 0.8 / 0.6 cycle duration, the powered model uses 3 W; mutually exclusive |
| Field/pen attachment | 3 / 4 W auto-collection/repeat |
| Quarry drill/deep upgrade | 6 W at 0.75 duration / 10 W at 0.5 duration; mutually exclusive |
| Speed kit | one per powered station, ×0.75 duration and ×1.5 W |
| Efficiency kit | one per powered station, ×0.75 W; may combine with speed kit |
| Offline cap | 43,200 s (12 hours); no active boost offline |
| Manual/queued jobs | 99 batches max per queue, reservations per running batch |
| Terminal | 600 cumulative Worldseed; 1 prestige point per world; no mandatory reset |
| Save | schema version 1; autosave each mutation or 15 seconds; two backup slots |

## Sustained terminal example (exact rational rate)

The catalog includes a specific example using two advanced generators, three mechanical orchard collectors, two automated fields, seven powered Quarry work gangs, two mastered enemy grinders, and one or more powered stations as listed. It is a **steady-state material/power/capacity witness**, not a claimed real-tick schedule or required optimal build. Before enabling the Press, fill buffers and assign output targets with slack. For each row the rate is cycles/min (fractions are exact); the endgame press sets the throughput target.

| Flow | Type | Cycles/min | Dedicated slots/assignment | Extra attachment W |
|---|---|---:|---:|---:|
| `press_worldseed` | task | 2 | 1 | 0 |
| `advanced_alloy` | task | 1 | 1 | 0 |
| `bronze_powered` | task | 0.5 | 1 | 0 |
| `electric_iron` | task | 1 | 1 | 0 |
| `electric_copper` | task | 7/6 | 1 | 0 |
| `electric_tin` | task | 1/4 | 1 | 0 |
| `make_control` | task | 2/3 | 1 | 0 |
| `make_polymer` | task | 4/3 | 1 | 0 |
| `make_crystal` | task | 4/3 | 1 | 0 |
| `fired_powered` | task | 2/3 | 1 | 0 |
| `stabilize` | task | 2/3 | 1 | 0 |
| `compost` | task | 8/3 | 1 | 0 |
| `ration` | task | 7/9 | 1 | 0 |
| `field_crop` | task | 9/4 | 1 | 3 |
| `field_oil` | task | 8/9 | 1 | 3 |
| `mine_coal` | task | 1/3 | 1 | 6 |
| `mine_iron_raw` | task | 1/4 | 1 | 6 |
| `mine_copper_raw` | task | 7/24 | 1 | 6 |
| `mine_tin_raw` | task | 1/16 | 1 | 6 |
| `mine_heavy_ore` | task | 2/5 | 1 | 6 |
| `mine_quartz` | task | 5/9 | 1 | 6 |
| `mine_gem` | task | 8/15 | 1 | 6 |
| `resin` | cultivar | 10/9 | 1 | 0 |
| `clay` | cultivar | 2/3 | 1 | 0 |
| `starter` | cultivar | 5/4 | 1 | 0 |
| `stoneback` | grind | 1/3 | 1 | 0 |
| `glowbug` | grind | 4/9 | 1 | 0 |

Machine counts: worldseed_press ×1, alloy_furnace ×1, processor ×4, circuit_bench ×1, polymer_line ×1, precision_line ×1, stabilizer ×1, bench ×1, field ×2, quarry ×7, orchard ×3, grinder ×2. No speed/yield/soil upgrades are required for this witness. Alloy and bronze recipes share the one alloy furnace by quota; bench recipes are instant and demand-limited. All listed concurrent loads sum to 180 W ignoring mutually exclusive station work, conservatively below 200 W. One uninterrupted Worldseed press makes two per minute; 600 take five ideal hours after ramp-up. Build a second full input chain to scale, not just another press. Use reactor-like high capacity as a purely abstract game resource; no simulation of real-world equipment.

## Milestone boards (7 boards, 52 milestones)

IDs are namespaced by board. Predicates are monotonic historical facts, persisted counters or unlocked technology (never require current inventory). The event contract is specified in the engine requirements. No board rewards beyond local badge/records.

| Board | Milestone ID | Label | Predicate |
|---|---|---|---|
| `rootwork` | `first_harvest` | First harvest | kind=event; event=harvest:starter |
| `rootwork` | `first_dirt` | Make dirt | kind=event; event=craft:make_dirt |
| `rootwork` | `second_plot` | Build a second plot | kind=event; event=build:plot |
| `rootwork` | `stone` | Discover Stonewood | kind=tech; id=stone_cultivar |
| `rootwork` | `clay` | Discover Claywood | kind=tech; id=clay_cultivar |
| `rootwork` | `collector` | Build a collector | kind=event; event=build:collector |
| `rootwork` | `clockwork` | Build a clockwork twerker | kind=event; event=build:clockwork_twerker |
| `rootwork` | `auto_clay` | Ten auto-collected clay | kind=counter; key=clayAutoCollected; threshold=10 |
| `cultivation` | `first_field` | Open Farm | kind=tech; id=field |
| `cultivation` | `first_crop` | Harvest crops | kind=event; event=harvest:field_crop |
| `cultivation` | `soil` | Unlock compost soil | kind=tech; id=compost_soil |
| `cultivation` | `pen` | Open animal pen | kind=tech; id=animal_pen |
| `cultivation` | `animal` | Harvest animal produce | kind=event; event=harvest:pen_product |
| `cultivation` | `oil` | Unlock oil crop | kind=tech; id=oil_field |
| `cultivation` | `resin` | Discover Resinwood | kind=tech; id=resin_cultivar |
| `metallurgy` | `kiln` | Build kiln | kind=tech; id=kiln |
| `metallurgy` | `coal` | Discover Fuelwood | kind=tech; id=coal_cultivar |
| `metallurgy` | `first_copper` | Refine copper | kind=event; event=produce:copper |
| `metallurgy` | `first_iron` | Refine iron | kind=event; event=produce:iron |
| `metallurgy` | `first_tin` | Refine tin | kind=event; event=produce:tin |
| `metallurgy` | `first_bronze` | Make bronze | kind=event; event=produce:bronze |
| `metallurgy` | `quarry` | Open Quarry | kind=tech; id=iron_pick |
| `metallurgy` | `electric_bronze` | Powered alloy batch | kind=event; event=craft:bronze_powered |
| `supply_lines` | `buffer_full` | Fill a manual buffer | kind=event; event=buffer:full |
| `supply_lines` | `buffer_resume` | Recover from full buffer | kind=event; event=buffer:resumed |
| `supply_lines` | `router` | Build sorting network | kind=tech; id=router |
| `supply_lines` | `repeat` | Complete an automatic repeat batch | kind=event; event=machine:repeat_completed |
| `supply_lines` | `batch_chain` | Finish a powered batch after auto-producing an input | kind=event; event=machine:automated_input_completed |
| `spark` | `grid` | Build Grid | kind=tech; id=grid |
| `spark` | `first_fuel` | Consume fuel | kind=event; event=grid:fuel_started |
| `spark` | `battery` | Build battery | kind=event; event=build:battery |
| `spark` | `power_recovered` | Recover a stalled powered task | kind=event; event=grid:task_resumed |
| `spark` | `biofuel` | Build fermentation line | kind=tech; id=biofuel_line |
| `spark` | `advanced` | High-capacity generator | kind=tech; id=advanced_grid |
| `fieldwork` | `quartz` | Find quartz bed | kind=tech; id=quartz_bed |
| `fieldwork` | `deep` | Find deep ore bed | kind=tech; id=deep_bed |
| `fieldwork` | `gem` | Find gem bed | kind=tech; id=gem_bed |
| `fieldwork` | `win_burrower` | Defeat Burrower | kind=event; event=arena:win:burrower |
| `fieldwork` | `win_stoneback` | Defeat Stoneback | kind=event; event=arena:win:stoneback |
| `fieldwork` | `win_glowbug` | Defeat Glowbug | kind=event; event=arena:win:glowbug |
| `fieldwork` | `win_titan` | Defeat Titan | kind=event; event=arena:win:titan |
| `fieldwork` | `master_burrower` | Master Burrower | kind=counter; key=wins:burrower; threshold=5 |
| `fieldwork` | `master_stoneback` | Master Stoneback | kind=counter; key=wins:stoneback; threshold=5 |
| `fieldwork` | `master_glowbug` | Master Glowbug | kind=counter; key=wins:glowbug; threshold=5 |
| `fieldwork` | `master_titan` | Master Titan | kind=counter; key=wins:titan; threshold=5 |
| `fieldwork` | `first_grinder` | Fabricate first combat drop | kind=event; event=grinder:first_complete |
| `convergence` | `polymer` | Make polymer | kind=event; event=produce:polymer |
| `convergence` | `crystal` | Make precision crystal | kind=event; event=produce:crystal |
| `convergence` | `catalyst` | Stabilize catalyst | kind=event; event=produce:catalyst |
| `convergence` | `core` | Make convergence core | kind=event; event=produce:convergence_core |
| `convergence` | `press` | Build Worldseed Press | kind=tech; id=worldseed_press |
| `convergence` | `win` | Make 600 Worldseed | kind=counter; key=worldseedProduced; threshold=600 |

Validation command: `python3 tools/validate_progression.py` from TFT root. See [verification](05-acceptance-and-roadmap.md) for scope and limitations.
