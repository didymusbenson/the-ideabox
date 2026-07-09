# Core Loop

The game is structured as a series of **days**. Each day is a **session** of client appointments.
There are two nested loops: the **client loop** (one reading) and the **day loop** (a set of
clients plus an end-of-day reckoning).

## The client loop

Each client visit unfolds as **two distinct scenes** — a consultation, then the reading.

### Scene 1 — The consultation (chat)

1. **Arrival & concern.** The client presents themselves and, through a **choice-driven back-and-forth
   conversation**, states what they came in about — a worry, a decision, a question about their future
   ("Should I take the job?", "Is he cheating?", "Will my mother be okay?"). This is their
   *presenting concern*; it may or may not be their real need (see
   [`clients-and-narrative.md`](./clients-and-narrative.md)). Tone and character live here.
2. **Into the reading.** When the consultation is done, the visit moves into the reading — a separate
   scene (a dim modal overlay or a transition to the reading table; see
   [`art-direction.md`](./art-direction.md)).

### Scene 2 — The reading

3. **Perform the reading, step by step.** In this dedicated scene the method is *performed* as a
   pseudo-puzzle: randomized features are revealed progressively (cards turn, palm lines are
   identified, chart placements resolve), and **at each step the player makes an interpretation
   choice** — applying the method's fixed meanings in one valid direction toward this client. See
   [`divination-methods.md`](./divination-methods.md).
4. **Aggregate & deliver.** The per-step interpretation choices are **aggregated into a single final
   outcome / advice**, delivered to the client. Their in-the-moment reaction plays out now;
   longer-term consequences are recorded and revealed on later days.

> **Requirement:** the reading must expose *both* a "did I read it faithfully / by the book" decision
> (accuracy → the Score) and a "which valid direction did I steer it" decision (→ the Story). A turn
> that only tests one axis undercuts the core tension.

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
