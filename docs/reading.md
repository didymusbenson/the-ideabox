# The Reading — the client puzzle

The reading is the core verb of the game. **Each client visit is a hand-authored deduction puzzle.**
The player leans on a toolkit of **instruments** to work out what this specific person's fortune says,
then delivers it through dialog. When the advice **aligns** with what the instruments actually
support, the client is satisfied. When it doesn't, they aren't — whether because the player misread
the puzzle, or chose to misalign on purpose.

This replaces the earlier random-draw model entirely. Nothing about a reading is randomized.

## Predetermined, not random

Every client has a **hard-set tarot spread** and a hand-authored "correct" reading. The old
requirement that readings be random and un-lookup-able is **retired** — and with it the distractor
pools, generic fallbacks, and the SLM scaling path that only existed to manage randomness.

The fun is no longer "build a coherent fortune out of randomness." It's **solving the client** —
Papers-Please / Strange-Horticulture deduction: cross-reference your instruments to figure out the
right read for this particular person, then say it well.

## The instruments (what the player leans on)

A single reading is solved by consulting several instruments. The player leans on whichever ones help;
harder clients require cross-referencing more of them. Each has its own doc under
[`instruments/`](./instruments/).

| Instrument | Provides | Doc |
|-----------|----------|-----|
| **Tarot spread** | The predetermined cards and their meanings — the centerpiece | [`instruments/tarot.md`](./instruments/tarot.md) |
| **Star chart / calendar** | Astrological facts from the client's birth date (sign, placements) | [`instruments/astrology.md`](./instruments/astrology.md) |
| **Palmistry** | Meanings read from the client's hand | [`instruments/palmistry.md`](./instruments/palmistry.md) |
| **Observation** | Tells from what the client wears and how they present | [`instruments/observation.md`](./instruments/observation.md) |
| **Identity (ID / wallet)** | Hard facts about the person, explored as an interactable object at intake | [`instruments/identity.md`](./instruments/identity.md) |

**Two kinds.** *Divination instruments* (tarot, astrology, palmistry) carry a **"book"** of fixed
meanings. *Evidence instruments* (observation, identity) supply **facts about the person**. The puzzle
is making the two cohere — the cards, the sign, the hand, and who this person visibly is should line
up into one reading.

## The loop (two beats)

See [`core-loop.md`](./core-loop.md) for the full loop; in brief:

1. **Intake** — the client states their intention and question, hands over an **interactable
   ID/wallet** the player can explore, and presents an appearance the player can read.
2. **The reading** — the predetermined spread is laid out. The player **consults the instruments** to
   work out the correct reading, and **chooses dialog** that reflects it. Solving and advising
   interleave: you consult devices as you decide what to say.

## Alignment = satisfaction (the Score)

- Dialog choices reference facts drawn from the instruments, surfaced as **color-coded keywords** (a
  card meaning, a sign, a tell). See [`art-direction.md`](./art-direction.md).
- **Solid alignment between methodology and what you say → a more satisfied client.** This is the
  accuracy axis (the Score), expressed per visit as satisfaction.
- Solve the deduction wrong and you'll pick dialog based on a wrong read — misaligned, and the client
  feels it.

## Deliberate misalignment = the Story

The correct reading isn't always what the client needs to hear. The player can **knowingly pick
misaligned-but-humane dialog** — costing satisfaction, but steering the client's arc toward a better
outcome. This is the Story axis (see [`scoring-and-story.md`](./scoring-and-story.md) and
[`clients-and-narrative.md`](./clients-and-narrative.md)).

Three states worth distinguishing (whether the *game* distinguishes them mechanically is an open
question):

- **Aligned** — you solved it and said it. Accurate, satisfying.
- **Misaligned by error** — you got the puzzle wrong. Inaccurate, unsatisfying, and it doesn't help
  them.
- **Misaligned on purpose** — you solved it, then chose the humane deviation. Inaccurate, unsatisfying,
  but it can help them.

## Authoring a client puzzle

Each client is hand-authored. At minimum an encounter defines:

- **Intention & question** — what they ask.
- **The predetermined tarot spread** and its **correct reading**.
- **The evidence** in play — ID/wallet contents, appearance/tells, birth date → sign, hand features —
  and which instruments the puzzle expects the player to lean on.
- **The correct synthesis** the instruments should cohere into (the aligned reading).
- **Dialog options** — aligned and misaligned — with color-coded keywords mapping to fortune facts.
- **True need** (which may diverge from the correct reading) and the **story branches** for how the
  player advises.

## Hard requirement (inverted)

Readings are **hand-authored per client** — never random or model-generated. This is the deliberate
reversal of the previous model.

## MVP scope

All five instruments are in play; **tarot is the centerpiece**, with astrology, palmistry,
observation, and identity as supporting instruments (palmistry and astrology are no longer deferred).
Difficulty scales with how many instruments a client's puzzle forces the player to cross-reference.
