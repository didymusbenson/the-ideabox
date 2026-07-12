# "I'm Not a Psychic" — Documentation

**Working title:** I'm Not a Psychic
**Phase:** PLANNING (requirements). No tech stack or implementation decisions yet — those come in DESIGN.
**Type:** A narrative, choice-based **deduction** game.
**The reading:** each client is a hand-authored puzzle solved with a toolkit of **instruments** —
tarot spread (centerpiece), star chart, palmistry, observation, and ID/wallet (see
[`reading.md`](./reading.md) and [`instruments/`](./instruments/)).

## The one-line pitch

You are *not* a psychic — but you run a psychic business. Each client is a puzzle: you cross-reference
your instruments (tarot spread, star chart, palmistry, what they wear, what's in their wallet) to work
out the "correct" reading, then decide what to actually tell them. You don't believe a word of it.
They do.

## The central tension (read this first)

The game pulls in two directions at once, and the whole design hangs on the gap between them:

- **The Score** rewards **solving the client and saying it straight** — advice that *aligns* with what
  the instruments actually support leaves the client satisfied.
- **The Story** rewards *helping the person* — sometimes the accurate reading isn't what they need, so
  you **deliberately misalign**: cost yourself satisfaction to steer them toward a happier ending,
  ideally until they no longer need you.

Choosing between a satisfied client and a helped one is the core of the experience. (And a third
possibility keeps you honest: misalign because you got the puzzle *wrong*, and you satisfy no one and
help no one.)

## How to read these docs (progressive disclosure)

Each file is self-contained and scoped to one concern. Load only what your task needs.

| File | What it covers | Read it when you need… |
|------|----------------|------------------------|
| [`vision.md`](./vision.md) | Fantasy, tone, design pillars, references | The "why" and the feel |
| [`art-direction.md`](./art-direction.md) | Visual style, palette, composition, the reading scene, instrument/reference UI | Anything about how the game looks |
| [`core-loop.md`](./core-loop.md) | The per-client and per-day loop, the two-beat visit (intake → reading), the day scorecard | How a session actually plays |
| [`reading.md`](./reading.md) | The **client puzzle** — predetermined readings, the instrument toolkit, alignment = satisfaction | The reading mechanics in general |
| [`instruments/`](./instruments/) | One doc per instrument: [`tarot`](./instruments/tarot.md), [`astrology`](./instruments/astrology.md), [`palmistry`](./instruments/palmistry.md), [`observation`](./instruments/observation.md), [`identity`](./instruments/identity.md) | The specifics of one instrument |
| [`clients-and-narrative.md`](./clients-and-narrative.md) | Client model, one-off vs. recurring arcs, memory/consequence, happy endings | Characters, story, branching |
| [`scoring-and-story.md`](./scoring-and-story.md) | The two axes in detail — alignment/satisfaction vs. narrative outcome, and how they conflict | The tension mechanic, feedback, endings |
| [`shop-and-economy.md`](./shop-and-economy.md) | **WIP / isolated.** Clients paying, satisfaction, a between-days shop, and "fudge" upgrades | The money layer (still being figured out) |
| [`glossary.md`](./glossary.md) | Shared vocabulary | You hit an ambiguous term |
| [`open-questions.md`](./open-questions.md) | Unresolved decisions, unconfirmed assumptions, parking lot | Deciding what to nail down next |

## Status of the docs

These are a **first draft** distilled from the initial pitch. Requirements capture *intent and
direction*; they deliberately avoid over-specifying mechanics, numbers, and technical detail —
that granularity belongs to DESIGN and IMPLEMENTATION. Anything not yet decided lives in
[`open-questions.md`](./open-questions.md) so it stays visible instead of getting silently invented.
