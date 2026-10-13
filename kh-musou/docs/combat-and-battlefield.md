# Combat and battlefield

## Player-facing direction

Preserve a Kingdom Hearts-inspired action vocabulary, then arrange moves into musou input sequences.
Do not equate musou scale with a flat light-attack loop or sacrifice aerial movement to increase counts.
Exact controls, animation timings, damage, and move names are design decisions after observation.

| Layer | Prototype requirement | Evidence to collect |
|---|---|---|
| Movement | Responsive ground travel, jump, aerial steering and landing; coherent combat transitions | Stop/start/turn response, jump arc, attack movement, recovery and landing transitions |
| Ground attacks | A short input-buffered chain with distinct branches/finishers | Startup, active and recovery intervals, tracking, hitstop and interruption |
| Air attacks | An air chain and clear entry/exit into ground play | Launch eligibility, air control, fall behavior, juggle response and landing rules |
| Magic | At least one ranged interaction exercising distant targets | Cast window, projectile/area shape, travel and impact timing, interruption |
| Defense | Guard and an evasive option with deliberate state rules | Directionality, vulnerable windows, feedback, counter/recovery opportunities |
| Musou grammar | Ordered attack inputs select authored moves/finishers | Buffer rules, branch priority, held vs tapped input and state-dependent legality |

### Proposed data contract, not an extracted KH format

A move specification should contain a stable ID, input/eligibility conditions, animation reference,
movement policy, cancel/buffer windows, hit shapes, target filters, damage/status effects, hit reactions,
resource use, and recovery behavior. Keep gameplay hit timing explicit and testable. Decide whether
movement is animation/root-driven, code-driven, or hybrid through a measured animation spike. Do not
let animation LOD silently disable gameplay windows or require a full visible skeleton for all hit tests.

Test one-on-one feel before dense waves: startup readability, moving attacks, ground-to-air transitions,
guard feedback, repeated input, hits during turns, and missed attacks. Then repeat under crowd pressure.
A crowd system that changes player timing or drops valid hits is not an acceptable optimization.

## Battlefield layer

Campaign direction follows the Dynasty Warriors pattern of multiple fronts, allies, objectives, and
changing urgency. The prototype is intentionally smaller:

1. An ally tries to reach and hold a marked control point.
2. Enemies pressure the ally and point; the player can intercept or defeat them.
3. A reinforcement event changes the threatened approach and is communicated clearly.
4. The player wins by securing the point and keeping the ally alive through the encounter; failure is
   explicit if the ally is defeated. Numerical durations and spawn counts remain tuning variables.

This is a **proposed test scenario**, not a locked campaign formula or a claim about DW internals.
Every visibly represented reinforcement must become an actual entity. Do not display a fake army in
an unreachable backdrop to communicate scale. Spawn/despawn rules need authored, honest boundaries;
never delete an engaged or targeted enemy merely to control load.

## Scope gates

Only after the small slice passes should research expand into connected battlefields, competing
objectives, ally commands, commanders, progression, character rosters, or a campaign. No DW executable
decompilation is needed to prototype these high-level patterns. Multiplayer, open worlds, full KH
systems replication, and a complete commercial roster are outside the first proof.
