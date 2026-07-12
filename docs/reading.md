# The Reading — the client puzzle

The reading is the core verb of the game. **Each client visit is a hand-authored deduction puzzle —
and the player is running a grift.** The point isn't really to be a good psychic; it's to keep the
client **believing** long enough to send them away satisfied. The player leans on a toolkit of
**instruments** to work out what this specific person's fortune says, then delivers it through dialog,
all while managing how much the mark buys it (see [Suggestibility](#suggestibility--the-grift-meter)).

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
   work out the correct reading, and **chooses dialog** that reflects it — all against a draining
   suggestibility meter. Solving and advising interleave: you consult devices as you decide what to say.

## Suggestibility — the grift meter

Every visit has a live **suggestibility** meter: how much the client believes the psychic *right now*.
It is the currency of the grift, and managing it is the moment-to-moment game.

- **It starts** at a value set by the client (some people are more credulous than others) and by shop
  aids like **incense** that make people more suggestible (see [`shop-and-economy.md`](./shop-and-economy.md)).
- **It drains from two things:**
  - **Noticed errors** — saying something flat-out wrong that the client *catches* (it contradicts
    what they know about themselves, or is transparently generic). Sharp drops.
  - **Fumbling** — time spent flipping through the instruments' reference books in front of the client.
    A real psychic wouldn't need to look everything up, so visible searching slowly **burns** belief.
- **Hit zero → walk-out.** If suggestibility empties mid-session, the client cuts it short and leaves
  **dissatisfied** — the hard per-visit fail state.
- **Keep it high → a satisfied client.** The more belief you preserve, the more they accept the
  reading and the better they leave. Suggestibility is the live currency behind the Score.

### The squeeze: accuracy vs. the clock

Consulting instruments is how you avoid noticed errors — but consulting *costs* suggestibility. So
every visit is a squeeze: **dig through the books to be sure** (accurate, but you burn belief and look
like a fraud) vs. **wing it from memory** (fast, but you risk a noticed error that costs even more).
**Mastery is the way out:** the better the player knows the books, the less they need to look, the
less belief they burn. Learning the instruments is the real skill curve.

### This is also the answer to "can you lie?"

Suggestibility is the mechanic behind the grift: **you can say whatever you like** — the only risk is
that the client *notices* it's wrong. A lie that fits what they know rides free; a lie or mistake that
contradicts their reality costs belief. That's what makes deliberately misaligning to help someone (the
Story, below) a *gamble* — a bet that the humane thing won't get caught.

## Alignment = satisfaction (the Score)

- Dialog choices reference facts drawn from the instruments, surfaced as **color-coded keywords** (a
  card meaning, a sign, a tell). See [`art-direction.md`](./art-direction.md).
- **Saying things that align with the correct reading avoids "noticed errors"** — it keeps
  suggestibility up and sends the client away satisfied. This is the accuracy axis (the Score),
  expressed per visit as preserved belief and satisfaction.
- Solve the deduction wrong and you'll advise from a mistaken read; when the client catches it,
  suggestibility drops — and if it bottoms out, they walk.

## Deliberate misalignment = the Story

The correct reading isn't always what the client needs to hear. The player can **knowingly pick
misaligned-but-humane dialog** — a gamble against the suggestibility meter (if the client notices the
deviation, belief drops), but one that can steer their arc toward a better outcome. This is the Story
axis (see [`scoring-and-story.md`](./scoring-and-story.md) and
[`clients-and-narrative.md`](./clients-and-narrative.md)).

Three states worth distinguishing (whether the *game* distinguishes them mechanically is an open
question):

- **Aligned** — you solved it and said it. Belief preserved, client satisfied.
- **Misaligned by error** — you got the puzzle wrong. If caught, belief drops; it helps no one.
- **Misaligned on purpose** — you solved it, then chose the humane deviation. A bet that it won't be
  noticed; if it lands, it can help them even at a cost to satisfaction.

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
