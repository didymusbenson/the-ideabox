# Kingdom Hearts Musou

**Working title. Status:** Research / planning; no implementation yet. **Engine:** Unreal Engine (version TBD). **Target:** PC.

A standalone action game interpreting **Kingdom Hearts × Dynasty Warriors**: the expressive movement,
aerial combat, magic, defenses, and recognizable Heartless encounters of Kingdom Hearts, organized
into a musou battlefield with combos, objectives, allies, and shifting pressure. This is not a mod or
a proposal to transplant a recovered commercial game into another engine.

## Non-negotiable

**Every visible enemy is a real, reachable, fightable entity.** There are no decorative, untouchable
hordes. An enemy may have a legitimate, readable defensive or temporarily invulnerable state; it may
not become immune merely because it is distant or outside the expensive simulation tier. Moving
toward it **or attacking it at long range** must produce the correct interaction with the same enemy.

Distance-based processing is allowed only if it preserves identity, position, relevant state, and
correct interactions. Scale, rendering quality, battlefield size, and roster breadth must yield to
this requirement rather than disguising its failure.

## Engine and platform decisions

The user selected **Unreal Engine** and **PC** on 2026-10-13. Windows is an initial-build assumption,
not an explicitly selected operating system. Exact Unreal version, minimum hardware, graphics budget,
input support and target frame rate remain open. The reference distribution is Steam, with exact
game/build still to verify. Development is planned on the user’s MacBook Pro, a separate machine
from the current secondary computer; Mac host and PC build target are distinct. These decisions authorize no installation or game
implementation by themselves. See the [engine record and validation gates](docs/engine-evaluation.md).

## Combat routes under consideration

- Three playable Keyblade Knights inspired by Terra, Ventus and Aqua, turning BBS command attacks
  into musou combos; Shotlock treatment remains open.
- Sora's KH2-inspired moveset, with longer-combo finishers and a possible timed Drive Form ultimate.

Neither route is selected. [Compare the routes](docs/combat-routes.md), including provisional mappings,
source-edition cautions and a suggested small comparison before full roster production.

## First playable proof

A small approved route slice (or a bounded comparison of the two routes); two contrasting,
research-verified Heartless behaviors; one compact battlefield and objective; and a genuinely interactive horde. Prove enemy fidelity, combat feel, and
measured performance before attempting a campaign. Begin with original/procedural placeholder assets.
The desired scope is a research direction, not a promise to reproduce either commercial series.

## Read next

- [Project charter](docs/charter.md): requirements, boundaries, and decision ownership
- [Combat routes](docs/combat-routes.md): three Knights versus Sora, payoff options and open decisions
- [Combat and battlefield](docs/combat-and-battlefield.md): player grammar and musou structure
- [Enemy fidelity](docs/enemy-fidelity.md): evidence and behavior specification workflow
- [Interactive horde](docs/interactive-horde.md): persistent entities and correctness tests
- [Toolchain research](docs/toolchain-research.md): OpenKH-first research and escalation limits
- [Engine record](docs/engine-evaluation.md): Unreal/PC decision, historical comparison and validation gates
- [Prototype plan](docs/prototype-plan.md): executable work packages and acceptance gates
- [Open questions](docs/open-questions.md): unresolved choices, explicitly not invented answers
- [Sources](docs/sources.md): evidence register and reproduction requirements
- [Notes](notes.md): signed feedback; keep the pitch intact

Research compiled 2026-10-13. No commercial assets or executables are included, and no extraction or
decompilation was performed for this planning pass.
