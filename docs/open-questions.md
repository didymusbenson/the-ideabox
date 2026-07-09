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

**Resolved:** MVP is **Tarot only** (palmistry/astrology deferred). Interpretation options are
**authored per encounter** for the MVP (SLM generation is a post-MVP scaling path). The
random-vs-authored reconciliation uses fixed meaning tokens + authored option pools (with distractors)
+ generic fallbacks for un-authored tokens. The two axes **split across the beats**: the **reading** is
"doing it right" (accuracy, with distractors); the **consultation** *applies* the locked reading items
via **color-coded keyword** dialog (story). See [`methods/tarot.md`](./methods/tarot.md).

Still open:

- **Deck & vocabulary size** vs. per-encounter authoring cost. Smaller = cheaper to author, less
  variety; larger = more authoring or more reliance on generic fallbacks.
- **Distractor design** — how many misreadings per card and how obvious/subtle, so accuracy stays a
  real test without feeling like gotchas.
- **Aggregation rule** — how the locked per-card choices map onto the client's authored story branches.
- **Fallback coherence** — keeping generic fallback options (for un-authored meaning tokens) from
  feeling generic or breaking tone.
- **Keyword grounding** — may the player invoke keywords/advice *not* supported by their reading (make
  things up), and is that penalized, or is it a valid "lie to help them" lever tying into the
  Score/Story theme? (Consultation *agency* itself is resolved: the consultation is where all Story
  application happens.)
- **Consultation authoring** — how the color-coded keyword dialog is authored per encounter and mapped
  to reading items, and how many reading items a single consultation typically weaves together.
- **How much of tarot's real ruleset we adopt** (reversed cards? position modifiers?) vs. a
  game-legible subset — the book must be learnable in a few readings.
- **[Post-MVP] SLM-generated options** — if/when we add it, how to keep faithful-vs-distractor honest
  and outputs on-tone and safe with a model in the loop.
- **[Post-MVP] Palmistry & astrology: where does the randomness live** given their subjects (a hand, a
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

**Resolved:** visit order is **intake → reading → consultation** (read *then* consult, but the client
opens with an intention and question, so the reading is informed).

Still open:

- **How many clients per day, and how many days per run?** Placeholders only right now.
- **Do earlier readings in a day affect later ones** (fatigue, mood, carried information), or is each
  turn independent within the day?
- **Method choice** is moot for the MVP (Tarot only). Revisit when a second method exists: does the
  player choose the method, or is it dictated by the client/scenario?

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
