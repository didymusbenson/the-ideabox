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

## The reading & instruments

**Resolved (major pivot):** readings are **predetermined and hand-authored per client** — no
randomness. Play is **deduction**: cross-reference a toolkit of **instruments** (tarot spread, star
chart, palmistry, observation, ID/wallet) to solve the correct reading, then advise. **Alignment** of
advice with the solved reading = client **satisfaction** (Score); **deliberate misalignment** = the
Story. All instruments are in the MVP (tarot centerpiece); palmistry/astrology no longer deferred. The
old random-draw machinery (distractor pools, fallbacks, SLM scaling) is **retired**. See
[`reading.md`](./reading.md).

Still open:

- **Difficulty scaling** — how many instruments a client's puzzle forces the player to cross-reference,
  and how that ramps across the game.
- **Distinguishing the three misalignment states** — does the game mechanically tell apart *aligned*,
  *misaligned-by-error*, and *misaligned-on-purpose*? Or do the error and the humane deviation look
  identical on the satisfaction meter (leaning: identical, which is thematically sharp)?
- **Suggestibility tuning** — starting values (per client, per incense), drain rates for noticed errors
  vs. book-fumbling time, and whether it can ever *recover* mid-session or only fall.
- **What counts as a "noticed" error** — the client catches contradictions of what *they* know
  (facts, their situation) but presumably not obscure tarot misreadings they can't verify. Where's the
  line, and how is it made legible to the player?
- **Suggestibility → satisfaction mapping** — is the ending meter level the satisfaction score, or is
  a walk-out the only hard consequence and satisfaction otherwise driven by alignment? How do the two
  combine?
- **How evidence is surfaced** — clickable tells on the portrait, free exploration of the ID/wallet,
  guided inspection? (Also an art/UX question.)
- **Contradiction & withholding** — can instruments disagree, or facts be missing/deceptive, to deepen
  the deduction (a Papers-Please discrepancy hunt)? How much?
- **How much real tarot / astrology / palmistry** to adopt vs. a game-legible subset the player can
  learn in a few readings.
- **Instrument weighting** — can tarot alone solve a client, or is corroboration from the others always
  required?
- **Backlog instruments** (tea leaves, numerology, runes, scrying, pendulum) — ever in scope, or flavor
  only?

## Art direction

Confirmed: hi-res pixel art; split-screen view (client top-left, player silhouette bottom-right,
dialogue along the bottom); the reading is a separate scene; instruments/artifacts get personality;
cool blues/blacks/purples lead. Open:

- **Reading-scene presentation.** Dim-background modal overlay vs. a full transition to a reading
  table. Both keep it tactile; pick one (or allow both contextually).
- **Artifact rendering treatment.** Ornate/illustrated (Zachtronics-style, deliberate contrast) vs.
  in-world hi-res pixel. Either way, personality is the goal.
- **Warm/cool degree.** How far to push warm candlelight/artifacts against the cool room, vs. keeping
  it cool top to bottom.

## Core loop

**Resolved:** the visit is **two beats — intake → reading.** Intake gathers evidence (question,
ID/wallet, appearance); the reading is where the player consults instruments and chooses aligned (or
misaligned) dialog. Solving and advising interleave.

Still open:

- **How many clients per day, and how many days per run?** Placeholders only right now.
- **Do earlier readings in a day affect later ones** (fatigue, mood, carried information), or is each
  turn independent within the day?
- **Instrument availability** — are all instruments always on hand, or are some unlocked/limited (and
  does the shop gate any)?

## Clients & narrative

- **How many arc clients?** "A handful" — pin a target number for the full game and for the slice.
- **How is a client "leaving for good" framed** — bittersweet, triumphant, comedic, player's choice?
- **Does the protagonist have his own arc,** or stay a static cynic? Shapes tone and ending.
- **How legible is a client's *true need*** vs. their presenting concern — spelled out, hinted, or
  fully inferred by the player?

## Scoring & the two axes

- **Is the Story axis an explicit meter or purely felt** through consequences? (Leaning: felt.)
- **Does the game tell the player when the accurate reading and the client's need diverge,** or must
  they infer it?
- **How do the two axes resolve at the end** — graded separately, reconciled, or Story-over-Score?
- **What are the failure states** on each axis, and can either end a run?

## Deferred to DESIGN / IMPLEMENTATION (not planning concerns yet)

Listed so they're not mistaken for open *requirements* questions:

- Tech stack, engine, and platform-specific implementation.
- Exact UI, controls, and how a hand/spread/chart is presented and manipulated.
- Art direction and audio.
- Concrete scoring formulas and numeric tuning.
- Save/progression systems.
