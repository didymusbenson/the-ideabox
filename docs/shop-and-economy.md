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
   the reading** — e.g. peeking at or rigging the predetermined spread, a cheat-sheet that reveals a
   client's correct read, or a tool that manufactures a tell — bending the puzzle rather than just
   what he says about it.

## Satisfaction is now the core Score

Since the reading overhaul, **client satisfaction is the per-visit expression of the Score** — it
comes from **alignment** between the player's advice and the correct reading (see
[`reading.md`](./reading.md) and [`scoring-and-story.md`](./scoring-and-story.md)). So the money layer
plugs into an axis that already exists rather than introducing a new one:

- **Solve + align** → satisfied client → (plausibly) better pay.
- **Misalign** — by error or on purpose — → less satisfied → less pay.

That makes the money layer a **pressure on the Score/Story choice**: helping a client by deliberately
misaligning now has a visible cost in coin, not just in the scorecard.

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
  - *Capability* — unlock new instruments or deeper reads.
  - *Fudging* — bend or pre-arrange divination results (the loaded one; see guardrail above).

## Open questions specific to this feature

- **Does payment scale with satisfaction (alignment), and how steeply?** Satisfaction *is* the Score
  now (see above) — so what exactly turns a visit into money, and how hard does deliberate misalignment
  hit the wallet?
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
- [`reading.md`](./reading.md) / [`instruments/`](./instruments/) — define what "fudging" actually
  means per instrument (rigging the spread, revealing the read, faking a tell).
- [`open-questions.md`](./open-questions.md) — promote the cross-cutting questions above once they're
  real decisions.
