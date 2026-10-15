# V10 wave prototype checkpoint — 2026-10-15

V10 continues the existing 2/3/4-Soldier private wave arena and unchanged KH2FM Standard Lv30 Kingdom Key benchmark. Runnable local Mac package: Builds/WavePrototype-v10-private/Mac/KeybladeWarriors.app. Stable launcher in the game repo: Play-Mac-Waves.command. Commercial assets and builds remain private/local.

Game checkpoint: d39b4d6bd399a69e631975fd1b2ad14e01cf3a7d on playable/private-character-preview (local repository has no remote).

Verifier checkpoint: 9bdd271d228ad8c3fff675b34d812033721a1458 in the local converter repo (no remote).

## Corrections supported by new evidence

The source-character damage gate used the cosmetic 0.65-second flashing timer as an ordinary-hit immunity grant. A private native trace through Sora's damage acceptance, HP override/base arithmetic, reaction, and immunity predicates did not show that fixed grant in the ordinary-hit path. Distinct special-state flags/timers exist, including context-specific rebound/ability grants; these are not a basis for a generic duration. V10 removes only the invented cosmetic gate, retaining source hitbox-off and contact caches. This does not implement every KH2 special-state immunity system. Actual Soldier202 contacts now apply 11 and 6 damage separately when collision connects.

A new normal-binding simulated input check reproduced an aerial body-capsule bug: Sora could remain about 140cm above the arena repeatedly entering landing on a Soldier. The Unreal adapter now makes fighter capsules unwalkable and sweeps to radial separation before continuing the source arc. Source attack/hurt geometry and timing are unchanged. Three repeated editor runs and the final packaged test reach the arena floor by about 1.5 seconds. This body solver is an arena adaptation, not extracted KH2 collision behavior.

The project Mac plist sets the existing early UE allocator environment option through Launch Services. An ordinary no-argument earlier V10 app build rendered the arena and logged ANSI; the final signature and plist verify. The command launcher retains -ansimalloc. This is app-local, not an engine patch or global setting. Direct executable CLI still needs the flag.

## Validation

Final V10 package: pattern, native controller, recovery, simulated normal input, and complete-wave suites all pass with exit0. Rendered complete-wave run also passes: two distinct enemies contacted by one source swing; all nine Soldiers reached/defeated through player contacts; live enemy damage/defeat; full restart. Actual package PNGs saved and inspected locally. Wave-clear fixtures make enemies passive to isolate contact/progression, with live enemy attack checks separate; do not describe this as beating nine active enemies or an active-horde performance benchmark.

Rendered capture-enabled run: per-wave P95 frame times 10.97/10.88/10.93ms. Capture-correlated peaks 137.53ms in wave1 and 125.16ms during wave3 warmup remain visible; do not hide these or claim a definitive prior hitch root cause. Existing V09 no-capture measurements remain a separate record.

Physical sustained WASD and relative mouse motion remain pending: native automation can tap but cannot hold or send continuous relative motion. Simulated events exercise normal bindings/polling and are not hardware tests. No physical controller was identified. The Mac locked again before final repeated interactive launch checks; no independent implementation work was blocked on the unanswered user question. Windows is untested.

Remaining fidelity limits: deterministic Soldier cadence/crowd adapter rather than full BDX; incomplete revenge-value/special-state immunity systems; camera/pitch/focus rules are usability adaptations; no silently added guard/dodge/magic/healing. Source combo selection and hit confirmation remain the basis of combat, with no arbitrary DW branching. Scope remains the wave prototype.
