# Keyblade Warriors v06 — movement and combo inspection

Launch **Play Keyblade Warriors v06.command** when ready. V05 is preserved and its running game was left alone; close that older window yourself before comparing. WASD/mouse, Space jump, J/left click attack, R reset. The collision-view launcher adds cyan weapon and red enemy attack volumes. Release movement keys when checking a fresh reset.

Reference remains KH2 Final Mix Standard, level30 Sora, Kingdom Key, no optional combo or movement abilities. The final Sora build will be chosen later. STR21/MAG21/DEF18, baseHP20 with story bonuses unset; Soldier battle30 HP67.

Two baseline corrections supersede V05: Combo Master is unequipped, so a missed action cannot advance the combo; Damage Control activates at quarter HP, rather than half HP. With baseHP20, an11-damage hit leaves9HP and another equal hit defeats Sora.9HP does not qualify for Damage Control.

- [ ] **Equipped rig:** inspect idle, running, jumping and attacks. Sora, Soldier and Kingdom Key should retain their textures; no gray slots, floating weapon, chain detachment or stretched limbs. Let idle/run loop a few times.
- [ ] **Full single action:** tap attack once. Sora should move with the attack, then finish its followthrough. Check feet/body/weapon stay together, with neither stationary sliding nor a doubled lunge.
- [ ] **Forward two-hit route:** approach a straight-ahead Soldier with a short gap, approximately1.8–3metres, and tap once. The longer forward stroke can make two separate contacts. With both connecting, hits rise by2 and HP goes67→63→61 (4 then2damage). Count actual contacts, not button presses.
- [ ] **Close and offset swings:** repeat from close range, then with the enemy offset to the side. Look for the conditional side swing rather than the same fixed action from every position. It must not snap you toward an enemy behind you.
- [ ] **Hit-confirmed ground combo:** get close enough to connect before continuing. Chain two normals into a distinct finisher. Try straight-on and offset approaches; the finishing arc can change. Front finisher power200 gives10damage; side finisher power150 gives8. Inputs after a completed finisher start a fresh chain.
- [ ] **Whiff rule:** attack empty space and press again during recovery. Without Combo Master, that missed action should finish and stop rather than spend the buffer to advance. Repeat after a successful contact and verify continuation works.
- [ ] **Air route:** jump, connect and continue attacks. Confirm separate air motions/finisher; a missed air action should not advance. Check landing clears the chain and restores falling/jumping normally. One jump is expected with movement abilities disabled.
- [ ] **Collision and movement:** attack toward an arena wall. The capsule should stop rather than pass through or teleport. No late movement burst should appear when the attack ends. Startup, gaps between hit windows and recovery should not deal extra damage.
- [ ] **Front/back reactions:** hit the Soldier from the front and, while it is committed to an attack, from behind. Look for distinct reactions. Two-hit attacks should produce two readable contacts without abruptly snapping the reaction back to its first frame.
- [ ] **Player interruption:** let the Soldier hit while you are attacking or have queued another action. Sora should play a damage reaction; the interrupted action must stop moving/damaging, and the queued attack must not reappear when the reaction finishes.
- [ ] **Repeat/reset:** defeat either side, then R. Confirm20/20,67/67, zero hits, equipped idle restored, and no old movement, hit confirmation or buffer carrying into the new encounter. Repeat several times.

Report the item, position (front/side/air), stage, result and whether it repeats after R. A short recording is useful for motion, attachment or reaction problems.

What remains provisional: this implements a subset of the original target selector, not its complete scoring/flags. Exact input grace, i-frames, hitstun/action recovery, knockback units, blow landing/recovery, revenge/AI and death effects still need work. Source planar travel is restored; general walking/jumping remains the prototype controller. Damage cap units, intermediate rounding and the exact critical-HP boundary still need a vanilla-game comparison. Windows is unbuilt/untested. The final abilities and story bonuses remain undecided.
