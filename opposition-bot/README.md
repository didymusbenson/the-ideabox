# Opposition Bot

A reusable architecture for a formidable but fair opposition agent in a partially observed political, strategic, or narrative simulation.

The bot is not omniscient. It receives delayed and fallible observations, maintains explicit beliefs, selects objectives, constructs plans, tests those plans against likely opposition, and controls when to observe, probe, press, commit, consolidate, or disengage.

The design is intended to remain self-contained here so it can later be transplanted into a larger simulation project.

## Design goals

- **Formidable through adaptation, not cheating.** The bot should learn, exploit, and revise faster than a brittle scripted opponent without reading hidden truth.
- **Auditable decisions.** Important beliefs, scores, plans, and committed state changes should be explainable after the fact.
- **Deterministic simulation core.** Given the same initial state, seed, and inputs, the committed history should be reproducible.
- **Scalable attention.** Most populations remain aggregated; entities are promoted to individual simulation only when politically connected, observed, targeted, or narratively relevant.
- **Portable components.** Belief, planning, tempo, scheduling, and adjudication should have explicit interfaces rather than being fused into one agent prompt.

## Architecture

```text
Actor-specific observations
          |
          v
1. Belief state / POMDP approximation
   "What is probably happening?"
          |
          v
2. Utility objective selection
   "What matters most now?"
          |
          v
3. HTN / GOAP planning
   "What sequence could achieve it?"
          |
          v
4. Adversarial evaluation
   "How might others counter it?"
          |
          v
5. OODA tempo control
   "Observe, probe, press, commit, wait, or withdraw?"
          |
          v
Proposed events -> adjudicator -> committed deltas
          |                         |
          +---- event ledger <------+
                    |
                    v
          new actor-specific observations
```

OODA is the outer feedback loop. The five components make its orientation, decision, and action stages concrete.

## Core concepts

### 1. Belief state / POMDP approximation

The bot plans from what it believes, not from true world state. Its model tracks competing hypotheses about actor intent, readiness, loyalty, location, and other strategically relevant facts. New observations update those beliefs according to source reliability, age, deception risk, and consistency with prior evidence.

Information gathering is therefore a real action: a reversible probe may have little immediate payoff but high value if it distinguishes weakness from a trap.

Exact POMDP solving is usually intractable for a large simulation. The proposed first implementation uses factored beliefs plus a small set of competing hypotheses, with particle filtering or Monte Carlo sampling available later.

### 2. Utility objective selection

Candidate objectives are scored continuously rather than activated by rigid scripts. A basic score can combine strategic value, urgency, feasibility, confidence, resource cost, political risk, and opportunity cost.

Hysteresis prevents thrashing: the bot retains its current objective unless a replacement is materially better or the present objective becomes invalid.

### 3. HTN / GOAP planning

- **HTN** provides authored campaign doctrine by decomposing abstract tasks into recognizable phases.
- **GOAP** searches among actions with preconditions, effects, and costs to fill tactical gaps or find alternate routes.

A hybrid is preferred: HTN chooses campaign shape; GOAP adapts the details to current conditions.

### 4. Adversarial evaluation

Before execution, candidate plans are tested against plausible counteractions. Strict minimax is often too pessimistic for political simulations, so expectimax, opponent-specific response models, shallow Monte Carlo rollouts, and regret-sensitive scoring are better defaults.

The bot should prefer plans that remain acceptable when its leading hypothesis is wrong, especially when actions are costly or irreversible.

### 5. OODA tempo control

Tempo does not mean acting as often as possible. It means choosing how quickly to close the loop and how much evidence to demand before commitment.

The initial controller has six modes:

- **MONITOR:** gather routine observations at low cost.
- **PROBE:** use reversible actions to reduce consequential uncertainty.
- **PRESS:** exploit a confirmed, perishable advantage with short loops.
- **COMMIT:** execute a costly or difficult-to-reverse plan.
- **CONSOLIDATE:** restore resources, reduce decision debt, and measure consequences.
- **DISENGAGE:** stop or unwind a plan whose assumptions or acceptable-loss bounds failed.

Different systems operate at different cadences: strategic, operational, crisis, and event-triggered reactive loops. A crisis wakes only the relevant subsystem rather than accelerating the entire world.

## Event-driven simulation

Three structures have separate responsibilities:

```text
Event queue  = pending future work
Event ledger = append-only history of proposals and committed outcomes
State store  = current authoritative truth
```

The queue orders work by simulation time, priority, and a monotonic sequence number. Handlers calculate proposed deltas without mutating state. The adjudicator validates the proposal against current truth, commits accepted deltas atomically, records the result, and emits delayed actor-specific observations and follow-up events.

See [`docs/architecture.md`](./docs/architecture.md) for the detailed decision model and [`docs/event-queues.md`](./docs/event-queues.md) for algorithms and reference code.

## Recommended first implementation

```text
Binary-heap event queue
+ append-only event ledger
+ factored probabilistic beliefs
+ utility objective selection with hysteresis
+ HTN campaign templates
+ GOAP tactical search
+ shallow expectimax or Monte Carlo counterplay
+ six-mode tempo controller
```

## Open design questions

- Which belief factors are generic engine primitives, and which belong to a specific scenario?
- How should confidence decay differ for intent, capability, location, and institutional loyalty?
- What limits should govern probes so information gathering has political and resource costs?
- How much adversarial search is affordable per strategic, operational, and crisis loop?
- Which event and ledger formats should be stable portability contracts?
- When should an individual or institution collapse back into an aggregate cohort?
