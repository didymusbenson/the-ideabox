# Scoring & Story — the two axes

This is the mechanic the whole game is built to produce. There are **two independent measures of
how well the player is doing**, they are judged by different standards, and they routinely conflict.

## Axis 1 — The Score (accuracy / satisfaction)

- **What it measures:** whether the player **solved the client's puzzle and said it straight** — advice
  that *aligns* with what the instruments actually support.
- **How it's judged:** by **alignment** between the chosen dialog and the correct reading derived from
  the instruments (see [`reading.md`](./reading.md)). Solid alignment → a satisfied client. Objective:
  there is a correct reading to hit.
- **When it's surfaced:** per visit as **client satisfaction**, and at the **end-of-day scorecard**
  (see [`core-loop.md`](./core-loop.md)).
- **A perfect rating** comes from correctly cross-referencing the instruments and delivering the
  aligned reading — no misreads, no deliberate shading.
- **Getting it wrong** means the deduction failed: you advise from a mistaken read, the dialog
  misaligns, and the client leaves unsatisfied.

## Axis 2 — The Story (outcome / humanity)

- **What it measures:** whether the player's advice actually *helped the person* — moved arc clients
  toward happy endings and, ideally, toward not needing the psychic anymore.
- **How it's judged:** by narrative consequence over time — how clients' lives go, revealed across
  subsequent days (see [`clients-and-narrative.md`](./clients-and-narrative.md)). Subjective and
  human, not rules-based.
- **When it's surfaced:** gradually, through returning clients and their changed situations, and in
  endings.

## Why they conflict

The **accurate** reading and the **genuinely-helpful** advice are **not always the same thing.**

- The cards may support a grim, accurate verdict that would crush a client who needs hope.
- The instruments might all point to "stay the course" when what the person needs is permission to
  leave.
- Aligning perfectly can keep a client dependent; telling them what they need can cost you their
  satisfaction but set them free.

Both axes live in the **same dialog choices** during the reading. Aligning your advice with the
solved puzzle satisfies the client (Score). **Deliberately misaligning** — saying what they need
instead of what the instruments support — costs satisfaction but can steer their story (Story). This
is the design's central knot: the game rewards you (satisfaction, money, a clean scorecard) for the
*accurate* answer, while the *humane* answer often asks you to throw that reward away.

There is also a third state that keeps the choice honest: **misaligning by mistake.** Get the
deduction wrong and you also leave the client unsatisfied — but you help no one. Only a *knowing*
deviation, made after you've actually solved the puzzle, is a real act of care.

> **Play it straight (satisfy the client, protect the Score) — or say what this person needs to hear
> (serve the Story)?** — knowing that a wrong answer looks the same on the satisfaction meter as a
> kind one.

A run that chases a perfect Score may leave a trail of accurate readings that didn't help anyone. A
run that chases good outcomes may be a mess of dissatisfied clients. The interesting space is in
between, deciding — client by client — which one this moment is worth.

> **Requirement:** the two axes must be **separable and independently legible**. The player has to
> be able to feel "I nailed the reading but it was the wrong thing to say," and vice versa. If a
> single number collapses both, the core tension disappears.

## Open design questions on feedback (not yet decided)

Captured here and in [`open-questions.md`](./open-questions.md):

- **Visibility of the Story axis.** Is narrative outcome shown as an explicit meter/score, or only
  felt through what happens to clients? (Leaning: keep it soft and felt, in contrast to the hard
  Score — but undecided.)
- **Does the player know when the axes diverge?** Are they told "the method says X but they need Y,"
  or must they infer it from the client? The amount of telegraphing changes the whole feel.
- **How the two combine at the end.** Does the game grade you on both separately, force a
  reconciliation, or let the Story quietly override the Score in what the player remembers?
- **Failure states.** What "doing badly" looks like on each axis, and whether either can end a run.

## The takeaway for anyone building this

Every feature should ask: *does this sharpen the choice between the Score and the Story?* Systems
that make the reading feel like real craft strengthen Axis 1. Systems that make clients feel like
real people with futures strengthen Axis 2. The game lives in the collision between them.
