# Open Questions & Assumptions

The parking lot. Everything here is **undecided or unconfirmed** and was deliberately *not* invented
in the requirements. Resolve these as the concept firms up; move settled answers into the relevant
doc and delete them here.

## Unconfirmed — needs an owner decision

These came up in the initial pitch conversation and have no answer yet:

- **[Platform] Where does the game run?** Web, mobile, desktop, console? Undecided. Affects nothing
  in requirements but blocks DESIGN.
- **[Audience] Who is this for?** Tone leans adult/wry; target audience not specified.
- **[Scope] Solo or team? Timeline? Constraints?** No team size, deadline, or hard constraints
  captured. Needed to right-size the first slice.

## Divination methods

- **[Big one] Reconciling random readings with authored story.** Readings must be randomized and
  non-look-up-able, yet still produce authored, per-client story branches. Working model
  (`divination-methods.md`): fixed meanings + player's chosen *interpretive direction* + aggregation,
  so branches key off the player's stance, not the specific cards. Needs validation and a concrete
  aggregation rule.
- **Constraining randomness without re-scripting.** Can a fully random draw be incoherent or tonally
  wrong for a client? If we weight/limit the draw to keep readings coherent, how without
  re-introducing look-up-ability?
- **Which methods make the first slice?** Proposed: 1–2 done well (tarot lead, optionally palm).
  Confirm.
- **How much of each method's real-world ruleset do we adopt** vs. invent a game-legible subset? The
  "book" needs to be learnable in a few readings, which may mean simplifying real palmistry/tarot.
- **Tarot specifics** (in [`methods/tarot.md`](./methods/tarot.md)): reversed cards? spread
  size/shape? how many valid directions per card, and are they authored or derived from a few
  interpretive axes? how do per-card choices aggregate into one outcome?
- **Palmistry & astrology: where does the randomness live** given their subjects (a hand, a
  birth-derived chart) are less obviously random than a shuffled deck? See the method stubs.
- **Are the backlog methods** (tea leaves, numerology, runes, scrying, pendulum) ever in scope, or
  flavor only?

## Art direction

Confirmed: hi-res pixel art; split-screen consultation (client top-left, player silhouette
bottom-right, dialogue along the bottom); the reading is a separate scene; artifacts get personality;
cool blues/blacks/purples lead. Open:

- **Reading-scene presentation.** Dim-background modal overlay vs. a full transition to a reading
  table. Both keep it tactile; pick one (or allow both contextually).
- **Artifact rendering treatment.** Ornate/illustrated (Zachtronics-style, deliberate contrast) vs.
  in-world hi-res pixel. Either way, personality is the goal.
- **Warm/cool degree.** How far to push warm candlelight/artifacts against the cool room, vs. keeping
  it cool top to bottom.

## Core loop

- **How many clients per day, and how many days per run?** Placeholders only right now.
- **Do earlier readings in a day affect later ones** (fatigue, mood, carried information), or is each
  turn independent within the day?
- **Can the player choose the method,** or is it dictated by the client/scenario? Pitch implies
  sometimes-chosen; needs a rule.

## Clients & narrative

- **How many arc clients?** "A handful" — pin a target number for the full game and for the slice.
- **How is a client "leaving for good" framed** — bittersweet, triumphant, comedic, player's choice?
- **Does the protagonist have his own arc,** or stay a static cynic? Shapes tone and ending.
- **How legible is a client's *true need*** vs. their presenting concern — spelled out, hinted, or
  fully inferred by the player?

## Scoring & the two axes

- **Is the Story axis an explicit meter or purely felt** through consequences? (Leaning: felt.)
- **Does the game tell the player when the method and the need diverge,** or must they infer it?
- **How do the two axes resolve at the end** — graded separately, reconciled, or Story-over-Score?
- **What are the failure states** on each axis, and can either end a run?

## Deferred to DESIGN / IMPLEMENTATION (not planning concerns yet)

Listed so they're not mistaken for open *requirements* questions:

- Tech stack, engine, and platform-specific implementation.
- Exact UI, controls, and how a hand/spread/chart is presented and manipulated.
- Art direction and audio.
- Concrete scoring formulas and numeric tuning.
- Save/progression systems.
