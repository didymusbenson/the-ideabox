# Open Questions & Assumptions

The parking lot. Everything here is **undecided or unconfirmed** and was deliberately *not* invented
in the requirements. Resolve these as the concept firms up; move settled answers into the relevant
doc and delete them here.

## Unconfirmed — needs an owner decision

These came up in the initial pitch conversation and have no answer yet:

- **[POC goal] ✅ RESOLVED.** The POC is proving out the **workflow** — building a game from scratch
  with Claude Code, docs-first, phase by phase. The game is the vehicle, not the deliverable, and
  only has to be coherent enough to be an honest test. See `vision.md` → "What this POC is trying to
  prove." (Consequence: slice scope is judged by "does this exercise the workflow representatively,"
  not by "is the game fun.")
- **[Platform] Where does the game run?** Web, mobile, desktop, console? Undecided. Affects nothing
  in requirements but blocks DESIGN.
- **[Audience] Who is this for?** Tone leans adult/wry; target audience not specified.
- **[Scope] Solo or team? Timeline? Constraints?** No team size, deadline, or hard constraints
  captured. Needed to right-size the POC slice.

## Divination methods

- **Which methods make the POC slice?** Proposed: 1–2 done well (palm and/or tarot). Confirm.
- **How much of each method's real-world ruleset do we adopt** vs. invent a game-legible subset? The
  "book" needs to be learnable in a few readings, which may mean simplifying real palmistry/tarot.
- **How random is tarot (and other draw-based methods)?** Fully random draws vs. authored/weighted
  draws that guarantee a designed choice. Affects how tightly narrative can be authored.
- **Are the backlog methods** (tea leaves, numerology, runes, scrying, pendulum) ever in scope, or
  flavor only?

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
