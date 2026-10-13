# Open Questions & Assumptions

The parking lot. Everything here is **undecided or unconfirmed** and was deliberately *not* invented
in the requirements. Resolve these as the concept firms up; move settled answers into the relevant
doc and delete them here.

## Unconfirmed — needs an owner decision

**Resolved:** **Platform** = Steam-first (desktop), mobile-minded for a future port; engine leaning
**Godot 4** (final pick is DESIGN). **Scope** = **solo** project.

Still open:

- **[Audience] Who is this for?** Tone leans adult/wry; target audience not specified.
- **[Timeline/constraints]** No deadline or hard constraints captured. Needed to right-size the first
  slice.

## The reading & instruments

**Resolved (major pivot):** readings are **predetermined and hand-authored per client** — no
randomness. Play is **deduction**: cross-reference a toolkit of **instruments** (tarot spread, star
chart, palmistry, observation, ID/wallet) to solve the correct reading, then advise. **Alignment** of
advice with the solved reading = client **satisfaction** (Score); **deliberate misalignment** = the
Story. All instruments are in the MVP (tarot centerpiece); palmistry/astrology no longer deferred. The
old random-draw machinery (distractor pools, fallbacks, SLM scaling) is **retired**. See
[`reading.md`](./reading.md).

**Resolved:** difficulty is **per-client and about people, not puzzle size** — driven by their
suggestibility default, the gap between what they *want read* and what's inferable, and their **method
affinities** (preferred vs. rejected instruments; a rejected method is a noticed error). A **noticed
error** is: saying something they know is wrong, misreading something familiar, or using a rejected
method. Suggestibility **defaults are per client** (buffs/debuffs TBD). Feedback is **non-verbal —
the client's sprite reacts** (no bald meter).

Still open:

- **Distinguishing the three misalignment states** — does the game mechanically tell apart *aligned*,
  *misaligned-by-error*, and *misaligned-on-purpose*? Or do the error and the humane deviation look
  identical (leaning: identical, which is thematically sharp)?
- **Suggestibility numbers** — drain rates for noticed errors vs. book-fumbling time, buff/debuff
  values, and whether it can ever *recover* mid-session or only fall.
- **Suggestibility → satisfaction mapping** — is the ending belief level the satisfaction score, or is
  walk-out the only hard consequence and satisfaction otherwise driven by alignment? How do they
  combine?
- **How evidence is surfaced** — clickable tells on the portrait, free exploration of the ID/wallet,
  guided inspection? (Art/UX.)
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
cool blues/blacks/purples lead; **feedback is non-verbal — the client's sprite reacts** (needs a range
of belief/mood states per client). Open:

- **Reading-scene presentation.** Dim-background modal overlay vs. a full transition to a reading
  table. Both keep it tactile; pick one (or allow both contextually).
- **Artifact rendering treatment.** Ornate/illustrated (Zachtronics-style, deliberate contrast) vs.
  in-world hi-res pixel. Either way, personality is the goal.
- **Warm/cool degree.** How far to push warm candlelight/artifacts against the cool room, vs. keeping
  it cool top to bottom.

## Core loop

**Resolved:** the visit is **two beats — consultation (interview) → reading.** The consultation is
player-paced evidence-gathering (question, wants, ID/wallet, appearance) with no suggestibility
pressure, ended by the player saying **"let's get started."** The reading is where the player consults
instruments and chooses aligned (or misaligned) dialog against the draining meter.

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

- **Does the game tell the player when the accurate reading and the client's need diverge,** or must
  they infer it?
- **How do the two axes resolve at the end** — graded separately, reconciled, or Story-over-Score?
- **What are the failure states** on each axis, and can either end a run?

## Deferred to DESIGN / IMPLEMENTATION (not planning concerns yet)

Listed so they're not mistaken for open *requirements* questions:

- Engine lock (leaning Godot 4) and platform-specific implementation. Platform *target* is set
  (Steam-first, mobile-future); the engine decision itself is DESIGN.
- Exact UI, controls, and how a hand/spread/chart is presented and manipulated.
- Art direction and audio.
- Concrete scoring formulas and numeric tuning.
- Save/progression systems.
