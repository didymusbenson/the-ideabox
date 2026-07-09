# Divination Methods — the shared reading framework

Divination methods are the core verb of the game. This document defines what is **common to every
method**: how a reading is structured, how randomness and rules and player choice fit together, and
the contract each method must fulfill. The specifics of each method live in its own doc under
[`methods/`](./methods/) — tarot, in particular, gets a full treatment of its own.

This file deliberately avoids UI, controls, and exact rulesets — those are DESIGN work and per-method
detail.

## A reading is its own scene

A client visit unfolds as **three beats** (see [`core-loop.md`](./core-loop.md)):

1. **Intake** — the client states their intention and question (short; enough to know the concern).
2. **The reading** — a **separate scene** where the divination is performed and interpretations are
   committed. It pulls focus, either as a dim-background modal overlay or a full transition to a
   reading table (presentation is an open question; see [`art-direction.md`](./art-direction.md)).
3. **Consultation** — the visit returns to the two-hander and plays out *from the reading*: the player
   delivers it and the client reacts.

The reading comes **before** the full consultation — commit, then sell — but because the client opens
with a question, the reading is informed, not blind.

## A reading is a step-by-step pseudo-puzzle

Inside the reading scene, the method is *performed*, not selected from a list:

- The reading proceeds in **steps**, with features revealed **progressively** — cards turn one at a
  time, palm lines are identified in sequence, chart placements resolve in order.
- Getting the *procedure* right has a **technical, pseudo-puzzle quality** — the reading has to be
  conducted correctly for it to hold together.
- **At each step the player interprets the revealed feature** — reading it correctly, or misreading
  it. This is the "doing it right" / accuracy layer; *applying* those interpretations to the client
  happens afterward, in the consultation.

## The core model: random draw · read it right · apply it

This is the mechanism that makes readings work — layers kept separate, and **split across the two
beats** of a visit:

1. **The draw is random.** Which cards come up is randomized per reading, **not authored per client.**
   (Hard requirement; see below.)
2. **Read it right — the reading beat.** Each card has a canonical meaning — *The Tower* = sudden
   upheaval. This is **"the book."** In the reading, the player interprets each card correctly (or
   misreads it); doing it right is the **Score** (see [`scoring-and-story.md`](./scoring-and-story.md)).
   Correct interpretations **lock in** as *reading items.*
3. **Apply it — the consultation beat.** A locked interpretation can be applied to the client in more
   than one faithful direction. In the consultation the player does this through dialog whose choices
   are **flavored with color-coded keywords mapping to the reading items.** How the player applies them
   is where the **Story** branches.

**Aggregation.** The reading's correctness aggregates into the accuracy score; the consultation's
applications aggregate into the outcome that feeds the client's story.

### How the MVP realizes this (authored option pools)

For the MVP this is concrete and authored per encounter:

- **In the reading**, each card offers **interpretation options** — the faithful read plus
  **distractors** (plausible misreadings that cost the Score). The player picks; correct picks lock in
  as reading items.
- **In the consultation**, authored dialog options are **flavored with color-coded keywords that map
  to those reading items**, and applying them toward the client's need is the Story choice.

Full detail lives in [`methods/tarot.md`](./methods/tarot.md). A model-generated alternative (an SLM
producing options on the fly) is a **post-MVP scaling path**, not the MVP.

### The two-valid-interpretations principle

A single interpretation, once locked, can be **applied in more than one faithful direction** — and
that application happens in the consultation.

> *The Tower* reads as unexpected upheaval (getting that right is the reading). Applying it, the player
> can frame it as **"a disaster to brace against"** or **"a necessary collapse that clears the way"** —
> both faithful, opposite advice.

The Score cares whether you *read* it right; the Story cares how you *apply* it.

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
| Tarot | [`methods/tarot.md`](./methods/tarot.md) | Sequential interpretation of drawn cards | **MVP — the focus method** |
| Palm reading | [`methods/palmistry.md`](./methods/palmistry.md) | Close observation of a fixed subject | Post-MVP (deferred) |
| Astrology / star charts | [`methods/astrology.md`](./methods/astrology.md) | Synthesis of a structured chart | Post-MVP (deferred) |

Backlog "possibly others" (tea leaves, numerology, runes, scrying, pendulum) remain unconfirmed; each
would need the full contract above before it's in scope.

## MVP scope for methods

**The MVP ships Tarot and only Tarot.** Prove the reading loop is fun with one well-built method
before adding others. Palmistry and astrology are deferred (their docs are skeletons), and the
model-generated (SLM) option approach is a post-MVP scaling path. See
[`methods/tarot.md`](./methods/tarot.md).
