# The Complete Nuts & Bolts Guide to Magic Set Design

A comprehensive reference synthesized from Mark Rosewater's complete Nuts & Bolts series (#1-18), covering every stage of designing a Magic: The Gathering set from initial concept to final mechanics layering. Organized to follow the design process sequentially.

---

## Part 1: Before You Design a Single Card

### The Starting Point: Initial Ideation (N&B #14)

Every set begins with an idea — and the idea matters less than the commitment to focus on it.

**The Four-Step Ideation Process:**

1. **Get an idea.** It can come from flavor, mechanics, a world concept, a single card, or a play pattern. Start with something — *anything* — that excites you.
2. **Understand the extensions of your idea.** What does this idea imply? What does it naturally lead to?
3. **Explore the implications of those extensions.** Ask: *"If we want to do this, what does it mean for the set?"* How does each idea restrict or expand remaining design space?
4. **Turn your list into a structure.** Take the unstructured brainstorm and organize it into a coherent plan. Assign priorities, identify conflicts, begin building a skeleton.

**Whiteboard exploration technique:** List all player expectations for the set's theme — both mechanical and creative. Have team members vote on the most compelling ideas. Create a prioritized list.

*"The biggest danger of Magic design isn't going the wrong way, it's not having a path to follow."*

**Always have a focal point.** One primary idea must guide decision-making. The idea itself is less important than the willingness to commit to it.

**Example:** Ravnica started with a single focused premise: *"Build a multicolor block around ten equally treated two-color pairs."* Everything else — guilds, guild mechanics, flavor — flowed from that.

### The Three Questions (N&B #9)

Before full design begins, the set must answer:

1. **What is this set about?** The identity must be expressible in seven words or less.
2. **Why should players care?** The emotional hook.
3. **What makes this set different?** The unique selling point.

**Example:** Kaladesh's vision: *"Feel like an optimistic aetherpunk inventor."*

*"A Magic set is not a random selection of cards thrown together."*

---

## Part 2: Building the Foundation

### Card Codes: The Language of Set Design (N&B #1)

Every card in a design file gets a **card code** — a stable identifier that persists even as names, abilities, and rarities change during design.

**Format:** Two letters + two numbers (e.g., CW01)

**First letter — Rarity:**
| Code | Rarity |
|------|--------|
| C | Common |
| U | Uncommon |
| R | Rare |
| M | Mythic Rare |
| L | Basic Land |
| T | Token |

**Second letter — Color/Frame:**
| Code | Color |
|------|-------|
| W | White |
| U | Blue |
| B | Black |
| R | Red |
| G | Green |
| Z | Multicolor |
| A | Artifact |
| L | Land (non-basic) |

**Numbering rules:**
- Always two digits (01-99)
- Creatures before non-creatures within each color
- Sorted roughly by mana cost (cheapest → most expensive)
- Cycle cards grouped at the same number across colors (CW03, CU03, CB03, CR03, CG03)

**Special numbers:**
- **99** — Cut from set but might return
- **88** — Potential addition being considered
- **00** — General notes

*"R&D cannot think in terms of a particular card. Instead we think about a slot."* — This is the foundational insight. Design is about what a position in the set needs to accomplish, not about falling in love with specific implementations.

### The Design Skeleton (N&B #2, #13)

The design skeleton is *"the most important tool in designing a set."* It maps out every card slot by color, rarity, and type — a blueprint that ensures nothing important is forgotten.

**Building the skeleton step by step:**

**Step 1: Determine set size and rarity breakdown.**
Standard modern set: 261 cards total (81 commons, 100 uncommons, 60 rares, 20 mythic rares under Play Booster structure).

**Step 2: Determine creature count.**
Target approximately 50% creatures across the set. Each color has its own ratio:

| Color | Creature % at Common |
|-------|---------------------|
| White | 62% |
| Blue | 50% |
| Black | 56% |
| Red | 53% |
| Green | 59% |

**Step 3: Distribute creatures across colors.**
In a 60-common set: White ~8, Green ~7, Black ~6, Red ~5, Blue ~4, Artifacts ~1. This reflects each color's identity.

**Step 4: Track creature sizes.**
Every creature falls into one of three categories:
- **Small:** P/T of 0/1 to 2/3
- **Medium:** P/T of 3/3 to 4/5
- **Large:** P/T of 5/5+

Each color needs a distribution across these sizes.

**Step 5: Plan the mana curve.**
Distribute cards across mana values 1-5+ within each color. Example for White common creatures:
- 1 MV: 1 creature
- 2 MV: 2-3 creatures
- 3 MV: 2-3 creatures
- 4 MV: 1-2 creatures
- 5-6 MV: 1 creature

**Step 6: Assign evergreen keywords.**
Each color has access to specific keywords. Control how many appear at common to ensure gameplay identity:
- White: Flying (3), Vigilance (2), First Strike, Lifelink
- Blue: Flying, Flash, Ward
- Black: Flying, Deathtouch, Menace, Lifelink
- Red: Haste, First Strike, Trample, Menace
- Green: Trample, Reach, Deathtouch, Vigilance

**Step 7: Allocate non-creature slots.**
Instants, sorceries, enchantments distributed across colors. Artifacts (~5 common). Lands (~5 common, color-producing).

**Step 8: Layer in set-specific mechanics.**

*"The skeleton isn't there to lock the designer in but to make the designer aware of what things they need to allocate."* It is a living document — adapt it as the set takes shape.

### Multicolor Design in the Skeleton (N&B #13, #16)

- Include a **10-card two-color cycle at uncommon** — one signpost card for each color pair.
- Under Play Booster structure, increase to **2 multicolor uncommons per pair**: one enabler and one payoff for the draft archetype.
- This creates a clearer signal to drafters about what each color combination is trying to do.

---

## Part 3: Filling the Skeleton

### Commons First (N&B #3)

*"If the theme of your set isn't in common, it isn't your theme."*

Commons are the heart of a set. They appear most frequently in boosters and define the play experience. The set's core concept must be provable through commons alone.

**Prioritization order — tackle the hardest elements first:**
1. **New mechanics** — most constrained, fewest viable designs
2. **Multicolor cards** — multiple requirements to satisfy
3. **Cycle cards** — must work as a cohesive group
4. **Cards with multiple simultaneous requirements**

**Don't wait for perfection.** Get playable cards into slots so you can playtest. Use the "99 slot" to track cards you like that don't currently fit.

**Look for dual-purpose cards.** Cards that serve two design needs simultaneously are extremely valuable — but they must feel like one cohesive card, not two ideas forced together.

**Watch for complexity creep.** The tendency for individual cards to accumulate more text as design proceeds. Especially dangerous at common. If a mechanic cannot be made simple enough for common, it may not be viable for the set.

### Higher Rarities (N&B #4)

Each rarity has a distinct job:

**Uncommons serve five roles:**
1. Carrying the set's mechanical themes with more complexity than commons allow
2. Providing larger creatures and spells
3. Adding card complexity (what NWO restricts at common)
4. Helping players win — stronger cards that enable comebacks
5. Shaping draft — signpost and build-around cards

**Rares use four strategies to create excitement:**
1. Make cards **big** — impressive scale and impact
2. Make cards **efficient** — powerful effects for low costs
3. Make cards **flavorful** — resonant top-down designs
4. Make cards **unique** — effects that don't exist elsewhere

**Mythic Rares:**
- *"Every mythic rare has to have the potential to be awesome."*
- Must create memorable gameplay moments
- Should excite different player psychographics
- Not simply "more powerful" rares — qualitatively different in feel

### New World Order — Complexity by Rarity (N&B #4)

Three types of complexity, each managed by rarity:

1. **Comprehension Complexity** — How hard is it to understand what a card does?
2. **Board Complexity** — How much does a card add to the mental load of tracking game state?
3. **Strategic Complexity** — How hard is it to figure out optimal use?

Commons must be kept low in all three. Complexity increases at higher rarities. This framework was created to lower barriers for new players but ended up improving the game for everyone.

---

## Part 4: Finding Your Mechanics

### Seven Paths to a Mechanic (N&B #17, Part 1)

1. **Spontaneous Generation** — Inspired by gameplay experiences or moments of insight. Example: Flashback came from wanting to cast a spell again from the graveyard.
2. **Fulfilling Longstanding Desires** — Solving gameplay limitations or fulfilling player wishes. Example: "Can't be countered" addressing the desire to guarantee spell resolution.
3. **Expanding Existing Cards** — Taking a unique card's ability and broadening it. Example: Changeling generalized from Mistform Ultimus.
4. **Naming Existing Patterns** — Formalizing patterns that already exist informally.
5. **Designing to Set Theme** — Creating a mechanic to support the set's concept. Example: Morbid in Innistrad making death mechanically relevant.
6. **Filling Skeleton Gaps** — A mechanic born from structural need. Example: Fabricate in Kaladesh.
7. **Solving Playtest Problems** — A mechanic created in response to challenges discovered during testing. Example: Bestow in Theros solving the Aura vulnerability problem.

### Evaluating Design Space (N&B #17, Part 1)

For any candidate mechanic, ask:
- **What card types** can it go on? (Creatures only? Instants/sorceries? All types?)
- **Which colors** can use it? (All five? Only two or three?)
- **At what rarities** can it appear? (Simple enough for common?)
- **When** can it be used? (Combat only? Any time? Your turn only?)
- **What strategic implications** does it create?

### The Exploration Process (N&B #17, Part 2)

1. Create a **mechanic outline** — describe what it does in plain language
2. **Design multiple cards** with the mechanic across different card types
3. **Build 40-card decks** with 4-8 cards using the new mechanic (the rest known cards to isolate the mechanic's impact)
4. **Playtest to find the fun** — you are not balancing yet, you are discovering what's enjoyable
5. **After each playtest, ask four questions:**
   - Was the mechanic enjoyable?
   - Which designs worked best/worst?
   - Which cards synergized well?
   - Did players understand the mechanic?

**Volume expectations:** Design 40-50 mechanics in the exploration phase to find the ONE that actually works and ships. This is a high failure rate by design. Most ideas will not pan out, and that is normal.

**Start with commons and uncommons.** If the mechanic doesn't work at the most basic level, it won't work at higher rarities.

*"A Magic designer's job is not to make every individual card as special as possible, it's to maximize the potential for the whole game."*

### As-Fan: Your Density Control Knob (N&B #12, #17)

**As-fan** measures how frequently a mechanic appears in an average booster pack.

- Track mechanic frequency across rarities
- Calculate expected appearances per booster based on collation math
- If as-fan is too low, the mechanic won't feel like a set theme
- If as-fan is too high, it crowds out other mechanics
- Uncommons count as roughly half a common for as-fan calculations

*"Getting the as-fan is tricky."* This is one of the hardest and most important structural challenges in set design.

---

## Part 5: Layering Mechanics Together

### The Layering Process (N&B #18)

Once you've identified your mechanics individually, layer them into the set **one at a time**. The order matters — each mechanic you add constrains what you can do with subsequent mechanics.

**Steps:**
1. Add mechanics one at a time — never integrate everything simultaneously
2. Prioritize mechanics before adding — rank from most to least important
3. Understand that each addition creates limitations for subsequent mechanics

**Prioritization criteria:**
- **Complexity level** — simpler mechanics may go in first to establish a baseline
- **Set embodiment** — the mechanic that most represents the set's identity takes priority
- **Synergy potential** — mechanics that interact with many others may be better early
- **Space requirements** — mechanics needing many cards must be integrated early to get room

### Mechanic Budget (N&B #15)

- **3-6 named/keyword mechanics** per set
- **1-4 unnamed mechanics** (themes without keyword labels)
- A **"_______ matters" theme** (e.g., "artifacts matter," "graveyard matters")
- All mechanics must reinforce the set's core concept

### Testing Mechanics in Combination (N&B #18)

1. Create initial 40-card playtesting decks with the first mechanic
2. Test mechanics in isolation before combining
3. Iterate based on feedback — adjust or replace underperformers
4. Analyze three factors: Fun factor, mechanical potential, interaction with other mechanics

**Look for connections.** The best sets have mechanics that naturally interact with each other.

**Use reprints as placeholders.** Fill decks with known cards to focus testing on the new mechanic.

*"Restrictions breed creativity."* The constraints imposed by earlier mechanics force more creative work on later ones.

---

## Part 6: Designing for Limited

### Why Limited Matters (N&B #12)

Limited play ensures more cards are relevant — not just Constructed all-stars. It serves as a sampler of the set's mechanics and themes; it's where most players first experience the set.

### Modularity vs. Linearity Spectrum (N&B #12)

- **Modular mechanics** work independently and go in any deck (e.g., flying)
- **Linear mechanics** require specific other cards to function (e.g., tribal synergies)
- Understand where your mechanic falls — linear mechanics demand more structural support

### Concentrating Mechanics (N&B #12)

Concentrate mechanics in fewer colors to increase density where they appear. Use existing, already-planned cards to do double duty supporting new mechanics.

### Draft Archetype Design (N&B #15)

For each of the 10 two-color pairs, determine:
- **Primary mechanics:** What mechanics define this archetype?
- **Victory route:** How does this deck win?
- **Speed:** Aggro, midrange, or control?
- **Novelty level:** How different is this from archetypes players have seen before?

### Structural Infrastructure (N&B #15, #16)

Every set needs these invisible support structures:
- **Mana fixing** — but be cautious with 3+ color lands to prevent goodstuff piles
- **Mana sinks** — things to do with excess mana in the late game
- **Deck smoothing** — card draw, scry, cycling to reduce flood/screw
- **Evasion abilities** — ways to break board stalls (flying, menace, trample)
- **Threats and answers** — balanced ecosystem of bombs and removal

### Play Booster Changes (N&B #16)

The shift from Draft Boosters to Play Boosters changed the math:
- Commons reduced from 101 to **81**
- Uncommons increased from 80 to **100**
- Result: uncommons carry more weight in defining the Limited environment
- Every common must be playable — no room for filler with reduced slots
- Raise average creature power levels — creatures should be pushed
- Use modal effects and ETB abilities to increase card utility

---

## Part 7: Playtesting and Iteration

### The Iterative Design Loop (N&B #5)

1. Make cards
2. Playtest cards
3. Take detailed notes
4. Change cards based on notes
5. Repeat

*"Nothing is going to help you better figure out what needs to get done than playing with the cards."*

### The All-Common Playtest (N&B #5)

Start playtesting as soon as commons are filled in — don't wait for higher rarities.

**Expected characteristics (don't panic):**
- Harder to come back from behind (no rare bombs for comebacks)
- More stalemates (similar creature sizes)
- More generic gameplay (less variety)
- Higher card repetition

These are normal. Do not judge an all-common playtest against a normal Magic environment.

**Five questions to ask during every playtest:**
1. What's fun?
2. What's not fun?
3. Are cards meeting design expectations?
4. Is anything confusing?
5. Are themes coming through?

### Take Notes Immediately

Memory fades quickly. Write notes during or right after the playtest. Require playtesters to experiment — assign different colors, insist on trying different strategies.

### The Four Stages of Iteration (N&B #6)

Evaluate in expanding concentric circles:

**Stage 1: Individual Card Focus**
Rate every card after each playtest: Yes / No / Unsure / Didn't Play. Identify what's working and what isn't.

**Stage 2: Two-Card Interactions**
Maintain two lists:
- **"Combo" list:** Pairs with positive synergies
- **"Bombo" list:** Pairs with negative interactions, anti-synergies, feel-bad moments
- Cards with multiple Bombo interactions should be cut

**Stage 3: Mechanical Themes**
Zoom out to keyword mechanics and recurring motifs. Track distribution across colors. Verify mechanics drive intended deckbuilding choices. Ensure each mechanic has enough support.

**Stage 4: Theme Interaction**
Zoom out further to how major themes work together. Create **"glue" cards** — cards that bridge between different mechanical themes. Evaluate whether the set feels cohesive or fragmented.

### Gatecrash Case Study (N&B #5)

Real-world example of how playtesting drives mechanic evolution:

| Guild | Initial Mechanic | Playtest Result | Final Outcome |
|-------|-----------------|----------------|---------------|
| Simic | Evolve | Very fun, worked well | Kept |
| Boros | Battalion | Very fun, successful | Kept |
| Dimir | Grind (milling) | Fun for dedicated players, frustrating for dabblers | Iterated |
| Gruul | Rowdy | Crazy powerful, needed rebalancing | Changed multiple times → Bloodrush |
| Orzhov | Unnamed | "A bust" — confusing, didn't hang together | Completely replaced → Extort |

This is normal. Some mechanics work, some need tweaking, some must be scrapped entirely.

---

## Part 8: Evaluation and Polish

### The Seven Evaluation Questions (N&B #9)

A structured self-assessment framework for the entire set:

1. **Unified Vision:** *"Can you describe your set in seven words or less?"*
2. **Vision Alignment:** Does every element serve the core vision?
3. **Mechanical Coherence:** Do different mechanics and elements work together?
4. **Playability:** Is the set fundamentally enjoyable?
5. **Depth and Discovery:** Does the set reward repeated exploration?
6. **Innovation:** Does the set introduce something genuinely new?
7. **Magic Identity:** Does the set still feel like Magic?

### The Three Stages of Design (N&B #7)

**Stage 1: Vision (~4 months)**
- Define the core identity — what is this set *about*?
- Create a clear direction everyone can articulate
- Spur creative ideas, explore broadly
- Define priorities
- Build foundational structure

**Stage 2: Integration (~4 months)**
- Test and stress the mechanics chosen during Vision
- Build connections between components
- Identify and fill design gaps
- Remove unnecessary elements

**Stage 3: Refinement (~4 months)**
- Find the best possible execution of each mechanic
- Fix remaining problems — fine-tuning, not rebuilding
- Fine-tune creative connections (flavor text, names, art direction)
- Final adjustments and polish

*"If everything is of equal importance, nothing is important."* — Prioritize ruthlessly.

Do not move to the next stage until the current stage's goals are fully met.

### Practical Design Tips Across the Series

- **"The two rule"** — In initial playtesting, limit card duplicates to two copies to see more of the set.
- **Keep detailed notes** on how individual cards and mechanics perform.
- **Use emotional distance** — take time away before evaluating. You need objectivity.
- **Involve outside perspectives** — designers become too close to their work.
- **Be brutally honest** about strengths and weaknesses.
- **Be willing to make significant changes even late in the process.**

*"Good design requires emotionally bonding to the thing you're creating"* — but it also requires the willingness to cut what is not working.

---

## Part 9: Rosewater's Master Principles

The overarching philosophy that permeates every article in the series:

1. **Think in slots, not cards.** Every position exists to serve a function. Individual cards are replaceable; the function they serve is not.

2. **Commons define everything.** They carry the theme, define the experience, and determine whether the set's identity is real or aspirational.

3. **The set outranks the card.** Always. No exceptions. Kill your darlings.

4. **Hardest elements first.** New mechanics, cycles, and multicolor cards have the fewest viable designs. Lock them in before simpler, more flexible elements.

5. **Iterate with feedback.** *"It's not just 10,000 hours. It's 10,000 hours with constant feedback."* Iteration without feedback is just repetition.

6. **Playtesting is not playing.** *"You are not there to win, you are there to experience the cards in your set."* Coverage over competition.

7. **Restrictions breed creativity.** Every constraint — the skeleton, the color pie, the rarity system, the mechanic budget — is a tool that makes good design possible.

8. **Somewhat different is good. Too different is alienating.** Balance innovation with familiarity. Every set needs both the new and the known.

9. **Design is disheartening.** Accept that most of what you create will be cut. Remain open. Use data over gut feeling. Treat design as continuous improvement, not a single burst of inspiration.

10. **Start anywhere. Just start.** *"The biggest danger of Magic design isn't going the wrong way, it's not having a path to follow."*

---

## Sources

All content synthesized from Mark Rosewater's Nuts & Bolts series (2009-2024):

| # | Title | Year | Core Topic |
|---|-------|------|------------|
| 1 | Card Codes | 2009 | Internal labeling system |
| 2 | Design Skeleton | 2010 | Set structure blueprint |
| 3 | Filling In the Design Skeleton | 2011 | Populating commons |
| 4 | Higher Rarities | 2012 | Uncommon/rare/mythic design |
| 5 | Initial Playtesting | 2013 | All-common playtests |
| 6 | Iteration | 2014 | The evaluate-revise loop |
| 7 | Three Stages of Design | 2015 | Vision/Integration/Refinement |
| 9 | Evaluation | 2017 | Seven diagnostic questions |
| 12 | Limited Mechanics (Part 1) | 2020 | Designing mechanics for draft |
| 13 | Design Skeleton Revisited | 2021 | Updated skeleton framework |
| 14 | Initial Ideation | 2022 | Starting from nothing |
| 15 | Structural Support | — | Infrastructure and archetypes |
| 16 | Play Boosters | — | Post-Play Booster skeleton changes |
| 17 | Finding Your Mechanics (Parts 1 & 2) | — | Mechanic discovery and testing |
| 18 | Layering Your Mechanics | — | Integrating mechanics into the set |
