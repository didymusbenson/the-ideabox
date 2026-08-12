# Event Queues and Ledger

## Responsibilities

```text
Event queue  = ordered pending work
Event ledger = permanent record of proposed, rejected, and committed events
State store  = current authoritative state
```

An event queue is not history. Processed or cancelled work leaves the queue; durable outcomes remain in the ledger.

## Event lifecycle

1. An actor or system proposes an event.
2. The scheduler inserts it with execution time, priority, and sequence number.
3. The scheduler removes the next due event.
4. The adjudicator validates it against current state and permissions.
5. A handler calculates deltas without mutating state.
6. Accepted deltas commit atomically.
7. The ledger records proposal, adjudication, deltas, and generated observations.
8. Follow-up events and actor-specific observation deliveries enter the queue.

The event must be validated when executed, not only when scheduled: intervening events may invalidate its assumptions.

## Queue algorithms

### FIFO queue

Use a double-ended queue for arrival-order work:

```python
from collections import deque

queue = deque()
queue.append(event)
event = queue.popleft()
```

Typical applications include command inboxes, already-ordered same-tick work, and observation delivery where simulation time is handled elsewhere. Append and pop-left are constant time.

### Binary-heap priority queue

Use a min-heap for discrete-event simulation:

```python
import heapq

heapq.heappush(heap, (event.time, event.priority, event.sequence, event))
event = heapq.heappop(heap)[-1]
```

Insertion and extraction are logarithmic. A monotonic sequence number makes equal-time, equal-priority ordering stable and deterministic.

### Timing wheel

Divide near-future time into fixed-resolution buckets. Advancing time moves around the wheel and processes the current bucket. Timing wheels can handle very large timer volumes efficiently when time resolution and maximum delay are constrained.

### Calendar queue

Partition time into dynamically sized ranges and order events within each bucket. It can outperform a heap for enormous, well-distributed workloads, but tuning and pathological time distributions add complexity. Begin with a heap and profile before replacing it.

## Reference implementation

```python
from dataclasses import dataclass, field
from itertools import count
import heapq
from typing import Any, Callable

_sequence = count()


@dataclass(order=True)
class ScheduledEvent:
    time: int
    priority: int
    sequence: int = field(init=False)
    kind: str = field(compare=False)
    payload: dict[str, Any] = field(compare=False)
    actor_id: str | None = field(default=None, compare=False)
    event_id: str | None = field(default=None, compare=False)
    cancelled: bool = field(default=False, compare=False)

    def __post_init__(self):
        self.sequence = next(_sequence)


class Simulation:
    def __init__(self, state):
        self.time = 0
        self.state = state
        self.queue: list[ScheduledEvent] = []
        self.handlers: dict[str, Callable] = {}
        self.ledger: list[dict[str, Any]] = []

    def register(self, kind, handler):
        self.handlers[kind] = handler

    def schedule(self, event):
        if event.time < self.time:
            raise ValueError("cannot schedule an event in the past")
        heapq.heappush(self.queue, event)

    def run_until(self, end_time):
        while self.queue and self.queue[0].time <= end_time:
            event = heapq.heappop(self.queue)
            if event.cancelled:
                continue

            self.time = event.time
            self.process(event)

        self.time = end_time

    def process(self, event):
        self.ledger.append({
            "phase": "proposed",
            "time": self.time,
            "event_id": event.event_id,
            "event": event.kind,
            "actor": event.actor_id,
            "payload": event.payload,
        })

        handler = self.handlers[event.kind]

        # Handlers calculate results; they do not mutate authoritative state.
        result = handler(self.state, event)

        if not result["accepted"]:
            self.ledger.append({
                "phase": "rejected",
                "time": self.time,
                "event_id": event.event_id,
                "event": event.kind,
                "reason": result["reason"],
            })
            return

        apply_deltas_atomically(self.state, result["deltas"])

        self.ledger.append({
            "phase": "committed",
            "time": self.time,
            "event_id": event.event_id,
            "event": event.kind,
            "deltas": result["deltas"],
            "observations": result.get("observations", []),
        })

        for followup in result.get("followups", []):
            self.schedule(followup)
```

`apply_deltas_atomically` should validate the complete delta set before applying any part of it. A production implementation should write ledger and state changes within one transaction or use a durable commit protocol so a crash cannot leave them inconsistent.

## Example observation handler

```python
def handle_intelligence_report(state, event):
    report = event.payload

    if report["source_id"] not in state["active_sources"]:
        return {
            "accepted": False,
            "reason": "source unavailable",
        }

    return {
        "accepted": True,
        "deltas": [],
        "observations": [{
            "observer": event.actor_id,
            "kind": "intelligence",
            "data": report["claim"],
            "reliability": report["reliability"],
            "observed_at": report["observed_at"],
        }],
        "followups": [
            ScheduledEvent(
                time=event.time,
                priority=20,
                kind="opposition_reorient",
                actor_id=event.actor_id,
                payload={},
            )
        ],
    }
```

## Observations, not omniscience

Schedule delivery of scoped observations instead of copying truth into an actor's state:

```python
ScheduledEvent(
    time=now + communication_delay,
    priority=10,
    kind="deliver_observation",
    actor_id="opposition_bot",
    payload={
        "claim": "province readiness is low",
        "source": "regional_office",
        "reliability": 0.62,
        "observed_at": now,
    },
)
```

This makes geography, bureaucracy, sensor quality, interception, deception, and communication delay first-class mechanics.

## Cancellation and stale work

Removing arbitrary entries from a heap is awkward. Use lazy cancellation:

```python
event.cancelled = True
```

Discard the event when it reaches the head. For durable replay, record cancellation as its own event rather than relying only on mutable in-memory flags.

Version plans so superseded actions cannot fire:

```python
payload = {
    "plan_id": "plan-17",
    "plan_version": 4,
}
```

At execution:

```python
if event.payload["plan_version"] != state["plans"]["plan-17"]["version"]:
    reject_as_stale()
```

Also support idempotency keys so retrying a delivery or command does not commit the same logical action twice.

## Determinism rules

- Use integer simulation ticks or fixed-point time, not wall-clock floats.
- Break ties with persisted monotonic sequence numbers.
- Seed randomness explicitly and record either seeds or sampled outcomes.
- Keep handlers pure: input state plus event produces proposed deltas.
- Give every event and causally generated follow-up a stable ID.
- Record schema versions in ledger entries.
- Never depend on dictionary iteration, thread timing, or external response order.
- Revalidate events at execution time.

## Ledger shape

A useful committed record includes:

```json
{
  "schema_version": 1,
  "phase": "committed",
  "event_id": "evt-1042",
  "caused_by": "evt-1031",
  "simulation_time": 880,
  "actor_id": "opposition_bot",
  "kind": "conduct_probe",
  "proposal": {},
  "adjudication": {
    "accepted": true,
    "ruleset_version": "v1"
  },
  "deltas": [],
  "observation_ids": ["obs-440"],
  "random_draws": [],
  "state_hash_after": "..."
}
```

The post-commit state hash catches replay divergence and continuity corruption. Periodic snapshots can accelerate loading, while the ledger remains the reconstruction authority after the snapshot boundary.

## Basic applications

- delayed messages and intelligence reports;
- movement and travel completion;
- construction, recruitment, and recovery timers;
- scheduled institutional decisions;
- resource production and upkeep;
- expiring opportunities and commitments;
- plan wake-ups driven by tempo mode;
- promotion and collapse of simulated individuals;
- consequences that unfold over several timescales;
- deterministic replay and debugging.

## Opposition-bot loop as events

```text
deliver_observation
  -> update_belief
  -> orient
  -> score_objectives
  -> build_candidates
  -> evaluate_counterplay
  -> select_tempo
  -> propose_action
  -> adjudicate and commit
  -> generate delayed observations
  -> schedule next wake-up
```

These may be separate queued events when observability and interruption matter, or one atomic orientation transaction when intermediate stages are implementation detail. Strategic decisions should retain trace records even if their internal stages are not separate world events.
