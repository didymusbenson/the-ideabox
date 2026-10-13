# Unbelievable — Design Log

Running journal of design decisions and their rationale. When we change a mechanic, cut a card, shift an archetype, or make any significant design choice, it gets logged here with the reasoning. Prevents re-litigating settled decisions across conversations.

**Format:** Date, decision, rationale, what it affects.

---

## Log

### 2026-02-27 — Project Setup
- **Decision:** Established project structure with 7 set documents and 8 reference documents.
- **Rationale:** Reference library built from 30+ Mark Rosewater articles to provide expert-level design grounding.
- **Affects:** All future design work references this library.

---

### 2026-02-27 — Set Identity & Faction Structure
- **Decision:** Committed to core concept "Magic players rule an isekai plane." Five MTG player archetypes (Spike, Timmy, Johnny, Vorthos, Mel) as shard-aligned legendary characters. Each character owns one shard, giving them an enemy pair (core identity) and two allied pairs (shared borders with adjacent characters). All 10 two-color draft archetypes emerge from this structure. Natives are unfactioned — they populate the world across all colors without their own faction identity.
- **Rationale:** Shards over wedges because the two strongest archetype-to-color mappings (Timmy=RG, Johnny=UR) both land in shards. Shards over 10 separate factions for simplicity — 5 factions cover all 10 pairs with the allied-pair overlaps creating natural "border" archetypes. Follows the Shards of Alara model (proven structure). Natives stay unfactioned to avoid designing 10 factions.
- **Alternatives Considered:** (1) Each character = one two-color pair, needing 5 native factions for the other 5 pairs. Rejected for complexity. (2) Wedges instead of shards. Rejected because Timmy loses green and Johnny loses UR. (3) Allied pairs vs. enemy pairs (no three-color). Rejected because Timmy=RG and Johnny=UR split across allied/enemy — neither side is clean without three-color.
- **Affects:** worldBuilding-lore.md, worldBuilding-gameplay.md, draftArchetypes.md, setSkeleton.md (multicolor slots), mechanics.md (mechanic distribution across shards), cardFile.md (legendary creature slots).

---

<!-- Template for new entries:

### 2026-02-27 — Plane Name: Shandalark
- **Decision:** Plane named Shandalark. Aesthetic direction committed: unapologetically classic Magic high fantasy, not tied to any Earth mythology. The game itself is the source material.
- **Rationale:** Evokes Shandalar (existing MTG baseline-fantasy plane, never had a set) while being original. Isekai set needs a world that feels like *Magic* so the arrivals' game knowledge is meaningful. Celtic/Sumerian mythology explored and rejected — real-world mythology doesn't serve this set's identity, and Celtic is already well-covered in MTG (Lorwyn, Eldraine). Per fundamentals.md: "Commit to a focal point and build outward."
- **Alternatives Considered:** Ahndil (Celtic Annwn + Sumerian Dilmun portmanteau) — abandoned because blending two mythologies diluted both, and the set's resonance comes from Magic itself, not Earth cultures. Shandalar (the actual plane) — considered as holding name but carries continuity baggage.
- **Affects:** worldBuilding-lore.md (plane identity, aesthetic direction).

---

### 2026-02-27 — Mechanic: Forsake
- **Decision:** Committed Forsake as the set's first and primary keyword mechanic. "Forsake N — You lose N life and become forsaken. A forsaken player can't gain life." Forsaken is a permanent player designation (like the city's blessing). Cards can check "if you're forsaken" for payoffs.
- **Rationale:** Mechanically embodies the set's core isekai theme — irreversible commitment, giving up your old world for power. The two-part cost (immediate life loss + permanent restriction) creates meaningful risk/reward decisions. Wide design space via the N parameter, multiple usage patterns (cost, trigger, ability), and "if you're forsaken" payoffs. Modular — works independently but rewards building around it. Simple enough for common (binary status, no tracking). Per N&B #18: the mechanic that most embodies the set goes first in the layering order.
- **Affects:** mechanics.md (mechanic #1, layering priority #1), draftArchetypes.md (BR archetype primary mechanic).

**Addendum — Forsake assigned to BR (Rakdos / Johnny-Vorthos border).** Black primary, red secondary. Forsake is the mechanical home of BR's identity but not necessarily the complete build-around — "if you're forsaken" payoffs shape the reward structure while the archetype's play pattern remains open. Naturally bleeds into adjacent archetypes (UR, BG) through mono-black and mono-red cards.

---

### 2026-02-27 — Creature Type: Dinosaurs in Naya
- **Decision:** Dinosaurs committed as a primary, mechanically relevant creature type in Naya (RGW) — Timmy's tribe.
- **Rationale:** Dinosaurs are the most resonant tribe for Timmy's identity (big creatures, spectacle, raw power). Already perfectly color-aligned in RGW from Ixalan precedent. Fits the set's "classic Magic high fantasy" aesthetic — Shandalark is a plane that has everything players expect from a Magic world, and Dinosaurs are now an established part of that palette.
- **Affects:** worldBuilding-lore.md (creature type palette), worldBuilding-gameplay.md (primary creature types), draftArchetypes.md (RW Timmy core, RG and GW border archetypes may have Dinosaur density), setSkeleton.md (creature type distribution), cardFile.md (Dinosaur creatures across RGW).

---

### 2026-02-27 — Creature Type: Wizards in Esper
- **Decision:** Wizards committed as a primary, mechanically relevant creature type in Esper (WUB) — Spike's tribe.
- **Rationale:** Spike as empire-builder and villain — the competitive player who recognizes that trained spellcasters following optimized strategy is the highest-EV path to dominance in a world that runs on MTG rules. Wizards are naturally concentrated in Blue and Black (the two heaviest Wizard colors historically), and White Wizards (battlemages, tacticians, war-mages) are well-established. Full shard coverage. Esper shares Grixis's villain energy through the UB overlap — both Spike and Johnny sit in villain-adjacent color space for different reasons (Spike through calculated ambition, Johnny through unpredictable experimentation).
- **Affects:** worldBuilding-lore.md (creature type palette), worldBuilding-gameplay.md (primary creature types), draftArchetypes.md (WB Spike core, WU and UB border archetypes may have Wizard density), setSkeleton.md (creature type distribution), cardFile.md (Wizard creatures across WUB).

---

### 2026-02-27 — Creature Type: Dragons in Jund
- **Decision:** Dragons committed as a primary, mechanically relevant creature type in Jund (BRG) — Vorthos's tribe.
- **Rationale:** Vorthos is the arrival with the deepest connection to the plane itself. Rather than conquering or exploiting, Vorthos befriends Shandalark's oldest and wisest inhabitants — Dragons with deep knowledge of the plane's history and nature. Dragons are Red primary with Black and Green secondary, perfectly matching Jund's color identity (Alara's Jund shard was literally dragon territory). Dragons are arguably the most quintessential Magic creature type, reinforcing the set's "unapologetically Magic" aesthetic. The relationship (friendship/alliance, not domination) distinguishes Vorthos from every other arrival's approach to power.
- **Affects:** worldBuilding-lore.md (creature type palette), worldBuilding-gameplay.md (primary creature types), draftArchetypes.md (BG Vorthos core, BR and RG border archetypes may have Dragon density), setSkeleton.md (creature type distribution), cardFile.md (Dragon creatures across BRG).

---

### 2026-02-28 — Creature Type: Zombies in Grixis
- **Decision:** Zombies committed as a primary, mechanically relevant creature type in Grixis (UBR) — Johnny's tribe.
- **Rationale:** Johnny's Zombies aren't mindless hordes — they're creations, prototypes, combo engines given form. Johnny builds and tinkers with the dead the way a combo player iterates through decklists. Each Zombie is an experiment in necromantic engineering. Zombies are Black primary with Blue secondary (Dimir Zombies have strong precedent: Innistrad, Amonkhet) and Red tertiary (Grixis shard from Alara was zombie territory). Full shard coverage. Thematically connects Johnny's "chain reaction chaos" story beat — the experiments that spiral out of control are literally walking around.
- **Affects:** worldBuilding-lore.md (creature type palette), worldBuilding-gameplay.md (primary creature types), draftArchetypes.md (UR Johnny core, UB and BR border archetypes may have Zombie density), setSkeleton.md (creature type distribution), cardFile.md (Zombie creatures across UBR).

---

### 2026-02-28 — Creature Type: Birds in Bant
- **Decision:** Birds committed as a primary, mechanically relevant creature type in Bant (WUG) — Mel's tribe. Birds on Shandalark are a mix of humanoid-bird hybrids (aarakocra/Rito-style avian people with arms, wings, and civilization) and actual birds (storm-riders, paradise plumagers, raptor sentinels).
- **Rationale:** Birds over Elementals — Elementals had the more direct thematic fit ("the system made manifest") but risked feeling generic. Birds provide: (1) strong WUG color coverage (Aven in WU, Birds of Paradise in G), (2) a distinct flying-swarm identity that no other arrival's tribe occupies, (3) natural predator/prey dynamic with Vorthos's Dragons (swarm of small flyers vs. individual bombs), (4) visual distinctiveness. The thematic connection to Mel works through perspective and emergent systems — flock behavior, migration patterns, and aerial perspective as expressions of structural understanding. The humanoid-bird hybrid angle (aarakocra/Rito) gives the tribe civilization and personality, while actual birds round out the creature type with simpler common-rarity designs.
- **Alternatives Considered:** Elementals — effortless color coverage and thematic directness, but risked feeling generic without a strong mechanical hook (Lorwyn needed Evoke to give them identity). Birds provide more built-in mechanical and visual identity.
- **Affects:** worldBuilding-lore.md (creature type palette), worldBuilding-gameplay.md (primary creature types, Mel's tribe decision resolved), draftArchetypes.md (GU Mel core, GW and WU border archetypes may have Bird density), setSkeleton.md (creature type distribution), cardFile.md (Bird creatures across WUG).

---

### YYYY-MM-DD — [Short Title]
- **Decision:** What was decided.
- **Rationale:** Why. Reference specific design principles if applicable.
- **Alternatives Considered:** What else was on the table and why it was rejected.
- **Affects:** Which documents/areas of the set this impacts.

-->
