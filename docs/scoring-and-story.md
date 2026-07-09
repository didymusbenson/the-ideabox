# Scoring & Story — the two axes

This is the mechanic the whole game is built to produce. There are **two independent measures of
how well the player is doing**, they are judged by different standards, and they routinely conflict.

## Axis 1 — The Score (craft / accuracy)

- **What it measures:** how correctly the player performed the divination *by the book* — did they
  read the method's subject accurately and give the interpretation the method's rules call for.
- **How it's judged:** against each method's ruleset (the "correctness check" in
  [`divination-methods.md`](./divination-methods.md)). Objective and rules-based.
- **When it's surfaced:** primarily at the **end-of-day scorecard** (see
  [`core-loop.md`](./core-loop.md)).
- **A perfect rating** comes from following the psychic rules by the book — every reading
  method-accurate, no shading, no bending.

## Axis 2 — The Story (outcome / humanity)

- **What it measures:** whether the player's advice actually *helped the person* — moved arc clients
  toward happy endings and, ideally, toward not needing the psychic anymore.
- **How it's judged:** by narrative consequence over time — how clients' lives go, revealed across
  subsequent days (see [`clients-and-narrative.md`](./clients-and-narrative.md)). Subjective and
  human, not rules-based.
- **When it's surfaced:** gradually, through returning clients and their changed situations, and in
  endings.

## Why they conflict

The method-correct reading and the genuinely-helpful advice are **not always the same thing.**

- The cards may call for a grim, "accurate" verdict that would crush a client who needs hope.
- The by-the-book palm reading might tell someone to stay the course when what they need is
  permission to leave.
- Telling a client exactly what the method dictates can keep them dependent; telling them what they
  need can cost you accuracy points but set them free.

Crucially, the split shows up *within a faithful reading*, not only when the player breaks the rules.
A single feature usually supports **more than one by-the-book interpretation** (the
two-valid-interpretations principle in [`divination-methods.md`](./divination-methods.md)): *The
Tower* faithfully means upheaval, but "brace for disaster" and "a necessary collapse" are both
accurate and send the client opposite ways. So the **Score cares whether you read the meaning
faithfully; the Story cares which faithful direction you chose** — and the player is choosing
directions step by step as the reading is performed, then living with the aggregate.

So on any given reading the player faces a real choice:

> **Play it by the book (protect the Score) — or say what this person needs to hear (serve the
> Story)?** — and, even when staying by the book, *which faithful direction* to steer toward.

A run that chases a perfect Score may leave a trail of "accurate" readings that didn't help anyone.
A run that chases good outcomes may be a mess of method-inaccurate readings. The interesting space
is in between, and in deciding — client by client — which one this moment is worth.

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
