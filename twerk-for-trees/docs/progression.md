# Progression & tech branches

The macro shape of the game: a **resource-tree trunk** that sprouts **tech branches** as you reach key
materials, all feeding toward **large-scale automated production**. Resources are never just a score —
they're the currency you spend on the tools and machines that upgrade your infrastructure, which in
turn produce more resources. Every branch is both *paid for by* and *feeds back into* that loop.

Specific numbers (gate costs, timers, yields, tiers) are deferred to the detailed progression design;
this doc fixes the **structure and unlock order**, not the math.

## The trunk — the resource-tree phase

The spine of the whole game. You:

1. **Twerk a plot's tree for drops.**
2. **Convert drops into materials** (process/craft them into usable resources).
3. **Upgrade through tree types** — each new tree is a new resource, and unlocking the next tree is
   generally done by *applying an earlier processed resource back onto a plant* (the combine-to-unlock
   pattern borrowed from Sky Factory 4 — see [`inspiration-sky-factory-4.md`](inspiration-sky-factory-4.md)).

Tree drops are the raw input for everything downstream. Climbing the tree ladder is what opens the
branches below.

## The branches — unlocked by hitting key materials

Each branch is **gated behind reaching a specific material on the trunk.** Once open, a branch deepens
in parallel with everything else — progress stops being a single line and becomes several tracks
advancing at once.

> These branches are *realized* as the game's tabbed **zones**, with unlocks purchased in the Workshop
> — see [`zones-and-interface.md`](zones-and-interface.md) for the interface. In short: the trunk is the
> **Orchard**, automation is a **Workshop** upgrade family, farming is the **Farm**, smelting/alloys run
> through the **Workshop → Factory** (fed by the Quarry), and power/machinery is the **Factory**. Two
> pillars below aren't captured in the original branch list: the **Quarry** (high-throughput ores, coal,
> and gems — the fast replacement for slow ore-trees) and the **Arena** (simplified idle combat).

1. **Automation — gate: Clay.**
   The first branch. Reaching clay unlocks **simple automation: faster / self-harvesting trees**
   (auto-twerkers) so plots produce without constant manual tapping. This is the start of the pitch's
   "earn the right to stop tapping" — idle viability begins here and deepens through the game.

2. **Farming — gate: seeds drop from a tree (can trigger early).**
   At some point a tree drop yields **seeds**, opening a **farming branch** — growing crops alongside
   trees as a parallel production line. Because the trigger is a *drop*, this branch can open at various
   times, making it a pleasant surprise rather than a fixed step.

3. **Smelting & Alloys — gate: Metals.**
   Once metal-bearing trees come online, unlock **smelting** (raw metal drops → ingots) and then
   **alloys** (combining metals into higher-grade materials). Alloys are the input to better tools and
   machines — the branch that turns raw output into *quality*.

4. **Power & Machinery — gate: after metals / smelting.**
   With metals and alloys available, unlock **power generation and machinery** — machines that process,
   multiply, and automate production at scale. This is where the operation goes industrial and the
   other branches get force-multiplied.

## The economy loop — what resources are *for*

```
   twerk / harvest ──► drops ──► process into materials
         ▲                              │
         │                              ▼
   more & faster           spend on tools & machines
   production        ◄──   (upgrade infrastructure)
```

Nothing is hoarded for its own sake. Materials are spent on the tools and machines that make production
faster, bigger, and more automated — which yields more materials to spend on the next upgrade. Each
branch plugs into this same loop: automation speeds the harvest, smelting/alloys raise material
quality, power/machinery multiplies throughput, farming widens the input base.

## Direction — toward large-scale automated production

The through-line is the transformation the pitch promises, at macro scale: **from hand-tapping one tree
to running an automated factory that produces most resources on its own.** Everything the player builds
across the branches is, ultimately, a multiplier funnelled at the endgame below.

## Endgame — the Singularity (Universal Paperclips lineage)

The terminal goal is borrowed from **Universal Paperclips**: the entire operation exists to mass-produce
**one specific resource — the *singularity resource*** — in absurd, ever-accelerating quantity. Every
branch is really a lever on how fast that one resource is produced: automation harvests faster,
smelting/alloys and power/machinery multiply throughput, farming widens the input base. Reaching a
threshold quantity of the singularity resource triggers the **Singularity** — the run's win state.

At the Singularity, the player chooses:

- **Endless mode — keep grinding.** Stay in the world and push the number higher forever. There's no
  further progression to unlock, but you can keep optimizing — including **maxing/capping every other
  resource** for completion's sake. Pure number-go-up, for players who want it.
- **New world — prestige.** Start over in a fresh world carrying a **permanent prestige upgrade**, so the
  next run bootstraps and scales faster. This is the meaningful "replant the world" the rest of the
  design points at.

**Tone bonus worth leaning into:** Universal Paperclips is a cheerful optimizer quietly converting the
universe into paperclips. TFT's cute-not-sexy twist — a wholesome twerking farmer who accidentally turns
a whole world into a monoculture of one resource — is the same joke in a greener coat of paint, and the
writing can wink at it.

## Branch map

```
                         ┌─────────────────────────────┐
                         │   TRUNK: resource-tree phase │
                         │  (tree types → materials)    │
                         └──────────────┬──────────────┘
        reach Clay   ┌──────────────────┼───────────────────┐   seeds drop
             ────────┤                  │                    ├────────
                     ▼                  ▼ reach Metals        ▼
              ┌────────────┐     ┌───────────────┐    ┌────────────┐
              │ AUTOMATION │     │ SMELTING &    │    │  FARMING   │
              │ self-harvest│    │ ALLOYS        │    │ (parallel  │
              │ trees       │    │ ingots→alloys │    │  crops)    │
              └────────────┘     └──────┬────────┘    └────────────┘
                                        ▼ after metals/smelting
                                 ┌──────────────┐
                                 │ POWER &      │
                                 │ MACHINERY    │
                                 │ scale it up  │
                                 └──────┬───────┘
                                        ▼
                   funnel all output → the SINGULARITY RESOURCE
                                        ▼
                     produce an ungodly amount → SINGULARITY (win)
                                        ▼
                 ┌──────────────────────┴───────────────────────┐
                 ▼                                               ▼
        endless mode: number-go-up,               new world: prestige upgrade,
        max/cap other resources                   replant & scale faster
```

## Open questions

- **Which resource is the singularity resource?** The endgame *shape* is decided (mass-produce one
  terminal resource → Singularity → endless-vs-prestige fork), but the resource itself is undefined. Is
  it a top-tier material the tree economy naturally funnels into, or a bespoke end-resource (e.g. a
  "World Seed" / "Life" currency) crafted only from broad automated output? Its identity also sets the
  win-screen fantasy.
- **Is there prestige *before* the Singularity?** The current framing ties prestige to reaching the
  Singularity (win, then optionally replant). Decide whether a smaller partial-prestige exists earlier
  for players who stall — and note the MVP tests a scaled-down proxy of this loop, not the full
  singularity threshold.
- **Endless-mode caps.** What exactly can still be maxed/capped in endless mode, and is hitting every
  cap its own (cosmetic?) completion reward?
- **Exact gate materials and order.** Clay → automation is fixed; which *metal tier* opens smelting,
  and whether power strictly requires alloys, is still to pin down.
- **Do branches gate each other?** e.g. does Power & Machinery require Alloys as an input, making the
  branches a dependency graph rather than four independent tracks? (Leaning yes — it creates nice
  cross-branch pull.)
- **How does farming feed the rest?** Parallel-but-separate income, or do crops become inputs the other
  branches consume (fuel, food for workers, alloy reagents)?
- **Seeds trigger.** Guaranteed by a certain point, or genuinely luck-based? Affects how reliably the
  farming branch opens.
- **Numbers everywhere** — gate costs, timers, yields, alloy recipes — deferred to the progression-math
  pass.
