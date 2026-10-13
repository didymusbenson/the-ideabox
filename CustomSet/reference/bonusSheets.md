# Designing Bonus Sheets for Magic: The Gathering

A reference document for building bonus sheets — supplementary reprint collections that ship alongside a main set. Every principle and data point is sourced from official WotC articles, Mark Rosewater's columns, or verified set data.

---

## 1. What Is a Bonus Sheet?

A bonus sheet is a collection of reprinted Magic cards associated with a specific set, printed on their own sheet with a unique card treatment (frame, art, set code). They occupy a **guaranteed slot** in every booster pack — this is what distinguishes them from the older Masterpiece Series, which appeared at very low (lottery-ticket) rates.

Bonus sheet cards are **legal in Limited** (Draft and Sealed) for the set they ship with but **do not change their Constructed format legality**. A card that isn't Standard-legal doesn't become Standard-legal by appearing on a bonus sheet.

**Source:** [Bonus Sheet — MTG Wiki](https://mtg.fandom.com/wiki/Bonus_sheet); [Collecting Strixhaven](https://magic.wizards.com/en/news/feature/collecting-strixhaven-school-mages-2021-03-25)

---

## 2. Standard Size and Rarity Structure

Every major bonus sheet from 2021–2024 follows a remarkably consistent template:

| Bonus Sheet | Set (Year) | Total | Uncommon | Rare | Mythic |
|---|---|---|---|---|---|
| Mystical Archive | Strixhaven (2021) | 63 | 18 | 30 | 15 |
| Retro Artifacts | The Brothers' War (2022) | 63 | 18 | 30 | 15 |
| Multiverse Legends | March of the Machine (2023) | 65 | 20 | 30 | 15 |
| Enchanting Tales | Wilds of Eldraine (2023) | 63 | 18 | 30 | 15 |
| Breaking News | Outlaws of Thunder Junction (2024) | 65 | 20 | 30 | 15 |

**The baseline is ~63–65 cards: ~18–20 uncommons, 30 rares, 15 mythic rares.** No commons — the lowest rarity on a bonus sheet is uncommon.

**Source:** [Collecting Strixhaven](https://magic.wizards.com/en/news/feature/collecting-strixhaven-school-mages-2021-03-25); [Collecting Outlaws of Thunder Junction](https://magic.wizards.com/en/news/feature/collecting-outlaws-of-thunder-junction); [Bonus Sheet — MTG Wiki](https://mtg.fandom.com/wiki/Bonus_sheet)

---

## 3. Distribution in Packs

### One-Per-Pack Model (2021–2024 Standard)

Through 2024, the standard model was **one guaranteed bonus sheet card per booster pack** in a dedicated slot (not replacing a main set card).

For Play Boosters with a bonus sheet, the pack slot works as follows (using Breaking News / OTJ as the documented example):

- **Slot 13** is always a bonus sheet card (OTP in OTJ's case)
- **~67% of the time:** an uncommon
- **~33% of the time:** a rare or mythic rare
- Within the rare/mythic pool, the standard 2:1 rare-to-mythic ratio applies (each specific mythic appears roughly once every 75 packs)

**Source:** [Collecting Outlaws of Thunder Junction](https://magic.wizards.com/en/news/feature/collecting-outlaws-of-thunder-junction); [Play Booster Fact Sheet: OTJ — MTG Scribe](https://mtgscribe.com/2024/04/05/outlaws-of-thunder-junction-play-booster-fact-sheet/)

### Reduced-Rate Models (2025+)

Starting in 2025, WotC began experimenting with lower distribution rates:
- FINAL FANTASY "Through the Ages": **1-in-3 packs**
- "Stellar Sights" (Edge of Eternities): **1-in-8 packs**

This means the one-per-pack model is no longer assumed for all bonus sheets.

**Source:** [State of Design 2025](https://magic.wizards.com/en/news/making-magic/state-of-design-2025)

---

## 4. Design Principles (from WotC Sources)

### 4a. The Bonus Sheet Must Be Integral to the Set

> "One of the things R&D cares about is that a bonus sheet is integral to the set it's included in. Some sets have themes that make that easy, while others have themes that make it much more difficult."
> — Mark Rosewater, [Storm Scale: Throne of Eldraine through Strixhaven, Part 2](https://magic.wizards.com/en/news/making-magic/storm-scale-throne-of-eldraine-through-strixhaven-part-2)

Every successful bonus sheet has a tight thematic connection to its host set:

| Bonus Sheet | Set Theme | Bonus Sheet Filter |
|---|---|---|
| Mystical Archive | Magical university | Instants and sorceries (famous spells in the library) |
| Retro Artifacts | Artifact war (Brothers' War) | Artifacts in retro brown frames |
| Multiverse Legends | Multiverse invasion | Legendary creatures from across the multiverse |
| Enchanting Tales | Fairy tales | Enchantments (fairy tale magic) |
| Breaking News | Outlaw frontier | "Crimes" — spells that target opponents or their stuff |

The thematic filter does double duty: it makes the bonus sheet feel like it belongs in the set's world AND it constrains the card pool to a manageable selection space.

### 4b. Most Cards Should Play Well in Limited

> "There are numerous factors that go into choosing cards to put on a bonus sheet, but one of those factors is how the cards will play in Limited."
>
> "It's okay to have some cards that players would be excited to open and own that don't play well in Limited, but we want most cards on a bonus sheet to be a positive addition to Limited play."
> — Mark Rosewater, [Odds & Ends: The Brothers' War](https://magic.wizards.com/en/news/making-magic/odds-and-ends-the-brothers-war)

The best-received bonus sheets were praised specifically for Limited integration:

- **Brothers' War:** "The biggest compliment from fans concerned how the cards on the sheet were chosen to help make the Limited gameplay better. Many cards on the sheet enhanced existing archetypes or created interesting new draft themes that were synergistic with the main cards in the set." — [State of Design 2023](https://magic.wizards.com/en/news/making-magic/state-of-design-2023)

- **March of the Machine:** "Another common compliment was how cleverly the bonus sheet was used to enhance Limited gameplay, with many cards on the sheet enhancing various draft archetypes." — [State of Design 2023](https://magic.wizards.com/en/news/making-magic/state-of-design-2023)

The worst-received bonus sheets failed on this axis:

- **Wilds of Eldraine:** "Players enjoyed the card selection and the art, but there were some complaints that the bonus sheet cards didn't play better in Limited." — [State of Design 2024](https://magic.wizards.com/en/news/making-magic/state-of-design-2024)

- **Thunder Junction:** "Contained too many powerful cards." — [State of Design 2024](https://magic.wizards.com/en/news/making-magic/state-of-design-2024)

### 4c. Control the Bomb Density

A recurring criticism across multiple State of Design articles is bonus sheets warping Limited by introducing too many bombs:

- **March of the Machine** lowlight: "A common complaint was that victory was too often tied to opening bombs, either from the main set or from the bonus sheet." — [State of Design 2023](https://magic.wizards.com/en/news/making-magic/state-of-design-2023)

- **Thunder Junction:** "Got mixed reviews... Contained too many powerful cards." — [State of Design 2024](https://magic.wizards.com/en/news/making-magic/state-of-design-2024)

Play Design's perspective: bonus sheets are fine "as long as there are extra cards available allowing them to kick out problematic cards." The biggest impact is "making the bonus sheet an integral part of the Limited environment. That's the element that takes the most time to balance properly." — Andrew (Play Design), via [Storm Scale: Throne of Eldraine through Strixhaven, Part 2](https://magic.wizards.com/en/news/making-magic/storm-scale-throne-of-eldraine-through-strixhaven-part-2)

### 4d. Reprints Are a Finite Resource

> "Reprints are a resource, used in many different products, that we have to carefully dole out."
> — Mark Rosewater, [Storm Scale: Throne of Eldraine through Strixhaven, Part 2](https://magic.wizards.com/en/news/making-magic/storm-scale-throne-of-eldraine-through-strixhaven-part-2)

Not every set gets a bonus sheet. The Storm Scale rating for bonus sheets is **4** ("The popularity of bonus sheets means I expect us to repeatedly use them, although judiciously, in the future"), meaning they're likely but not guaranteed for any given set.

### 4e. Card Selection Happens Late in Design

> "Usually the second half of set design."
> — Mark Rosewater, when asked at what stage bonus sheet cards are selected. [Blogatog](https://markrosewater.tumblr.com/post/798962490776207360/hi-mark-at-what-stage-of-design-are-bonus-sheet)

This makes sense — you need the main set's mechanics, archetypes, and Limited environment to be largely defined before you can choose reprints that synergize with them.

### 4f. Different Bonus Sheets Serve Different Audiences

> "There are many different kinds of bonus sheets, aimed at different types of players. We'll keep making the ones you enjoy most, but also ones that other players enjoy most. That's the core to trading card game design, there's always a mix."
> — Mark Rosewater, [Blogatog](https://markrosewater.tumblr.com/post/788670894473117696/as-an-almost-purely-limited-player-i-also-much)

Some bonus sheets prioritize Limited playability, others prioritize reprint equity and collector excitement. The best do both.

### 4g. The Bonus Sheet Should Not Conflict with the Main Set

The Brothers' War team chose not to put artifact reprints in the main set because the bonus sheet was already filling that role. The existence of a bonus sheet shapes what goes into the main set's card file.

> "The set ended up getting a bonus sheet of artifact reprints, so it felt wrong to put artifact reprints in the main set."
> — Mark Rosewater, [Odds & Ends: The Brothers' War](https://magic.wizards.com/en/news/making-magic/odds-and-ends-the-brothers-war)

---

## 5. Card Selection Criteria

Synthesized from Rosewater's comments across multiple sources, the factors that go into choosing bonus sheet cards:

1. **Thematic fit** — Does this card match the bonus sheet's filter (card type, mechanical theme, flavor)?
2. **Limited gameplay** — Will this card be a positive addition to the draft environment? Does it support existing archetypes or create interesting new ones?
3. **Player excitement** — Is this a card players would be excited to open and own, even if it doesn't play perfectly in Limited?
4. **Power level** — Is this card safe for the Limited environment? Can Play Design "kick out problematic cards" if needed?
5. **Reprint availability** — Is this card available for reprinting, or is it allocated to another product?
6. **Visual/aesthetic fit** — Does the card look good in the bonus sheet's unique frame treatment?

**Source:** [Odds & Ends: The Brothers' War](https://magic.wizards.com/en/news/making-magic/odds-and-ends-the-brothers-war); [Storm Scale: Strixhaven](https://magic.wizards.com/en/news/making-magic/storm-scale-throne-of-eldraine-through-strixhaven-part-2)

---

## 6. Impact on Limited

### Positive Effects (When Done Well)
- Adds variety and replayability to the draft format
- Can enhance existing archetypes by providing additional support cards
- Creates interesting draft decisions (bonus sheet cards compete for picks against main set cards)
- Provides access to powerful or nostalgic cards in a Limited context

### Negative Effects (When Done Poorly)
- Too many bombs make the format feel like a lottery ("victory too often tied to opening bombs")
- Cards that don't integrate with the set's mechanics feel like dead picks
- Can cause players to force colors around a bonus sheet bomb, disrupting normal draft signals
- Cards with mechanics not in the main set add complexity without synergy

### Rosewater's Assessment

> "We've done a lot to think about what cards we put onto the bonus sheet as it relates to draft. It's less random than I think you think it is."
> — Mark Rosewater, [Blogatog](https://markrosewater.tumblr.com/post/724490601644605440/as-some-one-who-loves-draft-i-absolutely-hate)

---

## 7. Structural Considerations for Custom Set Design

Based on the patterns above, a custom set bonus sheet should consider:

### Size
- **Target: ~63–65 cards** (the proven template)
- Rarity split: ~18–20 uncommon / 30 rare / 15 mythic rare
- No commons on the bonus sheet

### Thematic Filter
- Choose a card type or mechanical theme that connects to the main set's identity
- The filter should be narrow enough to constrain selection but broad enough to fill 63+ slots with interesting cards

### Limited Integration
- Prioritize cards that support the main set's draft archetypes
- Keep bomb density in check — a few exciting mythics are fine, but most cards should play at a reasonable Limited power level
- Avoid cards with mechanics that don't appear in the main set unless those mechanics are simple enough to grok immediately

### Timing
- Design the bonus sheet in the second half of set design, after the main set's mechanics and archetypes are defined
- Be prepared to swap cards in and out as Limited playtesting reveals problems

### Relationship to Main Set
- The bonus sheet handles the set's reprint needs — don't duplicate reprint slots between the bonus sheet and main set
- The main set's 261 cards should be almost entirely new designs; the bonus sheet is where reprints live

---

## 8. Complete Bonus Sheet History

| Year | Set | Bonus Sheet Name | Cards | Theme |
|---|---|---|---|---|
| 2006 | Time Spiral | Timeshifted | 121 | Cards from Magic's past in original frames |
| 2021 | Time Spiral Remastered | Timeshifted | 121 | Remaster of original timeshifted cards |
| 2021 | Strixhaven | Mystical Archive | 63 | Instants and sorceries |
| 2022 | The Brothers' War | Retro Artifacts | 63 | Artifacts in retro frames |
| 2023 | Shadows over Innistrad Remastered | Shadows of the Past | — | Horror-themed reprints |
| 2023 | March of the Machine | Multiverse Legends | 65 | Legendary creatures |
| 2023 | Wilds of Eldraine | Enchanting Tales | 63 | Enchantments |
| 2024 | Outlaws of Thunder Junction | Breaking News | 65 | "Crime" spells |
| 2024 | Outlaws of Thunder Junction | The Big Score | 30 | Treasure-themed cards |
| 2024 | Modern Horizons 3 | New-to-Modern / Horizons | — | Format staple reprints |
| 2025 | Innistrad Remastered | Retro Frame | — | Horror reprints |

**Source:** [Bonus Sheet — MTG Wiki](https://mtg.fandom.com/wiki/Bonus_sheet); [30 Years, Part 2](https://magic.wizards.com/en/news/making-magic/30-years-part-2)

---

## Sources

All principles verified against official WotC sources:

1. [State of Design 2021](https://magic.wizards.com/en/news/making-magic/state-design-2021-08-16) — Mystical Archive reception, "potent tool" quote
2. [State of Design 2023](https://magic.wizards.com/en/news/making-magic/state-of-design-2023) — Brothers' War and March of the Machine bonus sheet assessment
3. [State of Design 2024](https://magic.wizards.com/en/news/making-magic/state-of-design-2024) — Wilds of Eldraine and Thunder Junction bonus sheet assessment
4. [State of Design 2025](https://magic.wizards.com/en/news/making-magic/state-of-design-2025) — FINAL FANTASY bonus sheet, reduced distribution rates
5. [Storm Scale: Throne of Eldraine through Strixhaven, Part 2](https://magic.wizards.com/en/news/making-magic/storm-scale-throne-of-eldraine-through-strixhaven-part-2) — Storm Scale 4, "integral to the set," Play Design perspective, reprints as resource
6. [Odds & Ends: The Brothers' War](https://magic.wizards.com/en/news/making-magic/odds-and-ends-the-brothers-war) — Card selection criteria, Limited considerations
7. [Collecting Strixhaven](https://magic.wizards.com/en/news/feature/collecting-strixhaven-school-mages-2021-03-25) — Mystical Archive structure and pack distribution
8. [Collecting Outlaws of Thunder Junction](https://magic.wizards.com/en/news/feature/collecting-outlaws-of-thunder-junction) — Breaking News pack slot and rarity odds
9. [30 Years, Part 2](https://magic.wizards.com/en/news/making-magic/30-years-part-2) — Bonus sheet history
10. [Bonus Sheet — MTG Wiki](https://mtg.fandom.com/wiki/Bonus_sheet) — Comprehensive list and definitions
11. Rosewater Blogatog posts: [Selection timing](https://markrosewater.tumblr.com/post/798962490776207360/hi-mark-at-what-stage-of-design-are-bonus-sheet), [Draft impact](https://markrosewater.tumblr.com/post/724490601644605440/as-some-one-who-loves-draft-i-absolutely-hate), [Different audiences](https://markrosewater.tumblr.com/post/788670894473117696/as-an-almost-purely-limited-player-i-also-much)
