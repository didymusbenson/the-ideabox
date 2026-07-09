# Vision

## The fantasy

You run a small psychic parlor. People come to you at the worst and most uncertain moments of
their lives — a shaky marriage, a job that's going nowhere, grief they can't put down — and they
want you to tell them what happens next. You perform the ritual: you take the hand, you deal the
cards, you draw the chart. You read it "correctly." You deliver the verdict.

You don't believe in any of it. Not for a second. But you are good at it, because the *methods*
are consistent and the *people* are legible, and somewhere in the theater of it you realize you
can actually change how these lives go — not with magic, but with the words you choose to attach
to the magic.

The player is a **skeptic who is nonetheless in the business of belief.** That contradiction is
the character.

## Tone

- **Dry, dismissive, sarcastic.** The protagonist's inner voice treats divination as obvious
  nonsense and says so — to the player, if not always to the client's face.
- **Warm underneath.** The comedy of disbelief sits on top of genuine stakes. These are real
  people with real problems; the game is not cynical *about them*, only about the mysticism.
- **Deadpan, not zany.** Think a tired professional who has seen every kind of desperation and
  has a wry comment for each.

## Design pillars

Everything in the game should serve at least one of these. If a feature serves none, cut it.

1. **Divination is a real mechanic, not a cutscene.** Each method is a distinct, learnable
   system with its own rules the player performs and can get right or wrong. Reading is *play*,
   not a menu of pre-written outcomes.
2. **The Skeptic's Voice.** The protagonist's disbelief is ever-present and is the primary source
   of humor and character. The player is always in on the joke that this is theater.
3. **Rules vs. Compassion.** The Score (do the method correctly) and the Story (help the person)
   are separate, and they conflict. The player is constantly deciding which one to serve.
4. **People, not prophecies.** Clients are the point. Their arcs, their memory of what you told
   them, and their eventual happy (or unhappy) endings are what the player is really playing for.

## What this POC is trying to prove

**The proof of concept is about the *workflow*, not the game.** The thing being validated is
whether we can take a game from a blank repository to something real **from scratch using Claude
Code** — planning docs-first, then designing and building on top of them. The game
("I'm Not a Psychic") is the **vehicle** for that experiment, not the deliverable.

What this means for how we work:

- **The real success criterion is the process:** does a docs-first, phase-by-phase workflow
  (PLANNING → DESIGN → IMPLEMENTATION) with Claude Code actually carry a from-scratch game project
  forward coherently? Are the requirements legible enough to design from? Does each phase build
  cleanly on the last?
- **The game only has to be coherent enough to be an honest test.** It does *not* need to be
  independently validated as "fun." It needs to be real enough — real mechanics, real clients, real
  choices — that building it exercises the workflow the way a genuine project would. A toy that's too
  thin wouldn't prove anything about the workflow; that's why the game design is taken seriously.
- **Artifacts are part of the proof.** These docs, and how well they hold up as the source of truth
  across sessions and phases, are themselves evidence about whether the workflow works.

So when weighing a game-design decision, the tie-breaker is usually: *which choice makes this a
better test of building-from-scratch-with-Claude-Code?* — often that means enough depth to be
representative, without gold-plating the game itself.

## Touchstones (illustrative, not prescriptive)

- **Strange Horticulture** — running an occult shop, identifying things by a rulebook, serving
  customers whose stories are affected by your choices. The closest structural cousin.
- **Papers, Please** — a repeated rules-based judgment loop that accumulates moral weight; the
  procedure *is* the game, and bending the rules has human cost.
- **Reigns / choice-driven narrative games** — advice as branching consequence over time.

These are reference points for feel and structure only. They do not dictate scope, art, or tech.
