# V12 playable wave prototype and Mac startup checkpoint

Private local package: Builds/WavePrototype-v12-private/Mac/KeybladeWarriors.app. Primary launcher: Game/KeybladeWarriors/Play-Mac-Waves.command, with the verified paced 30-FPS preset. V10/V11 remain preserved; builds and commercial assets are not uploaded.

Game checkpoint: b2b7a2c09fdb1db8a836e24bd075533c95fd6f2e on playable/private-character-preview. Startup code checkpoint 82b2a2c. Converter/verifier checkpoint: 21bcbfe9fd6834de7eac869fe46090bbf4ce442e on master. Both source repositories currently have no remote; these code checkpoints are local.

## Completed verification

The Mac-only game entry initializes the real command line, disables the early MemTag performance-profiler channel and LLM before Cocoa, then forwards to Unreal's existing main. This addresses the observed early LLM PopTag failure path; allocator choice alone had not been reliable. No engine source patch or global environment change. LLM/memory-tag profiling is unavailable in this Mac game build while the workaround is active. Windows/editor entry paths remain unchanged.

Ten unrestricted rapid startup/exit launches pass: five raw Binned3 and five with the bundle ANSI environment. Three actual delivered-launcher headless launches also pass, including its relative working directory and argument forwarding. Every run records the pre-Cocoa disable marker and clean engine exit. These are direct-executable/command-launcher tests, not repeated Finder/Launch Services or hardware-input tests.

All five packaged gameplay suites pass, as do the strict active-enemy headless scenarios. Paced rendered integration also passes both scenarios: a full nine-Soldier clear (122 contacts, 18 enemy telegraphs/five strike phases, ordinary restart; 83.6 game seconds / 86.20wall seconds) and a wave 3 defeat after ground/air finishers (five defeats, 94 contacts/two confirmed air contacts, 25 telegraphs/seven strike phases, three ordinary damage events, HP0 and restart; 68.27 game seconds / 70.86wall seconds). No enemy passivity, HP grants, protection, teleporting, or direct damage is used in the integrated fixture. Wall-clock durations rule out accelerated-simulation claims.

Actual package screenshots were saved and the victory view inspected: wave 3, Heartless 0, defeated 9, 122 contacts, Sora's source portrait/gauge and the clear/restart overlay. Private exact evidence is in PlayableEvidence/FirstSlice/FINAL-VERIFICATION-v12.json and the v12 startup/package/rendered/capture folders.

## Preserved scope and limits

Three batches of 2, 3, 4 real Soldier Heartless, source-backed ground/air attack selection and finishers, hit/hurt sphere tracks, battle stats, health/death and full restart. Benchmark unchanged: KH2FM Standard Lv30 Kingdom Key, STR21 MAG21 DEF18 HP20, no story stat bonuses or optional combo abilities. No arbitrary DW branches were substituted for source combo selection.

Physical sustained keyboard/relative mouse and hardware controller remain unverified; the user check was not answered. Windows is unbuilt/untested. Source clips/timing/geometry are retained, but full BDX AI, revenge-value/special-state immunity and optional guard/dodge/magic/healing/audio are incomplete. Wave/crowd/body-collision/camera/control rules include documented arena adaptations. No original-game input replay comparison or complete KH2-fidelity claim.

The delivered preset is the verified paced 30-FPS mode. Older uncapped rendered bot losses and earlier startup failures remain recorded; they are not presented as clears. Existing 60/120Hz controller checks and a 60Hz active clear at 3HP are separate V11 evidence, with the combat implementation retained.
