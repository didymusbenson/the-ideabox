# Core Loop

The game is structured as a series of **days**. Each day is a **session** of client appointments.
There are two nested loops: the **client loop** (one reading) and the **day loop** (a set of
clients plus an end-of-day reckoning).

## The client loop

Each client visit is a **hand-authored deduction puzzle** played across **two beats**: the
consultation, then the reading. See [`reading.md`](./reading.md) for the reading model and
[`instruments/`](./instruments/) for the toolkit.

### Beat 1 — The consultation (the interview)

1. **Interview and inspect, at your own pace.** The client sits down and states their **intention**,
   their **question** ("Should I take the job?", "Is he cheating?"), and **what they want read**. This
   beat is **evidence-gathering**: the player picks up and **explores** the interactable **ID / wallet**
   and reads the client's **appearance** (see [`instruments/identity.md`](./instruments/identity.md) and
   [`instruments/observation.md`](./instruments/observation.md)). Their stated concern is their
   *presenting concern*; it may or may not be their real need (see
   [`clients-and-narrative.md`](./clients-and-narrative.md)). The player takes as long as they want here
   — no suggestibility pressure yet — and ends the beat by saying **"let's get started."**

### Beat 2 — The reading (solve, then say it)

2. **Consult the instruments and advise — against a draining meter.** In a dedicated scene (a dim
   overlay or a transition to the reading table; see [`art-direction.md`](./art-direction.md)), the
   client's **predetermined tarot spread** is laid out. The player **consults their instruments** — the
   tarot book, the star-chart calendar, palmistry, and the evidence gathered in the interview — to work
   out the correct reading, and **chooses dialog** to deliver it. Dialog choices carry **color-coded
   keywords** mapping to fortune facts. Solving and advising interleave: you consult devices as you
   decide what to say. See [`instruments/tarot.md`](./instruments/tarot.md).
   - **This beat runs against a live [suggestibility](./reading.md#suggestibility--the-grift-meter)
     meter** — the mark's belief. Noticed errors (saying something they know is wrong, misreading
     something familiar, or using a **method they reject**) and time spent flipping through the books
     both drain it; if it hits zero the client **walks out dissatisfied** (the per-visit fail state).
     Progress is read off the **client's own reactions** — their sprite shifts as belief rises or falls
     (see [`art-direction.md`](./art-direction.md)).

> **The two axes, in the dialog choices:** saying what the instruments actually support (**alignment**)
> earns satisfaction — the accuracy axis, the Score. Knowingly saying what the client *needs* instead
> (**deliberate misalignment**) costs satisfaction but can steer their story — the Story axis. Getting
> the deduction *wrong* also misaligns, but helps no one. See
> [`scoring-and-story.md`](./scoring-and-story.md).

## The day loop

A day is a curated set of client turns:

- **Composition.** Each day mixes **one-off clients** (self-contained appearances) with **arc
  clients** (recurring characters whose storylines span the game). The mix is authored, not random.
- **Progression within the day.** Clients are seen in sequence. Earlier readings may color later
  ones (mood, fatigue, information the player has picked up) — the extent of this is an open
  question, but the day is a deliberately shaped sequence, not an unordered list.
- **End-of-day scorecard.** When the day ends, the player receives a **scorecard** summarizing the
  readings they gave and how well they **aligned with the methodology** — i.e. their clients'
  satisfaction. This is the Score axis surfaced. See [`scoring-and-story.md`](./scoring-and-story.md).
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

- A **deduction challenge** (solve the client's puzzle from the instruments) — the Score.
- A **human choice** (say what's accurate, or what they need) — the Story.
- **Legible feedback** — per visit and at end of day for alignment/satisfaction; over subsequent days
  for narrative outcome.
- **Memory** — recurring clients must reflect what the player told them before.
