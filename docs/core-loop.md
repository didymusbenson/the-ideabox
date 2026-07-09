# Core Loop

The game is structured as a series of **days**. Each day is a **session** of client appointments.
There are two nested loops: the **client loop** (one reading) and the **day loop** (a set of
clients plus an end-of-day reckoning).

## The client loop

Each client visit unfolds as **three beats**: a short intake, the reading, then the consultation.
The reading comes *before* the full consultation — the player commits to interpretations and only
then plays the scene out — but the client still arrives with a stated intention and question, so the
reading is **informed, not blind**.

### Beat 1 — Intake (arrival)

1. **Intention & question.** The client sits down and states, briefly, their **intention** (what
   they're hoping for) and the **question** they want the cards to answer ("Should I take the job?",
   "Is he cheating?", "Will my mother be okay?"). This is enough for the player to know the concern;
   the deeper conversation comes *after* the reading. This is their *presenting concern*, and it may
   or may not be their real need (see [`clients-and-narrative.md`](./clients-and-narrative.md)).

### Beat 2 — The reading (separate scene)

2. **Perform the reading, step by step.** In a dedicated scene (a dim overlay or a transition to the
   reading table; see [`art-direction.md`](./art-direction.md)), the spread is **drawn at random**. As
   each card turns, the game surfaces this encounter's authored **interpretation options** for that
   card's meaning, keyed to the client's stated question. The player picks one and it **locks in**;
   then the next card. See [`methods/tarot.md`](./methods/tarot.md).
3. **Aggregate.** The locked-in choices across the spread aggregate into the reading's overall
   message.

### Beat 3 — Consultation (delivery)

4. **Play the scene out.** The visit returns to the two-hander. The player delivers the reading, the
   client reacts and opens up, and the scene plays out from what was drawn and locked. The outcome
   feeds the client's story; the in-the-moment reaction lands now, while longer-term consequences
   surface on later days.

> **Requirement:** the reading must expose *both* a "did I read it faithfully / by the book" decision
> (accuracy → the Score) and a "which valid direction did I steer it" decision (→ the Story). Because
> the player commits interpretations before the full consultation, **the delivered reading is the
> material the consultation is played from.**

## The day loop

A day is a curated set of client turns:

- **Composition.** Each day mixes **one-off clients** (self-contained appearances) with **arc
  clients** (recurring characters whose storylines span the game). The mix is authored, not random.
- **Progression within the day.** Clients are seen in sequence. Earlier readings may color later
  ones (mood, fatigue, information the player has picked up) — the extent of this is an open
  question, but the day is a deliberately shaped sequence, not an unordered list.
- **End-of-day scorecard.** When the day ends, the player receives a **scorecard** summarizing the
  readings they gave and their **accuracy according to method** — how "by the book" they played.
  This is the Score axis surfaced. See [`scoring-and-story.md`](./scoring-and-story.md).
- **Between days.** Narrative state advances: arc clients' situations move based on the advice they
  were given, returning clients are scheduled, and new clients enter. The consequences of yesterday
  become the setup for a future day.

## Session shape (rough, to be tuned)

> Numbers here are directional placeholders for planning, not committed values.

- A **day**: a handful of clients (enough to feel like a working shift, few enough that each one
  matters).
- A **run / full game**: multiple days forming a season, over which arc clients rise and resolve.
- **First slice**: a small number of days that can demonstrate the full loop end-to-end, including at
  least one arc client who returns and visibly changes based on prior advice.

## What the loop must deliver each pass

- A **mechanical challenge** (perform the method correctly) — the Score.
- A **human choice** (what to actually tell them) — the Story.
- **Legible feedback** — at end of day for craft accuracy; over subsequent days for narrative
  outcome.
- **Memory** — recurring clients must reflect what the player told them before.
