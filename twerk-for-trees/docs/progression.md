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
to running an automated factory that produces most resources on its own.** The endgame is some
**large-scale progression goal** that can only be met by broad, automated output across every branch —
and **prestige ("replant the world")** resets the trunk with permanent multipliers so each cycle
bootstraps and scales faster than the last.

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
                        large-scale automated production goal
                                        ▼
                          prestige → replant with multipliers
```

## Open questions

- **What is the large-scale endgame goal, concretely?** A megastructure, escaping/filling the void, a
  production quota, a final tree? Undefined — and it anchors the whole late game, so worth deciding.
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
