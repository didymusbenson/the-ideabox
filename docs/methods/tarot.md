# Method: Tarot — the MVP

> **Status: MVP — the focus method.** Tarot is the *only* divination method in the MVP; palmistry and
> astrology are deferred. This is the most detailed method doc, and the reading model defined here is
> the reference other methods will adapt later. Builds on the shared framework in
> [`../divination-methods.md`](../divination-methods.md) — read that first.

## Where tarot sits in the visit

The visit is three beats (see [`../core-loop.md`](../core-loop.md)): **intake → reading →
consultation.** The client arrives with a stated **intention and question**, *then* the reading is
performed, *then* the consultation plays out from what was drawn. So the reading is informed by the
question but committed *before* the deeper conversation — you draw, you lock, then you sell it.

## Subject

A **spread**: cards drawn from the deck into positions, each **position** carrying its own
significance (e.g. past / present / future, or situation / obstacle / outcome). The reading is the
synthesis of the drawn cards across their positions.

## The book — simplified card meanings

Each card is assigned a **simplified meaning token** the game treats as canonical — *The Tower* →
**"Big Change"**, *The Hermit* → **"Withdraw / Reflect"**, and so on. This keeps the "book" legible
and learnable, and it's the vocabulary everything else keys off. Reading a card faithfully to its
meaning token is what earns the **Score**. The player learns these from the in-world tarot reference
book (see [`../art-direction.md`](../art-direction.md)).

## The model: authored interpretation options per encounter

This is the decided MVP approach (authored, not model-generated — see "Scaling" below).

- For a given **encounter**, the writer authors — keyed to the client's stated question — a set of
  **interpretation options** for the meaning tokens that can come up. *At minimum, each encounter
  defines what the options ARE.*
- Each option is a line of dialog the player can deliver, tagged with two things:
  - **faithful or distractor** — does it actually match the drawn card's meaning? (→ the **Score**)
  - **story direction** — which way it steers the client. (→ the **Story**)

So an encounter is, in essence, a table: *meaning token → a few interpretation options, each tagged.*

### How a reading plays (step by step)

1. Cards are **drawn at random** into the spread. *Which* cards come up is not authored for this
   client.
2. Cards **turn one at a time.** For each card, the game looks up its meaning token and surfaces this
   encounter's authored options for that token. The player **picks one, and it locks in** — no
   take-backs. Then the next card.
3. When the spread is done, the locked choices **aggregate** into the reading's overall message,
   which the player then delivers in the consultation, and which feeds the client's story.

### Fixed meaning, chosen direction (the Tower example)

*The Tower* = "Big Change." For a client asking about their marriage, this encounter might author:

- **"This is the end — brace yourself."** *(faithful · ominous direction)*
- **"An old thing is breaking so a better one can grow."** *(faithful · hopeful direction)*
- **"The cards say nothing will change."** *(distractor — this misreads 'Big Change')*

The first two are both *by the book* (both honor "Big Change") and score the same on **accuracy**;
they send the client opposite ways (**Story**). The third is a trap that costs accuracy.

## Where the Score lives: distractors

Because the player is handed options, accuracy would evaporate if every option were faithful — there
would be no wrong answer. So each card's option set includes **distractors**: plausible-looking
*misreadings* of the drawn card. Picking faithful options protects the Score; the player has to
actually know the book to tell faithful from distractor. (The ratio and how obvious distractors are is
an open tuning question.)

## Coverage: keeping random draws authorable

A random draw over the full deck means an encounter could surface a meaning token the writer didn't
tailor for. Two levers keep authoring tractable without breaking randomness:

- **A small deck / vocabulary** — fewer meaning tokens to author per encounter.
- **Generic fallback options** — for tokens an encounter didn't specifically author, fall back to
  generic faithful/distractor options for that meaning. Off-topic cards still read coherently; only
  the *story-bearing* tokens need bespoke authoring.

Exact deck size, vocabulary size, and how much is bespoke vs. fallback are open tuning questions.

## Hard requirement: non-scripted

The draw must be **random**, never pre-arranged per client. A player must not be able to look up "this
client draws these cards → say this." The authored part is the *option pool keyed to the question and
the card meanings* — not a fixed card sequence.

## Aggregation → outcome → story

The locked choices sum along two lines:

- **Accuracy** — how many faithful vs. distractor picks (→ the Score / scorecard).
- **Story direction** — the aggregate lean of the faithful picks (ominous ↔ hopeful, act ↔ wait,
  etc.) selects which authored **story outcome** the client walks away with, feeding their arc.

How exactly the aggregate maps onto authored story branches is an open question.

## Scaling (post-MVP, not now): SLM-generated options

The authoring cost of bespoke options is the main drawback of the authored model. Post-MVP, a **small
language model** could generate interpretation options from the drawn card + the client's question,
removing that cost and scaling to any card/client. It's explicitly **out of the MVP** — we prove the
loop is fun with authored options first, then consider the model as a scaling path. Tracked in
[`../open-questions.md`](../open-questions.md).

## Open questions specific to tarot

- **Deck & vocabulary size** vs. authoring cost per encounter.
- **Distractor design** — how many per card, and how obvious/subtle they are.
- **Spread design** — size and shape; fixed, or chosen by player/scenario? How do positions modify a
  card's meaning token?
- **Reversed cards?** A second meaning layer, or upright-only for the MVP?
- **Aggregation rule** — how locked choices map onto authored story branches.
- **Consultation-after agency** — how much choice the delivery beat has vs. just playing out the
  locked reading.
- **Fallback coherence** — keeping generic fallback options from feeling generic.
- **The "fudge" hook** — if the [shop](../shop-and-economy.md) ships, arranging the draw is the
  obvious tarot cheat; costs/risks TBD there.
