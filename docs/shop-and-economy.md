# Shop & Economy (WORK IN PROGRESS — isolated)

> **Status: EXPLORATORY.** This feature is not fully worked out. It is kept in its own document on
> purpose so it can evolve (or be cut) without disturbing the core requirements. Do not treat
> anything here as settled, and do not wire it deeply into the other docs yet — the touchpoints
> below are noted as open questions, not committed integrations.

## The idea

Clients are paying customers. Running the psychic business has a money layer:

1. **Clients pay for readings.** A visit produces income.
2. **Satisfaction affects the visit.** How happy the client is with their reading factors into that
   visit's outcome/score (and plausibly into what they pay or whether they return).
3. **Money is spent between days.** Earnings accumulate across a day and can be spent in a
   between-days **shop** on **upgrades**.
4. **Some upgrades let the player cheat.** Notably, upgrades exist that let the protagonist **fudge
   the results of a fortune-telling** — bending what the method produces rather than what he says
   about it.

## New concept this introduces: the visit score

This adds a **per-visit** measure of client satisfaction that is separate from the existing
end-of-day method-accuracy scorecard (the "Score" in [`scoring-and-story.md`](./scoring-and-story.md)).

- **Method accuracy** = did you read it by the book. Judged at end of day.
- **Client satisfaction** = did the client feel good about their visit. Judged per visit.

These are not the same thing, and that's interesting: a method-accurate reading can leave a client
miserable, and a satisfying visit can be method-nonsense. How satisfaction relates to the two
existing axes is an **open question** (see below), not yet resolved.

## The "fudge" upgrades — why they matter

Upgrades that let the player fudge a fortune are the most design-significant part of this feature,
because they reach straight into the core tension:

- Fudging is a way to **buy your way out of the Score-vs-Story dilemma** — make the method "produce"
  the result you want so the reading you *need* to give is also the reading the book appears to call
  for.
- This should have a **cost or risk**, or it trivializes the central choice. What that cost is
  (money, a chance of being caught, a narrative/karma consequence, degraded satisfaction if
  detected) is undecided.

> **Design guardrail:** the shop must not accidentally dissolve the Score/Story tension. If money +
> fudging lets the player always have it both ways for free, the heart of the game is gone. Fudging
> should be a *tempting, costly* option, not a clean solution.

## Rough shape (all placeholder, all revisable)

- **Earn:** each visit yields money, likely modulated by client satisfaction.
- **Bank:** money carries across days.
- **Spend:** a between-days shop offers upgrades.
- **Upgrade categories (candidates, not committed):**
  - *Quality-of-life* — things that make readings easier, clearer, or faster.
  - *Capability* — unlock new methods or deeper reads.
  - *Fudging* — bend or pre-arrange divination results (the loaded one; see guardrail above).

## Open questions specific to this feature

- **Satisfaction vs. the two axes.** Is satisfaction a third independent axis, an input to the
  Score, an input to the Story, or its own thing entirely? How does it relate to giving a client the
  method-correct reading vs. what they need to hear?
- **Does payment scale with satisfaction, accuracy, both, or neither?** What exactly turns a visit
  into money?
- **What can the player *do* about a poor payer** — nothing, or does money pressure push them toward
  crowd-pleasing (or fudging)?
- **Fudging cost/risk model.** What makes fudging a real trade-off rather than a free win? Money
  cost, detection risk, satisfaction penalty if caught, narrative consequence?
- **Is money a soft flavor layer or a real pressure?** Can the player go broke? Does the business
  itself have stakes (rent, staying open), or is money purely an upgrade currency?
- **Shop scope for the first slice.** Does the first slice need the shop at all, or is it a
  post-slice addition? (Given its WIP status, likely *out* of the first slice — confirm.)

## Touchpoints to reconcile later (kept out of the other docs for now)

When this feature firms up, these are the docs it will need to reach into:

- [`scoring-and-story.md`](./scoring-and-story.md) — introduce satisfaction and reconcile it with the
  two axes; account for fudging's effect on the Score.
- [`core-loop.md`](./core-loop.md) — add "client pays" to the client loop and a "between-days shop"
  step to the day loop.
- [`divination-methods.md`](./divination-methods.md) — define what "fudging" a method's result
  actually means per method.
- [`open-questions.md`](./open-questions.md) — promote the cross-cutting questions above once they're
  real decisions.
