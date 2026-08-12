# Zones & interface

TFT is presented as a **tabbed interface**, where each tab is a **zone** with its own idle and active
tasks. The player works tasks to collect items, then spends those materials in the **Workshop** to
**build expansions** — unlocking new zones, tools, crafting recipes, and upgrades that remove or raise
progression barriers. The starting set of tabs is below; **the model is designed to extend** (more
zones may be added later).

At a glance, TFT sits at the intersection of **Melvor Idle** (multi-skill tabbed idle structure +
simplified combat), **Sky Factory 4** (resource-tree bootstrapping and tech progression), **Universal
Paperclips** (the singularity endgame), and **Cookie Clicker / Adventure Capitalist** (idle-with-active
feel and the twerk clicker core).

## The tabs (starting set)

### The Orchard — *default; the core*
Tree plots, always available from the start. Twerk a plot's twerker to speed its timers, harvest drops,
craft dirt to build new plots, and climb tree types (see [`progression.md`](progression.md) and the
project README). The Orchard is the game's beating heart and its earliest input source — everything
else bootstraps from what trees produce.

### The Workshop — *the unlockables hub*
The crafting menu and the game's central progression screen. Spend collected materials to **build
expansions**: unlock new zones/tabs, craft tools, unlock recipes, and remove or upgrade progression
barriers. If a gate exists anywhere in the game, the Workshop is usually where you *pay to open it* —
"reach clay → unlock automation," "reach metals → unlock smelting," and the zone unlocks below all
resolve here. Think of it as the spine the other zones plug into.

### The Farm — *crops & livestock (unlocked)*
Opens when the farming branch triggers (seeds drop in the Orchard). Handles all **crops and livestock**
— a parallel production line to trees, with its own idle/active tasks and outputs the other zones can
consume.

### The Quarry — *high-throughput mining (unlocked)*
Boosts output of **ores, coal, and gems**. The Orchard *can* produce these via resource-trees, but
slowly and in low volume; the Quarry is the **high-throughput alternative** once unlocked, turning the
mineral supply from a trickle into a stream. It's the zone that keeps smelting, alloys, and the Factory
actually fed.

### The Factory — *technology & automation (unlocked)*
Produces **technology resources**, with **each machine producing a different item**. Reaching the tech
age here is what kicks off **true automation and the race toward the Singularity** — the Factory is the
endgame engine, converting broad resource output into the terminal singularity resource (see the
endgame section of [`progression.md`](progression.md)).

### The Power Grid — *the shared power supply (unlocked)*
Build **various types of generators** from collected resources; together they produce the game's
**power supply**. Power is a **global constraint on automation**: every automation machine — the
Orchard's auto-twerkers, the Farm's and Quarry's automation, the Arena's auto-battlers, and all Factory
machines — **draws power while it runs**, and the Grid must generate at least as much as those machines
demand.

Each automation machine can be **toggled on/off**, and a machine that's off draws nothing. So the player
manages a **power budget**: if total demand exceeds supply (an accidental over-draw), you **power down**
lower-priority machines to bring demand back under the Grid's output — or expand the Grid with more and
better generators to run everything at once. This turns automation from "unlock and forget" into an
ongoing **supply-vs-demand balancing act**, and makes growing generation a progression goal in its own
right.

### The Arena — *idle combat (unlocked)*
Simulated combat in the **Melvor Idle** lineage, deliberately **simplified** — no rich combat triangle,
no hundreds of equipment pieces. The model:

- A **risk/reward success rate** (a % chance to win) and an **HP** pool to manage.
- On **death**, a **cooldown** before the player can fight again.
- Unlockables progress it from **manual fighting → auto-battle → mob-grinders** that fight with no
  manual input at all (the same "earn the right to stop tapping" arc as the Orchard's automation).
- Yields **mob drops** — unique items available *only* through combat — which are **required for
  certain unlocks elsewhere**, notably some **zone upgrades** and certain **Factory machines**. That
  puts the Arena on the **critical path**, not off to the side: you can't fully progress other zones
  without fighting (or automating the fighting).

*(More zones may be added later; the tab model is built to extend.)*

## Cross-cutting model

- **Every zone has idle + active tasks.** Idle ticks along while you're away; active play (twerking,
  fighting, directing machines) is meaningfully faster — consistent with the idle-with-active-boost
  positioning in the pitch.
- **The Workshop is the loop's hub.** Zones generate materials → the Workshop converts materials into
  unlocks and upgrades → unlocks open new zones and better tasks → those generate more materials.
  Progression is a loop that keeps passing through the Workshop.
- **Zones interlock.** Later zones consume earlier zones' outputs (the Factory needs Quarry metals, Farm
  inputs, Orchard resources; smelting needs ore; some upgrades and machines need **Arena mob drops**),
  so no zone is an island — this is the concrete form of the cross-branch dependency the progression doc
  leans toward.
- **Power is the global automation budget.** Automation isn't free: every running machine across every
  zone draws from the **Power Grid**, which must out-produce total demand. Machines toggle on/off, so
  when supply is tight the player chooses which automation runs — load-shedding by hand, or building more
  generation. Power is the constraint that keeps "just automate everything" from being trivial.

## How this maps onto the progression branches

The tech branches in [`progression.md`](progression.md) are *realized* as these zones and Workshop
unlocks:

| Progression branch | Where it lives |
|---|---|
| Resource-tree trunk | **The Orchard** |
| Automation (gate: clay) | Cross-zone upgrades bought in **the Workshop** (self-harvesting trees, later auto-battle, auto-machines) |
| Farming (gate: seeds) | **The Farm** |
| Smelting & alloys (gate: metals) | **The Workshop** (recipes) fed by **the Quarry**, flowing into **the Factory** |
| Power & machinery | **The Power Grid** (generation) + **the Factory** (machines) |
| *(new)* High-throughput minerals | **The Quarry** — not in the original branch list; the efficient replacement for slow ore-trees |
| *(new)* Combat | **The Arena** — a new pillar the branch model didn't cover |

## Open questions

- **Zone unlock order & gates.** What's the intended sequence (Farm / Quarry / Factory / Arena) and the
  gate material or milestone for each?
- **Signature tasks per zone.** What are each zone's concrete idle vs. active actions?
- **Arena's economic role — decided.** Combat produces **mob drops**: unique, combat-only items gating
  some zone upgrades and certain Factory machines, so the Arena is on the critical path. Still to
  define: *which* specific upgrades/machines require mob drops, whether drops are mob-type-specific
  (different enemies → different drops), and how the drop economy scales once auto-battle/mob-grinders
  make combat passive.
- **Quarry vs. ore-trees.** Does the Quarry fully replace resource-tree mining, or do slow ore-trees
  stay as an early fallback / for tree-only variants?
- **How many zones, ultimately**, and does the Singularity live only in the Factory or draw from every
  zone's output at once?
- **UI scale.** With seven+ tabs each running idle/active tasks, how much can happen at once before the
  player's attention (and the "active is faster" promise) breaks down?
- **Power Grid unlock timing.** When does the Grid come online, and does *all* automation require power —
  including the earliest clay-gated self-harvesting trees — or only later "powered" automation? (Needs
  reconciling with the automation gate in [`progression.md`](progression.md); one option: early
  automation is hand-cranked/mechanical and the Grid arrives with the tech age.)
- **Over-draw behavior.** In the moment demand exceeds supply before the player intervenes, what
  happens — do machines auto-shut in a priority order, run slower, or does the Grid "trip"? Is there a
  player-set priority / auto-load-shedding option so it's not pure manual babysitting?
- **Generators: build cost vs. fuel.** Do generators just cost resources to build, or also consume
  ongoing fuel (coal, etc.) to run — and are there clean vs. dirty generator tiers with trade-offs?
- **One grid or many.** Is power a single global pool, or per-zone grids the player balances separately?
