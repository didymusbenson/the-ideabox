# Draft Archetypes and Set-Wide Themes in Magic: The Gathering

A comprehensive reference for designers structuring a Magic set's draft environment, archetype identity, and mechanical themes. Covers the standard 10 two-color pair system, faction structures, three-color designs, recurring set-wide themes, archetype speed balance, and supporting themes at common.

---

## 1. The 10 Two-Color Pair System

### How It Works

The standard structure for modern Magic draft environments is **ten two-color archetypes**, one for each possible pair of Magic's five colors. This system has been the backbone of limited design since roughly Innistrad (2011), and was formally codified as design technology during the 2010s. Every modern draftable set uses this structure unless deliberately departing from it (e.g., Strixhaven's five-college model, Streets of New Capenna's three-color families, or Khans of Tarkir's wedge clans).

The ten pairs are divided into five **allied** pairs (colors adjacent on the color wheel) and five **enemy** pairs (colors opposite on the color wheel):

| Allied Pairs | Enemy Pairs |
|---|---|
| WU (Azorius) | WB (Orzhov) |
| UB (Dimir) | UR (Izzet) |
| BR (Rakdos) | BG (Golgari) |
| RG (Gruul) | RW (Boros) |
| GW (Selesnya) | GU (Simic) |

### How Signpost Uncommons Work

**Signpost uncommons** are multicolored uncommon cards -- one (or now two) per color pair -- that telegraph what a given archetype wants to do. They are the single most important structural tool for communicating draft archetypes to players.

**Pre-Play Booster era (before 2024):** Each color pair received one gold signpost uncommon. Designers had to choose whether that single card was an **enabler** (helping the archetype function) or a **payoff** (rewarding the archetype's strategy). This created tension because one card had to do both jobs.

**Play Booster era (2024 onward):** The multicolor uncommon slots increased from 10 to 20. Each color pair now gets **two** gold signpost uncommons -- one enabler and one payoff. This gives designers room to more clearly signal both what the archetype does and why it is worth pursuing.

Signpost cards should be:
- **Pushed in power level** beyond a normal uncommon -- they need to be worth building around
- **Pushed in complexity** -- they carry more rules text and strategic depth than typical uncommons
- **Pickable early** -- ideally first-pick caliber to reward committing to the archetype
- **Clear in message** -- a player who reads the signpost should understand what the archetype wants

### How Each Pair Gets Mechanical Identity

Archetype identity emerges from the intersection of two colors' natural strengths. Each color has its own tendencies (white goes wide, blue draws cards and flies, black kills and recurs, red burns and attacks, green ramps and stomps), and the pair's archetype leverages what the two colors share or complement.

Designers determine four things for each archetype (per Rosewater's Nuts & Bolts #15):

1. **Primary mechanics** -- What mechanics define this archetype?
2. **Victory route** -- How does this deck win?
3. **Speed** -- Is it aggro, midrange, or control?
4. **Novelty level** -- How different is this from archetypes players have seen before?

The recommended balance for novelty across all ten archetypes:
- **3-4 archetypes** should feel familiar and comfortable
- **4 archetypes** should be slight variations on known themes
- **2 archetypes** can be genuinely novel departures

---

### Historical Catalog of Two-Color Pair Archetypes

Below is a catalog of what each color pair has been across multiple sets. This demonstrates both the defaults and the range of variation possible.

#### WU (Azorius) -- Default: Flyers / Skies / Tempo

The most consistent archetype across Magic's history. Blue and white both have access to flying creatures, and combining them into an evasive air force is natural and intuitive.

| Set | Archetype |
|---|---|
| Foundations (FDN) | Flyers (Empyrean Eagle) |
| Final Fantasy (FIN) | Flyers |
| Bloomburrow (BLB) | Flyers (Birds) |
| Aetherdrift (DFT) | Artifacts |
| Lord of the Rings (LTR) | Flyers / Draw-second-card |
| Modern Horizons 3 (MH3) | Flying + Energy |
| Brothers' War (BRO) | Soldier Tribal |
| Dominaria United (DMU) | Flying Tempo / Spells |
| Kamigawa: Neon Dynasty (NEO) | Vehicles |
| Midnight Hunt (MID) | Spirits / Disturb |
| Strixhaven (STX) | N/A (not a supported pair) |
| Ravnica Allegiance (RNA) | High-toughness matters (High Alert) |
| Guilds of Ravnica (GRN) | N/A (not in this half) |

**Design notes:** WU Flyers is the most reliable "auto-pilot" archetype in Magic. When designers want to break from it (Vehicles in NEO, Soldiers in BRO), the departure stands out. Flying is simply one of the strongest mechanics in limited, so WU decks tend to overperform.

---

#### UB (Dimir) -- Default: Control / Graveyard / Mill

Blue-black naturally gravitates toward secrets, card advantage, and the graveyard. The pair has the best card selection and the most removal, making it a natural control color combination.

| Set | Archetype |
|---|---|
| Foundations (FDN) | Graveyard Threshold (Dreadwing Scavenger) |
| Aetherdrift (DFT) | Artifact Attrition |
| Lost Caverns of Ixalan (LCI) | Control / Descend |
| Lord of the Rings (LTR) | Amass |
| Brothers' War (BRO) | Draw-Two Tempo |
| Dominaria United (DMU) | Control / Drain-and-Gain |
| Kamigawa: Neon Dynasty (NEO) | Ninjutsu |
| Midnight Hunt (MID) | Zombies / Decayed |
| Guilds of Ravnica (GRN) | Surveil Control |
| Streets of New Capenna (SNC) | Five mana values in graveyard |

**Design notes:** UB is flexible because both colors interact with the graveyard, the hand, and the library. Mill, Surveil, self-mill, reanimation, and threshold/delirium all live here comfortably.

---

#### BR (Rakdos) -- Default: Aggro / Sacrifice / Aristocrats

Black-red is almost always aggressive, leveraging haste, menace, sacrifice outlets, and direct damage. The "aristocrats" pattern (sacrifice creatures for value while draining the opponent) is its most distinctive identity.

| Set | Archetype |
|---|---|
| Foundations (FDN) | Raid / Sacrifice (Perforating Artist) |
| Final Fantasy (FIN) | Aggro |
| Lost Caverns of Ixalan (LCI) | Aggro / Pressure |
| Brothers' War (BRO) | Sacrifice (strongest archetype in format) |
| Dominaria United (DMU) | Aggro / Sacrifice |
| Kamigawa: Neon Dynasty (NEO) | Artifact Sacrifice |
| Midnight Hunt (MID) | Vampires |
| Guilds of Ravnica (GRN) | N/A (not in this half) |
| Ravnica Allegiance (RNA) | Spectacle Aggro |

**Design notes:** BR is one of the most mechanically consistent pairs. Sacrifice is so natural to black-red that it appears even when not the explicit theme. The pair's identity is deeply rooted in trading resources (life, creatures) for damage and card advantage.

---

#### RG (Gruul) -- Default: Big Creatures / Stompy / Ramp

Red-green plays the biggest creatures and attacks the hardest. It rarely has complex synergy demands -- instead, it wins by playing threats that are individually larger than the opponent's.

| Set | Archetype |
|---|---|
| Foundations (FDN) | Power 4+ Matters (Ruby, Daring Tracker) |
| Lost Caverns of Ixalan (LCI) | Dinosaurs |
| Brothers' War (BRO) | Powerstone Midrange |
| Dominaria United (DMU) | Domain Stompy |
| Kamigawa: Neon Dynasty (NEO) | Modified Creatures |
| Midnight Hunt (MID) | Werewolves / Day-Night |
| Ravnica Allegiance (RNA) | Riot Aggro |

**Design notes:** RG is the simplest archetype to design and the easiest for new players to understand. "Play big creature, attack" is always a valid game plan. When designers want to add complexity (Modified in NEO, Werewolves in MID), the large-creature foundation remains.

---

#### GW (Selesnya) -- Default: Go-Wide / Tokens / +1/+1 Counters

Green-white excels at putting many creatures on the board, then enhancing them with counters, anthems, or combat tricks. It is the quintessential "army" color pair.

| Set | Archetype |
|---|---|
| Foundations (FDN) | +1/+1 Counters (Wardens of the Cycle) |
| Bloomburrow (BLB) | Go-Wide Tokens |
| Lost Caverns of Ixalan (LCI) | Go-Wide Aggro |
| Brothers' War (BRO) | Artifacts ETB / +1/+1 Counters |
| Dominaria United (DMU) | Go-Wide Tokens |
| Kamigawa: Neon Dynasty (NEO) | Enchantments |
| Midnight Hunt (MID) | Humans / Coven |

**Design notes:** GW has the highest creature density of any pair (white and green both run ~60% creatures at common). Tokens, counters, and going wide are all natural expressions of what these colors do. Enchantments (NEO) and tribal (MID) are departures that still leverage creature density.

---

#### WB (Orzhov) -- Default: Lifegain / Sacrifice / Attrition

White-black is, by Rosewater's own admission, "probably the color pair that is toughest to nail down as an archetype." Both colors have excellent removal but their creatures do not naturally synergize. Designers often solve this with lifegain, sacrifice, or aristocrats themes.

| Set | Archetype |
|---|---|
| Foundations (FDN) | Lifegain (Fiendish Panda) |
| Lost Caverns of Ixalan (LCI) | Vampires / Sacrifice |
| Brothers' War (BRO) | Graveyard Recursion Aggro |
| Dominaria United (DMU) | Aristocrats |
| Kamigawa: Neon Dynasty (NEO) | Artifacts & Enchantments (controlling both) |
| Midnight Hunt (MID) | Sacrifice / Aristocrats |
| Strixhaven (STX) | Silverquill -- Tempo / Aggro |
| Ravnica Allegiance (RNA) | Afterlife / Aristocrats |

**Design notes:** WB struggles because white's creatures (small, wide) and black's creatures (expensive, individually powerful) do not curve together well. The pair needs a mechanical bridge. Lifegain, sacrifice, and tokens-into-value are the most common solutions. Strixhaven's aggressive Silverquill was a notable reinvention.

---

#### UR (Izzet) -- Default: Spells Matter / Prowess / Instants & Sorceries

Blue-red is the "spellslinger" pair. It cares about casting instants and sorceries, often rewarding the caster with damage, tokens, card draw, or creature buffs.

| Set | Archetype |
|---|---|
| Foundations (FDN) | Spells / Tempo (Enigma Drake) |
| Bloomburrow (BLB) | Prowess / Spell Cost Reduction |
| Modern Horizons 3 (MH3) | Energy |
| Brothers' War (BRO) | Noncreature Spells / Prowess (Third Path Iconoclast) |
| Dominaria United (DMU) | Spells / Pseudo-Prowess (Balmor, Battlemage Captain) |
| Kamigawa: Neon Dynasty (NEO) | Artifacts Matter |
| Midnight Hunt (MID) | Spells |
| Strixhaven (STX) | Prismari -- Big Spells + Ramp |
| Guilds of Ravnica (GRN) | Jump-start |

**Design notes:** UR is one of the most consistent archetypes after WU Flyers. "Cast instants and sorceries, get rewarded" is an endlessly flexible template. The main design challenge is ensuring UR decks have enough creatures to function in limited -- since the archetype naturally wants to run more noncreature spells than other decks.

---

#### BG (Golgari) -- Default: Graveyard / Midrange / Value

Black-green is the graveyard pair. It fills the graveyard, recurs from it, and generates value through death and regrowth. It is almost always a midrange strategy.

| Set | Archetype |
|---|---|
| Foundations (FDN) | Morbid (Deadly Brew) |
| Final Fantasy (FIN) | Graveyard Midrange |
| Bloomburrow (BLB) | Squirrels / Forage |
| Aetherdrift (DFT) | Graveyard Midrange (best deck in format) |
| Lost Caverns of Ixalan (LCI) | Graveyard / Descend |
| Modern Horizons 3 (MH3) | Modification / Counters |
| Lord of the Rings (LTR) | Reanimation / Sacrifice + Food |
| Wilds of Eldraine (WOE) | Food Tokens |
| Brothers' War (BRO) | Graveyard Midrange |
| Dominaria United (DMU) | Graveyard |
| Kamigawa: Neon Dynasty (NEO) | Graveyard / Channel |
| Midnight Hunt (MID) | Morbid / Creatures Dying |
| Guilds of Ravnica (GRN) | Undergrowth |

**Design notes:** BG is perhaps the most reliably recurring theme in all of limited. "Graveyard matters" appears in BG in nearly every set. When it departs (Food in WOE, Modification in MH3, Squirrels in BLB), the graveyard still tends to be involved. The pair's natural card advantage through recursion makes it a reliable midrange performer.

---

#### RW (Boros) -- Default: Aggro / Go-Wide / Equipment

Red-white is almost always the most aggressive deck in any format. It curves low, attacks early, and tries to end the game before slower decks establish control.

| Set | Archetype |
|---|---|
| Foundations (FDN) | Go-Wide Aggro (Heroic Reinforcements) |
| Final Fantasy (FIN) | Classic Aggro |
| Wilds of Eldraine (WOE) | Celebration (multiple permanents per turn) |
| Lord of the Rings (LTR) | Low-curve Aggro (Haste + First Strike) |
| Brothers' War (BRO) | Aggro |
| Dominaria United (DMU) | Aggro / Enlist |
| Kamigawa: Neon Dynasty (NEO) | Samurai / Warriors (Exalted-style) |
| Midnight Hunt (MID) | Aggro / Day-Night |
| Strixhaven (STX) | Lorehold -- Graveyard Value / Spirits |

**Design notes:** RW is the "fun police" of limited -- it keeps greedy decks honest by threatening to kill them before their plans come online. Strixhaven's Lorehold was a famous reinvention that made RW a controlling, graveyard-value archetype instead of aggro. NEO's Samurai (attacking alone for bonuses) was another creative departure while keeping the combat focus.

---

#### GU (Simic) -- Default: Ramp / Value / +1/+1 Counters

Green-blue pairs green's mana acceleration and large creatures with blue's card draw and tempo. It is often the least defined archetype in any format.

| Set | Archetype |
|---|---|
| Foundations (FDN) | Ramp / Landfall (Tatyova, Benthic Druid) |
| Modern Horizons 3 (MH3) | Eldrazi Spawn Ramp |
| Wilds of Eldraine (WOE) | 5+ Mana Value Matters |
| Brothers' War (BRO) | Prototype Ramp |
| Dominaria United (DMU) | Domain / Ramp |
| Kamigawa: Neon Dynasty (NEO) | Ramp / Splash |
| Midnight Hunt (MID) | Flashback |
| Ravnica Allegiance (RNA) | Adapt / +1/+1 Counters |

**Design notes:** GU is historically the weakest and hardest-to-define archetype. Ramp is its most common identity, but ramp strategies struggle in tempo-oriented limited formats where spending a turn accelerating means falling behind on board. GU often ends up as "good stuff" rather than a cohesive synergy deck. Strixhaven's Quandrix (8-lands-matter, Fractals with +1/+1 counters) was one of the more successful attempts to give it a distinct identity.

---

## 2. Five Allied Pair Sets

### Structure

Some sets support only five archetypes instead of ten, using exclusively allied-color pairs (WU, UB, BR, RG, GW). This approach was pioneered in the original Ravnica block's split structure and has been used in sets like Guilds of Ravnica and Ravnica Allegiance, as well as enemy-pair equivalents like Strixhaven.

**Advantages of five archetypes:**
- In a typical eight-player draft, five archetypes divide more cleanly among players than ten. Erik Lauer (retired Magic designer) argued that with five archetypes, only one archetype would go undrafted, reducing the "feel-bad" of a wasted strategy.
- Designers have an easier time ensuring all five archetypes have enough card density and cross-synergy.
- More cards are playable across multiple archetypes, improving "pivotability" -- the ability to change strategy mid-draft.

**Disadvantages:**
- Five pairs leaves five other pairs completely unsupported, which can feel restrictive.
- Players who open powerful cards in unsupported pairs have no archetype to build.
- Replayability may be lower since fewer distinct strategies exist.

### The Original Ravnica Block: 4/3/3 Guild Split

The original Ravnica block (2005-2006) was the first major faction set. It divided all ten guilds across three sets:

| Set | Guilds |
|---|---|
| **Ravnica: City of Guilds** (large set) | Boros (RW), Dimir (UB), Golgari (BG), Selesnya (GW) |
| **Guildpact** (small set) | Gruul (RG), Izzet (UR), Orzhov (WB) |
| **Dissension** (small set) | Azorius (WU), Rakdos (BR), Simic (GU) |

The split was 4/3/3, with the large set getting four guilds and each small set getting three. This created a unique drafting experience where different guilds were available depending on which packs were being opened.

**Key design constraint:** The 4/3/3 split had to ensure every color appeared in at least one guild per set, so no color was completely absent from any individual expansion.

### The Return to Ravnica Approach: 5/5

Return to Ravnica (2012-2013) used a cleaner 5/5 split:

| Set | Guilds |
|---|---|
| **Return to Ravnica** | Azorius (WU), Izzet (UR), Rakdos (BR), Golgari (BG), Selesnya (GW) |
| **Gatecrash** | Orzhov (WB), Dimir (UB), Gruul (RG), Boros (RW), Simic (GU) |

Each set was drafted independently as a self-contained five-guild environment.

### Guilds of Ravnica / Ravnica Allegiance: Another 5/5

The third visit to Ravnica (2018-2019) also used a 5/5 split:

| Set | Guilds |
|---|---|
| **Guilds of Ravnica** | Dimir (UB), Izzet (UR), Golgari (BG), Boros (RW), Selesnya (GW) |
| **Ravnica Allegiance** | Azorius (WU), Orzhov (WB), Rakdos (BR), Gruul (RG), Simic (GU) |

Each guild received a unique keyword mechanic: GRN had Surveil (Dimir), Jump-start (Izzet), Undergrowth (Golgari), Mentor (Boros), and Convoke (Selesnya). RNA had Addendum (Azorius), Afterlife (Orzhov), Spectacle (Rakdos), Riot (Gruul), and Adapt (Simic).

**Lesson learned:** Guilds of Ravnica was considered a weaker limited environment because Boros and Dimir were significantly overpowered relative to the other three guilds, reducing archetype diversity. Ravnica Allegiance corrected this with better balance and the bonus "Gates" archetype that allowed five-color drafting.

---

## 3. Ten Guild Sets

### Full 10-Guild Simultaneous Support

Supporting all ten guilds in a single set is the most ambitious approach. It requires enough card density for each archetype while maintaining color balance.

**Key requirements:**
- **20 signpost uncommons** (2 per pair under Play Booster structure) or 10 (1 per pair pre-Play Booster)
- **Sufficient monocolor support** in each color that cards are playable across multiple archetypes
- **A unifying set mechanic** or theme that cuts across all ten pairs to provide cohesion
- **Balanced mana fixing** -- enough to enable two-color decks without enabling "good stuff" five-color piles

**The Ravnica model:** Each guild gets a unique keyword mechanic. This is the clearest possible signal to players but requires designing ten separate mechanics, which is an enormous design space demand. This is why Ravnica blocks split guilds across multiple sets.

**The non-Ravnica model:** Most sets that support all ten pairs do NOT give each pair its own keyword. Instead, they use 3-6 set-wide mechanics and concentrate specific mechanics in specific color pairs. For example, Innistrad: Midnight Hunt used Disturb (concentrated in WU), Decayed (concentrated in UB), and Day/Night (concentrated in RG), while Flashback and basic removal crossed all colors.

### How Non-Ravnica Sets Structure 10 Archetypes

The standard approach is:
1. **Define 2-3 monocolor identities** per color (e.g., white cares about tokens AND lifegain)
2. **Each two-color pair emerges from the intersection** of its two colors' identities
3. **Signpost uncommons crystallize** the intersection into a clear archetype
4. **Shared mechanics** provide glue cards that work across multiple archetypes

This was Dominaria United's approach: White focused on going wide and tokens, Blue on instants/sorceries, Black on death-matters, Red on aggro and damage, Green on Domain and ramp. Each two-color pair emerged naturally from combining these identities.

---

## 4. Shard Sets (Three-Color Allied)

### What Shards Are

A shard is a three-color group consisting of one color and its two allies on the color wheel. The five shards are:

| Shard | Colors | Named After |
|---|---|---|
| **Bant** | GWU (Green-White-Blue) | Shards of Alara |
| **Esper** | WUB (White-Blue-Black) | Shards of Alara |
| **Grixis** | UBR (Blue-Black-Red) | Shards of Alara |
| **Jund** | BRG (Black-Red-Green) | Shards of Alara |
| **Naya** | RGW (Red-Green-White) | Shards of Alara |

### Shards of Alara (2008-2009)

The first shard set. Each shard was flavored as a fragment of a shattered world that had developed in isolation with only three colors of mana.

**Design philosophy:** "What would a world look like with two colors of mana missing?" Grixis (UBR) had no green (no growth/life) and no white (no order), creating a barren world of undead horror. Naya (RGW) had no blue (no artifice) and no black (no death), creating a primal jungle paradise.

**Each shard received:**
- A unique mechanical identity and keyword
- Legendary creatures in the shard's three colors
- Common/uncommon support concentrated in the shard's colors

**Mana fixing strategy:**
- **Obelisks** at common: One for each shard, tapping for three colors of mana (artifact mana rocks)
- **Tri-lands** at uncommon: Lands entering tapped that tap for any of the shard's three colors (e.g., Jungle Shrine for Naya)
- **Panoramas** at common: Fetchable lands that could search for basic lands of the shard's colors
- **Cycling** on select cards: Insurance against color-screw, allowing uncastable cards to be cycled away

**Critical design decision:** Only 3 low-rarity cards per shard required all three colors to cast. Most multicolored cards used "pay-as-you-can" color requirements (e.g., Bant Battlemage could be cast with just white mana but was at its best in a three-color deck). This reduced the risk of three-color mana bases while rewarding players who achieved them.

**Lessons learned:**
- The shards played well individually but some did not synergize well with the shards that overlapped them in color. Alara's factions were interesting but not always intersynergistic.
- Three-color draft environments require abundant but not overpowered mana fixing. If fixing becomes a first-pick, drafting feels bad because players spend premium picks on mana rather than spells.
- The actual draft decks were often two colors splashing a third, not true three-color decks. This is healthy and should be expected.

### Streets of New Capenna (2022)

The second shard set, themed around five crime families in an art-deco city.

**The five families:**
| Family | Colors (Shard) | Mechanic |
|---|---|---|
| **Brokers** | GWU (Bant) | Shield counters |
| **Obscura** | WUB (Esper) | Connive |
| **Maestros** | UBR (Grixis) | Casualty (sacrifice to copy spells) |
| **Riveteers** | BRG (Jund) | Blitz (haste + sacrifice at end of turn) |
| **Cabaretti** | RGW (Naya) | Alliance (landfall for creatures) |

**Structural innovation:** Streets of New Capenna used **five primary three-color archetypes** AND **five secondary two-color allied archetypes**. The two-color archetypes bridged adjacent families:
- WU: Counters on creatures (bridging Brokers and Obscura)
- UB: Five mana values in graveyard (bridging Obscura and Maestros)
- BR: Sacrifice (bridging Maestros and Riveteers)
- RG: Treasure tokens (bridging Riveteers and Cabaretti)
- GW: Citizen tribal / tokens (bridging Cabaretti and Brokers)

**Draft reality:** Despite being a three-color set, the best decks were typically two colors splashing a third. Starting with an allied pair and adding a third color for powerful gold cards was the recommended strategy.

### General Considerations for Three-Color Shard Design

1. **Mana fixing must be abundant but not dominant.** Players need to cast their spells, but fixing should not be so good that five-color "good stuff" decks become the default.
2. **Design cards that are castable at two colors but rewarded at three.** Reduce the number of cards requiring all three colors at low rarities.
3. **Two-color bridges between shards** allow players to pivot between adjacent strategies during a draft.
4. **Expect two-color-plus-splash decks** as the most common outcome. True three-color decks should be achievable but not mandatory.

---

## 5. Wedge Sets (Three-Color Enemy)

### What Wedges Are

A wedge is a three-color group consisting of one color and its two enemies on the color wheel. The five wedges are:

| Wedge | Colors | Named After |
|---|---|---|
| **Abzan** | WBG (White-Black-Green) | Khans of Tarkir |
| **Jeskai** | URW (Blue-Red-White) | Khans of Tarkir |
| **Sultai** | BGU (Black-Green-Blue) | Khans of Tarkir |
| **Mardu** | RWB (Red-White-Black) | Khans of Tarkir |
| **Temur** | GUR (Green-Blue-Red) | Khans of Tarkir |

### Khans of Tarkir (2014)

The definitive wedge set and one of the most beloved limited formats in Magic's history.

**The five clans:**
| Clan | Colors | Mechanic | Style |
|---|---|---|---|
| **Abzan** | WBG | Outlast (+1/+1 counters, sorcery speed) | Grindy, late-game |
| **Jeskai** | URW | Prowess (buff on noncreature spell cast) | Tempo, spell-based |
| **Sultai** | BGU | Delve (exile graveyard cards to reduce costs) | Value, graveyard |
| **Mardu** | RWB | Raid (bonus for having attacked this turn) | Aggro |
| **Temur** | GUR | Ferocious (bonus if you control power 4+) | Big creatures |

**Key design decisions:**

1. **Enemy-color gold cards as pivot points.** Each wedge contains one enemy-color pair (Abzan has WB, Jeskai has UR, Sultai has BG, Mardu has RW, Temur has GU). The set included two cycles of enemy-color uncommon gold cards that belonged to multiple clans. For example, a WB card could go in either Abzan (WBG) or Mardu (RWB). This allowed drafters to start in an enemy pair and choose their third color later.

2. **Morph as universal glue.** Morph (play any creature face-down as a 2/2 for 3 mana, then flip it face-up later for its morph cost) appeared across all five colors and all five clans. It served as the connective tissue that held the format together, providing:
   - Color-fixing insurance (a face-down creature costs generic mana)
   - Bluffing and hidden information
   - A shared mechanical language across all archetypes
   - Consistent board development regardless of archetype

3. **Clan centering on an ally color, not the enemy color.** Intuitively, wedges should center on the color that enemies the other two. But Tarkir's clans were centered on one of the allied colors instead (e.g., Abzan centered on white, not black). This was because the block's timeline-shift story required the clans to transition into two-color pairs in the third set (Dragons of Tarkir), and centering on an allied color made that transition smoother.

**Draft strategy:** Erik Lauer pointed out that wedge sets naturally push players toward enemy-color pairs early in the draft, because starting in an enemy pair (e.g., WB) leaves options open for which wedge to join (Abzan by adding G, or Mardu by adding R). Starting in an allied pair (e.g., WG) only leads to one clan (Abzan), reducing flexibility.

**Mana fixing:** At least one dual land appeared in every pack. Tri-lands (e.g., Frontier Bivouac for Temur) were powerful uncommons. The format could support ambitious five-color decks if a drafter committed to lands early, but this was a strategy with high variance.

**Lesson from Shards of Alara that Tarkir corrected:** Alara's factions were sometimes inconsistently synergistic with adjacent factions. Tarkir's enemy-color gold cards specifically addressed this by creating mechanical bridges between clans.

### Design Space Limitation

Rosewater has noted that three-color design space is inherently limited. There are not enough distinct three-color card designs to sustain an entire block focused exclusively on three-color cards. Both Alara and Tarkir addressed this: Alara's second set (Conflux) pivoted to a five-color theme, and Tarkir's block structure deliberately avoided drafting two three-color sets together.

---

## 6. Faction vs. Non-Faction Sets

### What Makes a Faction Set

A **faction set** groups cards into named, flavorful factions with distinct mechanical and creative identities. Factions are identified by watermarks, unique keywords, dedicated legendary creatures, and a shared aesthetic.

**Examples of faction sets:**
| Set | Factions | Type |
|---|---|---|
| Original Ravnica block | 10 guilds | Two-color |
| Shards of Alara | 5 shards | Three-color allied |
| Khans of Tarkir | 5 clans | Three-color wedge |
| Strixhaven | 5 colleges | Two-color enemy |
| Streets of New Capenna | 5 families | Three-color allied |
| Ixalan | 4 tribes | Mixed colors |
| Innistrad | 5 monster types | Tribal + color-based |

### What Non-Faction Sets Do Instead

A **non-faction set** uses unnamed mechanical themes. The 10 two-color archetypes exist but are not associated with named groups, watermarks, or specific lore factions.

**Examples:** Dominaria United, Brothers' War, Bloomburrow, Foundations, Zendikar Rising, Theros Beyond Death.

In these sets, the archetypes are communicated purely through mechanics, signpost uncommons, and as-fan density -- not through named identity.

### Trade-Offs

| Consideration | Faction Sets | Non-Faction Sets |
|---|---|---|
| **Player engagement** | Very high -- names and lore create identity and allegiance | Lower -- archetypes are less memorable |
| **Draft clarity** | Extremely clear -- "I'm drafting Dimir" is unambiguous | Relies on mechanical literacy to identify archetypes |
| **Design constraint** | Heavy -- each faction needs a unique mechanic, keyword, and creative identity | Lighter -- mechanics can be shared more freely |
| **Flexibility** | Lower -- committing to factions locks in structure early | Higher -- archetypes can shift during design |
| **Repeat visit potential** | High -- players want to return to factions they love | N/A -- each set is standalone |
| **Cross-faction play** | Must be designed carefully or drafts feel locked-in | Natural -- monocolor cards flow between archetypes |
| **Mechanic budget** | Consumed quickly (one keyword per faction = 5-10 keywords) | Standard 3-6 named mechanics |
| **World-building** | Factions define the world and its conflicts | World defined by other means (geography, history, etc.) |

### When to Use Factions

Use named factions when:
- The world's identity is defined by the relationships between groups
- You want players to feel allegiance to a specific color combination
- The set's marketing benefits from identifiable, nameable groups
- You are willing to invest the mechanic budget (one unique keyword per faction minimum)

Use unnamed themes when:
- The set's identity comes from a mechanical concept (e.g., "artifacts matter," "graveyard matters") rather than group conflict
- You want maximum flexibility for the 10 archetypes to share mechanics
- The world is defined by something other than factions (geography, history, single-culture stories)
- You need to conserve mechanic budget for set-wide keywords

### The Ravnica Lesson on Faction Identity

Ravnica established that **flavoring cards that belong together as belonging together in story** helps players intuitively draft correctly. When a card has a Dimir watermark and says "Surveil," players instinctively combine it with other Dimir cards. This is a communication tool that non-faction sets must replace with other signals (like signpost uncommons and as-fan density).

---

## 7. Common Set Themes

A catalog of recurring mechanical themes that appear across Magic sets, with notes on which colors traditionally support them and historical examples.

### Tribal / Typal

**What it is:** Cards that care about specific creature types. "Whenever you cast an Elf spell" or "Elves you control get +1/+1" are tribal payoffs. The enablers are simply creatures of the relevant type.

**Colors and typical creature types:**
- **White:** Soldiers, Knights, Humans, Angels, Cats
- **Blue:** Wizards, Merfolk, Spirits, Faeries, Birds
- **Black:** Zombies, Vampires, Skeletons, Rats, Demons
- **Red:** Goblins, Dragons, Elementals, Warriors
- **Green:** Elves, Beasts, Dinosaurs, Treefolk, Insects

**Historical examples:**
- Onslaught block (2002): The original "all-tribal" block with Soldiers, Wizards, Zombies, Goblins, Elves, and Beasts
- Lorwyn/Shadowmoor block (2007-2008): Deep tribal design with eight creature types and "changeling" as glue
- Innistrad (2011): Monster tribal -- Humans (GW), Spirits (WU), Zombies (UB), Vampires (BR), Werewolves (RG)
- Ixalan (2017): Four-faction tribal -- Vampires (WB), Merfolk (GU), Pirates (UBR), Dinosaurs (RGW)

**Design consideration:** Tribal is inherently **linear** -- it demands a critical mass of the specific creature type to function. This means tribal themes need high as-fan at common and careful density management.

---

### Graveyard Matters

**What it is:** Cards that gain value from cards in the graveyard, whether through recursion (bringing cards back), threshold effects (bonuses for having enough cards in the graveyard), or delve-style cost reduction.

**Colors:**
- **Primary:** Black (recursion, reanimation), Green (recursion of creatures and lands)
- **Secondary:** Blue (self-mill, flashback), Red (phoenixes, impulsive effects)
- **Tertiary:** White (recursion of small creatures and enchantments)

**Specific mechanics:** Flashback, Delve, Undergrowth, Escape, Disturb, Descend, Delirium, Threshold, Morbid, Embalm, Eternalize, Unearth

**Historical examples:**
- Odyssey block (2001): The first graveyard-centric block, with Threshold and Flashback
- Innistrad (2011): Graveyard as a core theme alongside tribal horror
- Theros Beyond Death (2020): Escape mechanic -- exile cards from graveyard to recast spells
- Innistrad: Midnight Hunt/Crimson Vow (2021): Disturb, Decayed, Flashback

**Design consideration:** Graveyard themes require **self-mill enablers** at common (cards that put cards from your library into your graveyard). Without sufficient self-mill, the graveyard never fills, and payoffs are stranded. The ratio of enablers to payoffs is critical.

---

### Artifacts Matter

**What it is:** Cards that reward you for controlling, casting, or sacrificing artifacts. Also includes artifact-centric themes like Equipment, Vehicles, and artifact tokens (Treasures, Clues, Food, Powerstones, Blood).

**Colors:**
- **Primary:** Blue (artifact synergy, Thopters), Red (artifact sacrifice, improvise)
- **Secondary:** White (Equipment synergy, artifact creatures), Black (artifact sacrifice)
- **Tertiary:** Green (artifact destruction, though Kaladesh gave green artifact synergy)
- **Colorless:** Artifacts are inherently available to all colors

**Historical examples:**
- Mirrodin block (2003): The original "artifacts matter" block -- so powerful it broke Constructed
- Kaladesh block (2016): Energy, Vehicles, artifact synergy with an optimistic inventor aesthetic
- Brothers' War (2022): Powerstones, artifact creatures, Prototype (reduced-cost artifact creature mode)
- Kamigawa: Neon Dynasty (2022): Artifacts AND enchantments as dual themes

**Design consideration:** Artifact tokens (Treasure, Clues, Food, Blood, Powerstones, Map) are one of the most powerful design tools for artifact themes because they can be created by any color at common, providing universal enablers without requiring an artifact-heavy card set.

---

### Enchantments Matter

**What it is:** Cards that reward you for controlling, casting, or being enchanted by enchantments. Includes Aura-specific themes and enchantment creatures.

**Colors:**
- **Primary:** White (enchantment synergy, Aura support), Green (enchantment synergy, constellation)
- **Secondary:** Blue (enchantment creatures in Theros), Black (enchantment creatures in Theros and Duskmourn)
- **Tertiary:** Red (least natural fit, but can be made to work)

**Historical examples:**
- Theros block (2013): Constellation (triggers when an enchantment enters the battlefield), enchantment creatures, bestow Auras
- Theros Beyond Death (2020): Return of Constellation, enchantment creatures
- Kamigawa: Neon Dynasty (2022): Enchantments as "tradition" half of the tradition-vs-technology theme
- Duskmourn: House of Horror (2024): Enchantment creatures and Rooms (a new enchantment subtype)

**Design consideration:** Enchantments matter requires **enchantment density** at common. Standard sets do not have enough enchantments to support a "cares about enchantments" theme unless the set includes enchantment creatures or other ways to add enchantment types to permanents that would otherwise not be enchantments (like turning spells into Auras or creating enchantment tokens).

---

### Lands Matter / Landfall

**What it is:** Cards that trigger or improve when lands enter the battlefield, or care about the number/type of lands you control.

**Colors:**
- **Primary:** Green (land searching, ramp, land synergy), Red (landfall aggression)
- **Secondary:** White (landfall tokens), Blue (landfall card draw), Black (landfall drain)
- **Note:** Landfall is distributed across all colors but concentrated in green

**Related mechanics:** Landfall, Domain, Converge

**Historical examples:**
- Zendikar block (2009): The original "lands matter" block, with Landfall as the signature mechanic
- Battle for Zendikar (2015): Return of Landfall alongside Allies
- Zendikar Rising (2020): Third visit to Landfall, with modal double-faced cards that were spells on one side and lands on the other
- Dominaria United (2022): Domain (rewarding you for controlling different basic land types)

**Design consideration:** Landfall is one of the most **modular** mechanics in Magic -- it triggers from something every player does every turn (playing a land), so it requires almost no dedicated enablers. Extra land drops and land-fetching spells amplify it but are not required. This makes it excellent as a low-maintenance set theme.

---

### Tokens Matter

**What it is:** Cards that create creature tokens, and cards that reward you for having or sacrificing tokens. Includes both creature tokens and artifact tokens.

**Colors:**
- **Primary:** White (Soldier tokens, 1/1 tokens), Green (Beast tokens, Saprolings, large tokens)
- **Secondary:** Red (Goblin tokens, Elemental tokens), Black (Zombie tokens, Rat tokens)
- **Tertiary:** Blue (Thopter tokens, Illusion tokens)
- **Artifact tokens:** Treasure (any color, primarily Red/Black), Clue (primarily Blue/Green), Food (primarily Green/Black), Blood (primarily Black/Red)

**Historical examples:**
- Selesnya guild across all Ravnica sets: Token generation as a primary identity
- Innistrad sets: Zombie tokens, Spirit tokens, Human tokens
- Throne of Eldraine (2019): Food tokens as an artifact token type
- Ixalan (2017): Treasure tokens introduced as a universal resource

**Design consideration:** Token themes naturally support sacrifice, go-wide, aristocrats, and artifact-matters strategies. They are among the most versatile themes because tokens simultaneously serve as creatures, artifacts (in the case of Treasure/Clue/Food), and sacrifice fodder.

---

### +1/+1 Counters Matter

**What it is:** Cards that place +1/+1 counters on creatures, and cards that reward you for having creatures with counters.

**Colors:**
- **Primary:** Green (growing creatures, Hydras), White (bolster, support, small-creature buffs)
- **Secondary:** Blue (adapt, evolve), Black (wither synergies, undying)
- **Tertiary:** Red (riot, unleash)

**Historical examples:**
- Ravnica: Simic (evolve), Abzan (outlast), Ozolith-style strategies
- Innistrad: Midnight Hunt: Coven (caring about different power values, enabled by counters)
- Ikoria (2020): Keyword counters placed on creatures
- Kamigawa: Neon Dynasty: "Modified" creatures (includes having counters)

**Design consideration:** +1/+1 counters are one of Magic's most versatile tools because they can be added to any creature. They serve as rewards, enable threshold checks, and interact with numerous mechanics. However, R&D avoids mixing +1/+1 and -1/-1 counters in the same set to prevent tracking confusion.

---

### Lifegain Matters

**What it is:** Cards that gain life, and cards that trigger or improve when you gain life.

**Colors:**
- **Primary:** White (Lifelink creatures, life-total-matters cards), Black (drain effects, paying life then regaining it)
- **Secondary:** Green (lifegain riders on creatures)
- **Tertiary:** Blue (rarely), Red (rarely)

**Typical color pair:** WB (Orzhov) is the most common home for lifegain matters.

**Historical examples:**
- Ajani's Pridemate: The archetypal lifegain payoff (grows with each life gain instance)
- Strixhaven: Witherbloom (BG) used lifegain as its primary theme with Dina, Soul Steeper
- Foundations: WB lifegain with Fiendish Panda

**Design consideration:** Lifegain is naturally modular -- many cards incidentally gain life. The challenge is creating enough **payoffs** that make "gain life" matter strategically, rather than just being a minor bonus. Without strong payoffs, lifegain is not a real archetype.

---

### Instants and Sorceries Matter (Spellslinger)

**What it is:** Cards that reward you for casting instants and sorceries. Includes Prowess, Magecraft, and "whenever you cast a noncreature spell" triggers.

**Colors:**
- **Primary:** Blue (card draw, counterspells, cantrips), Red (burn spells, impulsive draw)
- **Secondary:** White (cantrips in some sets), Black (removal spells count)
- **Typical color pair:** UR (Izzet) is the definitive spellslinger pair

**Historical examples:**
- Every modern set gives UR a spellslinger identity
- Strixhaven: Prismari (UR) focused on "big spells" with Magecraft
- Prowess was an evergreen keyword from 2014-2020 before being retired to deciduous

**Design consideration:** Spellslinger archetypes face a tension in limited: they want to cast many noncreature spells, but limited decks need creatures to win. Designers must include creature-payoffs (like Third Path Iconoclast, which makes tokens when you cast noncreature spells) so the archetype can maintain board presence.

---

### Sacrifice / Aristocrats

**What it is:** Cards that sacrifice permanents for value, and cards that trigger when creatures (or other permanents) die. Named after the Constructed deck "The Aristocrats" built around Cartel Aristocrat and Falkenrath Aristocrat.

**Colors:**
- **Primary:** Black (sacrifice outlets, death triggers), Red (sacrifice for damage)
- **Secondary:** White (token generation as sacrifice fodder, Afterlife-style effects)
- **Typical color pair:** BR (Rakdos) or WB (Orzhov)

**The three components:**
1. **Sacrifice outlets** -- cards that let you sacrifice creatures (e.g., "Sacrifice a creature: deal 1 damage")
2. **Death triggers** -- cards that reward you when creatures die (e.g., "Whenever a creature you control dies, drain 1")
3. **Fodder** -- disposable creatures or tokens to sacrifice (Zombie tokens, Decayed tokens, Servo tokens)

**Historical examples:**
- Innistrad sets: Death triggers across BR and WB
- Brothers' War: BR Sacrifice was the best archetype in the format
- Kamigawa: Neon Dynasty: BR Artifact Sacrifice
- Ravnica Allegiance: Afterlife (creatures that make Spirit tokens when they die)

**Design consideration:** Aristocrats requires all three components (outlets, triggers, and fodder) to function. If any component is missing at sufficient density, the archetype falls apart. Designers must ensure all three are present at common.

---

### Additional Recurring Themes

**Auras/Equipment Matter:** Caring about attaching Auras or Equipment to creatures. Primary in White, secondary in Red. Examples: Theros (Heroic/Auras), Zendikar Rising (Equipment), original Mirrodin (Equipment).

**Energy:** A resource counter that players accumulate and spend. Primary in all colors but concentrated differently per set. Examples: Kaladesh block (2016-2017), Modern Horizons 3 (2024).

**Cycling/Discard Matters:** Caring about discarding cards or cycling. Primary in Blue and Red. Examples: Amonkhet (2017), Ikoria (2020).

**Domain/Converge:** Caring about controlling different basic land types. Primary in Green (land searching) with payoffs across all colors. Examples: Dominaria United (2022), Invasion block (2000).

**Voting/Choice Mechanics:** Cards that present choices. Less of a "theme" and more of a design tool. Examples: Conspiracy sets.

**Historic Matters:** Caring about legendary permanents, artifacts, and Sagas. Example: Dominaria (2018).

**Modified Creatures:** Caring about creatures that have been modified (equipped, enchanted, or given counters). Example: Kamigawa: Neon Dynasty (2022).

---

## 8. Archetype Speed

### Why Speed Diversity Matters

A healthy limited environment requires a range of speeds across its archetypes. If all ten archetypes are the same speed, games become predictable and the format loses strategic depth. The aggro-midrange-control triangle provides natural tension:

- **Aggro** beats **control** (kills before the control deck stabilizes)
- **Control** beats **midrange** (outvalues it in the long game)
- **Midrange** beats **aggro** (bigger creatures stonewall the aggressive start)

This rock-paper-scissors dynamic ensures no single strategy dominates, and players must adapt their approach based on what they face.

### The Recommended Speed Distribution

Per Rosewater's Nuts & Bolts #15, designers should aim for a mix across the ten archetypes:

- **3 fast archetypes** (aggro)
- **3 medium archetypes** (midrange)
- **3 slow archetypes** (control)
- **1 archetype** goes in whichever category needs a fourth

This distribution ensures each speed category has multiple representatives so that multiple drafters can share a strategy without completely cannibalizing each other's picks.

### Which Color Pairs Default to Which Speed

**Typically Aggro:**
- **RW (Boros):** Almost always the fastest deck in the format. Goes wide, attacks early, punishes stumbles.
- **BR (Rakdos):** Aggressive with sacrifice value. Can be midrange but defaults to fast.
- **RG (Gruul):** Aggressive with larger creatures. Sometimes midrange-leaning, but the default is to attack.

**Typically Midrange:**
- **BG (Golgari):** The quintessential midrange archetype. Trades resources, recurs value, grinds.
- **GW (Selesnya):** Often goes wide with tokens and counters. Can be aggressive but usually midrange.
- **WB (Orzhov):** Attrition-based, trading life and creatures for value. Speed depends on the specific implementation.

**Typically Control:**
- **UB (Dimir):** Card advantage, removal, and inevitability. Almost always the slowest or second-slowest deck.
- **WU (Azorius):** Evasive creatures backed by interaction. Tempo-oriented rather than true control, but slower than aggro.
- **GU (Simic):** Ramp into large threats. Slow by nature because it spends early turns developing mana rather than attacking.

**Variable:**
- **UR (Izzet):** Can be fast (Prowess aggro) or slow (big spells control). Speed depends heavily on the set's specific implementation.

### The Danger of Speed Imbalance

**Zendikar (2009)** is a cautionary example. The format was extremely fast due to aggressive Landfall creatures, and there were not enough cards printed to punish the aggro strategy. Players who wanted to draft slower decks had no viable tools to do so, leading to widespread frustration. The lesson: every speed must have tools available, and aggressive strategies must have answers that slower decks can draft.

**The "fun police" role:** Aggro serves as the format's speed regulator. Without viable aggressive decks, greedy multicolor decks and slow control strategies dominate unchecked. One or two aggressive archetypes must be strong enough to punish decks that spend too long setting up. Boros typically fills this role.

### How to Push Speed Variation

- **Aggro archetypes** need: cheap creatures (1-2 mana value), haste, combat tricks, efficient burn/removal, reach (ways to deal the last few points of damage)
- **Midrange archetypes** need: efficient creatures at 3-4 mana value, removal, card advantage, value on death/ETB
- **Control archetypes** need: high-toughness blockers, card draw, unconditional removal, board wipes (at uncommon+), win conditions that end games

---

## 9. Supporting Themes at Common

### Why Common Matters

Mark Rosewater's foundational principle: *"If the theme of your set isn't in common, it isn't your theme."*

Commons appear in every booster pack and make up the majority of a limited player's card pool. A theme that exists only at uncommon or rare will not show up consistently enough to be a real draft archetype. Every archetype must have its core pieces available at common.

### Enablers vs. Payoffs

Every synergy-based archetype consists of two categories of cards:

**Enablers** are cards that make the archetype function. They are the fuel.
- In a graveyard deck, self-mill creatures and cheap creatures that die easily are enablers.
- In a spellslinger deck, cheap instants and sorceries are enablers.
- In a tokens deck, cards that create tokens are enablers.

**Payoffs** are cards that reward you for having enablers. They are the engine.
- In a graveyard deck, Threshold creatures or cards that get stronger with cards in the graveyard are payoffs.
- In a spellslinger deck, Prowess creatures and "whenever you cast an instant or sorcery" cards are payoffs.
- In a tokens deck, anthem effects and "whenever a creature enters the battlefield" triggers are payoffs.

### The Enabler-to-Payoff Ratio

The recommended ratio is approximately **2:1 enablers to payoffs** in a drafted deck. A typical limited deck will have:
- **2-5 payoff cards**
- **3-8 enabler cards**

This ratio implies design-level density targets:
- **Enabler as-fan:** Approximately 6/9 of a card per pack (enablers are weaker individually and can be picked up later in drafts)
- **Payoff as-fan:** Approximately 4/9 of a card per pack (payoffs lean toward uncommon because they are stronger cards that get picked earlier)

Why the enabler as-fan is not a strict 2:1 relative to payoff as-fan: enablers tend to be less contested in draft because they are individually weaker. A self-mill creature is not exciting on its own. This means enablers wheel (come back around the table) more often, so each drafter naturally accumulates more enablers than payoffs.

### "Bosses" vs. "Leaders"

Within the enabler/payoff framework, there is a useful subcategory distinction:

**Bosses** are payoff cards that sit passively and wait for other cards to do the work. They reward the archetype's theme but do not contribute to it themselves. Example: A card that says "Whenever you gain life, put a +1/+1 counter on this creature" is a boss -- it benefits from lifegain but does not itself gain life.

**Leaders** are cards that both contribute to the theme AND benefit from it. Example: A card that says "Lifelink. Whenever you gain life, put a +1/+1 counter on this creature" is a leader -- it gains life (enabling other payoffs) while also growing from lifegain triggers.

Leaders are better **glue** for ensuring sufficient density of a theme, but bosses provide stronger **incentives** to pursue the archetype. The best archetype designs include both.

**Payoff-enablers** (cards that function as both) are extremely valuable because they take up one slot but count toward both categories.

### The As-Fan Question

**As-fan** measures how many copies of a card type or mechanic appear in an average booster pack.

**Calculation basics:**
- A common appears in roughly 1 of every 4-5 packs (depending on set size)
- An uncommon appears in roughly 1 of every 8-10 packs
- As a rough rule of thumb, uncommons count as approximately half a common for as-fan purposes

**The scaling vs. threshold distinction:**
- **Scaling mechanics** get better the more you have (e.g., +1/+1 counters -- every additional counter matters). These need **higher as-fan** because each additional card adds incremental value.
- **Threshold mechanics** need a specific amount and then reward you (e.g., Delirium -- four card types in graveyard). These need **lower as-fan** because once you hit the threshold, additional enablers provide diminishing returns.

The more a mechanic leans toward scaling, the higher its as-fan needs to be. The more it leans toward threshold, the lower you can get away with.

### Minimum Support at Common Per Archetype

Under the Play Booster structure (81 commons, 100 uncommons), each two-color archetype should have at minimum:
- **2 monocolor commons** supporting the archetype (one in each color)
- **2 monocolor uncommons** supporting the archetype (one in each color)
- **2 multicolor uncommon signposts** (one enabler, one payoff)

This gives each archetype a floor of 6 dedicated support cards, plus whatever set-wide mechanics naturally feed into the archetype.

However, six dedicated cards is a **minimum, not a target.** Strong archetypes often have 10-15+ cards that contribute to the strategy when you include monocolor cards that incidentally support the theme.

### Concentrating Mechanics in Fewer Colors

A key technique from Rosewater's Nuts & Bolts #12: to increase the density of a mechanic where it appears, concentrate it in fewer colors rather than spreading it thin across all five. If a "graveyard matters" theme appears in all five colors, each color gets only a few cards. If it appears in only black and green, those two colors get many graveyard cards, and the mechanic will be well-supported in the BG archetype.

This is why most sets concentrate their signature mechanics:
- Flashback appears in all colors but is concentrated in blue and green
- Morph appears in all colors but at varying densities
- Prowess appeared almost exclusively in blue and red

### The Role of "Glue" Cards

**Glue cards** bridge between archetypes. They are cards that serve double duty, supporting two or more different archetypes simultaneously. A creature that mills cards when it enters the battlefield is glue between a self-mill archetype (UB graveyard) and a spellslinger archetype (if it is an instant or sorcery trigger enabler).

The best sets are built with extensive glue:
- **Fabricate** in Kaladesh was glue between the "+1/+1 counters" theme and the "tokens/artifacts" theme, because it let you choose between getting a counter or getting a Servo token.
- **Decayed Zombie tokens** in Midnight Hunt were glue between the Zombie tribal deck (UB), the sacrifice deck (WB Aristocrats), and the go-wide strategy (token-based).

When evaluating a set's archetype structure, look for opportunities where one card can serve multiple archetypes. Cards that are only useful in one archetype ("narrow" cards) reduce draft flexibility and risk leaving players stranded if their archetype is overdrafted.

### Modularity vs. Linearity at Common

From Nuts & Bolts #12, every mechanic falls somewhere on the modularity-linearity spectrum:

**Modular mechanics** (e.g., flying, flashback, cycling) work independently. A flashback card is good in any deck -- you cast it once, then cast it again later. No other cards are required to make it function.

**Linear mechanics** (e.g., tribal, constellation, Slivers) require specific other cards to function. A "lord" that gives +1/+1 to all Elves is useless without Elves. Constellation does nothing without enchantments to trigger it.

**At common, lean toward modular.** Commons need to be useful in the widest possible range of decks. Highly linear commons (that are dead outside their archetype) reduce the number of playable cards for players not in that archetype, which makes the draft experience worse.

**At uncommon, linearity is acceptable.** Uncommons are where build-around payoffs and archetype-specific rewards live. Signpost uncommons are intentionally linear -- they reward one archetype specifically.

**At rare and mythic, any level of linearity is fine.** Players expect rares to be powerful but potentially narrow.

The ideal common for archetype support is a card that:
1. Is perfectly playable in any deck of its color (modular floor)
2. Becomes notably better in the archetype it supports (linear ceiling)

Example: A 2/2 creature for 2 mana that mills two cards when it enters the battlefield. Any deck plays a 2/2 for 2. But the graveyard deck gets extra value from the mill.

---

## Sources

**Primary sources (Mark Rosewater's Nuts & Bolts series):**
- Nuts & Bolts #12: Limited Mechanics -- modularity vs. linearity, as-fan, concentration
- Nuts & Bolts #15: Structural Support -- archetype design, speed balance, enablers vs. payoffs
- Nuts & Bolts #16: Play Boosters -- updated signpost structure, 20 multicolor uncommons
- Nuts & Bolts #18: Layering Your Mechanics -- mechanic interaction, Fabricate as glue

**Faction design:**
- Mark Rosewater, "Faction Packed" (2018) -- faction set principles and trade-offs

**Historical archetype data compiled from draft guides for:**
Foundations, Final Fantasy, Bloomburrow, Aetherdrift, Lost Caverns of Ixalan, Lord of the Rings, Modern Horizons 3, Wilds of Eldraine, Brothers' War, Dominaria United, Kamigawa: Neon Dynasty, Innistrad: Midnight Hunt, Strixhaven, Streets of New Capenna, Guilds of Ravnica, Ravnica Allegiance, Khans of Tarkir, Shards of Alara

**Archetype design theory:**
- MTGNexus, "So You Want to Build a Set: Draft Archetypes"
- Riptide Lab, "Bosses vs. Leaders: A Dichotomy in Archetype Definers"
- Color Pair Building Blocks (Wizards of the Coast, 2015)
