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

## How this repo is organized

- Every idea gets a top-level folder named for it.
- A folder holds its own `README.md` as the entry point, plus whatever the idea needs — design docs
  (`docs/`), notes, references, and eventually source code if it grows into a prototype or build.
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
