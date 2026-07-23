# Twerk for Trees (TFT)

**Status:** Planning / prototype candidate

## Pitch

An incremental / idle game that loosely mirrors the progression loop of the Minecraft modpack
**Sky Factory 4**: start with nothing but a single tree in the void, and bootstrap an entire
resource economy out of it. Players begin by working basic trees for wood, unlock **resource trees**
that fruit metals and materials, then branch into technology tiers and automation — each unlock
feeding the next — until the manual grind of the early game is running itself and you're steering a
factory instead of shaking a sapling.

The name is the hook: every **plot** has a **little animated character** who **twerks — throws ass —
when you tap on them.** The tone is deliberately **cute, not sexy** (think chunky, wholesome,
googly-eyed mascots), which is the whole joke: a wholesome idle farmer dressed up in a cheeky title.
Mechanically, **tapping a plot's twerker drives that plot's timers down** — growth and harvest run on
timers, and twerking is the active input that accelerates them. Early game you tap constantly; the
whole tech arc is a quest to *earn the right to stop tapping* by automating it away. (You never fully
escape it — the best late-game multipliers still reward active twerking.)

## Core mechanics: the twerk, the plots & idle vs. active

Three ideas carry the whole game.

- **The twerk (active input).** Plants grow and produce on **timers**. Every **plot** has its own cute
  character, and **tapping that character makes it twerk, driving the timers of the plant(s) in that
  plot down faster.** A plot may hold one or more plants, so a twerker works its whole plot. Twerking is
  the active lever — you pick the plot that matters right now and shake it home.
- **The plots & dirt (capacity).** You start with **one plot holding one tree.** That tree's resources
  let you **craft dirt**, and dirt is what builds your **next plot** — where you grow your next tree.
  Every expansion is literally horticultural: a new plot bootstrapped from the output of the ones you
  already have. More plots = more twerkers and more timers running in parallel, so plot count (and,
  later, plants per plot) is the core capacity ladder. The strategic tension is always "wider (craft
  dirt, add plots) vs. deeper (better tools/upgrades on the plots you have)."
- **Idle that rewards showing up.** It runs idle — plants keep growing while you're away, so you can
  check in and collect — but the **most progress happens when you're actively twerking.** In that
  idle/active balance it sits comfortably in the lineage of **Cookie Clicker** and **Adventure
  Capitalist**: pleasant to leave running, much faster to play. Automation gradually keeps idling
  viable deep into the game, but active play is always ahead.

Everything else — resources, tools, tech, automation — is unlocked and paid for by what those plots
produce. **Resources unlock tools and upgrades** (faster timers, better yields, auto-twerkers), which
in turn make the next batch of dirt, the next plot, and the next plant category worth it.

## The core loop (the Sky Factory 4 lineage)

1. **Tap the twerker** → its growth/harvest timer drops faster; collect wood, saplings, the
   occasional apple when the timer lands.
2. **Craft the starter tools** → a way to turn saplings into sticks, sticks + wood into your first
   processing station (the compost barrel / sieve analog).
3. **Craft dirt → build a plot** → turn your tree's output into dirt, and dirt into your **next plot**,
   where the next tree goes. This is the early-game heartbeat: every new plot is bootstrapped from the
   ones you already have, and plot count is your first real capacity ladder.
4. **Sieve the basics** → early resources (pebbles, seeds, scraps) that let you *plant new kinds of
   trees* on the plots you've built.
5. **Resource trees** → iron trees, gold trees, gem trees, and stranger ones — each a tree that fruits
   a material you previously had to grind for. Growing the tree replaces the grind.
6. **Tech branches** → spend accumulated resources to unlock processing (smelting, compression,
   multiplication) that turns raw fruit into higher-tier goods.
7. **Automation** → build harvesters, auto-planters, and auto-twerkers that run the loop while idle,
   converting active twerking into passive income.
8. **Unlock gate → new tier** → each milestone opens a new tree family + tech branch, and the loop
   repeats one layer up. Prestige/reset mechanics (a "replant the world" soft reset) carry a
   permanent multiplier so each run bootstraps faster than the last.

The satisfaction curve is the Sky Factory feeling: *"I used to do this by hand and now a machine does
it a thousand times faster"* — repeated at every tier.

## Design pillars

- **Every grind becomes a tree.** The fantasy is turning labor into horticulture — anything you
  farm manually should eventually become a tree you grow and then a machine you automate.
- **Cute, not sexy.** The twerking mascots are wholesome and silly — chunky, googly-eyed, more
  Saturday-morning than nightclub. The title is a cheeky bait-and-switch for a genuinely wholesome
  idle farmer; the art direction must protect that or the joke curdles.
- **Tap-to-hasten, don't tap-to-earn.** The active input speeds *timers*, it doesn't mint resources
  per tap — so twerking is about choosing which **plot** to push, not mashing for raw output.
- **Idle-friendly, active-rewarding.** It ticks along while you're away (check in, collect, leave), but
  the fastest progress is hands-on — the Cookie Clicker / Adventure Capitalist bargain. Automation
  keeps idling viable as the game deepens; active play stays ahead.
- **Wide vs. deep.** Capacity is finite; every session is a choice between crafting dirt to add plots
  (more parallel timers) and upgrading the plots you already run (faster/better timers). That tension
  is the strategy layer under the idle math.
- **Legible progression.** At any moment the player can see the next unlock and roughly what it costs.
  No opaque walls; the dopamine is in the visible next step.
- **Numbers go up, but readably.** Exponential growth with clean tiering and good notation so late
  game stays comprehensible instead of turning into scientific-notation soup.
- **Original everything.** Loosely inspired by Sky Factory 4's *loop*, but no Minecraft assets,
  names, textures, recipes, or trademarked terms — original art, original tree/tech taxonomy, original
  tone (the twerk framing is ours).

## Vertical slice (MVP)

A single playable arc that proves the loop is fun end to end:

1. One plot with one tree and its twerker, and the tap-to-hasten timer loop — harvesting that *feels
   good* on its own, before any economy.
2. The **dirt → next plot** bootstrap: craft dirt from the first tree's output to build a second plot
   and plant a second tree, so the core expansion loop and "wider vs. deeper" are testable in the slice.
3. The first processing station and a sieve loop yielding 2–3 early resources.
4. Three plant categories (e.g. a wood tier, a stone/metal tier, one "surprise" tier) with distinct
   fruit, timers, and costs — each with its own twerker.
5. One tech branch with 4–6 upgrades culminating in the **first piece of automation** (an auto-twerker
   that works a plant's timer for you) — the moment the player watches the loop run without them.
6. One prestige/soft-reset with a permanent multiplier, so the second run visibly outpaces the first.
7. A clear "next tier locked — coming soon" wall so testers feel the pull past the slice.

Success test: does a playtester, on hitting the first automation unlock, immediately want the next one?

## Proposed stack

Incremental games live and die on *frictionless access* and *idle-while-away* math, which points at
**web-first (TypeScript)** — instant load, no install, trivial to share for playtests, and offline/idle
progress is just a timestamp diff. Save to local storage first, cloud sync later. **Mobile matters** —
the twerk gesture is tailor-made for touch — so build responsive/touch-first from day one and treat a
PWA or thin native wrapper as the mobile path rather than a separate codebase. (Engine is a DESIGN
call; the point is a lightweight, portable, math-heavy client — not a heavy game engine.)

## Open questions

- **Tap feel (decided in shape, open in tuning).** The twerk is: tap a plot's twerker → it twerks →
  the plot's timers speed up. Still to tune: does a tap subtract a flat chunk of time, multiply the
  timer speed while you tap, or fill a "hype" gauge that boosts the plot? And can you meaningfully work
  multiple plots at once, or is attention deliberately scarce?
- **Dirt & plot pacing.** How much dirt a plot should cost and how fast plots come — this curve sets
  the wide-vs-deep tension and largely determines how grindy the mid-game feels. (Specific numbers to
  come when we design the actual progression.)
- **Idle/active gap (decided in shape, open in tuning).** Idle works; active is meant to be
  meaningfully faster. Still to tune: *how much* faster active is, and how far automation closes the
  gap so idlers stay first-class rather than punished.
- **Prestige shape.** One global soft-reset, or per-tree/per-branch resets? Affects long-term retention
  and how "replant the world" feels thematically.
- **Monetization / scope intent.** Passion prototype, free web toy, or something with cosmetic
  monetization later? Changes nothing about the MVP but frames the roadmap.
- **How weird do the trees get?** Grounded (wood → iron → gold → gems) or escalating into absurdity
  (data trees, time trees)? The tone ceiling is worth deciding early.

## Milestones

- [ ] **Twerk spike:** one plot, one tree, one twerker. Tune the tap-to-hasten feel and land the
      animation until *tapping a twerker to rush its timer* is satisfying with zero economy attached.
      If it isn't fun here, it won't be fun with numbers on top.
- [ ] Add the dirt → next plot bootstrap so wide-vs-deep is playable.
- [ ] Add the harvest → craft → sieve loop and the first 2–3 resources.
- [ ] Add resource trees and one tech branch; land the first automation unlock.
- [ ] Add prestige + permanent multiplier; verify run 2 beats run 1.
- [ ] Balance pass on the idle/active curves; playtest the "want the next unlock" pull.
- [ ] Wrap the vertical slice with a locked next-tier teaser.

## Scope guards

- No full tech tree, no huge tree roster, no multiplayer, and no meta-progression beyond one prestige
  in the vertical slice.
- Don't build the economy until the twerk itself is fun on its own.
- Don't add a second tier until the first tier's automation payoff genuinely lands.
- Keep number growth readable — resist adding mechanics that require a spreadsheet to enjoy.
