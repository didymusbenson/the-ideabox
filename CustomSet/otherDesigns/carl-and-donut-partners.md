# Carl & Donut — Partner Commanders

Top-down design based on *Dungeon Crawler Carl*. Locked "Partner with" pair.

**Combined color identity:** Temur (URG)
**Combined CMC to deploy both:** 6

---

## Carl, Compensated Anarchist {1}{R}{G}

Legendary Creature — Human Warrior

Partner with Donut, Former Child Star

Trample

If a nontoken artifact would be put into a graveyard from the battlefield, exile it instead and put a +1/+1 counter on Carl.

1{T}: Choose a card exiled with Carl. He deals damage equal to its mana value to any target. Put that card into its owner's graveyard.

**3/2**

---

## Donut, Former Child Star {1}{B}{R}

Legendary Creature — Cat Wizard

Partner with Carl, Compensated Anarchist

Deathtouch

*Clockwork Triplicate* — {2}{B}{R}, {T}: Create two tokens that are copies of target creature you control, except they're artifacts in addition to their other types and they have haste. Exile them at the beginning of the next end step.

**1/2**

---

## Design Notes

### Carl

- **Trample** represents the Boots of Butt-Kicking — he kicks through blockers.
- **Replacement effect** exiles ALL nontoken artifacts that die on the board (yours and opponents'), acting as artifact graveyard hate while stockpiling ammunition.
- **Tap ability** turns exiled artifacts into direct damage scaled by mana value, then returns the card to its owner's graveyard. This means you can recur the artifact later, and if it dies again, Carl catches it again — a repeatable loop.
- **Tension between attacking and activating** is intentional. He's a 3/2 trampler that grows tempting to swing with, but holding him back as artillery may be more valuable.
- **Donut's tokens are excluded** from the replacement effect (nontoken clause). The partner synergy is indirect — Donut provides board presence and value, Carl converts the deck's actual artifact cards into damage.

### Donut

- **Clockwork Triplicate** is the centerpiece ability. Two artifact creature token copies with haste, exiled at end step. The "triplicate" is the original + 2 copies = 3 total.
- **1/2 statline** reflects low constitution — she's fragile and not a fighter, but her ability is powerful enough to carry her.
- **Haste on the tokens** provides red color justification and makes the copies immediately useful as attackers or sacrifice fodder for other effects.
- **Intended play pattern:** Main phase 1 activate Donut → attack with hasty copies → use them before end step or let them expire.

### Core Gameplay Loop

1. Play creatures and artifacts worth building around.
2. Donut copies creatures, creating hasty artifact tokens for immediate value (ETBs, attacks).
3. Your real artifacts that die in combat or to removal get exiled with Carl.
4. Carl taps to fire exiled artifacts as damage, scaled by mana value.
5. Fired artifacts return to graveyard for potential recursion.
6. Repeat.

---

## Open Questions

1. **Should Carl's tap ability cost mana?** Currently free — strong with untap effects. Adding {R} or {1} would slow the snowball. Is the tap restriction alone sufficient?

2. **Donut's color identity:** With Magic Missile removed, her only red contribution is haste granted to the tokens. That's a legitimate red mechanic but it's thin. Should she stay UR, or drop to mono-U? (Combined identity is Temur either way.)

3. **Donut's fragility at 1/2:** Intentional flavor-wise but she dies to anything. She'll need protection pieces in the 99 to stick around. Worth considering whether the deck can function when she's repeatedly removed.

4. **Carl's replacement effect is global** — it exiles opponents' artifacts too, which shuts down their artifact recursion. This is a powerful incidental hate piece. Is that a feature or does it make Carl too oppressive in artifact-heavy metas?

5. **Mana value scaling on Carl's tap:** High-CMC artifacts become massive damage. A single 6+ mana artifact dying turns Carl into a one-shot cannon. Consider whether there should be a cap or if the scaling is the point.
