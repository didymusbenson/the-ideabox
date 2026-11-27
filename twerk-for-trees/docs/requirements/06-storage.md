# 06 — Storage capacity and progression tree

**Status:** v1.1 implementation baseline candidate. A real capacity ceiling is now part of progression, in addition to the per-producer local buffers already specified. Storage is a first-class economic branch: build storage using resources at that era, raise the ceiling, unlock better technology, then build bigger solutions. This replaces the earlier uncapped-global-stock assumption; no unlimited bank and no silently swallowed harvests.

## SF4 research and design rationale

The pack's [Age of Storage definitions](https://github.com/DarkPacks/SkyFactory-4/tree/6bbfe9681e7443eeef2143723430614a5f8e20c1/src/config/triumph/script/sf4/age_storage) comprise 36 files including root and completion variants. Its [advancement language](https://github.com/DarkPacks/SkyFactory-4/blob/6bbfe9681e7443eeef2143723430614a5f8e20c1/src/resources/skyfactory4/lang/en_us.lang) describes wooden crates/barrels, higher-capacity metal containers, 64×/256×/1k×/4k× capacity upgrades, an overflow upgrade, shipping containers, compact chest/backpack, hoppers, Simple Storage Network access, requests and automation, and later digital item/energy storage.

The [pack-specific BDS&M crafting script](https://github.com/DarkPacks/SkyFactory-4/blob/6bbfe9681e7443eeef2143723430614a5f8e20c1/src/scripts/crafttweaker/recipes/mods/bdsandm.zs) verifies actual increasing materials: wood plus chest → wood crate; iron plates plus wooden crate → metal crate; iron blocks plus metal crate → larger shipping container. Its capacity-upgrade recipes likewise escalate through timber, tin, gold/diamond and emerald/obsidian families. The [Compact Storage config](https://github.com/DarkPacks/SkyFactory-4/blob/6bbfe9681e7443eeef2143723430614a5f8e20c1/src/config/compactstorage.cfg) uses different materials for chests/backpacks and builder dimensions; [BDS&M config](https://github.com/DarkPacks/SkyFactory-4/blob/6bbfe9681e7443eeef2143723430614a5f8e20c1/src/config/bdsandm.cfg) permits multipurpose barrels. Simple Storage Network brings logical inventory access and requests rather than itself guaranteeing arbitrary capacity. The [AE2 config](https://github.com/DarkPacks/SkyFactory-4/blob/6bbfe9681e7443eeef2143723430614a5f8e20c1/src/config/AppliedEnergistics2/AppliedEnergistics2.cfg) explicitly disables channels and enables storage cells and energy components; [Extra Cells config](https://github.com/DarkPacks/SkyFactory-4/blob/6bbfe9681e7443eeef2143723430614a5f8e20c1/src/config/AppliedEnergistics2/extracells.cfg) enables size-dependent byte overhead for new item types. The endgame board adds very large digital cells and a million-item filing challenge. These are distinct approaches to storage: more physical volume, better access and routing, then dense storage. These are pinned source findings, not measured gameplay or exact item counts for the external base mods.

**TFT translation:** make storage expansion meaningful in each age, not a one-time setting. Keep one approachable inventory across tabs (like an inventory network), no physical item slots or cable puzzle. Use escalating resource recipes and additive modular capacities, and unlock optional stock routing/overflow control through the industrial network. Do not copy SF4 recipes, mod names or assets. The TFT values below are proposed for playtesting, based on the prior root and endgame economy, not claimed SF4 unit conversions.

## ST-01 — What fills storage?

One shared warehouse capacity for all item units, not one independent unlimited stack per resource. One resource unit occupies one storage unit regardless of type, including seed, catalysts and Worldseed. A resource-specific target is an optional production policy, not another hard cap. This is deliberately easy to explain, and forces real choices between collecting more, spending supplies, and building larger storage.

```text
capacity = 160 + sum(module_count[tier] * units_per_module[tier])
used = sum(on_hand items) + sum(all reserved item inputs)
free = max(0, capacity - used)
available(resource) = on_hand(resource)        # excludes already reserved
```

- Count reserved inputs: moving an item from on-hand to a job reservation cannot create phantom free space. Temporary safety minima affect automated spending, not occupancy.
- Uncollected ready bundles and finished blocked batches are **outside the warehouse but bounded** by local producer buffer caps. No unlimited output queue (default 3 completed cycles for manual producers; up to 12 with buffer kits; one held delivered batch for a timed station). A completed buffer cannot be freely moved to another producer or used for crafting without collection.
- Completed tech, buildables, attachments, plot structures, storage modules, power charge, profile points, world records and progress counters are not inventory items. Their costs consumed upon construction, no duplicated hidden stock. No stack weight multipliers in v1.
- Numeric safe-integer engine limit remains independent of gameplay storage. Each capacity check is atomic and applies offline and online. No new content can exceed the cap except explicitly preserved legacy overflow (below).

## ST-02 — Capacity tier tree and costs

Base storage: **160 units** in the starter store. In Workshop's Storage section, pay first-module technology cost to create the first module. Each tier requires the previous tier and its listed technology capabilities. Each can be expanded to **four total modules** using the same bill of materials as the first. They stay built and add capacity permanently in that world; no teardown, power-dependent capacity loss or storage maintenance bill in v1. No prestige needed.

| Tier | Increment per module | Total capacity, one of each so far | Material bill (per module) | Additional prerequisites beyond prior tier |
|---|---:|---:|---|---|
| Starter store | 160 | 160 | Free | Start |
| Wooden bins | +160 | 320 | 8 timber, 2 dirt | None |
| Clay-lined silo | +640 | 960 | 6 clay, 6 stone, 8 timber | Clay cultivar |
| Reinforced warehouse | +2,560 | 3,520 | 6 iron, 4 bronze, 2 fired parts | Heat lining and iron pick |
| Networked storage rack | +10,240 | 13,760 | 3 control, 8 iron, 4 glass, 2 advanced alloy | Router, circuit bench, alloy furnace, deep bed |
| Crystal memory vault | +40,960 | 54,720 | 8 advanced alloy, 6 control, 4 crystal, 4 polymer | Precision and polymer lines |
| Folded-space repository | +163,840 | 218,560 | 12 alloy, 8 crystal, 6 catalyst, 1 convergence core | Convergence and high-capacity Grid |

Maximum with four of all six tiers: **873,760 units**. Earlier tiers remain buildable until respective cap (no need to max each); late players can build larger modules instead of spamming bins. Cap scales 4× per tier, raising storage relative to the preceding bottleneck. Each upgrade is visibly affordable within the prior minimum-tier capacity, including a fully occupied bank. Purchase debits materials and adds capacity atomically; it never requires extra inventory space for the structure. No duplicate unlock effects from double taps.

```text
Starter -> Wooden bins -> Clay-lined silo -> Reinforced warehouse
                            |                         |
                            +-> Sorting network -----+-> Networked rack
                                                            |
                                                            v
                                                     Crystal vault
                                                            |
                                                            v
                                                     Folded repository
```

The Sorting network (existing `router`) now explicitly needs the silo as a prerequisite and adds repeat/stock-policy tools. It does **not** add capacity itself. The industrial rack requires the network, refined alloy and control parts; this is a real progression convergence. Worldseed Press requires the rack, ensuring the last production chain has space to finish a first run. Crystal and folded modules are optional scale/Endless goals, not required victory badges. Existing local buffer upgrades still exist and remain a separate axis: increased **warehouse** capacity doesn't add harvest buffer cycles, and vice versa.

Add "Supply Lines" board milestones for acquiring all six module tiers, first warehouse-full and resumed transfer. Board completion still optional, not a condition for required upgrades.

## ST-03 — Full warehouse and atomic transfer

- Manual collect: transfer oldest complete ready bundles in order while each entire bundle fits. If next bundle cannot fit, leave it intact with visible exact space deficit. No partial collection or dropping a random output by default. Example used 155/160, starter bundle 6 -> hold. Spend/discard one ordinary unit, then entire 6 fits to reach 160/160. Unique seed may make a bundle 7; show real amount. Do not roll seed a second time on retry.
- Automatic collector: same capacity check at every delivery, with `hold` default. If the next bundle cannot fit, it remains in bounded ready queue; the plot may keep progressing only until local queue capacity. There is no additional output at a full buffer. Resume once enough space for the next oldest bundle, deterministic ordering by task priority then stable ID after material-spending/capacity transitions. Powered attachments denied power must not deposit until authorized by allocator; mechanical collectors require no power.
- Timed recipe: reservation occupies warehouse until completion. A manually started timed recipe can reserve inputs even at full stock if it has no held output; automatic repeating jobs wait if their projected net output cannot fit (actual concurrent stock changes may still block a completion). At completion consume reservation exactly once, then attempt output. If insufficient room, hold one completed output bundle outside warehouse, without spending inputs again. Machine cannot start next batch until bundle delivered; it can complete a job already in progress. Power off after completing blocked output, no phantom active draw. Example used160 includes 2 reserved, job consumes2 then produces3; at 158 used it holds 3, waits until another 1 unit is spent, then deliver to 160. Cancellation before completion returns reservation and unchanged used occupancy. Cannot cancel an already consumed/finished bundle to refund inputs.
- Instant bench recipe: compute net used after debit and output credit, accept only if capacity and inputs fit simultaneously. If net output would exceed cap, reject atomically; offer max craftable quantity. At full warehouse allow net-zero and net-negative crafts, unlocks, builds and fuel spending. Auto bench rules and generated storage purchases never bypass stock.
- Storage full is a normal economy state, not an exception/error modal. A blocked task retains exact unfinished or pending state; freeing capacity, buying a storage module or spending in Workshop triggers a retry. Offline catch-up runs same storage rules, stops capped producers/queues; never credit imaginary overflow or ignore cap while away.
- **Always-recoverable:** user may explicitly discard selected ordinary **unreserved** resource units from Inventory even before any network upgrade; preview selected name/quantity, irreversible confirmation. No payment/progression reward. Protect the only Field seed and terminal Worldseed from ordinary discard/auto-void. No hidden irreversible discard by default. If first expansion is blocked by miscellaneous stock, spend/convert or intentionally discard recoverable surplus, collect starter input and purchase bins. Guaranteed seed can't be lost; starter remains plantable. Reserved inputs cannot be discarded; cancel ordinary job to return them first.

## ST-04 — Network stock policies

After Sorting network, a Storage policy tab exposes per-material optional target quantity and reserve minimum. Set reserve ≤ target ≤ capacity (null target means unbounded up to warehouse capacity). Quantities are units on hand plus reserved for target, while reserve minimum applies to automated available spending. Reserve and target may overlap (e.g. keep at least 20 coal and target 100 coal); they are not physical reservations or extra storage. Defaults: no target, reserve0, overflow Hold. Policy only applies to automated delivery/crafting, manual spending/collection uses hard cap; show if manual action exceeds a target/reserve.

- `Hold` (default): if any ordinary output would exceed its configured target or warehouse cap, keep the whole bundle, wait. This is conservative but can eventually halt mixed-output trees. UI identifies the exact limiting by-product. No automatic delete even if it would be helpful.
- `Trim excess to target` (individual ordinary resources, explicit confirmation on enable): after subtracting any amount exceeding configured target, try to deposit the remaining complete bundle; if still beyond global cap, hold remainder instead of deleting additional resources; no discard of protected outputs. Only selected ordinary resource's excess above its target may be discarded automatically. Commit trims and credit together (if remainder doesn't fit, retain original bundle and retry; no loss on failed transfer). Record discarded quantities in local session/offline summary. No generic “void all when full” switch. Turning trim off affects future batches and never reconstructs previously discarded resources.
- Automatic repeat/target stock policy prevents production on inputs held for fuel/critical chain, using priority and stock goals. If global inventory is saturated with surplus, suggest increasing storage, spending excess, raising/adjusting targets or opting into one clear trim rule. No forced min/max targets on the beginner; only show once useful.
- Every setting is persisted and visible. On power loss, held storage stays accessible and retains its capacity: the module represents built infrastructure, not a live powered device. Actual powered transfer and production still require the Grid; no power-free industrial recipe via storage.

## ST-05 — Endgame and Endless

Worldseed is stored like any material; the victory counter is lifetime **world** delivered output, not stock. The first full-world win requires 600 accumulated deliveries. The rack gate ensures a meaningful minimum 13,760 item capacity (one each through the fourth module). The two/minute terminal example's initial stock budget 3,000, output 600 and positive average byproducts after 300min total ~8,842 units. This gives headroom with no trimming for the arithmetic witness. Actual batching can still jam, so the runtime 60-minute warm-up/steady-state test and full threshold run must exercise bounded storage. Capacity upgrade and stock policies are independently useful.

In Endless after winning, the finite warehouse will eventually fill. A special explicit **Archive Worldseeds** action can retire any number of current Worldseed units without payout or new item/currency, preserving world cumulative production/records and victory. This is not automatic discard and is disabled before first win. Player can also build the larger optional vaults or free other supplies. Endless means continuing production and records, **not** an infinite simultaneously stored inventory. Replant resets warehouse to base160 and all module tech/build counts, along with world stock. Latest prestige perks remain unchanged; no storage prestige perk in this baseline.

## ST-06 — UI

- Always indicate used / capacity (e.g. 114/160) in global resource bar; compact progress ring or segmented bar, warn visually and text at >=80%, "Storage full" at cap; no repeated toast. Tap opens Inventory > Storage detail.
- Storage detail: available/free/reserved counts, top occupied resources, current module counts/max, next buyable module cost and resulting capacity, deep links to missing materials. Show locked upcoming tier and why (not all six rows endlessly scrolled on phone). Offline summary reports space-full stopped producers, held output and opted-in discarded excess. 
- Workshop Storage: first and repeatable tier recipes, a visible graph/sequence of tier prerequisites, current + capacity gain without stack inventory minutiae. Preview multi-buy true total and count limits. Build while full if costs feasible; exact result reflected immediately.
- Global producer status differentiates **Warehouse full**, **Local buffer full**, **Target reached**, **Input missing**, **Power unavailable**. When there are multiple blockers, show first actionable with expandable detail. Tap storage reason opens Inventory/Storage with relevant item. Manual collect displays exact needed free units. No inaccessible inventory at critical cap.
- Network-only policies per resource with number stepper/quantity input and defaults, overflow opt-in confirmation; show currently lost excess count. Discard uses explicit confirmation, only unreserved ordinary material; no negative quantities. Worldseed archive only after win with distinct label and consequence message.
- Persist storage module counts, policies, optional manual trim totals and held outputs; derive capacity and used, don't store stale derived totals. Validate count cap and known tech. If importing an earlier uncapped prototype snapshot with stock above current tier capacity, preserve data in over-capacity recovery (no new net-increasing credits; allow spending/discard/upgrade until fits), never silently trim. Full release has no prior shipped saves as of this spec.

## ST-07 — Verification

The v1.1 catalog encodes six additional tech tiers and six repeatable module types. [Design validator](../../tools/validate_progression.py) checks exact capacity arithmetic, upgrade material totals fitting previous tier, no bypass of tier prerequisite, positive costs and caps, full-stock reservation/held-output examples, cap-aware sequential quantity witness and terminal average stock budget. Root route still fits starter 160: conservative peak ≤131 units, no mandatory storage click before the original slice capstone. The actual sustained first-run witness (all 51 tech, all 34 construction types sampled) produced 600 Worldseeds without exceeding installed capacity; peak stock 8,788 including byproducts. This is an accounting/design check, not a scheduler or gameplay test.

See the updated [acceptance matrix](05-acceptance-and-roadmap.md) for storage-specific runtime tests. Tune capacity increments and module costs after player traces; if the early bank prevents legitimate first expansion, fix recipe/starting cap, never give silent infinite inventory.
