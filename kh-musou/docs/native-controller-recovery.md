# Native controller recovery — V08 verified, 2026-10-14

V08 is built and verified. The rendered Mac package passed all 21 controller checks at 30 fps, correct private asset and material loading, source collision loading, and a full restart. Editor build, all three automation suites, and normal/extended encounter checks also pass. No new manual visual acceptance is claimed. See [V08 status](native-controller-v08-status.md) and [one-pass inspection checklist](manual-inspection-v08.md).

Game final checkpoint `0536028d13b21c3e7eb8e89b375a372a66f96edb` (code `748480b`), converter final checkpoint `174cd3124d5c5ac381c987757f75244f8cdc99ae` (code `5900a3f`). These two repositories have no remotes, so their source is local-only and NOT backed up to GitHub. Recovery locations are `Game/KeybladeWarriors` and `Research/PortableKHExport` beneath the local Keyblade-Warriors workspace. This planning repository contains factual notes and the checklist only.

## Historical research and intermediate checkpoints — superseded by V08 status

The user explicitly asked to continue through the remaining work, not stop for another V07 manual handoff. Work remains active. This supersedes the earlier inference that the available files only support table-driven approximation: the original executable retains usable MSVC native RTTI/vtables. A complete drop-in script is still absent, but native movement and combat logic can be traced locally.

Read-only RTTI mapping found300 YS classes, later340 including kn animation providers. Headless native analysis recovered269 selected action/player functions and direct callees; subsequent targeted batches trace the selector, movement integration and animation clock. The source executable SHA256 is `9002b2de6a1f91a790bd0673de125d1cf833f7942bfec827cdcf6ba64d5849ed`. The executable is imported as data, never loaded/executed or patched. All generated decompiler bodies, addresses, analysis databases and binary-derived reports stay under ignored SourceAssets/Steam-KH/native-controller; none go to GitHub.

Verified behavioral findings pending coupled implementation:

- Jump ascent uses a nested sine curve to the apex, followed by quadratic descent. The native gravity constant is the float32 value0.40816327929496765 per global-frame unit squared. Apex time derives from sqrt(abs(2*height/gravity)); terminal fall is source SSTM FallMax. Ordinary locomotion sets/stops desired movement immediately, while aerial movement has separate smoothing.
- Base attack selection uses table order, Type1 selected-target and Type2 nearby-target conditions, Type3 defaults, ability/air/finisher flags, and Sub-ID fallback when a selected motion repeats. It does not use the prototype's unconditional alternating sequence or highest-score subset. Distance far bound, height lower bound and cone lower bound are exclusive in the recovered comparisons.
- Attack application uses PTYA jump height/min/max and travel-speed bounds, including ground-to-air routes. V07's blanket use of PLYR8/6/12 as per-stroke vertical velocity is not the recovered basic attack path and must be replaced.
- The newer official OpenKH Motion.FrameData names are FrameStart/FrameEnd/FramesPerSecond/FrameReturn. The legacy emulator exposes first/fourth values as FrameLoop/FrameCount. Existing visual-prefix trims8/42 match actual source start frames, not arbitrary holds. Correct event-clock origin and return-frame loops are being verified against native animation provider code before implementation.
- Target selection uses target collision type3 and its radius/height, distinct from hurt spheres. Source body collision bounds also differ from some prototype capsule values.

Portable analysis tools: official Ghidra12.1.4 archive SHA256 ddac49f903da9d5bac833e5cc79395098b9c33cfd3279be5f31bd00387d2d4db, verified before extraction. Reuses installed Android Studio JDK21.0.8. Ghidra's native decompiler was built locally for mac_arm_64 with Xcode clang; no game code or DRM changes, no system installation. Tool settings/cache/temp are placed under workspace Tools. Original analysis scripts are preserved in Research/PortableKHExport.

Next: finish native timing/selection/physics evidence, implement the baseline controller and asset-clock changes together, then run one combined validation/build batch. Do not claim full controller completion from research alone. V07 remains the last packaged build until its successor passes; no newer manual acceptance or visual proof exists yet.

## Active V08 integration checkpoint

Native-clock metadata and FBX generation passed (26 Sora/13 Soldier clips); Unreal animation import failed its clip-count check (1 exposed versus26 expected). Runtime native movement and selection helpers are checkpointed but not yet wired into the player/enemy actors. This intermediate game source has not been compiled and is not expected to compile until integration replaces the old air-velocity references. V07 remains the latest packaged build. Continue actor integration, repair animation discovery/import, then perform combined validation. Game and adapter still have no remotes: source checkpoints remain local-only, not backed up to GitHub. The user requested Astra continuation without a new task or another inspection gate.

## V08 integrated checkpoint

Game checkpoint748480b now wires the recovered movement/action clocks into both actors, native jump/air steering, ordered combo selection, source target geometry, source recoil and finisher launch/landing, animation return loops and command windows. Adapter checkpoint5900a3f validates all26 Sora/13 Soldier native-duration clips and retains original analysis tooling. Editor build and Timeline/SourceActions/NativeMovement automation pass. Normal/extended world encounters pass. The controller sequence passes at30fps, including185cm jump, landing unlock, all four damage events in the forward three-hit chain, finisher get-up, air interruption and restart. V08 Mac build/cook/package is running; V07 remains the previous verified package. Source commits are local-only: neither source repository has a remote. No raw native bodies or commercial assets were published.
