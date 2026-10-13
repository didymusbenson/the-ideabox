# Enemy fidelity and evidence

Recognizable Heartless are defined by behavior, not merely a model and hit points. Preserve a
researched enemy's movement signature, attack tells, attacks, defensive states, vulnerabilities,
interruptibility, and hit/death reactions. Musou adaptation may change encounter density and tuning;
record such changes instead of presenting them as faithful reproductions.

## First two candidates

Investigate **Shadow** and **Large Body** as contrasting candidates: a small mobile silhouette and a
large defensive silhouette. Their exact behavior, state names, guard rules, and vulnerable windows
are **unverified hypotheses here**, not accepted specifications. Replace a candidate if its chosen
edition lacks adequate observable/documented evidence. Names do not imply permission to redistribute
models, textures, animation, audio, or scripts.

## Research record for each enemy

Create one record per enemy and **per source edition/build**. KH2, KH2 Final Mix, different regions,
HD ports, and Birth by Sleep must not be treated as interchangeable.

- Source game, edition, region/platform, build/version and lawful source/provenance
- File/object identifiers, tool version/commit and extraction/parsing steps when later authorized
- State graph: entry conditions, transitions, exit conditions, timers and interrupt priorities
- Locomotion: acceleration, turning, range selection, ground/air interactions and recovery
- Attack: telegraph, facing/tracking, hit shape and timing, effect, cooldown and interruption
- Defense: guard direction, invulnerability/armor windows, valid counters, break/stagger behavior
- Hit reactions: small hit, stagger, launch, knockback, knockdown, recovery, death and simultaneous hits
- Evidence per rule: documentation URL, data field/script location, or recorded observation/timecode
- Confidence: documented / corroborated / inferred / unknown; separate implementation adaptation

An AI-generated explanation of bytecode, a decompiler function, or footage is a hypothesis. Require
human-readable evidence and reproduction; never accept convincing prose as proof.

## Verification ladder

1. Start with public documentation and source parsers; confirm the edition and actual supported fields.
2. When a lawful local source and tools are available, inspect relevant tables, animations and scripts.
3. Observe controlled encounters: approach angles, distances, attacks, blocks, launch attempts and
   repeated runs. Record what changed and what remained constant.
4. Cross-check the inferred transition or rule against script/data and observed results. Unknown
   native calls remain unknown until tested or inspected; a script disassembly alone is incomplete.
5. Implement a small independent behavior state machine using original placeholder assets.
6. Compare against a reference checklist; mark deliberate adaptations and unresolved discrepancies.

## Regression scenarios

Run each at sparse and dense counts, on flat ground and an obstacle route, in full and reduced-detail
simulation: idle→notice; approach→attack; player behind/to side; miss→recovery; hit during tell; guard
interaction; aerial/juggle interaction; magic at range; multiple simultaneous hits; death during tier
transition. Debug state and entity IDs should be visible to testers. A defensive state is allowed to
reject a hit only because of its documented rule, never because the enemy is cheap to simulate.
