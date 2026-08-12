# Physics & Sorcery

**Status:** Planning / prototype candidate

## Pitch

Build a small, copyright-clean strategy game inspired by the adventure-map loop of **Heroes of Might and Magic** and the large, chaotic battles of **Hero's Hour**—but make physical interaction the central mechanic rather than a visual flourish.

Heroes explore a compact overworld, capture resource sites, recruit stack-based armies, and fight battles where mass, momentum, terrain, knockback, projectiles, collapsing obstacles, and spell forces materially affect the outcome.

Working title: **Physics & Sorcery**.

## Design pillars

- **Fast strategy layer:** one small map, a few resources, towns, recruitment, and hero movement.
- **Readable army building:** units have clear battlefield roles and a small number of meaningful stats.
- **Physics creates stories:** charges break formations, explosions scatter light units, large creatures push through crowds, and terrain can redirect or amplify forces.
- **Short battles:** mostly automated combat with a small number of player-controlled spell or command interventions.
- **Original IP:** no copied names, factions, art, maps, UI, sounds, or rules text from either inspiration.

## MVP

1. One handcrafted adventure map with fog of war.
2. One player faction and one AI faction.
3. One town per faction, three unit tiers, and several neutral encounters.
4. Hero movement, resource collection, recruitment, and army-stack management.
5. One physics battlefield with:
   - melee and ranged units;
   - mass, impulse, knockback, and collision;
   - simple morale or routing;
   - two physics-based spells, such as push/pull and an explosive projectile.
6. Win by capturing the enemy town or defeating its hero.
7. Deterministic seeds and a battle replay/debug mode where practical.

## Proposed stack

Use **Godot 4** so the strategic layer and battle prototype can share one lightweight engine while preserving the option to use either 2D or 3D physics.

## Art-direction decision gate

Start with programmer art and run a short Blender-MCP spike before committing the project to 3D.

### Adopt stylized low-poly 3D only if the spike can reproducibly

- create and revise three visually coherent unit prototypes and several props;
- export them into Godot with correct scale, orientation, pivots, materials, and collision;
- produce one reusable animation workflow;
- regenerate or revise an asset without destructive manual repair;
- complete the round trip quickly enough that content production will not dominate the project.

Candidate tool: [`ahujasid/blender-mcp`](https://github.com/ahujasid/blender-mcp). It has straightforward `uvx` + Blender add-on setup and strong scene/blockout automation, but it exposes arbitrary Blender Python and its own documentation notes occasional connection and integration instability. Treat it as an assisted authoring tool, run it locally, pin versions, save before agent operations, and review every export.

If the spike fails any of the above, choose 2D. **2D is the default recommendation** because it better constrains the MVP and matches the large-unit-count battlefield.

## 2D Gemini asset pipeline

If 2D is selected, set up a reproducible Gemini-assisted pipeline rather than generating ad hoc sprite sheets:

1. Keep versioned faction style sheets, palettes, silhouettes, prompt templates, and negative constraints under `art/prompts/`.
2. Use the current image-capable Gemini model through Google's supported GenAI SDK; keep the model ID configurable rather than hard-coded.
3. Generate high-resolution source concepts or isolated key poses—not final sprite sheets.
4. Post-process automatically:
   - background removal / alpha cleanup;
   - crop and consistent canvas alignment;
   - scale normalization and palette reduction;
   - optional pixel-art downsampling;
   - contact-sheet and sprite-atlas packing.
5. Emit a manifest recording prompt hash, model/version, seed when available, source image, crop/pivot data, license/provenance notes, and final asset checksum.
6. Require human review for silhouette consistency, directional views, animation continuity, and faction identity.
7. Commit generated assets only after normalization; never require a live image API to run or test the game.

Reference: [Gemini image-generation documentation](https://ai.google.dev/gemini-api/docs/image-generation).

## Milestones

- [ ] **Spike A:** one battle with capsules/circles, two unit types, knockback, and one force spell.
- [ ] **Spike B:** test Blender MCP against the 3D acceptance criteria.
- [ ] **Decision:** lock 2D or 3D and document why.
- [ ] Build the selected asset pipeline; if 2D, implement the Gemini generation and normalization scripts.
- [ ] Add the minimal adventure map, town, recruitment, and encounter loop.
- [ ] Add AI, balance instrumentation, and one complete 20–30 minute scenario.
- [ ] Playtest whether physics changes tactics rather than merely producing chaos.

## Scope guards

- No procedural campaign, online multiplayer, elaborate story, or large faction roster in the first version.
- No autonomous bulk asset generation without review.
- Do not build the full strategy layer until the physics battle spike is genuinely fun and readable.
