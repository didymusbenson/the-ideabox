# Twerk for Trees (TFT)

**Status:** Planning / prototype candidate

## Pitch

An incremental / idle game that loosely mirrors the progression loop of the Minecraft modpack
**Sky Factory 4**: start with nothing but a single tree in the void, and bootstrap an entire
resource economy out of it. Players begin by working basic trees for wood, unlock **resource trees**
that fruit metals and materials, then branch into technology tiers and automation — each unlock
feeding the next — until the manual grind of the early game is running itself and you're steering a
factory instead of shaking a sapling.

The name is the hook: the game's active input is the **twerk** — a rhythmic tap/shake gesture that
knocks resources loose and accelerates growth. Early game you twerk constantly; the whole tech arc is
a quest to *earn the right to stop twerking* by automating it away. (You never fully escape it — the
best late-game multipliers still reward a well-timed twerk.)

## The core loop (the Sky Factory 4 lineage)

1. **Twerk a tree** → wood, saplings, the occasional apple.
2. **Craft the starter tools** → a way to turn saplings into sticks, sticks + wood into your first
   processing station (the compost barrel / sieve analog).
3. **Sieve the basics** → early resources (pebbles, seeds, scraps) that let you *plant new kinds of
   trees* instead of just harvesting the one you have.
4. **Resource trees** → iron trees, gold trees, gem trees, and stranger ones — each a tree that fruits
   a material you previously had to grind for. Growing the tree replaces the grind.
5. **Tech branches** → spend accumulated resources to unlock processing (smelting, compression,
   multiplication) that turns raw fruit into higher-tier goods.
6. **Automation** → build harvesters, auto-planters, and sorters that run the loop while idle,
   converting active twerking into passive income.
7. **Unlock gate → new tier** → each milestone opens a new tree family + tech branch, and the loop
   repeats one layer up. Prestige/reset mechanics (a "replant the world" soft reset) carry a
   permanent multiplier so each run bootstraps faster than the last.

The satisfaction curve is the Sky Factory feeling: *"I used to do this by hand and now a machine does
it a thousand times faster"* — repeated at every tier.

## Design pillars

- **Every grind becomes a tree.** The fantasy is turning labor into horticulture — anything you
  farm manually should eventually become a tree you grow and then a machine you automate.
- **Active input that idlers respect.** The twerk is a real skill/attention mechanic early on
  (timing, combos, "shake harder" burst windows), not just an autoclicker target — but automation
  makes idling genuinely viable, so both playstyles are first-class.
- **Legible progression.** At any moment the player can see the next unlock and roughly what it costs.
  No opaque walls; the dopamine is in the visible next step.
- **Numbers go up, but readably.** Exponential growth with clean tiering and good notation so late
  game stays comprehensible instead of turning into scientific-notation soup.
- **Original everything.** Loosely inspired by Sky Factory 4's *loop*, but no Minecraft assets,
  names, textures, recipes, or trademarked terms — original art, original tree/tech taxonomy, original
  tone (the twerk framing is ours).

## Vertical slice (MVP)

A single playable arc that proves the loop is fun end to end:

1. One tree, the twerk mechanic, and manual harvesting that *feels good* on its own.
2. The first processing station and a sieve loop yielding 2–3 early resources.
3. Three resource trees (e.g. a wood tier, a stone/metal tier, one "surprise" tier) with distinct
   fruit and costs.
4. One tech branch with 4–6 upgrades culminating in the **first piece of automation** — the moment
   the player watches the loop run without them.
5. One prestige/soft-reset with a permanent multiplier, so the second run visibly outpaces the first.
6. A clear "next tier locked — coming soon" wall so testers feel the pull past the slice.

Success test: does a playtester, on hitting the first automation unlock, immediately want the next one?

## Proposed stack

Incremental games live and die on *frictionless access* and *idle-while-away* math, which points at
**web-first (TypeScript)** — instant load, no install, trivial to share for playtests, and offline/idle
progress is just a timestamp diff. Save to local storage first, cloud sync later. **Mobile matters** —
the twerk gesture is tailor-made for touch — so build responsive/touch-first from day one and treat a
PWA or thin native wrapper as the mobile path rather than a separate codebase. (Engine is a DESIGN
call; the point is a lightweight, portable, math-heavy client — not a heavy game engine.)

## Open questions

- **What *is* a twerk, mechanically?** Tap-spam? A rhythm/timing gauge? A hold-and-shake with burst
  windows? This choice sets the whole game feel and should be prototyped first, before any economy.
- **Idle vs. active balance.** How much should automation outperform (or underperform) active play?
  Idlers and active players need different-but-fair curves.
- **Prestige shape.** One global soft-reset, or per-tree/per-branch resets? Affects long-term retention
  and how "replant the world" feels thematically.
- **Monetization / scope intent.** Passion prototype, free web toy, or something with cosmetic
  monetization later? Changes nothing about the MVP but frames the roadmap.
- **How weird do the trees get?** Grounded (wood → iron → gold → gems) or escalating into absurdity
  (data trees, time trees)? The tone ceiling is worth deciding early.

## Milestones

- [ ] **Twerk spike:** prototype the core gesture in isolation until *shaking one tree* is fun with
      zero economy attached. If it isn't fun here, it won't be fun with numbers on top.
- [ ] Add the manual harvest → craft → sieve loop and the first 2–3 resources.
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
