# Alternate combat routes: three Knights or Sora

Updated 2026-10-13. **Both routes remain open.** This records the user's alternate design directions,
not a selected engine, approved implementation milestone, fixed input scheme, or measured combat result.
The [original brief](charter.md#original-brief) is preserved unchanged.

## User direction

### Route A — Birth by Sleep-inspired three playable Keyblade Knights

Build around **three playable Knights**, based on the archetypes represented by Terra, Ventus and Aqua.
Translate their specific iconic command attacks into appropriate musou combos:

- **Terra archetype:** heavy, strong-swing **Strike** attacks.
- **Ventus archetype:** **Raid** attacks built around throwing the Keyblade.
- **Aqua archetype:** magic-enhanced attacks.

These are design emphases supplied by the user, not claims that each command family is exclusive to
that BBS character. Whether the Knights are those named characters or original characters based on
their archetypes remains open. The route's intended playable roster is three; a smaller experiment
would be sequencing toward that vision, not a replacement for it.

BBS's command deck is a source vocabulary for the attacks. **Translating deck commands into combos
does not automatically retain an equipped deck, cooldowns, command melding, or command leveling.**
Those systems would need their own decision. Nor does this direction automatically select Command
Styles, D-Links, or a literal reproduction of BBS's entire battle system.

Each character has a Shotlock concept. Three alternatives remain open:

1. **Preserve a distinct Shotlock:** targeting/lock acquisition and the attack, with the applicable
   follow-up input behavior. Exact controls, availability and individual Shotlock rules need research.
2. **Combo-finisher Shotlock:** completing a chain opens its Shotlock-style ender and reaction-command
   follow-ups. “Reaction command” describes the proposed adaptation; do not assume every source
   Shotlock has KH2-style reaction-command mechanics.
3. **Charged ultimate:** reserve the attack for a charged resource or ultimate opportunity; decide
   whether targeting and follow-ups remain. No charge source, cost, threshold or recharge is selected.

### Route B — KH2-inspired Sora and longer combo finishers

Focus on **Sora's moveset**. Arrange normal attacks into musou chains, with recognizable finishers
serving as enders for longer combos. The user's “Stun Impact, etc.” example expresses the desired
finisher role; exact move provenance must remain distinct from the KH2 reference label (see below).

An ultimate could put Sora into a **temporary Drive Form**, with **Valor** the supplied example.
This proposes a sustained altered moveset window rather than requiring every ultimate to be a single
burst. Duration, meter, entry/exit rules, available forms and whether any source party/resource
requirements carry over are all undecided. Valor is an example, not a committed sole form.

## Side-by-side design comparison

These are design hypotheses and production considerations, not observations that one route is better.

| Dimension | Three Knights / BBS vocabulary | Sora / KH2 vocabulary |
|---|---|---|
| Core identity | Three distinct archetypes expressed through command-derived chains | One expressive base moveset with longer-chain enders and possible form changes |
| Immediate choices | Character-specific reach, commitment and magic/weapon patterns | Chain branch/length, ender selection and when to enter a temporary form |
| Big payoff | Shotlock targeting, combo follow-up, or charged ultimate; unresolved | A timed alternate moveset, such as Valor; exact ultimate design unresolved |
| Content burden | Three coherent movement/combat kits, animations and balance profiles | Base kit plus meaningful form kit(s), transition animation and transformed-state rules |
| Crowd opportunity | Strikes control space; Raids test ranged paths; magic adds varied attack shapes | Chains mix crowd management and focused damage; forms change sustained crowd handling |
| Main design risk | Archetypes blur if mapped to identical chains; deck baggage complicates inputs | Long chains become unsafe or repetitive; form activation eclipses base combat |
| Main correctness pressure | Throw return paths, multi-target locks and follow-up target validity | Ender targeting plus form-state transitions during hit, defense, landing and expiry |
| Research coverage | Model export and PAM → ANB conversion exist; complete command/Shotlock behavior still needs exact-edition evidence and original runtime | Existing KH2 data/AI tooling helps research, but does not prove the better player design |

**Decision ownership:** the user chooses the fantasy and roster direction. Research can establish
source behavior, tool compatibility, implementation cost and prototype outcomes. It cannot convert
more mature KH2 inspection tools into a decision against the BBS route. Player reference and enemy
reference can be evaluated separately; any cross-game adaptation must be labeled.

## Provisional translation sketches

These illustrate roles and questions, not a binding button layout, unlock order, numerical balance,
or a claim that a source command already functions as a musou combo. Specific move candidates must
pass the source/edition check before a final roster is authored.

| Archetype | Candidate sequence shape | Payoff and test question |
|---|---|---|
| Terra-like Knight | Short grounded setup → committed strong swing → Strike-derived ender | Readable weight and area control; does its recovery leave room for defense under crowd pressure? |
| Ventus-like Knight | Mobile setup → thrown-Keyblade Raid → return or pursuit branch | Ranged control without losing melee flow; does the same distant enemy take valid outbound/return hits? |
| Aqua-like Knight | Weapon setup → magic-enhanced branch → area or focused ender | Distinct magic/weapon expression; do hit shapes and effects remain readable and authoritative? |
| Sora | Ground/air chain → selected longer-chain finisher | A deliberate payoff for extending the chain; can the player reach it without mandatory damage trading? |
| Sora in temporary form | Ultimate entry → altered chain/defense rules → expiry | Sustained transformation payoff; are damage, movement and recovery continuous at entry/exit? |

Keep cancel opportunities, target selection and air/ground legality explicit. The longer route to a
finisher should be a meaningful choice, not simply “more presses always wins.” Do not silently bind
these sketches to light/heavy buttons or fixed sequence lengths before input experiments.

## Source provenance and named move candidates

Public reference descriptions are discovery aids; they do not replace controlled exact-build
observation, timing measurements, or evidence of successful conversion. Imported inspiration is
permitted as a design choice when labeled, rather than rewritten as canonical KH2 behavior.

### BBS command palette: source facts versus proposed roles

The entries below use game-specific KHWiki secondary references checked 2026-10-13. “Exclusive” here
means among Terra, Ventus and Aqua in BBS, not across the franchise. These are BBS commands, not
Final Mix-only additions. Pin the actual edition/platform before measuring them.

| Kit | Verified source example | Provisional musou role, not source behavior |
|---|---|---|
| Terra | [Ars Solum](https://www.khwiki.com/Ars_Solum): exclusive multi-hit melee sequence with prompted continuation | Committed heavy chain with deliberate follow-up timing |
| Terra | [Meteor Crash](https://www.khwiki.com/Meteor_Crash): exclusive leaping slam with meteors | Strong slam ender and area payoff |
| Terra | [Windcutter](https://www.khwiki.com/Windcutter): exclusive spinning whirlwind attack | Crowd sweep / launcher branch |
| Ventus | [Strike Raid](https://www.khwiki.com/Strike_Raid): returning throw, **shared by all three**; Ventus starts with it | Foundation of a throw-oriented branch |
| Ventus | [Wind Raid](https://www.khwiki.com/Wind_Raid): exclusive guided, multi-hit throw | A ranged branch that tracks moving targets |
| Ventus | [Spark Raid](https://www.khwiki.com/Spark_Raid): exclusive throw that releases light beams on connection | Crowd-spreading throw ender |
| Aqua | [Barrier Surge](https://www.khwiki.com/Barrier_Surge): exclusive barrier-covered forward rush that deflects attacks | Advancing magic-enhanced branch; defense windows need explicit tuning |
| Aqua | [Magic Hour](https://www.khwiki.com/Magic_Hour): exclusive teleporting dives/light pillars with prompted continuation | Elaborate light-based ender |
| Aqua | [Triple Firaga](https://www.khwiki.com/Triple_Firaga): exclusive three-fireball spell | Spell-volley branch |

This palette supports the user's archetypes without asserting that Terra has no ranged tools or that
Ventus lacks fast melee. Command-deck attacks, Command Styles, Shotlocks and Finish Commands are
separate source systems; converting a deck attack into a musou chain ender is an intentional adaptation.

### Shotlock source mechanics and adaptation boundary

BBS Shotlocks use targeting to acquire locks before release. Reaching the maximum lock count enables
additional prompted attacks; the input varies by Shotlock rather than following a universal prompt.
Many Shotlocks are shared, while some are character-specific. Platform controls differ, so no single
button binding is prescribed here. Source descriptions do not establish KH3-style targeting slowdown
for BBS. [Shotlock reference](https://www.khwiki.com/Shotlock)

Use **Shotlock-specific prompted follow-ups** in evidence records. The user's suggested reaction
commands can name the adaptation, but should not silently conflate this with KH2's named Reaction
Command system. Finisher or ultimate conversion must decide target acquisition and follow-up rules.
All three alternatives above remain open.

### Sora examples and the Stun Impact edition correction

The official [Piggyback KH2 guide sample](https://www.piggyback.com/en/kh2_e_samplepages/) (printed
pp. 28–29) supports Slapshot and Slide Dash as normal move examples, Guard Break as a focused ground
finisher, Explosion as a crowd-oriented ground finisher, Finishing Leap as an alternate ground
finisher and Aerial Finish for air combat. Turning these into authored musou branches and longer-chain
enders is proposed design, not a claim KH2 used fixed musou button strings.

**Stun Impact is a KH1 Final Mix-origin move, not a KH2 base-Sora finisher.** Retain it as intentional
cross-game inspiration if desired. [Stun Impact](https://www.khwiki.com/Stun_Impact). KH2FM Limit Form's
crowd burst is Ripple Drive; Limit Form is separate from base Sora and Valor, and exclusive to Final
Mix. [Limit Form](https://www.khwiki.com/Limit_Form)

For edition-aware alternatives, [Finishing Leap](https://www.khwiki.com/Finishing_Leap) appears in KH2
and KH2FM with changes; [Magnet Burst](https://www.khwiki.com/Magnet_Burst) is a KH2FM aerial crowd
finisher. Record which edition and form supplies each selected move instead of blending their kits.

[Valor Form](https://www.khwiki.com/Valor_Form) is a gauge-limited, dual-Keyblade Drive Form focused on
melee; source magic and defensive options differ from base Sora, and the source normally requires
Goofy. This grounds a temporary-form ultimate concept, but retaining that party requirement, costs,
duration, recharge and altered defense remains a design choice. No source numerical values are
adopted as prototype tuning.

The KH2 guide is primary published evidence for the listed base moves. BBS details, form nuances and
edition distinctions above use clearly identified secondary references. No commercial game files were
inspected and no timing, conversion or exact-build reproduction is claimed.

## BBS tooling feasibility

The [pinned OpenKH assessment](toolchain-research.md#bbs-feasibility-serious-head-start-not-a-complete-combat-pipeline)
finds a serious research/asset head start: KhModels model export, PAM → ANB motion conversion and
attack-parameter clues. Direct PAM → animated FBX remains incomplete, converted motion has no attack
triggers, and combos/projectiles/Shotlocks need an original runtime. Exact-edition export/playback is
unverified. An optional Ventus/Strike Raid spike would test that pipeline without choosing this route
or reducing its three-Knight goal.

## A bounded comparison before production (recommendation)

If the user wants evidence before choosing, compare **one representative Knight kit** against a
**Sora base kit plus one temporary-form sketch**, using the same arena, enemy scenarios, placeholder
asset quality, time budget and target hardware. Choose which Knight to represent the route explicitly;
one cannot establish that all three will feel distinct. If the three-Knight route is selected, follow
with separate Terra-like, Ventus-like and Aqua-like identity checks before calling the roster proven.

Use one provisional Shotlock mode at a time, with targeting, finisher-follow-up and charged-ultimate
experiments clearly separated. A form sketch is needed to test Sora's proposed payoff fairly. Record
that unequal animation/research effort can bias the comparison; no prototype results exist yet.

Compare:
- Distinctness and recognizability of the intended character fantasy
- Ground/air flow, buffering, defense and recoverability when surrounded
- Combo branching value and finisher access during battlefield objectives
- Shotlock/form payoff, readability and target continuity
- Authored animation/content effort and unresolved exact-build evidence gaps
- Correct interactions and frame costs at the same measured crowd settings

This is an optional staging recommendation. It does not authorize building the game or shrink the
three-Knight production goal. The [prototype plan](prototype-plan.md) keeps route selection or
comparison scope explicit before implementation.

## Shared non-negotiable and route-specific regression cases

**Every visible enemy remains real, reachable and fightable**, including at long range. Reduced
processing must preserve the same enemy's identity, position, health and relevant action/status state.
All routes inherit the [interactive-horde correctness matrix](interactive-horde.md).

Additional proposed fixtures:
- A Raid or ranged magic attack crosses simulation tiers and hits the same target before approach;
  its return/secondary hits follow authored per-target hit rules without disappearing or duplicating.
- Shotlock acquisition includes eligible distant entities; target death, movement, occlusion and
  legitimate invulnerability between lock and release follow explicit rules. No fake locked targets.
- A multi-target finisher's damage comes from gameplay queries, not visual effects or animation LOD.
- Reaction/follow-up timing remains consistent under crowd load; loss of a target cannot stall the
  player indefinitely or cause an arbitrary replacement hit.
- Drive entry/expiry during a combo, guard, hit reaction, jump or landing preserves valid player and
  enemy state; no health resets, phantom hits or form-only actions persisting unintentionally.

No crowd-size claim, engine selection, shipped roster, or fidelity pass is established by this plan.
