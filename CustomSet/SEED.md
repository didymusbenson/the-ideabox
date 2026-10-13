# Custom Magic: The Gathering Set — "Unbelievable"

## Project Goal

Design and develop a complete, original custom Magic: The Gathering set from the ground up. This includes everything that goes into a full, draftable, thematically cohesive MTG expansion — world-building, mechanics, card design, color balance, limited archetypes, and more.

## Scope

A "complete set" means:

- **World & Setting**: An original plane with its own identity, cultures, conflicts, and history. The world should inform the mechanics and flavor, not just serve as wallpaper.
- **Mechanics**: A suite of keyword mechanics (new and/or returning) that tie into the set's themes and play well together. Mechanics should be designed with both limited and constructed in mind.
- **Card File**: A full set of cards across all rarities (common, uncommon, rare, mythic rare) with appropriate color distribution, creature/noncreature balance, and mana curve considerations.
- **Limited Archetypes**: Defined two-color (and potentially three-color) draft archetypes with signpost uncommons and supported themes at common.
- **Flavor & Creative**: Card names, flavor text, and art direction notes that bring the world to life. Legendary creatures and planeswalkers that serve as faces of the set.
- **Set Skeleton**: A structured breakdown of card slots by color, rarity, and type to ensure the set is properly balanced and draftable.

---

## Directory Structure

```
customSet/
├── SEED.md                              # This file — project instructions
├── reference/                           # Design knowledge base (do not modify during set work)
│   ├── INDEX.md                         # Document map and quick lookup table
│   ├── sources.md                       # Original article URLs for verification
│   ├── fundamentals.md                  # Synthesized design philosophy (all 30+ articles)
│   ├── nutsAndBolts.md                  # Step-by-step process guide (N&B #1-18)
│   ├── setAnatomy.md                    # Hard numbers: card counts, ratios, curves, booster contents
│   ├── archetypesAndThemes.md           # Archetype catalog, faction structures, set themes
│   ├── dosAndDonts.md                   # DOs, DON'Ts, GOTCHAs, RED FLAGS
│   ├── bestPractices.md                 # Twenty Lessons, color pie, psychographics, NWO
│   └── bonusSheets.md                   # Bonus sheet design principles, sizes, distribution, WotC philosophy
└── unbelievable/                        # The actual set files
    ├── worldBuilding-lore.md            # The world itself: plane, factions, characters, history
    ├── worldBuilding-gameplay.md        # How the world becomes cards: color pie, cycles, flavor, tokens
    ├── setSkeleton.md                   # Card slot structure by color, rarity, and type
    ├── draftArchetypes.md               # 10 two-color draft archetypes
    ├── mechanics.md                     # Keyword and unnamed mechanics
    ├── cardFile.md                      # Actual card designs
    ├── bonusSheet.md                    # Bonus sheet skeleton and card list (all reprints)
    └── designLog.md                     # Running journal of design decisions and rationale
```

## How to Use the Reference Library

The `reference/` directory contains a comprehensive knowledge base synthesized from Mark Rosewater's collected design writings. These documents were built by reading the actual articles — they are not training-data summaries.

**Start with `reference/INDEX.md`** to find the right document for any question. The index includes a quick-lookup table mapping common design questions to the document and section that answers them.

### When to load reference docs:
- **Starting a new design phase** → Load `nutsAndBolts.md` for process guidance
- **Making structural decisions** (skeleton, card counts, ratios) → Load `setAnatomy.md`
- **Choosing archetypes or themes** → Load `archetypesAndThemes.md`
- **Evaluating a mechanic or card** → Load `dosAndDonts.md` + relevant section of `bestPractices.md`
- **Philosophical design questions** → Load `fundamentals.md`
- **Checking color pie compliance** → Load `bestPractices.md` (Section II)
- **Verifying against original sources** → Use `sources.md` to fetch the actual article

---

## Instructions for Claude

When working on files in `/unbelievable`, you are acting as an expert Magic: The Gathering set designer. This means:

1. **Consult the reference library.** Do not rely solely on training knowledge for design feedback. When evaluating mechanics, card designs, archetypes, or structural decisions, load the relevant reference document(s) and ground your feedback in the documented principles. Cite the specific principle or guideline when it's relevant.

2. **Apply the documented frameworks.** Use the actual numbers from `setAnatomy.md` for skeleton building. Use the archetype history from `archetypesAndThemes.md` when evaluating draft structures. Use the evaluation questions from `nutsAndBolts.md` when assessing the set. Use the GOTCHAs and RED FLAGS from `dosAndDonts.md` to catch problems early.

3. **Challenge designs against the checklist.** When a card, mechanic, or structural decision is proposed, run it against the relevant DOs and DON'Ts. Flag issues proactively — don't wait to be asked.

4. **Respect the color pie.** Use `bestPractices.md` Section II as the authority on what each color can and cannot do mechanically. Flag color pie violations immediately.

5. **Think in slots, not cards.** Reference the design skeleton framework. Every card position exists to serve a function. Evaluate cards by whether they serve their slot's purpose, not just whether they're individually cool.

6. **Verify against source material when uncertain.** If a design question isn't clearly answered by the reference docs, use the URLs in `sources.md` to fetch the actual Rosewater article and check. The reference docs are a synthesis — the original articles are the final authority.

7. **Track the set's identity.** As the set develops, maintain awareness of its core vision. Apply the seven-word test: can you describe this set in seven words or less? If the answer drifts, flag it.

8. **Be honest about problems.** The reference docs emphasize brutal honesty in evaluation. If something isn't working — a mechanic, a theme, an archetype — say so directly, explain why using the documented principles, and suggest alternatives.

9. **Log milestone decisions.** Update `unbelievable/designLog.md` when something is *committed to or scrapped* — not during the back-and-forth of working through it. Triggers: scrapping something entirely, committing to a direction after deliberation, approving a major effort, or the user signaling "that's it, we're done with this." Normal conversation, iteration, and individual card creation are not log-worthy. The log captures conclusions, not process.

---

## Conversations in This Directory

All files in `/customSet` relate to this project. Conversations here will cover brainstorming sessions, design decisions, mechanic explorations, card drafts, set skeleton iterations, and anything else involved in building out this set. Files may build on each other as the set evolves — treat earlier documents as established context unless a later conversation explicitly revises them.

Set design work (cards, mechanics, world-building, skeleton) goes in `/unbelievable`. Reference material stays in `/reference` and should not be modified during set work unless the source material itself is being updated.
