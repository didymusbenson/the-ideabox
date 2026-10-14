# Keyblade Warriors — macOS and Windows setup

Keyblade Warriors is the working name. Unreal remains selected. macOS (Apple Silicon) and Windows (Win64) are now explicit targets. The full Sora versus three BBS-inspired Knights route remains open. This setup skeleton does not implement combat or select that route.

## Workspace

`/Users/didymusbenson/Documents/Repos/Keyblade-Warriors/planning` is a fresh clone of didymusbenson/the-ideabox, based on main at 3ad3d3bf8e57b5659c86328cee50f3eace383bda. The remote default branch points to an unrelated project, so setup uses main explicitly. Project: `kh-musou/unreal/KeybladeWarriors/KeybladeWarriors.uproject`. No public repository was created.

## Verified host and current blockers

MacBook Pro Mac16,5; M4 Max 14-core CPU; 36 GB RAM; macOS 26.3 (25D125); about 472 GiB free at inspection. Xcode 26.2 (17C52), Clang, macOS SDK 26.2, Blender 5.2.0 LTS and Git are installed. Unreal was not found. Standalone .NET and OpenKH were not found in checked locations; neither is required for a placeholder Blueprint setup. Unreal supplies its own required toolchain components; do not install speculative runtimes or OpenKH.

Official Epic release announcement confirms 5.8 is released (June 23, 2026); use the stable 5.8 family, not Preview or UE6. Exact hotfix/build pin is pending the authenticated Launcher library and installed Engine/Build/Build.version. Do not treat EngineAssociation=5.8 as an exact patch lock. Keep Xcode 26.2: Epic lists 26.0 minimum for 5.8, 26.1.1 recommended, and excludes 26.4. Actual macOS 26.3/editor compatibility is untested.

Official Launcher DMG downloaded from Epic to /tmp/KeybladeWarriors-EpicGamesLauncher.dmg; initial version 20.3.3 copied into ~/Applications/Epic Games Launcher.app. Sandboxed signature verification initially reported invalid signature; outside-sandbox strict codesign reported resource fork/Finder metadata detritus. Crucially, outside-sandbox Gatekeeper assessment ACCEPTED it as Notarized Developer ID. No security protections or quarantine were changed. Launched through the UI: official bootstrapper completed its update and the Epic Games sign-in screen is visibly present. Stopped before sign-in as requested. Account sign-in, license acceptance, authenticated engine library, and engine install have not been completed.

## Minimal dependency plan

Install only Core Components and Templates/Feature Packs for macOS; keep the built-in Third Person template/mannequin and Enhanced Input. Animation Montages and Animation Blueprints are built in. Add IK Rig/Control Rig only when retargeting or authoring actually needs them. No Fab/Marketplace packs, Lyra, MetaHuman, paid assets or experimental crowd systems are necessary now. No commercial game assets belong in this repository.

## Resume setup and validation

1. User signs in to Epic and reviews/accepts any new Epic/Unreal agreement themselves. Stop at any unexpected permission or payment.
2. In Launcher Unreal Engine > Library, select the stable 5.8 hotfix actually offered. Record exact patch and Build.version before creating content. Install only required Mac components plus templates. Engine installation has not been completed.
3. Open the skeleton in that editor. It contains descriptor/config only: no playable map, pawn, Third Person assets or combat. Verify plugin resolution and save a new blank test map before claiming an editor pass.
4. Add the engine-provided Third Person feature pack or create a sibling Third Person Blueprint project in a new empty directory, preserving this skeleton. Verify keyboard movement, jump and camera in PIE; save and reopen. Record results and editor log errors. No combat milestone is authorized here.
5. Package Development for Mac, launch the packaged .app locally, repeat movement/jump/camera, and record architecture, build ID and results. This test is pending.
6. On a separately verified supported Windows build host, install the same exact Unreal hotfix and required Visual Studio/MSVC/Windows SDK combination from Epic's version table. Package Win64, launch and repeat the smoke test. Neither a Windows host nor Windows build was verified. Mac/Windows source targeting does not establish Windows packaging from macOS.

## Validation status

Descriptor JSON and target/platform settings: static checks only. Editor launch, asset import, PIE, Mac packaging/launch and Windows packaging/launch: NOT RUN, blocked by unavailable verified engine installation. The Third Person template is planned, not imported. No full combat prototype built.

## Deck (independent)

Strict-host-key, BatchMode SSH to the user-provided destination reached the host but returned Permission denied (publickey,password). No host-key warning was bypassed, no credentials inspected, no new access created. Existing Terminal authentication is not accessible here. User can run a bounded manifest inventory in the already connected Deck Terminal and return only KH collection/app/build/install-path fields. No extraction or transfer is needed for this workspace.

## Official references

- https://www.unrealengine.com/news/unreal-engine-5-8-is-now-available
- https://www.unrealengine.com/download
- https://dev.epicgames.com/documentation/en-us/unreal-engine/macos-development-requirements-for-unreal-engine
- https://dev.epicgames.com/documentation/en-us/unreal-engine/setting-up-visual-studio-development-environment-for-cplusplus-projects-in-unreal-engine
- https://dev.epicgames.com/documentation/en-us/unreal-engine/third-person-template-in-unreal-engine

## Follow-up verification — 2026-10-13

Launcher UI confirms Unreal Engine **5.8.3** installation in progress (8% at observation). Completion and installed Build.version remain unverified. The previous sign-in blocker has been passed by the user.

Git LFS **3.8.0** installed through Homebrew and initialized with repository-local configuration. Root .gitattributes tracks kh-musou/unreal/**/*.uasset and **/*.umap. git check-attr confirms both resolve to filter=lfs before any binary content is committed. No history migration performed; hosted LFS quota/availability is not yet tested with a binary upload. Keep commercial game assets outside Git, including LFS.

Epic's Third Person documentation confirms movement, jump, mannequin animations and a basic arena. Its Combat variant offers targeting and health scaffolding; inspect it separately after the standard Mac smoke test. This does not establish KH-like combat behavior.

OpenKH source verification: Object Editor targets net8.0-windows and UseWPF=true, so it is not a native macOS GUI. global.json requests SDK 8.0.416 with latestFeature roll-forward. OpenKh.Command.Bar and OpenKh.Command.Bdxio target net8.0; they are Mac candidates, not tested Mac installations. No OpenKH or .NET installed in this step. Verify transitive/native dependencies and run fixture-based CLI tests before declaring compatibility. Object Editor documentation describes motion playback, collision groups, triggers and AI inspection; actual Sora/Soldier data inspection is pending local asset availability. No Deck access or asset transfer attempted.

Computer control: Launcher screenshot inspection works. Unreal editor input and observation remain unverified until its first launch. Test criteria: editor opens project without fatal/plugin errors; movement changes position, jump leaves/returns to ground, camera changes view; saved map reopens; packaged Mac app launches and repeats controls. Later combat criteria: ground and airborne attacks execute, one enemy receives expected damage and reacts, health/death behavior matches defined values. All remain NOT RUN. Subjective KH feel requires user playtesting.

Sources checked:
- https://dev.epicgames.com/documentation/en-us/unreal-engine/third-person-template-in-unreal-engine
- https://git-lfs.com/
- https://openkh.dev/tool/GUI.Kh2ObjectEditor/
- https://github.com/OpenKH/OpenKh/blob/master/OpenKh.Tools.Kh2ObjectEditor/OpenKh.Tools.Kh2ObjectEditor.csproj
- https://github.com/OpenKH/OpenKh/blob/master/global.json
- https://github.com/OpenKH/OpenKh/blob/master/OpenKh.Command.Bar/OpenKh.Command.Bar.csproj
- https://github.com/OpenKH/OpenKh/blob/master/OpenKh.Command.Bdxio/OpenKh.Command.Bdxio.csproj
