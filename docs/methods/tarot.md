# Method: Tarot

> **Status: IN PROGRESS.** This captures the *shape* of tarot as a playable method. Concrete rules,
> the card set, spread design, and numeric detail are still to be pinned down. It builds on the
> shared framework in [`../divination-methods.md`](../divination-methods.md) — read that first.

## Subject

A **spread**: cards drawn from the deck into positions, where each **position** carries its own
significance (e.g., past / present / future, or a situation / obstacle / outcome layout). The reading
is the synthesis of the drawn cards across their positions.

## The book — fixed card meanings

Each card has a **canonical core meaning** the game treats as correct — *The Tower* = sudden upheaval,
chaos, revelation; *The Hermit* = withdrawal, introspection, guidance; and so on. Reading a card
faithfully to its core meaning is what earns the **Score**. The player learns these meanings from the
in-world **tarot reference book** (see [`../art-direction.md`](../art-direction.md)).

## How a tarot reading plays (step by step)

1. Cards are **drawn at random** into the spread's positions. *Which* cards come up is not authored
   for this client (see the hard non-scripted requirement below).
2. Cards are **turned one at a time.** For each card, the player reads it **in its position** and
   makes an **interpretation choice** — applying the card's fixed meaning in one of its valid
   directions toward the client's concern.
3. Once all cards are turned, the per-card choices are **aggregated** into the reading's overall
   message and the advice delivered to the client.

### Fixed meaning, chosen direction (the Tower example)

*The Tower* faithfully means unexpected upheaval. Interpreting it, the player might steer toward:

- **"Brace for a disaster"** — warn the client, tell them to protect what they have; or
- **"A necessary collapse"** — tell them the upheaval clears the way for something better.

Both are *by the book* (both honor "unexpected upheaval") and score the same on **accuracy**. They
diverge in **story impact**. Multiply this across every card in the spread, and the *aggregate
direction* the player took becomes the reading's real message.

## Scoring vs. story in tarot

- **Score (accuracy):** did the player apply each card's canonical meaning faithfully — regardless of
  which valid direction they chose? Misreading a card (giving it a meaning it doesn't hold) is
  inaccurate.
- **Story (outcome):** which valid *directions* did the player choose, and did their aggregate steer
  the client toward a good outcome? This is judged narratively, over time.

## Hard requirement: non-scripted

The draw must be **random**, never pre-arranged per client. A player must not be able to look up "this
client draws these cards → say this." The authored part is the **set of story directions the reading
can take**, keyed to the player's interpretive stance — not to specific cards.

## Open questions specific to tarot

- **Reversed cards?** Are cards read upright-only, or do reversals add a second meaning layer?
- **Spread design.** Size and shape — fixed spread, or does the player/scenario choose? How do
  positions modify a card's meaning?
- **How many valid directions per card,** and are they authored per card or derived from a small set
  of interpretive axes (e.g., hopeful↔ominous, act↔wait)?
- **Aggregation rule.** How do per-card directional choices combine into one outcome, and how does
  that outcome map onto the client's authored story branches?
- **Constraining randomness without scripting.** Can a fully random draw be incoherent or tonally
  wrong for a client's concern? If we weight/limit the deck to keep readings coherent, how do we do
  that without re-introducing look-up-ability?
- **The "fudge" hook.** If the [shop](../shop-and-economy.md) ships, tarot is a prime place for
  result-fudging upgrades (arranging the draw) — costs/risks TBD there.
