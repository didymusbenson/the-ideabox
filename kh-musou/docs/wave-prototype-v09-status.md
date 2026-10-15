# V09 playable wave prototype — 2026-10-15

## Run

Private Mac app: `Builds/WavePrototype-v09-private/Mac/KeybladeWarriors.app`. Run its `Contents/MacOS/KeybladeWarriors` directly if Launch Services fails. macOS arm64 was built/tested; Windows targets remain source-only and untested. Assets and builds remain private/local.

WASD / left stick move; mouse / right stick camera; Space / controller A jump; LMB or J / controller X attack; Tab / R3 toggle lock-on; R restarts all waves. Time attack presses within the actual combo windows: ground A300 → A302 → A304 has four contact windows across three actions. Air selection/finishers remain the V08 source system. An unequipped Combo Master requires contact before continuation. A whiff does not advance the chain. There is no arbitrary Dynasty Warriors branch replacing KH2 attacks.

Three batches contain 2, 3 and 4 Soldiers, nine enemies total. Each is a real, separately colliding, damageable actor with actual source geometry/animation/hit tracks. Defeat all members to advance after 2.5 seconds; the third clear wins. R restores player, enemy identities, wave count and statistics through level restart. There are no decorative or invulnerable crowd stand-ins. Counts stay deliberately small after rendered multi-enemy measurements; this is no large-horde scalability claim.

The benchmark remains KH2FM Standard Lv30, Kingdom Key, no optional combo abilities. STR21/MAG21/DEF18, base HP20, zero story bonuses. Soldier benchmark HP67, STR29, DEF16. This is unforgiving: an ordinary hit deals11, a kick/dive17 before mitigation. No optional defensive/magic abilities, potions or between-wave healing were silently added. Final equipment/story bonuses remain configurable and undecided.

## What changed

- Real batch spawning, independent enemy life/state, clear/completion/defeat/restart HUD, kill/contact counts, individual enemy HP bars.
- Source Sora normal/hurt/defeated portrait from the existing local remastered P_EX100.a.us texture8; source gauge art from field2d/us/zz0field.2dd texture1. The quarter-circle health meter follows actual HP. Original Canvas assembly adapts the source sprites; it is not the original KH UI layout engine. No fake MP or Drive meter advertises an unavailable ability.
- Other Soldiers no longer spuriously act as visibility walls for weapon contacts or target acquisition. Arena walls still block hit queries. Actual source attack/hurt volumes, independent per-window contact caches and ordered player attack selection are retained.
- Lock-on camera tracks target yaw; per-target markers/bars use the same live enemy entity. Nearest-visible acquisition and the camera are still adaptations, not a claim of native scoring/camera equivalence.
- Soldier near/far normal motions201/202, kick203, jump3 and dive204 now use full source-clock clips and matching collision groups1/2/3/4/7. Four separate live contact tests cover the four damaging patterns. The zero-power group7 event is retained in private data but its special push/flag semantics remain unimplemented.
- Jump anticipation follows source frame12; jump height260, wait24 ticks after takeoff, and the capped distance/30 constant dive vector are supported by the local Soldier behavior script. The dive uses swept movement rather than provisional hit-reaction damping. Native collision/landing remain Unreal adaptations.

## Fidelity and evidence boundaries

Stopped predecessor was verified idle through supported read_thread, with a clean V08 game checkpoint0536028; no Unreal build/game process was active. V08 movement/action reconstruction remains the basis, rather than the earlier V05 snapshot. Planning's old "one Soldier / no horde yet" scope is superseded by Andrew's explicit wave assignment.

Source evidence: the locally owned Steam files and pinned OpenKH parsers/decoder. Private Soldier BDX action-table names map normal, kick and jump routines; normal chooses201 versus202 at planar distance200. Near/far attack windows, powers and shape groups come from ANB/ATKP/collision records. The full BDX behavior VM, difficulty/revenge queues, culling rules and probabilistic scheduling were not ported. A deterministic mix of patterns, staggered attack delay and local separation steering are documented arena adaptations. No source-fidelity claim follows merely from a passing Unreal test.

Remaining limits: eight-tick input buffer and held-input behavior are provisional; nearest-visible target scoring; full original blend/cancel priority rules; complete native damage rounding/formula, invulnerability and revenge/armor semantics; missing source death effects/audio/facial animation. The existing .65-second player recovery invulnerability is still provisional. In the far normal test, second-window contact is recorded but damage can be rejected by that recovery invulnerability; logs now distinguish attempted from applied damage. Original hit/hurt sphere sampling is adapted to Unreal sweeps/capsules. Optional abilities, magic, reaction commands and other Heartless types are outside this small playable milestone. Only Soldier waves are implemented. No user acceptance or perfect KH2 equivalence is claimed.

## Verification

World regression: `v09-final-checks.json`, four pattern contacts, all21 controller checks at30fps, extended travel/two-window/occlusion/interruption checks at60fps, complete wave contacts/progression/defeat/restart at30fps. Existing Timeline/SourceActions/NativeMovement automation is checked with the strict verifier. Build: `package-wave-v09-final.log` is the full asset cook; `package-wave-v09-verified.log` restages final code with unchanged cooked assets. Both must report BUILD SUCCESSFUL.

Packaged executable tests and rendered screenshots are recorded in `package-v09-results*.json`, `package-v09-*.log`, and `package-v09-captures/`. Test-specific wave clearing holds enemies passive so all nine deaths can be driven through real player attacks; live enemy pattern damage and final player defeat are separately tested. This does not claim that an automated bot beat nine attacking enemies. The normal game has active AI.

Rendered development observations before final packaging measured roughly86–119fps while other editor/cook work ran, with a400ms startup/streaming stall. Fixed-timestep/headless FPS logs are simulation cadence, not performance measurements. The packaged rendered run is the relevant final observation. These small counts do not establish a horde budget or hitch-free play.

Commercial assets, decoded scripts, native bodies and builds are ignored and never staged. Game and converter repositories have no remotes; commits there are local recovery checkpoints. Only factual planning/status text belongs on the existing Ideabox branch.

## Final packaged verification and frame times

Code checkpoint `4b209d3`; original conversion tooling `45a34f4`, both local-only. `FINAL-VERIFICATION-v09.json` records the exact executable SHA256, launch commands and results. All three independent packaged pattern/controller/wave scenarios exit0 and pass; the actual rendered packaged full-wave run and a separate no-capture full-wave benchmark also pass and exit0. Source Sora26/Soldier17 clips, collision tracks, source HUD and restart are verified from the package. Final code restage is `package-wave-v09-final-camera.log` (BUILD SUCCESSFUL), using the full private asset cook from `package-wave-v09-final.log`.

Separate no-capture, real-time packaged wave measurement, requested1280x800 window, on this Mac; no concurrent build/test work. Wave-test enemies are passive during player-driven clearing, so this is a small combat/collision/animation workload measurement, not an active-horde performance claim. First3seconds of each batch are reported separately from engaged combat.

| Batch | Enemies | Combat samples | Median ms | P95 ms | P99 ms | Worst combat ms | Warmup worst ms | Spawn ms |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
|1|2|2635|11.05|12.70|13.69|14.91|40.37|28.35|
|2|3|4254|10.42|11.29|11.77|13.53|12.21|1.46|
|3|4|5607|10.33|11.19|11.67|14.13|11.46|1.75|

The earlier400ms delta was not reproduced by the final package. Capture-enabled measurement recorded140.71ms near the first screenshot request and135.05ms at the third-wave capture, while sustained P95 stayed about11ms. The independent run without capture requests had no frame above14.91ms after warmup. This strongly distinguishes the observed spikes from sustained small-wave combat, but does not prove the exact cause of the older uninstrumented400ms stall. See `v09-package-benchmark.json` and `package-v09-waves-rendered.log`.

`MANUAL-INSPECTION-v09.md` distinguishes normal native-input observations from scripted tests. R, Tab, J and Space were observed in the real package, including live Soldier defeat and changing source portrait states. Quick synthetic WASD taps are not reliable evidence of held movement; normal keyboard/controller feel still requires hands-on acceptance. A first-focus camera warp observed there is fixed in the final package. Background packaged screenshot requests did not produce PNG files; final saved screenshots use the identical compiled Unreal game in editor-hosted game mode, and the package itself was separately viewed through the native UI. Do not label those PNGs as packaged screenshots.

## Recovery-invulnerability audit

The available ANB and ATKP records establish that the far normal has two distinct source windows: frames58..70 and91..112 at60Hz, with attack IDs1313/1314 and100/50power. Both ATKP records have Flags0 and Interval0; those facts alone do not establish the player's native recovery invulnerability duration or whether the second contact should damage an already-reacting Sora. The available public decomp DAMAGE file implements combo-count classification, not the complete player damage acceptance/invulnerability path; the saved native analysis is insufficiently labeled to claim that rule is proven.

The inherited .65-second player immunity remains explicitly provisional. In the live far-attack test first damage is11 (HP20→9), and the later source contact attempts6 but applies0. Logs record this rather than calling it two damaging hits. No blanket bypass or forced multi-hit damage was added. Exact native recovery timing and acceptance flags are a priority for a later source-fidelity pass; this prototype does not claim that behavior is KH2-equivalent.

## Mac launch workaround and current UI limitation

A later ordinary launch reproduced exit139 before engine logging; -nollm also failed. The saved Apple crash report points to FLLMTracker::PopTag through Binned3 allocation during a macOS application-open event. Engine MacPlatformMemory explicitly supports the early -ansimalloc option. Three normal-mode launches with -ansimalloc and a controlled quit exit0 and log Allocator:ANSI. The recommended `Play-Mac-Waves.command` selects that allocator. Do not claim the bare .app default startup crash is repaired. The package binary/gameplay code is unchanged.

The Mac locked during the final native-input follow-up. Earlier R/Tab/J/Space and portrait/defeat observations remain valid; final post-workaround native UI verification awaits an unlocked Mac. Background packaged wave and startup tests continue without bypassing the lock.

## Recommended launcher verification

Use `Game/KeybladeWarriors/Play-Mac-Waves.command`, or the task output `Play Keyblade Warriors Waves.command`. Both pass `-ansimalloc -windowed -ResX=1280 -ResY=800`. The ANSI allocator workaround completed the real rendered full-wave encounter, enemy defeat/restart and clean exit0. Three ordinary startup/controlled-quit launches also exit0 (`v09-normal-ansi-launches.json`). The controller, pattern and wave checks with this allocator are in `v09-ansi-checks/package-v09-results.json`. The bare default allocator's early Mac startup failure remains a known issue; the launcher avoids it without changing game combat code.

No-capture, real-time ANSI launcher measurements (`v09-package-ansi-benchmark.json`):

|Batch|Combat samples|Median ms|P95 ms|P99 ms|Worst combat ms|Warmup worst ms|Spawn ms|
|---|---:|---:|---:|---:|---:|---:|---:|
|1|2834|10.29|11.24|11.59|12.27|29.19|2.73|
|2|4351|10.12|10.94|11.33|15.99|11.68|1.43|
|3|5940|10.08|10.87|11.29|11.81|11.18|1.74|

Saved final gameplay PNGs: `v09-delivery-captures/KW-wave-multi-hit.png` and `KW-wave-three.png`; the matching editor-hosted game run passes complete waves/restart in `v09-delivery-visual.log`. They use the same final source code/assets, but are not packaged screenshots. The package HUD/portrait was also inspected with native UI before the Mac locked. No source asset or build was published.
