#!/usr/bin/env python3
"""Design-data validator and conservative, sequential planning check. Not a game simulation.

Run from twerk-for-trees: python3 tools/validate_progression.py
Uses only the Python standard library. No networking, installation or game state.
"""
from collections import Counter, defaultdict
from fractions import Fraction as Q
from pathlib import Path
import json
import math

ROOT = Path(__file__).resolve().parents[1]
DATA = json.loads((ROOT / "data/progression-v1.json").read_text(encoding="utf-8"))
D = DATA
def require(condition, message):
    if not condition:
        raise AssertionError(message)

def index(key):
    records = D[key]
    result = {r["id"]: r for r in records}
    require(len(result) == len(records), f"duplicate {key} ID")
    return result

R,T,B,C,J,E,G = (index(k) for k in ("resources","tech","builds","cultivars","tasks","enemies","generators"))
CFG = D["config"]
ZONES = {"orchard","workshop","farm","quarry","factory","grid","arena"}
SLOTS = {"bench","kiln","field","animal","processor","alloy_furnace","quarry","circuit_bench",
         "polymer_line","precision_line","stabilizer","fermenter","convergence","worldseed_press"}
def amounts(obj, label):
    for k,n in obj.items():
        require(k in R, f"{label}: unknown resource {k}")
        require(type(n) is int and n > 0, f"{label}: invalid amount {k}={n}")
def prereqs(obj):
    require(set(obj.get("requires", [])) <= T.keys(), f"unknown tech reference: {obj['id']}")
def structure():
    for obj in list(T.values()) + list(B.values()):
        prereqs(obj)
        amounts(obj["cost"],obj["id"])
        require(obj["id"] not in obj["requires"], f"self gate: {obj['id']}")
    for obj in C.values():
        prereqs(obj); amounts(obj["out"],obj["id"])
        require(obj["seconds"]>0, f"invalid cycle: {obj['id']}")
    for obj in J.values():
        prereqs(obj)
        amounts(obj["input"],obj["id"]); amounts(obj["output"],obj["id"])
        require(obj["zone"] in ZONES and obj["slot"] in SLOTS, f"bad location: {obj['id']}")
        require(obj["seconds"]>=0 and obj["watts"]>=0, "negative time/power")
        require((obj["seconds"]==0) == (obj["slot"]=="bench"), f"invalid instant recipe: {obj['id']}")
        require((obj["watts"]>0) == (obj["repeat"]=="powered"), f"power/repeat mismatch: {obj['id']}")
    for obj in E.values():
        prereqs(obj); amounts(obj["out"],obj["id"]); amounts(obj["firstWin"],obj["id"])
        require(0<obj["winChance"]<=1 and obj["seconds"]>0 and obj["grindSeconds"]>0,"bad combat data")
    for obj in G.values():
        require(obj["watts"]>0,"bad generator")
        for fuel in obj["fuel"]:
            require(fuel["id"] in R and fuel["seconds"]>0, "invalid fuel")
    for obj in T.values():
        effect=obj["effect"]
        require(effect.get("cultivar", "starter") in C,"missing cultivar effect")
        require(effect.get("zone", "workshop") in ZONES,"missing zone effect")
        require(effect.get("machine", "bench") in SLOTS,"missing slot effect")
        require(effect.get("generator", "combustion") in G,"missing generator effect")
    board_ids=set(); total_milestones=0
    for board in D["boards"]:
        require(board["id"] not in board_ids,"duplicate board"); board_ids.add(board["id"])
        ids=set()
        for m in board["milestones"]:
            require(m["id"] not in ids,"duplicate milestone in board"); ids.add(m["id"]); total_milestones+=1
            p=m["predicate"]
            if p["kind"]=="tech": require(p["id"] in T,"unknown milestone tech")
            elif p["kind"]=="counter": require(p["threshold"]>0 and (p["key"] in {"clayAutoCollected","worldseedProduced"} or p["key"].startswith("wins:") and p["key"][5:] in E),"invalid milestone counter")
            else: require(p["kind"]=="event" and bool(p["event"]),"invalid milestone event")
    print(f"Structure: {len(board_ids)} boards, {total_milestones} milestone predicates")
    for obj in B.values():
        effect=obj["capacity"]
        require(effect.get("requiresBuild","plot") in B,"missing build dependency")
        require(effect.get("generator","combustion") in G,"missing generator build")
        require(effect.get("machine","bench") in SLOTS|{"grinder"},"missing machine build")

def reachable():
    # Set-level check: existence of a noncircular path, ignoring quantities.
    known = set(); res = set(); stages = 0
    while True:
        before=(len(known),len(res))
        for c in C.values():
            if set(c["requires"])<=known: res.update(c["out"])
        if "cutting" in res: res.add("field_seed")
        for t in T.values():
            if set(t["requires"])<=known and set(t["cost"])<=res: known.add(t["id"])
        for j in J.values():
            if set(j["requires"])<=known and set(j["input"])<=res:
                if not j["watts"] or ("grid" in known and any(f["id"] in res for f in G["combustion"]["fuel"])):
                    res.update(j["output"])
        for e in E.values():
            if set(e["requires"])<=known and "food" in res: res.update(e["out"])
        if before==(len(known),len(res)): break
        stages+=1
    require(known==set(T), f"unreachable unlocks: {set(T)-known}")
    require(res==set(R), f"unreachable resources: {set(R)-res}")
    for b in B.values():
        require(set(b["requires"])<=known and set(b["cost"])<=res,f"unreachable build {b['id']}")
    print(f"Graph: {len(known)} tech and {len(res)} resources reachable in {stages} passes; {len(B)} builds reachable")

class Ledger:
    """One plot/job/fight operated at a time. No automation, time overlap, buffs, or RNG.
    Exact ingredient quantities, first-three starter harvest seed guarantee and conservative
    per-job fuel consumption. Victorious manual encounters are a witness, not average pacing.
    """
    def __init__(self):
        self.inv=Counter()
        self.known=set()
        self.plots=1; self.built=Counter(); self.first_wins=set(); self.wins=Counter()
        self.starter_harvests=0; self.actions=0; self.seconds=0; self.pressed=0
        self.trace=[]
    def debit(self, cost):
        require(all(self.inv[k]>=v for k,v in cost.items()),f"insufficient {cost} vs {self.inv}")
        self.inv.subtract(cost)
        require(all(v>=0 for v in self.inv.values()),"negative stock")
    def harvest(self, id):
        c=C[id]; require(set(c["requires"])<=self.known,f"locked tree {id}")
        self.inv.update(c["out"]); self.seconds+=c["seconds"]; self.actions+=1
        if id=="starter":
            self.starter_harvests+=1
            if self.starter_harvests==CFG["seed"]["guaranteedBy"]: self.inv["field_seed"]+=1
    def job(self,j, trail):
        cost=dict(j["input"])
        if j["watts"]:
            require("grid" in self.known and j["watts"]<=G["combustion"]["watts"],"no capable generator in sequential witness")
            # Each job has fresh fuel; discarded remaining burn time is conservative for feasibility.
            fuel=G["combustion"]["fuel"][0]
            units=math.ceil(j["seconds"]/fuel["seconds"])
            cost[fuel["id"]]=cost.get(fuel["id"],0)+units
        self.ensure_bundle(cost,trail)
        self.debit(cost); self.inv.update(j["output"])
        self.seconds+=j["seconds"]; self.actions+=1
        self.pressed+=j["output"].get("worldseed",0)
    def fight(self,e,trail):
        self.ensure("food",1,trail); self.debit({"food":1})
        self.inv.update(e["out"]); self.wins[e["id"]]+=1
        if e["id"] not in self.first_wins:
            self.inv.update(e["firstWin"]); self.first_wins.add(e["id"])
        self.seconds+=e["seconds"]; self.actions+=1
    def ensure(self,k,n,trail=()):
        require(k not in trail,f"circular quantity route: {' -> '.join(trail+(k,))}")
        while self.inv[k]<n:
            if k=="field_seed":
                require(self.starter_harvests<CFG["seed"]["guaranteedBy"], "unique seed already spent")
                self.harvest("starter"); continue
            trees=[c for c in C.values() if k in c["out"] and set(c["requires"])<=self.known]
            jobs=[j for j in J.values() if k in j["output"] and set(j["requires"])<=self.known]
            # Deterministic source priority: guaranteed quarry/field output, current cultivar,
            # powered crafting when reachable, manual crafting, then combat.
            repeat=[j for j in jobs if j["repeat"]=="buffered"]
            # Keep starter wood and litter production independent of any crafting.
            if repeat and k not in ("litter","cutting","timber"): self.job(repeat[0],trail+(k,)); continue
            if trees: self.harvest(trees[0]["id"]); continue
            powered=[j for j in jobs if j["watts"] and "grid" in self.known]
            if powered: self.job(powered[0],trail+(k,)); continue
            manual=[j for j in jobs if not j["watts"]]
            if manual: self.job(manual[0],trail+(k,)); continue
            enemies=[e for e in E.values() if k in e["out"] and set(e["requires"])<=self.known]
            require(enemies,f"no available producer for {k}; gates={sorted(self.known)}")
            self.fight(enemies[0],trail+(k,))
    def ensure_bundle(self,cost,trail=()):
        # Making one component may consume another. Refill the simultaneous cost bundle.
        for _ in range(1000):
            missing=[(k,n) for k,n in cost.items() if self.inv[k]<n]
            if not missing: return
            for k,n in missing: self.ensure(k,n,trail)
        raise AssertionError(f"unable to fill bundle {cost}")
    def pay(self,cost):
        self.ensure_bundle(cost)
        self.debit(cost)
    def unlock(self,id,trail=()):
        if id in self.known: return
        require(id not in trail,f"tech prerequisite loop {id}")
        t=T[id]
        for p in t["requires"]: self.unlock(p,trail+(id,))
        self.pay(t["cost"]); self.known.add(id)
        self.trace.append((id,self.seconds,self.actions))
    def build(self,id):
        b=B[id]
        for p in b["requires"]: self.unlock(p)
        dep=b["capacity"].get("requiresBuild")
        if dep and not self.built[dep]: self.build(dep)
        if b["capacity"].get("requiresEnemyMastery"):
            while self.wins["burrower"]<CFG["combat"]["masteryWins"]:
                self.fight(E["burrower"],())
        self.pay(b["cost"]); self.built[id]+=1
    def witness(self):
        self.build("plot"); self.plots+=1
        for id in ("screen","stone_cultivar","clay_cultivar"): self.unlock(id)
        self.build("collector"); self.build("clockwork_twerker")
        for id in T: self.unlock(id)
        require(self.known==set(T),"not all unlocks acquired")
        # Verify each repeatable construction is obtainable once, not only tech gates.
        for id in B:
            if id not in self.built and id!="plot": self.build(id)
        self.ensure("worldseed",CFG["singularity"]["threshold"])
        require(self.pressed==CFG["singularity"]["threshold"],"terminal counter diverged")
        require(all(n>=0 for n in self.inv.values()),"negative final stock")
        print(f"Sequential quantity witness: {len(self.known)} tech, each build type sampled, "
              f"{self.pressed} Worldseed, {self.actions} actions, {self.seconds}s summed work "
              "(not elapsed idle pacing)")

def root_route():
    # Catalog-driven exact parallel no-tap fixture; prompt manual collection.
    inv=Counter(); plots=[{"id":"starter","next":C["starter"]["seconds"]}]; now=0
    trace={}; auto_count=0
    def advance(to):
        nonlocal now, auto_count
        while min(p["next"] for p in plots)<=to:
            now=min(p["next"] for p in plots)
            for p in plots:
                if p["next"]==now:
                    crop=C[p["id"]]; inv.update(crop["out"])
                    if p.get("collect") and crop["id"]=="clay": auto_count+=crop["out"]["clay"]
                    p["next"]+=crop["seconds"]*p.get("factor",1)
        now=to
    def debit(cost):
        require(all(inv[k]>=n for k,n in cost.items()),f"root unaffordable at {now}: {cost}")
        inv.subtract(cost)
    def dirt():
        n=inv["litter"]//J["make_dirt"]["input"]["litter"]
        if n: debit({"litter":2*n}); inv["dirt"]+=n
    def buy(id,cost):
        debit(cost); trace[id]=now
    cfg=CFG["plotCost"]
    def new_plot(crop):
        p=len(plots); cost={ "dirt":cfg["dirtBase"]+math.floor((p-1)*cfg["dirtPerPrevious"]), "timber":cfg["timberBase"]+math.floor((p-1)*cfg["timberPerPrevious"])}
        buy(f"plot{p+1}",cost); plots.append({"id":crop,"next":now+C[crop]["seconds"]})
    advance(36); dirt(); new_plot("starter")
    advance(60); dirt(); buy("screen",T["screen"]["cost"])
    debit(J["screen_grit"]["input"]); inv.update(J["screen_grit"]["output"]); buy("stone",T["stone_cultivar"]["cost"])
    plots[1]={"id":"stone","next":now+C["stone"]["seconds"]}
    advance(78); dirt(); buy("clay",T["clay_cultivar"]["cost"])
    while inv["dirt"]<4: advance(min(p["next"] for p in plots)); dirt()
    new_plot("clay"); advance(now+2*C["clay"]["seconds"]); buy("collector",B["collector"]["cost"])
    plots[2]["collect"]=True; advance(now+C["clay"]["seconds"]); buy("clockwork",B["clockwork_twerker"]["cost"])
    factor=Q(str(CFG["timing"]["clockworkDurationMultiplier"]))
    plots[2]["factor"]=factor; plots[2]["next"]=now+C["clay"]["seconds"]*factor
    advance(now+4*C["clay"]["seconds"]*factor)
    trace["root_capstone"]=int(now)
    require(auto_count==CFG["singularity"]["proxy"]["clayAutoCollected"] and inv["clay"]==8,"root automatic clay mismatch")
    require(trace=={"plot2":36,"screen":60,"stone":60,"clay":78,"plot3":96,"collector":136,"clockwork":156,"root_capstone":220},f"root timing changed: {trace}")
    print("Root fixture:",trace,"auto-collected clay",auto_count,"remaining clay",inv["clay"])

def endgame():
    example=D["endgameExample"]; net=defaultdict(Q); busy=defaultdict(Q); watt_upper=0
    for f in example["flows"]:
        kind=f["kind"]; rate=Q(f["rate"])
        if kind=="task":
            task=J[f["id"]]; ins=task["input"]; out=task["output"]; sec=task["seconds"]; watts=task["watts"]; group=task["slot"]
            if group=="quarry" and f["automationWatts"]:
                sec=Q(sec)*Q(str(CFG["timing"]["quarryDrillDurationMultiplier"]))
        elif kind=="cultivar":
            c=C[f["id"]]; ins={}; out=c["out"]; sec=c["seconds"]; watts=0; group="orchard"
        else:
            require(kind=="grind","unknown flow kind")
            e=E[f["id"]]; ins=CFG["combat"]["grindInput"]; out=e["out"]; sec=e["grindSeconds"]; watts=e["grindWatts"]; group="grinder"
        for k,v in ins.items(): net[k]-=Q(v)*rate
        for k,v in out.items(): net[k]+=Q(v)*rate
        busy[group]+=Q(sec)*rate
        watt_upper+=watts+f["automationWatts"]
    for k,v in example["fuelPerMinute"].items(): net[k]-=Q(v)
    available=sum(G[id]["watts"]*num for id,num in example["generators"].items())
    # The concrete network uses advanced generators on coal (one unit/generator/minute).
    require(example["generators"]=={"advanced":2} and example["fuelPerMinute"]=={"coal":2},"update fuel accounting if generator topology changes")
    require(all(n>=0 for n in net.values()),f"net deficit: {dict(net)}")
    require(net["worldseed"]==example["targetWorldseedPerMinute"],"wrong target output")
    require(all(b<=example["slotCounts"][s]*60 for s,b in busy.items()),f"slot capacity exceeded: {dict(busy)}")
    require(watt_upper<=available,"simultaneous load exceeds installed power")
    print(f"Terminal flow: {net['worldseed']} Worldseed/min, {watt_upper}/{available} W conservative "
          "all-listed-task upper bound; nonnegative material rates and feasible slot-minutes")
    print("  Material rate slack:", ", ".join(f"{k}={n}" for k,n in net.items() if n and k!="worldseed"))
    print("  Source utilization:", ", ".join(f"{s} {float(b):.2f}/{example['slotCounts'][s]*60}s/min" for s,b in busy.items()))

if __name__=="__main__":
    structure(); reachable(); root_route(); Ledger().witness(); endgame()
    print("PASS: design checks; real scheduler, offline replay, combat RNG, UI, and balance still require implementation/QA.")
