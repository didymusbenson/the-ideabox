# 05 — Acceptance criteria, test strategy and implementation roadmap

This is a checklist for an actual engineering implementation, not a statement that game functionality has already shipped. Every release-blocking requirement has an observable pass criterion. Use fake clock/seed in unit and integration; use normal browser UI/real storage for final acceptance. Do not greenlight a feature just because a button renders.

## Design validation already performed

From TFT root run:

```sh
python3 tools/validate_progression.py
```

Current v1.1 storage candidate result (2026-11-27, local Python standard library; script reads this catalog):

```text
Structure: 7 boards, 60 milestone predicates
Storage: six tiers, 160 starting units -> 218560 with one each -> 873760 maximum; held-output and reservation accounting examples pass
Graph: 51 tech and 45 resources reachable in 13 passes; 34 builds reachable
Root fixture: {'plot2': 36, 'screen': 60, 'stone': 60, 'clay': 78, 'plot3': 96, 'collector': 136, 'clockwork': 156, 'root_capstone': 220} auto-collected clay 10 remaining clay 8 peak stock <=  131
Sequential quantity witness: 51 tech, each build type sampled, 600 Worldseed, 9053 actions, 133592s summed work, peak stock 8788, final capacity 436960 (not elapsed idle pacing)
Terminal flow: 2 Worldseed/min, 180/200 W conservative all-listed-task upper bound; nonnegative material rates and feasible slot-minutes
  Terminal average-rate stock budget: 8841.67/13760 units including initial stock and all positive net byproducts
  Material rate slack: litter=1/18, waste=1/18, crop=187/36, fiber=97/18, cutting=109/36, timber=15/4
  Source utilization: worldseed_press 60.00/60s/min, alloy_furnace 21.00/60s/min, processor 24.67/240s/min, circuit_bench 8.00/60s/min, polymer_line 16.00/60s/min, precision_line 21.33/60s/min, stabilizer 9.33/60s/min, bench 0.00/60s/min, field 61.83/120s/min, quarry 48.56/420s/min, orchard 61.67/180s/min, grinder 18.89/120s/min
PASS: design checks; real scheduler, offline replay, combat RNG, UI, and balance still require implementation/QA.
```

What this proves:
- Catalog references and quantities structurally validate; all 51 one-time tech, 45 resource types and 34 construction types can be reached; 7 boards/60 milestones defined.
- A deterministic root route with actual ingredient debits and catalog harvest quantities reaches the mechanical collector and clockwork upgrade before the slice capstone, no negative resources.
- A sequential accounting witness obtains every tech, samples every build type, pays recipe and conservative per-job fuel costs, and crafts 600 terminal units with hard shared capacity checks on every credit and paid storage expansion; no resource or technology cycles block the witness. It assumes prompt manual collection and victorious encounters; the summed work (133,592s) is deliberately not a real-world duration, idle forecast, or economic tuning result.
- Exact rational steady-state rates of the terminal plan are nonnegative, slot-minutes sufficient and even the all-listed-task simultaneous load upper bound (180 W) fits the 200 W supply. With one module at each tier through networked rack, 13,760 capacity fits ~8,842 units projected after 300min (initial stock, terminal output and every positive byproduct net). The base cap covers the root witness at ≤131 units; storage full/reservation examples pass. This is not a discrete event schedule or proof of startup buffering/power-loss recovery. The Press is at 100% utilization. Set target output and fill initial buffers; tests below must demonstrate the actual scheduler with warm-up.

The design checks exposed missing deep-ore/alloy stage requirements on late tech and a planning accounting issue where producing a component consumed another component; both were corrected before this baseline. Changing the candidate economy reruns the checker. A pass does **not** prove runtime correctness, player enjoyment or finish timing.

## Acceptance matrix

### A. Rootwork/interaction — P0 release gate

| ID | Scenario and exact expected behavior |
|---|---|
| A-01 | New full world, no persisted data: exactly one Starter plot, Orchard+Workshop, no other zones or tech, all stock 0, HP100, 160 warehouse units. No sign-in or network required after asset cache. |
| A-02 | Advance fake clock 11,999ms: no output; +1ms creates one ready starter bundle 3 timber/2 litter/1 cutting (possible unique seed). Inventory remains zero until collect. Collect once delivers exact amounts; repeated Collect does not duplicate. |
| A-03 | No input for 48s on unautomated starter: exactly three bundles ready, fourth does not complete; on collection 9 timber/6 litter/3 cuttings, seed exactly once by third completed harvest. Resume normal timer from boundary. |
| A-04 | Preseed both outcomes for seed chance (first two chance success/fail); guaranteed third completion if absent, never duplicate on 4th+, seed survives ready buffer/save/reload, only Farm consumes it. |
| A-05 | Start tree baseline cycle; four accepted tap intents per second for three seconds supply six total baseline work seconds (3s real +3s taps), no direct inventory mint; >8 accepted intents in rolling second rejected for progress. Cross-plot taps share cap; canceled pointer swipe yields no tap. |
| A-06 | Timer exactly 250ms before completion, one accepted tap completes one bundle. At exact time boundary simultaneous user intent resolves prior completion once then applies only to eligible new cycle. 100 rapid intents cannot duplicate bundles or skip cap. |
| A-07 | Follow root fixture: plot2 36s, screen/Stonewood 60s, Claywood 78s, plot3 96s, collector 136s, clockwork 156s, capstone 220s; verify each paid bundle exactly, 8 clay current/10 cumulative auto clay. No active taps or rare bonus required. |
| A-08 | Cost calculation second plot dirt3/timber2, third dirt4/timber3, multi-buy preview cumulative and correct; insufficient final cost rejects atomically, no partial purchase or negative stock. Max plots includes starting prestige plots. |
| A-09 | First collector auto-delivers exact output with Grid unavailable; clockwork 20s Claywood →16s effective duration (no electric supply); one attached collector cannot operate multiple plots or mint extra resources. |
| A-10 | Plant/switch known cultivar including starter on any existing free plot with no new seed cost, preserve finished ready bundles; cancel switch keeps old timer; confirm discards only incomplete growth. Detached attachment remains owned and assignable. No last-seed deadlock. |
| A-11 | Root trial capstone only when all 3 species, >=2 plots, installed collector and clockwork, auto clay≥10. Manually collecting 10 clay does not trigger. Slice-only next tier teaser is never confused with full-world victory; replant proxy mode saves separately. |
| A-12 | Accessibility: 320px phone, 200% zoom, keyboard and touch; tap target separate from collect/details, 44px targets, reduced motion/hold input preserves economy, no hidden keyboard or mandatory frantic gesture. Asset-free or reduced-motion fallback works. |

### B. Content and material progression — P1/P2 release gate

| ID | Scenario and exact expected behavior |
|---|---|
| B-01 | Every ID in catalog parses into typed entities, unlock gates all-of, no unknown resource or duplicate key. Unreachable or cyclic mandatory dependency blocks build with readable error; catalog changes require validator pass. |
| B-02 | Purchase locked Farm before seed has no effect; seed and materials sufficient purchase one field exactly, consume one unique seed, enable tab; repeat purchase rejected, no duplicate slot. Other tech with multiple effects each initial slot exactly once. |
| B-03 | Field crop three crops/two fibre/two waste per18s, manual buffer cap; 2 crops → one ration/feed, pen 1 feed → 2 animal produce+2 waste/30s. No input pen stalls without reserving anything. Oil field locked then 3 oil+1 waste+1 fiber per24s. |
| B-04 | Fresh Clay-to-kiln path: kiln cost exactly catalog; charcoal recipe timber2→charcoal1 without preexisting fuel; fired part and copper bootstrap consume only current-tier inputs. Smelt 2 raw copper +1 charcoal→1 copper, buy copper graft, subsequent Copperwood produces 3 raw/28s. Repeat same for coal/iron/tin/silica; no future resource required. |
| B-05 | Bronze manual cost 2 copper+1 tin+1 charcoal→3 bronze/12s, heat lining required; Quarry opens iron pick; 6 stone/15s, 6 coal/18s etc, raw not ingot. Unlock quartz/deep/gem bed at catalog gates; heavy ore obtainable before advanced alloy or drill; gem before precision line. |
| B-06 | Every task selection checks matching producer/machine and requirements, locked target never runs even if caller passes ID directly. Conditions and unmet cost shown accurately in UI; flow links reveal feasible first-acquisition source. |
| B-07 | Soil compost (duration×0.8) on 12s starter ->9.6s work before attachment, shaped tool output3 timber ×1.25 yields alternating whole outputs (3,4,4,4 over 4 batches =15), no fractional inventory; unique field seed never multiplied. Switching/reloading does not erase/add fractional carry. |
| B-08 | One powered station speed kit and efficiency kit 8W base→9W and 75% duration; double upgrade rejected; power draw and time preview accurate. Soil/tool tiers exclusive; clockwork and powered twerkers mutually exclusive. |
| B-09 | Manual vs electric conversion: same 2 raw iron; manual+charcoal yields1 iron, electric yields2 iron after8s/8W. No need to install advanced drill/precision crystal to unlock own material. |
| B-10 | End-to-end deterministic path from fresh world reaches all 51 tech, Worldseed Press, first Worldseed and victory without prestige or bulk gifts; optional boards/soil/crop/goals can be skipped. Integration fixture uses exact definitions, true scheduler and controlled RNG, not mock inventory except isolated tests. |

### C. Jobs, scheduling, energy, automation — P2 release gate

| ID | Scenario and exact expected behavior |
|---|---|
| C-01 | Two simultaneous jobs needing last 2 iron raw: one reserves 2 based on priority/ID; other waits, stock0 reserved2, no negative counts. Finish credits exactly 1 output batch; same timestamp completions settle before new reservations. |
| C-02 | Cancel ordinary timed job at 50%: reservation returns exactly once, no output, next valid start begins at full cycle. Switch target asks before discarding partial work; finished output cannot be lost or duplicated. |
| C-03 | Queue 3 jobs; only current job reserves; later queue entries cannot bypass stock. Repeat locked before Router, after unlock target replenishes only missing stock; min fuel reserve prevents automatic starvation. Max99 batches. Zero-duration craft processes atomically and no runaway repeated loop. |
| C-04 | Fill buffer then pause, resume after Collect frees capacity; manual fields/quarry still progress at base rate when powered attachment loses power until manual buffer full. Unpowered industrial machine holds exact progress and reservation. |
| C-05 | Empty Grid, 1 timber: start combustion, draw20W for up to15s of useful burn, fuel debited only once; disallow unfueled progress. Disable mid-burn, save/reload, resume remaining fuel. No active demand and full/no batteries: no burn. |
| C-06 | Supply20W, demand12+10W and charge20,000W·ms: allocate both 10s, then lower-priority 10W job pauses, high 12W continues, battery0; switch priority and valid feasible task starts without resource loss. Battery charges from surplus and cannot exceed capacity. |
| C-07 | At simultaneous fuel exhaustion, batch completion and new start: credit completed output only once; acquire fuel from stock if available; otherwise task waits. No silent fractional power. Tie break stable ID after priority. |
| C-08 | Grid fully drained, no coal or charcoal: plant/replant Starter, manually harvest wood, manual kiln charcoal or direct timber fuel, restart powered machine preserving partial work. All manual/mechanical systems function without electricity. |
| C-09 | Add field/pen/quarry attachment, one per target only. Drill speed 0.75 or deep mode 0.5 with correct W; without power fallback normal speed. Powered twerker 0.6 effective time with power, base speed when denied; speed change not double-applied. |
| C-10 | Save/reload mid-job, mid-fuel and mid battery depletion; online and offline results identical for same elapsed/inputs/RNG, including zero input/overflow, queue and pause reasons. |
| C-11 | Timed terminal setup from catalog: 2 advanced generators, 3 auto-collected plots, 2 automated fields, 7 mining stations, 2 mastered grinders, processors/other stations. Run at least 60 simulated min after warm-up with demand target and realistic buffers. No negative stock/power, no hard storage cap violations, sustained rate close to 2 Worldseed/min (at least 95% target after ramp-up as first tuning check). If discrete scheduling loses throughput, fix routing/buffer behavior before balance changes. Test increasing Press alone exposes bottleneck. |
| C-12 | Shared warehouse cap reached: overflow holds one finished output bundle and prevents additional starts; no extra resources or lost progress; explicit capacity status, user can consume existing input to clear. All arithmetic stays safe integer or explicit remainder. |

### D. Arena — P1/P2 release gate

| ID | Scenario and expected behavior |
|---|---|
| D-01 | Locked opponent cannot start; Arena purchase gives initial HP100, food required. Ration debited once, heals40 capped; action timer. Feed insufficient rejects before RNG/HP change. |
| D-02 | Fixed RNG winning Burrower first encounter yields 2 cores +1 first-win bonus, later wins yield2; win count increments once even on reload, no bonus from grinder. |
| D-03 | Force two losses (catalog damage) then third valid resolution guaranteed win; loss streak resets, canceled encounter spends ration but no pity/mastery progress. No inventory/equipment lost. |
| D-04 | HP reduced to0 ->60s cooldown then full recovery, no fight before exact expiry. Idle regen2 HP/s only when no active fight/cooldown; no negative HP. |
| D-05 | Ward motor required for auto-battle; HP threshold ceil(maxHP×0.6), ration and 6W; stall/continue at exact conditions; two consecutive auto losses pause until explicit resume, enemy pity remains. No hidden auto combat before unlock. |
| D-06 | Five wins per enemy grant mastery independently. Grinder requires at least one mastered to buy, only mastered enemy assignable, deterministic normal loot per period with ration and power, no HP or winner/mastery credit. Offline results and current reserve match online replay. |

### E. Saves, offline, world win — P0/P3 release gate

| ID | Scenario and expected behavior |
|---|---|
| E-01 | Save mid tree growth, buffer ready, reserved input, selected zone; reload same revision and exact state. Close/open numerous times with same timestamp produces no change. Save snapshot verified before showing success. |
| E-02 | Compare 1h uninterrupted foreground simulation to same 1h offline delta from identical world and RNG with no active input, matching quantities, timers, fuel, HP, milestones. Advance 15h offline: simulate exactly12h, report discarded3h, next reload cannot reclaim it. Negative clock delta0, no backwards state. |
| E-03 | Simulate completion transaction interruption before and after pointer switch; recover old or new valid revision, never mixed state/double output. Corrupt current checksum -> valid backup option, missing/unsupported newer -> no silent erase. |
| E-04 | Two tabs same save: only writer advances, follower read-only; takeover after release/expiry; stale revision/owner write refused, conflict message and export possible. No combined stock. |
| E-05 | Export/import valid snapshot preserves world, settings, perk/counter revisions. Invalid JSON, oversize, unknown resource, negative count, invalid reservation, future schema or checksum mismatch leaves existing state untouched. Confirmation cancel leaves prior data exactly unchanged. |
| E-06 | 599→600 terminal output commits once: exact consumed input, counter600, wonAt set, prestige earned+1, win event once. Reload, dismiss/reopen, collect further worldseeds do not grant more points. Current stock is not victory arbiter. |
| E-07 | Endless retains all inventories, job state, wins, unlocks, profile and production; no new mandatory tech. Later Replant selectable. Replant cancel leaves same state/revision; confirm spends selected valid points, resets world IDs, counters, jobs, fuel, mastery, tech, stock and applies only exact selected starting perks. Profile settings, record/history persist. Cannot replant before full win (except separate root trial mode). |
| E-08 | Buy each perk up to level3 then fourth denied, unspent points carried; starting dirt+2 per level, starter duration0.9^level, buffer+1 per level, extra empty plots capped. No point duplication via import of same active profile's old revision during normal gameplay; explicit backup restoration does not imply cross-device global sync. |
| E-09 | Balance/schema migration creates valid new revision, preserves last good backup, applies documented timer-fraction rule and known ID mappings, no free output. Service worker update waits safe save and prompts, cached offline app plays after restart. |
| E-10 | Storage full/unavailable: in-memory game still operable but prominent unsaved status/export, no false success. Offline resume summary once per committed delta, no manual re-credit. Performance 12h typical replay p95 target<2s, stress max roster<10s on test devices; record actual hardware and timings. |

### F. UI/system acceptance — all eligible builds

| ID | Scenario and expected behavior |
|---|---|
| F-01 | Each zone on 320×568, 390×844, 768×1024, landscape tablet, 1440×900 and 200% zoom: nav and critical controls reachable, no clipped/accidentally overlapped controls, only intentional tab scroll. |
| F-02 | First-run player discovers plot/stone/clay/collector without outside guide. Next goal and Workshop details show all missing requirements, ingredient→source links work, back returns. Unknown recipe never displays enabled button. |
| F-03 | Multiple producers share stock, timer update visible without layout flicker; resource detail actual/planned/minimum/reserve values distinguish production and consumption. Block reason reflects real state. No repeated routine toast/modal/click-away side effect. |
| F-04 | Arena/Factory/Grid visibility obey unlocks; preparing and enabling generators shows correct W/fuel, stalled jobs visible, target/detail updates without unnecessary reordering. |
| F-05 | Keyboard focus, semantic tags, screen reader labels; Escape cancels overlays, reduced motion and hold alternative no timer/stock change, contrast and touch targets validated. |
| F-06 | No third-party game IP assets/names shipped; cute animation visibly responds to tap, timer not frame-driven, audio optional and capped. Original placeholders sufficient for interaction spike; later assets replace without changing mechanics. |
| F-07 | Browser smoke: production static build loads, offline launch after caching, save persistence across browser restart, no unexpected network service besides static asset/update requests; no analytics or login dependency. |
| F-08 | Fatal content/load/save error shows actionable message and export/recovery, never blank screen or wipe local save. No unhandled promise rejection on normal gameplay. |

### G. Storage cap progression — P0 through P3 release gate

| ID | Scenario and exact expected behavior |
|---|---|
| G-01 | New world capacity160, used0, sum(on-hand+reserved). Root fixture peak≤131 including possible seed, no capacity upgrade required; initial bins visible. At used155, six-item starter bundle waits intact; free one then collect exactly6, used160. Seven-item seed bundle uses7. |
| G-02 | Three manual ready bundles, only first fits; collect oldest fitting prefix once, rest stay intact. Full local buffer halts timer. Collector reaches warehouse cap, stores held bundles up to local max, then pauses; free space and resumes; offline follows same logic. No default item deletion. |
| G-03 | At 160 used, reserve2 for timed job: still used160. Cancel returns2 exactly once (used160). Completion consumes reserved2 and attempts output3, used158 and pending3 (not deliverable). Spend1 then deliver3 exactly once to reach160; no input refund or repeated fuel while blocked. |
| G-04 | At full warehouse, wood bin valid stock bill8 timber+2 dirt -> used150/cap320. Tech purchase creates first module; repeat identical price adds another160 up to four total. Double tap/out-of-cost/5th rejects with no material spend. Unlock next clay tier only after bins and clay cultivar. |
| G-05 | Build one each, verify cumulative cap320/960/3520/13760/54720/218560. Four each max873760; no power dependency. Storage modules never occupy inventory, do not expand local buffer. Deep cap or initial free module cannot be bypassed via injected actions. |
| G-06 | With full stock, instant recipe 2 inputs→1 output succeeds with used−1; net-positive cannot exceed cap, reject atomically. Manual discard selected ordinary unreserved units only after confirm; cancel no change; seed and pre-win Worldseed protected. Player can recover from full junk stock and get storage inputs. |
| G-07 | Before Router no automatic trim. After Router target5 timber, 4 in stock, bundle3 timber+2 litter: Hold keeps entire bundle; explicit trim timber above target discards2 and delivers1 timber+2 litter if cap allows. If remainder doesn't fit retain whole original bundle and discard0. No trim of seed/Worldseed, no auto trash for global overflow. Policy and discarded counts persist. |
| G-08 | Base cap+modules and policies consistent across save/reload; used includes all reservations, held outputs bounded. Import uncapped prototype above cap preserves exact stock and pending outputs, enters recovery; block net-increasing credits but allow spend/discard/expansion until fits. No silent truncation. |
| G-09 | Router requires silo; rack requires warehouse, routing, controls/alloy; no Press before rack. Minimum cap13760 fits the planned 300min 600-terminal run with buffer setup. Run actual full path under scheduler and cap, no hidden infinite inventory or self-lock. |
| G-10 | Storage cap includes Worldseed; at full Warehouse before win output remains held, counter advances only when delivered. After win archive selected stock explicitly, cumulative record/point unchanged, frees exact units. Before win blocked. Endless can continue; Replant resets cap160, all modules and stock policies; settings/profile perks persist. |
| G-11 | Phone/tablet/desktop used/cap visible, warning at80%; full state distinguishes warehouse/local/input/power/target. Storage detail links next affordable module and missing ingredient; manual confirmation and trim controls accessible with keyboard+screen reader. Offline summary includes held and explicitly trimmed quantities. |
| G-12 | Simulate simultaneous output completions and capacity expansion; deterministic priorities/stable ID, reservations never double counted, one pending bundle/ordinary station, no race past cap; same millisecond and offline parity fixtures. |

## Implementation plan (sequenced, not a promise of dates)

Use the catalog and IDs first, not hardcoded UI constants. Each stage must leave a runnable testable build and a green checkpoint. Expand only after verifying previous layer; full app launch depends on choosing a repository/project location separately.

| Stage | Concrete work | Exit condition |
|---|---|---|
| S0 — foundation | Create new TS app shell, content schema/load and typed catalog, domain world state/actions/ledger, deterministic clock and fake RNG, test runner. Local save envelope basic backup/export. | Build starts; validator and serializable state tests green; no dependencies on live browser time in domain. |
| S1 — root spike | Starter plot and original animation stub, buffered production/tap/caps, shared inventory, exact bench/tech/build purchases, screen/stone/clay, collector + clockwork, 160 hard cap and first storage modules, next-goal UI. Root-trial mode separate. | A-01..12, G-01..06/G-08/G-11 relevant cases and E-01..05/E-10 relevant cases pass, actual browser touch/keyboard smoke, record first-collector playtest. Do not add industrial content before fun and stable interaction. |
| S2 — resource graph | Farm, manual kiln, coal/copper/iron/tin/silica, alloy and Quarry, selection/routing details, tool/soil, first Arena/manual combat, clay silo and metal warehouse. Add all applicable tech and producer screens. | B-01..08, D-01..04; end-to-end path no seeded inventory for required phase; save migration tested. |
| S3 — automation engine | Grid/generator and battery, event allocator, reservations and queues, repeat/targets, efficiency/speed, powered orchard/farm/quarry, Factory processor/alloy/router/circuit, networked storage rack and stock policies, Ward motor/grinders. | C-01..10/12, G-07/G-09/G-12, D-05..06, B-09, offline parity and recovery; no need to hand-feed every regular task once configured. |
| S4 — industrial/convergence | Deep/gem/quartz and advanced alloy, polymer, precision, catalyst, biofuel, Titan, high-capacity Grid, core and Press, crystal/folded storage and post-win archive; goals and full victory/Endless/Replant; profile perks and history. | B-10, C-11, G-09..12, E-06..09 and full-route witness implemented; replay and replant verified with exact real state. |
| S5 — product polish and calibration | Playtest on touch desktop/tablet/phone; inspect tap feel, time-to-first automation, power/job comprehension, late progression and steady state; tune versioned catalog; replace placeholders, responsive visual/accessibility QA, PWA/offline performance. | F-01..08 and relevant test suite on supported browsers; no known P0/P1 data-loss, progression, accessibility or offline blockers; verified web production build. |

## Explicitly not in first release

Spatial tile construction, procedural 3D world/exploration, live multiplayer/shared economy, real money, ads, account/cloud sync, social leaderboard, imported SF4 textures/recipes/branding, hundreds of species, advanced combat gear/triangles, separate prestige loop before victory, indefinite unbounded producer counts, infinite numeric precision beyond safe range. If the author later requests any, add requirements and a migration strategy rather than silently expanding scope.

## Balance and iteration

- Use telemetry-free local debug exports and consented human playtests. Measure time to first plot, collector, clockwork, first metal, first powered unattended producer, first mastery/grinder, first terminal throughput; ratios of hands-on/idle minutes and deficit reasons. Initial timings after Roots (especially full first-run time and total play sessions) need empirical tuning, not guesses posed as facts.
- Test both a "wide first" and "deep first" player, plus one who prefers manual/idle and one who actively taps. A gate that requires lucky long streak or unreasonably repetitive resource acquisition is a design defect. Don't add a currency to conceal a broken loop.
- Keep exact recipe dependencies and prices in catalog once accepted; tune batch yields, durations, fuel and costs in a separate balanceVersion, rerun validation + migration. Preserve same stable IDs. All release criteria should be tied to tests that exercise actual entry point, not UI snapshots alone.
