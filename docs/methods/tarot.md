# Method: Tarot — the MVP

> **Status: MVP — the focus method.** Tarot is the *only* divination method in the MVP; palmistry and
> astrology are deferred. This is the most detailed method doc, and the reading model defined here is
> the reference other methods will adapt later. Builds on the shared framework in
> [`../divination-methods.md`](../divination-methods.md) — read that first.

## Where tarot sits in the visit

The visit is three beats (see [`../core-loop.md`](../core-loop.md)): **intake → reading →
consultation.** The client arrives with a stated **intention and question**; *then* the reading is
performed; *then* the consultation plays out.

The two axes split cleanly across the last two beats:

- **The reading = "doing it right."** You interpret the spread correctly. This is the **accuracy**
  axis (the Score).
- **The consultation = applying it.** You take the interpretations you locked and apply them to the
  client through dialog. This is the **Story** axis.

You draw and read first, then sell it — informed by the question, but committed before the deeper
conversation.

## Subject

A **spread**: cards drawn from the deck into positions, each **position** carrying its own
significance (e.g. past / present / future, or situation / obstacle / outcome). The reading is the
synthesis of the drawn cards across their positions.

## The book — simplified card meanings

Each card is assigned a **simplified meaning token** the game treats as canonical — *The Tower* →
**"Big Change"**, *The Hermit* → **"Withdraw / Reflect"**, and so on. This keeps the "book" legible
and learnable. Reading a card faithfully to its meaning token is what earns the **Score**. The player
learns these from the in-world tarot reference book (see [`../art-direction.md`](../art-direction.md)).

## Beat 2 — The reading: read it right, lock it in

The reading is purely about **interpreting correctly** — no application to the client yet.

1. Cards are **drawn at random** into the spread. *Which* cards come up is not authored for this
   client.
2. Cards **turn one at a time.** For each card, the game offers **interpretation options** — the
   faithful read of that card plus **distractors** (plausible misreadings). The player picks, and it
   **locks in** — no take-backs.
3. Picking the faithful read is **"doing it right"** and earns accuracy; picking a distractor costs
   it. Each locked interpretation becomes a **reading item** — the raw material the consultation will
   apply.

### Where the Score lives: distractors

Because the player is handed options, accuracy would evaporate if every option were faithful — there
would be no wrong answer. So each card's option set includes **distractors**: plausible-looking
misreadings of the drawn card. The player has to actually know the book to tell faithful from
distractor. (Ratio and subtlety of distractors is an open tuning question.)

## Beat 3 — The consultation: apply it through color-coded keywords

Now the locked reading items get **applied** to the client. The player advises through dialog whose
choices are **flavored with color-coded keywords that map to specific reading items.** Seeing the
keywords, the player knows which parts of what they're saying are grounded in the cards they actually
drew — the visual bridge between reading and consultation.

*How* a reading item is applied is the Story choice, and this is where the two-valid-interpretations
principle plays out:

> *The Tower* was read (correctly) as **"Big Change"** — that was the reading. In the consultation the
> player can apply that item as:
> - **"Brace yourself — something is ending."** *(faithful application · ominous)*
> - **"An old thing is breaking so a better one can grow."** *(faithful application · hopeful)*
>
> Both faithfully apply "Big Change"; they send the client opposite ways.

**Open lever — grounding.** Whether the player may also say things *not* grounded in their reading
(make things up) — and whether that's penalized or is a valid "lie to help them" move — is an open
design question tying straight into the Score/Story theme.

## Aggregation → outcome → story

- **Accuracy** aggregates from the **reading**: how many faithful vs. distractor picks (→ the Score /
  scorecard).
- **Story** aggregates from the **consultation**: the lean of how reading items were applied (ominous
  ↔ hopeful, act ↔ wait, …) selects which authored **story outcome** the client walks away with.

How exactly the aggregate application maps onto authored story branches is an open question.

## Authoring, and keeping random draws authorable

Authored per encounter (not model-generated — see "Scaling" below):

- **Reading options** per card meaning: the faithful read + distractors.
- **Consultation dialog**: keyword-flavored options that apply the reading items to *this* client's
  question.

A random draw over the full deck could surface a meaning the writer didn't tailor. Two levers keep
authoring tractable without breaking randomness:

- **A small deck / vocabulary** — fewer meaning tokens to author per encounter.
- **Generic fallback options** — for tokens an encounter didn't specifically author, fall back to
  generic reading/consultation options. Off-topic cards still read coherently; only the *story-bearing*
  tokens need bespoke authoring.

## Hard requirement: non-scripted

The draw must be **random**, never pre-arranged per client. A player must not be able to look up "this
client draws these cards → say this." The authored part is the *option pools keyed to the question and
the card meanings* — not a fixed card sequence.

## Scaling (post-MVP, not now): SLM-generated options

The authoring cost of bespoke options is the main drawback of the authored model. Post-MVP, a **small
language model** could generate reading and/or consultation options from the drawn card + the client's
question, removing that cost and scaling to any card/client. It's explicitly **out of the MVP** — prove
the loop is fun with authored options first. Tracked in [`../open-questions.md`](../open-questions.md).

## Open questions specific to tarot

- **Grounding** — may the player apply keywords *not* backed by their reading (make things up)? Penalty,
  or a deliberate lever?
- **Deck & vocabulary size** vs. authoring cost per encounter.
- **Distractor design** — how many per card, and how obvious/subtle.
- **Spread design** — size and shape; fixed, or chosen by player/scenario? How do positions modify a
  card's meaning token?
- **Reversed cards?** A second meaning layer, or upright-only for the MVP?
- **Aggregation rule** — how applied reading items map onto authored story branches.
- **Consultation authoring** — how much keyword dialog per encounter, and how many reading items a
  single consultation typically weaves together.
- **Fallback coherence** — keeping generic fallback options from feeling generic.
- **The "fudge" hook** — if the [shop](../shop-and-economy.md) ships, arranging the draw is the obvious
  tarot cheat; costs/risks TBD there.
