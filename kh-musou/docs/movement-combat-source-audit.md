# Sora movement and combat: source audit, 2026-10-14

The existing controller was a partial reconstruction. V06 imported the character, weapon, animation poses, collision tracks and portions of combat tables, while Unreal prototype code supplied movement and action interactions. Its passing checks did not establish KH2 controller fidelity. The user's movement complaints are valid evidence of that gap.

## Can the entire original script be imported?

No complete reusable Sora movement/combat script has been found in the inspected sources. This is a bounded finding, not a claim that reconstructing the original controller is impossible.

- Original P_EX100.mdlx contains BAR types 4/7/23; P_EX100.mset contains type17 motion containers; P_EX100.a.us contains types18/24/25. No BDX behavior entry is present in these three top-level archives. Soldier M_EX010.mdlx does contain type3 BDX (m_ex), demonstrating why enemy script extraction and Sora controller extraction are different tasks.
- The pinned KH2FM decompilation has declarations for ACTION_IDLE control/calc_movement, ACTION_JUMP control/calc_movement/land/fall, PARTYATTACK and CHOOSE_ATTACK. Their corresponding .cpp files contain only their include, not the controller implementations. player.cpp has only an empty lockon_end. The remote HEAD was checked and is still the inspected commit 8b5bc4790ac3fe951ffaf15b6933d186ebab7a43.
- OpenKH's PlayerManager.ProcessPlayer is a simple 500-unit movement and animation-selection demo. It does not provide KH2's attack controller.
- A read-only CLR metadata audit of the local Windows executable found 1816 types, 597 method definitions, 152 marked native and 439 IL bodies. Managed names include forms/viewer utilities; no Sora/player-action controller methods were found. CLR metadata therefore does not provide an entire managed Sora controller. The executable was not loaded, executed, patched or modified; native code recovery remains separate research.

References: [KH2FM decompilation](https://github.com/GovanifY/kh2/tree/8b5bc4790ac3fe951ffaf15b6933d186ebab7a43), [OpenKH animation event documentation](https://openkh.dev/kh2/file/anb/anb.html), [OpenKH player demo](https://github.com/OpenKH/OpenKh/blob/7a3b945c538d32c6a285128c98aefba093f52ceb/OpenKh.Game/Entities/PlayerManager.cs).

## V07 reconstruction batch

The private combat metadata now carries the complete range/frame event lists for every currently imported clip, alongside collision/root tracks. Unknown events and parameters remain available in the private JSON rather than being discarded. Runtime execution intentionally covers the currently documented subset; storing every event does not implement every event.

A shared action policy now governs locomotion, landing, grounded attacks, aerial attacks, reactions and death. It supplies movement/jump permission, turning permission, momentum/friction treatment, timed gravity flags, floor restriction, ground-leave continuity, hitbox-off and stop-actions. Combo timing preserves finite and disjoint source windows instead of treating the first opening as permission through the rest of the clip. The existing three-action chain and whiff confirmation rule remain.

Target turning follows ANB range22/28 and frame15/21 timing, with line-of-sight checks, rather than a single unconditional facing snap. Root travel still uses the existing swept capsule adapter, and flag29 rejects travel without a walkable floor. A grounded action leaving the floor is conservatively cancelled unless flag49 maintains it. This ground-leave transition is adapter policy pending native implementation proof.

PRTY and PLYR are offset tables indexed by the object's NeoMoveset, not flat records. Sora's NeoMoveset1 resolves PRTY byte284 and PLYR byte240. PRTY supplies run8, walk2, jump-height185 and turning0.2617994 radians; PLYR supplies first/combo/finisher air vertical values8/6/12. The runtime uses a documented 60-updates/s conversion for speeds, giving run480cm/s and air480/360/720cm/s. This conversion is inferred for the native physics fields; animation trigger timing itself is documented60Hz. Jump velocity is derived from the source apex height using Unreal's retained gravity, not a recovered original integrator.

Blanket aerial zero-velocity/zero-gravity behavior is removed. Gravity suspension now requires source range3/24; the selected basic aerial attacks do not contain those flags. Each aerial stroke receives its separate PLYR velocity value. Jump/fall/landing pose clocks start from the beginning of their own phase, so fall no longer inherits elapsed jump time.

## Still unverified or incomplete

- Native physics update/integration, gravity, acceleration, braking, air steering, jump hold, ceiling response and exact units/turn interpolation.
- Full PTYA Type/Sub/Flag scoring, hard lock-on, target retention and switching, distance adjustment, ground-to-air routes and dynamic action branching.
- Complete action cancellation priorities, native input buffer lifetime and held-input behavior, command-disable events and all animation flags.
- Native aerial impulse ordering/conditional application: values are source data; their current application is reconstruction.
- Knockback velocities, blow landing/recovery chain, hitstun, invulnerability, revenge and enemy AI. Soldier BDX is identified but not executed by a compatible VM.
- Analog walk animation/blending and source animation loop subranges; historical visual-prefix trims for jump/landing remain explicit offsets. Current walk-speed parameter is retained but a separate walk clip is not imported.
- Player death action and source effects/audio/facial animation.

The next fidelity work is recovery or measurement of the missing native action functions and a full transition matrix for the chosen level30 Kingdom Key build. Further isolated timing tweaks must not be described as a complete KH2 controller port. No manual acceptance has occurred for V05, V06 or V07.
