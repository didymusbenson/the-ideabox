# Core Loop

The game is structured as a series of **days**. Each day is a **session** of client appointments.
There are two nested loops: the **client loop** (one reading) and the **day loop** (a set of
clients plus an end-of-day reckoning).

## The client loop

For each client who sits down at the table:

1. **Arrival & concern.** The client presents themselves and states what they came in about — a
   worry, a decision, a question about their future ("Should I take the job?", "Is he cheating?",
   "Will my mother be okay?"). This is their *presenting concern*. It may or may not be their real
   need (see [`clients-and-narrative.md`](./clients-and-narrative.md)).
2. **Choose / perform the method.** A divination method is used — some clients or scenarios call
   for a specific one; sometimes the player chooses. The player then *performs* that method: reads
   the hand, deals and reads the spread, draws the chart. This is the mechanical heart of a turn.
   See [`divination-methods.md`](./divination-methods.md).
3. **Interpret by the rules.** The player draws conclusions from what the method produced, using
   that method's ruleset. There is a method-correct interpretation; the player can hit it, miss it,
   or knowingly depart from it.
4. **Construct the advice.** The player turns the interpretation into guidance aimed at *this
   client's* concern. This is where the two axes split: the player can deliver the reading the
   method calls for, or shade the advice toward what the person actually needs to hear.
5. **Deliver & react.** The advice is given. The client responds in the moment. Consequences that
   play out over days are recorded but not necessarily revealed yet.

> **Requirement:** every client turn must expose *both* a "did I read it correctly" decision and a
> "what do I actually tell them" decision. A turn that only tests one axis undercuts the core
> tension.

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
