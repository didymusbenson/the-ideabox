# Deepstead

**Status:** Planning / prototype candidate

## Pitch

A cozy dwarven farming, mining, and automation game inspired by the daily-life rhythm of classic farm sims and the satisfying production chains of factory builders.

You inherit a neglected underground hold with a few exhausted tunnels, a broken lift, and a tiny mushroom plot. By day you cultivate cavern crops, care for subterranean animals, mine deeper strata, and build relationships with the settlement. Over time, hand-worked chores become connected systems of pumps, minecarts, belts, smelters, kitchens, and workshops—turning the abandoned hold into a warm, bustling deepstead.

Working title: **Deepstead**.

## Design pillars

- **Cozy industry:** automation should feel like caring for the settlement, not paving the world with machines.
- **Every layer has a purpose:** farming supports food and brewing; mining supplies construction; crafting improves both; relationships unlock knowledge and specialization.
- **Manual first, automate later:** the player personally learns each task before building systems that handle repetition.
- **A living underground home:** workshops, homes, taverns, shrines, and public spaces matter as much as raw throughput.
- **Readable production chains:** a few expressive resources and machines rather than hundreds of near-identical intermediates.

## Core loop

1. Wake in the hold and review requests, machine status, crop needs, and expedition plans.
2. Tend crops and animals, socialize, craft, or descend into the mine.
3. Gather ore, stone, water, spores, relics, and rare deep-biome materials.
4. Process resources through workshops and increasingly automated production lines.
5. Sell or fulfill contracts, improve the hold, and unlock new residents, machines, and cavern layers.
6. End the day at the tavern, feast hall, or home; relationships and settlement events advance over time.

## Farming

Underground agriculture should be more than ordinary crops with a cave skin:

- Fungi, mosses, root beds, crystal-fed plants, cave grain, and medicinal cultures.
- Growth depends on moisture, heat, soil composition, light source, and spore compatibility.
- Pumps and channels distribute water; heat pipes create new growing zones.
- Subterranean livestock can provide milk, eggs, wool, fertilizer, hauling, or pest control.
- Cooking and brewing convert farm output into stamina, buffs, gifts, and trade goods.

## Mining and exploration

- Hand-dug tunnels gradually give way to supported shafts, lifts, drills, explosives, and minecart networks.
- Deeper layers introduce heat, gas, flooding, unstable rock, ancient structures, and territorial creatures.
- Mining is spatial: careless excavation can collapse routes, drain aquifers, or expose hazards.
- Valuable discoveries include new ore, seeds/spores, machine plans, cultural relics, and shortcuts.
- Combat, if present, stays light and expedition-focused rather than becoming the main game.

## Automation

Automation grows directly out of chores the player already understands:

- Conveyor belts, chutes, minecarts, pipes, pumps, sorters, loaders, and storage bins.
- Crushers, washers, smelters, mills, kitchens, breweries, and assembly workshops.
- Mechanical, waterwheel, steam, geothermal, and rune-powered tiers.
- Simple priority/filter rules instead of requiring programming.
- Dwarven workers can supervise stations and specialize, but are residents with schedules and needs—not anonymous inserters.
- Noise, heat, dust, traffic, and aesthetics create reasons to design a pleasant hold rather than only maximizing throughput.

## Community and relationships

- A small cast of miners, growers, smiths, cooks, engineers, merchants, and historians.
- Friendship and romance are optional; all major characters also have useful non-romantic arcs.
- Residents teach recipes, machine refinements, crop lore, and excavation techniques.
- Settlement projects—bathhouse, tavern, shrine, library, rail station—change schedules and unlock communal events.
- Seasonal festivals are replaced or supplemented by dwarven calendar events: first brew, forge lighting, ancestor nights, caravan arrivals, and deep-earth cycles.

## Progression

### Early game: reclaim

- Clear rubble, repair basic rooms, grow food, mine by hand, and restore the lift.

### Mid game: connect

- Link farms, mines, workshops, storage, and residences with transport and utilities.
- Attract specialists and choose which industries define the settlement.

### Late game: flourish

- Operate multi-layer production chains, explore dangerous depths, restore monumental halls, and establish trade with distant holds.
- The end goal is a thriving, largely self-sustaining community—not infinite exponential extraction.

## MVP

1. One compact hold and one mine with three depth bands.
2. A day cycle with stamina, sleep, and a simple dwarven calendar.
3. Six crops, two livestock types, and basic cooking/brewing.
4. Mining with ore, stone, hazards, and one rare discovery type.
5. One complete automation chain:
   - mine ore;
   - transport it by chute, belt, or minecart;
   - crush and smelt it;
   - deliver ingots to storage or a workshop.
6. Five residents with schedules, requests, friendship progression, and one settlement event each.
7. Three settlement upgrades and one communal hall customization system.
8. A 30–45 minute vertical slice ending with restoration of the main forge.

## Proposed stack

Use **Godot 4** with a 2D or 2.5D presentation. A tile/grid foundation makes farming, excavation, routing, and logistics legible while leaving room for layered lighting, particles, and chunky dwarven machinery.

## Art direction

- Warm torchlight and glowing fungi against dark stone.
- Broad silhouettes, oversized tools, carved geometric motifs, and visibly hand-built machinery.
- Machines should clank, wobble, vent steam, and look maintained rather than sterile.
- Farms and homes gradually soften industrial spaces with color, banners, food, furniture, and communal decoration.
- Avoid directly copying the visual language, characters, names, UI, or assets of the inspirations.

## First prototype questions

- Is doing a task manually satisfying before automation exists?
- Does the first automated ore-to-ingot chain feel rewarding without becoming tedious to configure?
- Can farming and factory routing coexist on one readable grid?
- Do heat, water, dust, and traffic create interesting layouts or merely extra chores?
- Can residents participate in production without turning relationship characters into disposable labor units?
- Does expanding the hold feel like building a home rather than consuming a map?

## Milestones

- [ ] Prototype mining, hauling, crushing, smelting, and storage on one grid.
- [ ] Add one crop loop connected to cooking or brewing.
- [ ] Add the day cycle and one resident with a schedule and request chain.
- [ ] Test belts versus minecarts as the primary early logistics tool.
- [ ] Add one environmental constraint: water, heat, dust, or structural support.
- [ ] Build and playtest the main-forge vertical slice.
- [ ] Lock the visual perspective and content pipeline only after the grid interactions are readable.

## Scope guards

- No giant procedural world, multiplayer, combat-heavy dungeon crawler, or hundreds of recipes in the first version.
- Do not add automation systems before the corresponding manual task is enjoyable and understood.
- Keep the initial social cast small enough for authored schedules and story arcs.
- Optimize for a satisfying compact hold, not an endlessly scaling megafactory.
