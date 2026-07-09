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

### Beat 2 — The reading (separate scene) — *doing it right*

2. **Interpret the spread correctly.** In a dedicated scene (a dim overlay or a transition to the
   reading table; see [`art-direction.md`](./art-direction.md)), the spread is **drawn at random**. As
   each card turns, the player **reads it correctly** — picking the faithful interpretation from
   options that include plausible misreadings — and it **locks in**. Getting these right is the
   **accuracy** axis (the Score). The locked interpretations become the **reading items** the
   consultation is built from. This beat is *only* about reading the cards right. See
   [`methods/tarot.md`](./methods/tarot.md).

### Beat 3 — Consultation (application) — *what it means for them*

3. **Apply the reading through dialog.** The visit returns to the two-hander, and the player advises
   the client through dialog whose choices are **flavored with color-coded keywords that map to
   specific reading items** — the interpretations locked during the reading. *How* those items are
   applied to the client's need — which faithful direction, what advice — is the **Story** axis. The
   outcome feeds the client's story; the in-the-moment reaction lands now, while longer-term
   consequences surface on later days.

> **The two axes split across the two beats:** the reading tests *did I read it right* (accuracy → the
> Score); the consultation tests *how I apply it to this person* (→ the Story). You interpret first,
> then apply what you locked.

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
