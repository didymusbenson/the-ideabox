# "I'm Not a Psychic" — Documentation

**Working title:** I'm Not a Psychic
**Phase:** PLANNING (requirements). No tech stack or implementation decisions yet — those come in DESIGN.
**Type:** A narrative, choice-based game.
**MVP method:** Tarot only — other divination methods are deferred (see [`methods/`](./methods/)).

## The one-line pitch

You are *not* a psychic — but you run a psychic business. Clients arrive with real
problems; you perform readings (palm, tarot, star charts, and more), interpret them
by the rules of each method, and hand out advice. You don't believe a word of it. They do.

## The central tension (read this first)

The game pulls in two directions at once, and the whole design hangs on the gap between them:

- **The Score** rewards doing the divination *by the book* — reading the method correctly and
  giving the interpretation the method actually calls for.
- **The Story** rewards *helping the person* — steering clients toward happy endings, ideally
  to the point where they no longer need you.

Sometimes the advice a client needs to hear is not the advice the fortune calls for. Choosing
between a perfect reading and a good outcome is the core of the experience.

## How to read these docs (progressive disclosure)

Each file is self-contained and scoped to one concern. Load only what your task needs.

| File | What it covers | Read it when you need… |
|------|----------------|------------------------|
| [`vision.md`](./vision.md) | Fantasy, tone, design pillars, references | The "why" and the feel |
| [`art-direction.md`](./art-direction.md) | Visual style, palette, composition, the reading scene, reference-book UI | Anything about how the game looks |
| [`core-loop.md`](./core-loop.md) | The per-client and per-day loop, the three-beat visit (intake → reading → consultation), the day scorecard | How a session actually plays |
| [`divination-methods.md`](./divination-methods.md) | The **shared reading framework** — how every reading works (scene, steps, random/rules/choice) | The reading mechanics in general |
| [`methods/`](./methods/) | One doc per method: [`tarot`](./methods/tarot.md) (fleshed), [`palmistry`](./methods/palmistry.md) + [`astrology`](./methods/astrology.md) (stubs) | The specifics of one method |
| [`clients-and-narrative.md`](./clients-and-narrative.md) | Client model, one-off vs. recurring arcs, memory/consequence, happy endings | Characters, story, branching |
| [`scoring-and-story.md`](./scoring-and-story.md) | The two axes in detail — how craft accuracy and narrative outcome are tracked and how they conflict | The tension mechanic, feedback, endings |
| [`shop-and-economy.md`](./shop-and-economy.md) | **WIP / isolated.** Clients paying, satisfaction, a between-days shop, and "fudge" upgrades | The money layer (still being figured out) |
| [`glossary.md`](./glossary.md) | Shared vocabulary | You hit an ambiguous term |
| [`open-questions.md`](./open-questions.md) | Unresolved decisions, unconfirmed assumptions, parking lot | Deciding what to nail down next |

## Status of the docs

These are a **first draft** distilled from the initial pitch. Requirements capture *intent and
direction*; they deliberately avoid over-specifying mechanics, numbers, and technical detail —
that granularity belongs to DESIGN and IMPLEMENTATION. Anything not yet decided lives in
[`open-questions.md`](./open-questions.md) so it stays visible instead of getting silently invented.
