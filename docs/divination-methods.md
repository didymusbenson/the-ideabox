# Divination Methods — the shared reading framework

Divination methods are the core verb of the game. This document defines what is **common to every
method**: how a reading is structured, how randomness and rules and player choice fit together, and
the contract each method must fulfill. The specifics of each method live in its own doc under
[`methods/`](./methods/) — tarot, in particular, gets a full treatment of its own.

This file deliberately avoids UI, controls, and exact rulesets — those are DESIGN work and per-method
detail.

## A reading is its own scene

A client visit unfolds as **two scenes** (see [`core-loop.md`](./core-loop.md)):

1. **The consultation** — a choice-driven back-and-forth chat where the player draws out the client's
   concern (and hints of their true need).
2. **The reading** — a **separate scene** where the divination is actually performed. It pulls focus,
   either as a dim-background modal overlay or a full transition to a reading table (presentation is
   an open question; see [`art-direction.md`](./art-direction.md)).

## A reading is a step-by-step pseudo-puzzle

Inside the reading scene, the method is *performed*, not selected from a list:

- The reading proceeds in **steps**, with features revealed **progressively** — cards turn one at a
  time, palm lines are identified in sequence, chart placements resolve in order.
- Getting the *procedure* right has a **technical, pseudo-puzzle quality** — the reading has to be
  conducted correctly for it to hold together.
- **At each step the player makes an interpretation choice** about what the revealed feature means
  for *this* client.

## The core model: random draw · fixed meaning · chosen direction

This is the mechanism that makes readings work. Three layers, kept separate:

1. **The draw is random.** Which cards come up, which features are salient — randomized per reading,
   **not authored per client.** (Hard requirement; see below.)
2. **Meanings are fixed rules.** Each card or feature has a canonical core meaning — *The Tower*
   always means sudden upheaval, chaos, revelation. This is **"the book,"** and reading it faithfully
   is the **Score** (see [`scoring-and-story.md`](./scoring-and-story.md)).
3. **The player chooses the direction.** A fixed meaning can be validly applied in more than one
   direction for this client. The player picks which. This is where the **Story** branches.

**The reading aggregates.** The player's per-step interpretation choices sum into a single final
outcome / piece of advice, and *that* is what feeds the client's story.

### The two-valid-interpretations principle

A single feature often supports **multiple correct interpretations that diverge in story impact.**

> *The Tower* means unexpected upheaval. The player can frame that as **"a disaster to brace
> against"** or **"a necessary collapse that clears the way."** Both are faithful to the card — both
> are *by the book*. They send the client in opposite directions.

The Score doesn't care which faithful direction you chose; the Story cares a great deal.

## Hard requirement: readings are NOT scripted

- Readings must be **randomized**, never pre-written per client. **If a player can look up "this
  client → these cards → this answer," the game does not work.**
- The consequence — and a genuine open design problem — is that story impact must hang on the
  player's **interpretation choices and their aggregate direction**, *not* on which specific random
  features appeared. Different draws must be able to route into the same authored story branches.
- This raises real questions (how to constrain randomness so a draw is never incoherent for a client
  without secretly scripting it; how the aggregate stance maps to branches). Tracked in
  [`open-questions.md`](./open-questions.md) and worked per method in [`methods/`](./methods/).

## The contract every method must fulfill

Each method's own doc must define all of these:

1. **Subject** — the concrete thing examined (a hand and its lines, a dealt spread, a drawn chart).
2. **Fixed meanings ("the book")** — the canonical meaning of each feature; the standard the Score is
   judged against.
3. **Step reveal + interpretation choices** — how features are revealed in sequence and what
   interpretive choices the player makes at each step.
4. **Aggregation into advice** — how the per-step choices combine into the final outcome that feeds
   the client's story.
5. **Correctness check** — how "did the player read it faithfully" is evaluated (the Score input).
   Note: whether the *chosen direction* was good for the client is a Story judgment, handled
   separately.

## The methods

| Method | Doc | Character | Status |
|--------|-----|-----------|--------|
| Tarot | [`methods/tarot.md`](./methods/tarot.md) | Sequential interpretation of drawn cards | First fleshed-out method |
| Palm reading | [`methods/palmistry.md`](./methods/palmistry.md) | Close observation of a fixed subject | Stub — to be detailed |
| Astrology / star charts | [`methods/astrology.md`](./methods/astrology.md) | Synthesis of a structured chart | Stub — to be detailed |

Backlog "possibly others" (tea leaves, numerology, runes, scrying, pendulum) remain unconfirmed; each
would need the full contract above before it's in scope.

## First-slice scope for methods

A first slice does **not** need every method. Proposed: implement **one or two** fully and well —
tarot is the lead candidate (its own doc is the most developed), optionally paired with palm reading
as a contrasting "observe a fixed subject" method. Confirm in [`open-questions.md`](./open-questions.md).
