# Instrument: Star Chart / Calendar (Astrology)

> Builds on [`../reading.md`](../reading.md). A supporting divination instrument — **active in the
> MVP**, not deferred.

## What it is

A **reference tool** the player consults: a star-chart guide and calendar. Given the client's **birth
date** (usually pulled from their [ID](./identity.md)), the player looks up their **sign and
placements** and the meanings attached to them. It's a lookup/cross-reference instrument, not a
minigame.

## The book — astrological meanings

The guide maps dates → signs → meanings (traits, tendencies, "what the stars say" for this person).
Like tarot, these are fixed and learnable; simplified is fine.

## How it's used in the deduction

Astrology **corroborates or complicates** the tarot spread. If the cards suggest upheaval and the
client's sign is one the guide associates with resistance to change, the correct read leans a
particular way. When a client's birth date is available, checking the chart is often what separates an
accurate reading from a plausible-sounding wrong one.

## Open questions

- **How much real astrology** to adopt vs. a legible game subset.
- **Calendar/chart UI** — how the player performs the lookup (see [`../art-direction.md`](../art-direction.md)).
- **Birth-date availability** — always derivable from the ID, or sometimes missing/withheld to make
  the puzzle harder?
- **Weight** — how much astrology can swing a reading vs. tarot as the backbone.
