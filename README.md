# The Ideabox

A brainstorming space. Individual ideas — stories, games, code projects, pitches, anything — get
gathered here and specced out, each in its own folder. Some stay as a one-page pitch. Others grow
into full design docs, and some go all the way to working prototypes or full implementations. Nothing
here is committed to being built; the point is to give an idea a home the moment it's worth writing
down, and let it develop as far as it wants to.

## Projects

| Folder | Idea | Status |
|--------|------|--------|
| [`psychic-poc/`](./psychic-poc/) | *I'm Not a Psychic* — a narrative, choice-based deduction game where you run a psychic parlor without believing a word of it | Planning (requirements drafted) |
| [`the-deposit-manhwa/`](./the-deposit-manhwa/) | *The Deposit* (전세 게임) — a Squid-Game-style thriller where a landlord who gambled away his tenants' jeonse deposits must win them back in an underground tournament against the tenants themselves | Planning (series bible drafted) |
| [`physics-and-sorcery/`](./physics-and-sorcery/) | *Physics & Sorcery* — a physics-driven strategy game inspired by the adventure-map and army-building loops of classic fantasy strategy games | Planning (MVP and art-pipeline gate drafted) |
| [`deepstead/`](./deepstead/) | *Deepstead* — a cozy dwarven farming, mining, community, and automation game set in a reclaimed underground hold | Planning (vertical slice drafted) |

## How this repo is organized

- Every idea gets a top-level folder named for it.
- A folder holds its own `README.md` as the entry point, plus whatever the idea needs — design docs
  (`docs/`), references, and eventually source code if it grows into a prototype or build.
- **Every project also gets a `notes.md`** — the standing place for feedback, reactions, and open
  questions about the idea (see *Feedback* below). Create it with the folder, even if it starts empty.
- This root README is the index — add a row to the table above when you start a new idea.

## Contributing

**Additive work goes straight to `main`.** Starting a brand-new idea, or building out an idea you
started — new folders, new docs, deeper specs, prototype code, anything that *adds* — commit it to
`main`. No review gate; the whole space is meant to grow freely.

**Overwriting someone else's pitch goes through a PR.** If you're reworking, re-pitching, or
otherwise replacing the existing direction of an idea that **another contributor** originally pushed,
open a pull request so the original author can review the change first. This only applies when you're
overwriting someone else's contribution — reshaping your own idea, or adding a *new* exploration
alongside an existing one (a new folder, a clearly-marked alternate take) without discarding what's
there, stays additive and belongs on `main`.

In short: **add freely on `main`; only overwrite another person's idea by PR.**

## Feedback

The pitch — a project's `README.md` and its `docs/` — belongs to the idea's author. When you have
feedback on someone else's idea, **don't rewrite their pitch to register it.** Put it in that
project's **`notes.md`** instead: critiques, questions, suggestions, "have you considered," reactions.
That keeps the author's vision intact and gathers every outside perspective in one predictable place.

- `notes.md` is append-only in spirit — add your thoughts, sign them so it's clear who's talking, and
  leave others' notes as they are.
- Writing in a `notes.md` is always additive work, so it lands on `main` — no PR needed, even on
  another contributor's project.
- If feedback earns its way into the actual design, that's when the author (or a PR against their
  pitch) folds it into the `README`/`docs`. `notes.md` is where ideas get argued; the pitch is where
  they get committed to.
