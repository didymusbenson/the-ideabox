# Opposition Bot Architecture

## 1. Decision topology

```text
Observation delivery
        |
        v
Belief update
        |
        v
Objective scoring
        |
        v
Candidate planning
        |
        v
Counterplay evaluation
        |
        v
Tempo decision
        |
        v
Event proposal
        |
        v
Adjudication and atomic commit
        |
        v
Observation generation and delayed delivery
```

No decision component reads hidden truth. Only the adjudicator and state store know authoritative state; actors receive scoped observations.

## 2. Belief-state model

A POMDP is described by:

- `S`: possible world states;
- `A`: available actions;
- `T(s' | s, a)`: transition probabilities;
- `R(s, a)`: reward or cost;
- `O`: possible observations;
- `Z(o | s', a)`: observation likelihoods;
- `b(s)`: current probability distribution over states.

After action `a` and observation `o`, the conceptual update is:

```text
b'(s') proportional to
    Z(o | s', a)
    * sum over s of [T(s' | s, a) * b(s)]
```

The update has three stages:

1. **Predict:** evolve old beliefs through expected world transitions.
2. **Correct:** weight predicted states by how well they explain the observation.
3. **Normalize:** make posterior probabilities sum to one.

### Practical representation

Avoid one distribution over every possible world. Use factored estimates:

```python
beliefs = {
    "faction_red.intent": {
        "attack": 0.55,
        "defend": 0.20,
        "negotiate": 0.10,
        "deceive": 0.15,
    },
    "faction_red.readiness": {
        "low": 0.15,
        "medium": 0.50,
        "high": 0.35,
    },
}
```

Each estimate should retain provenance and freshness:

```python
from dataclasses import dataclass

@dataclass
class Estimate:
    probabilities: dict[str, float]
    updated_at: int
    confidence: float
    evidence_ids: list[str]
```

A small discrete updater:

```python
from collections import defaultdict


def update_belief(belief, action, observation, transition, observe):
    predicted = defaultdict(float)

    for old_state, old_probability in belief.items():
        for new_state, transition_probability in transition(
            old_state, action
        ).items():
            predicted[new_state] += (
                old_probability * transition_probability
            )

    posterior = {
        state: probability * observe(observation, state, action)
        for state, probability in predicted.items()
    }

    total = sum(posterior.values())
    if total == 0:
        return dict(predicted)

    return {
        state: probability / total
        for state, probability in posterior.items()
    }
```

A zero-likelihood observation should be treated as model failure or anomalous evidence, not proof that the world has no possible state. Preserve the prediction, record the anomaly, and consider widening the hypothesis set.

### Value of information

A probe is useful when it improves later decisions enough to justify its costs:

```text
probe value
= expected improvement in downstream decisions
- direct cost
- exposure risk
- delay cost
```

Approximate this by sampling each likely observation, updating beliefs, selecting the best resulting action, and comparing the expected result with acting immediately.

### Scalable approximations

- **Factored beliefs:** separate intent, capability, loyalty, and location.
- **Top hypotheses:** preserve several coherent explanations rather than one story.
- **Particle filters:** maintain sampled plausible worlds when dependencies matter.
- **Monte Carlo planning:** sample beliefs during candidate evaluation.
- **Threshold policies:** probe below confidence bounds; commit above risk-adjusted utility bounds.

Start with factored beliefs and explicit hypotheses. Add particles only where correlations materially affect decisions.

## 3. Utility objectives

A generic objective score:

```text
score
= strategic value
* urgency
* feasibility
* confidence
- resource cost
- political risk
- opportunity cost
```

Nonlinear curves should shape inputs. For example, urgency may remain low until a province approaches defection and then rise sigmoidally.

Add hysteresis:

```text
switch objectives only if
new score > current score * (1 + switch margin)
```

Forced invalidation bypasses hysteresis when the current objective becomes impossible or unacceptable.

## 4. HTN and GOAP

### HTN

Hierarchical Task Networks encode doctrine:

```text
Stabilize province
|- assess local conditions
|- choose political approach
|  |- negotiate with institutions
|  |- offer concessions
|  `- isolate hostile leadership
|- secure critical services
`- monitor reaction
```

Different actor types can have different decomposition methods, creating institutional character without changing the scheduler.

### GOAP

GOAP actions expose preconditions, effects, duration, observability, uncertainty, and cost:

```python
actions = {
    "recruit_informant": {
        "requires": {"funds": True},
        "adds": {"local_intelligence": True},
        "cost": 3,
    },
    "identify_leaders": {
        "requires": {"local_intelligence": True},
        "adds": {"leadership_mapped": True},
        "cost": 2,
    },
}
```

Dijkstra or A* can search symbolic states. Planning costs should include time, resources, exposure, reversibility, and uncertainty rather than a single abstract action count.

## 5. Adversarial evaluation

For each candidate plan:

1. identify what other actors could observe;
2. generate responses compatible with their beliefs, incentives, and capabilities;
3. simulate the bot's likely counter-response;
4. score the resulting branches.

Useful methods:

- **Expectimax:** probability-weight plausible responses.
- **Risk-sensitive search:** overweight severe but credible outcomes.
- **Opponent models:** condition responses on actor doctrine and preferences.
- **Monte Carlo rollouts:** sample uncertain worlds and event outcomes.
- **Regret minimization:** penalize plans that collapse when the leading belief is wrong.

A practical score:

```text
plan value
= expected outcome
- resource cost
- expected counteraction damage
- exposure cost
- irreversibility penalty
- model-risk penalty
```

## 6. Tempo controller

Tempo controls loop closure, evidence requirements, and scheduling cadence.

### Inputs

- decision latency;
- world volatility;
- observation age;
- opportunity half-life;
- action commitment and reversibility;
- uncertainty and confidence;
- initiative;
- resource readiness;
- loss rate;
- decision debt accumulated while acting quickly.

### Modes

```python
def choose_tempo(ctx):
    if ctx.plan_invalidated or ctx.loss_rate > ctx.loss_tolerance:
        return "DISENGAGE"

    if ctx.decision_debt > 0.60 or ctx.resources_depleted:
        return "CONSOLIDATE"

    if ctx.uncertainty > 0.65 and ctx.reversible_probe_available:
        return "PROBE"

    if ctx.opportunity_urgency > 0.80 and ctx.confidence > 0.60:
        return "PRESS"

    if (
        ctx.expected_advantage > 0.70
        and ctx.confidence > 0.75
        and ctx.resources_ready
    ):
        return "COMMIT"

    return "MONITOR"
```

The thresholds are scenario tuning parameters, not universal constants.

### Cadence

```python
intervals = {
    "MONITOR": 24,
    "PROBE": 8,
    "PRESS": 2,
    "COMMIT": 1,
    "CONSOLIDATE": 12,
    "DISENGAGE": 6,
}
```

A robust implementation also clamps cadence according to volatility and event budgets. Pressing faster than evidence can arrive creates decision debt and should eventually force consolidation.

### Operating inside another actor's loop

The objective is not merely to tick faster. The bot tries to change relevant conditions before another actor's orientation remains useful:

1. perform a reversible probe;
2. observe the response;
3. detect the opponent's commitment;
4. switch or press before that opponent reorients;
5. disengage if the observed response invalidates the plan.

This requires explicit observation delay, commitment, and plan-version mechanics; otherwise “tempo” degrades into arbitrary action bonuses.

## 7. Aggregate-to-individual simulation

Inactive populations should remain cohorts, provinces, or institutions. Promote an entity when it becomes:

- politically connected;
- directly observed;
- targeted by a plan;
- causally important to an active event;
- narratively relevant.

On promotion, instantiate details deterministically from aggregate state and a stable seed. On collapse, summarize durable effects back into the aggregate, retain identity references needed by the ledger, and discard transient detail. Promotion and collapse are committed events so replay reproduces the same boundary transitions.

## 8. Initial integration boundary

The opposition agent should expose narrow commands:

```text
receive(observation)
orient(now) -> belief deltas
select_objective(now) -> objective
plan(objective, now) -> candidates
red_team(candidates, now) -> scored candidates
choose_tempo(context) -> mode and next wake time
propose(plan_step) -> proposed events
```

Only the adjudicator may commit authoritative world deltas. This keeps bot intelligence replaceable and prevents accidental omniscience or direct mutation.
