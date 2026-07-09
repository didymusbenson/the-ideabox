# Divination Methods

Each divination method is a **self-contained mini-mechanic**: a system the player performs and can
get right or wrong. Methods are the core verb of the game. This document captures what every method
must provide and sketches the specific methods; it deliberately avoids UI, controls, and exact
rulesets — those are DESIGN work.

## What every method must provide

Any divination method added to the game must define all five of these:

1. **A subject to examine.** The concrete thing the player looks at or manipulates — a client's
   hand and its lines, a dealt tarot spread, a drawn star chart. This is the method's input surface.
2. **A ruleset.** The canonical meanings the game treats as *correct*: what a given line, card, or
   placement signifies. This is the "book" the Score is measured against.
3. **An interpretation step.** The player reads the subject against the ruleset and draws
   conclusions. There is a method-correct reading; the player can reach it, miss it, or deviate.
4. **An advice-construction step.** The player turns the interpretation into guidance for the
   client's specific concern. This is the hinge where the Story can diverge from the Score.
5. **A correctness check.** A way to evaluate whether the interpretation followed the method's rules
   — the input to the accuracy score. (Whether advice is "correct" is a *narrative* judgment handled
   separately; see [`scoring-and-story.md`](./scoring-and-story.md).)

> **Requirement:** methods must be genuinely *performed*, not selected from a list of pre-written
> outcomes. The player should feel they are reading, not picking.

## Design intent across methods

- **Distinct feel.** Each method should play differently — palmistry is close observation of a
  fixed subject; tarot is sequential interpretation of what comes up; astrology is synthesizing a
  structured chart. Variety keeps the loop fresh across days.
- **Learnable rules.** A player should be able to internalize a method's rulebook over a few
  readings and feel their competence grow. Mastery of the "book" is what makes the Score axis
  meaningful.
- **Shared advice layer.** However different the reading, all methods funnel into the same
  advice-construction step, so the Score-vs-Story choice is consistent regardless of method.

## The methods

### Palm reading (palmistry)
- **Subject:** the client's hand — the major lines (heart, head, life, fate), their length, depth,
  breaks, and intersections.
- **Play:** close observation of a mostly-fixed subject. The player inspects features, applies
  palmistry rules (e.g., what a long/short/broken line is said to mean), and assembles a reading.
- **Character:** the "detective" method — scrutinize, measure, conclude.

### Tarot
- **Subject:** cards as they are drawn into a spread, each position carrying its own significance.
- **Play:** sequential interpretation — read each card in its position, then synthesize the spread
  into a narrative. Some randomness in what comes up; skill is in interpreting it correctly.
- **Character:** the "storyteller" method — meaning emerges card by card.

### Astrology / star charts
- **Subject:** a chart derived from the client (e.g., signs, houses, placements).
- **Play:** synthesize a structured, multi-part chart into a coherent reading. More systemic and
  combinatorial than the others.
- **Character:** the "systems" method — many parts that must be read together.

### Backlog — "possibly others"
Candidates noted in the pitch as possible additional methods. Not committed; parked for now:
tea-leaf reading (tasseography), numerology, rune casting, scrying / crystal ball, pendulum reading.
Each would need the full five-part definition above before it's in scope.

## POC scope for methods

> **Assumption — to be confirmed** (see [`open-questions.md`](./open-questions.md)).

A vertical slice does **not** need every method. Proposed: implement **one or two** methods fully
and well (palm reading and/or tarot are the strongest first candidates — one "observe a fixed
subject" method and one "interpret what comes up" method) rather than many shallowly. Additional
methods are added once the loop is proven.
