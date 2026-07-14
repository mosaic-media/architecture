<!--
File: docs/engineering/guides/meg-010-performance-engineering/06-event-throughput.md
Document: MEG-010
Status: Draft
Version: 0.1
-->

# Event Throughput

---

# Purpose

This chapter defines how event throughput should be managed throughout the Mosaic platform.

Events form the communication backbone of the Reactive Runtime defined in MEG-002.

As the platform grows, event volume will naturally increase.

The goal is therefore not simply to process more events, but to process meaningful events efficiently while maintaining predictable behaviour.

---

# Throughput Objectives

The event system should be:

- scalable
- predictable
- observable
- resilient
- resource-efficient
- back-pressure aware

High throughput should never come at the expense of stability.

The platform should remain responsive under increasing event volume without compromising correctness.

---

# Throughput Philosophy

Event throughput should be achieved by reducing unnecessary work rather than accelerating unnecessary work.

The platform should prioritise:

- fewer events
- smaller events
- faster routing
- efficient consumers
- bounded execution

A million unnecessary events processed perfectly are still a million unnecessary events.

---

# Event Responsibilities

Each event should represent:

- a completed business action
- a meaningful state transition
- information required by downstream consumers

Events should not represent:

- implementation details
- debugging information
- logging messages
- temporary state
- internal control flow

Events communicate business intent.

They are not a substitute for function calls.

---

# Event Size

Events should remain compact.

An event should contain:

- identifiers
- timestamps
- required metadata
- business context necessary for consumers

Events should avoid carrying:

- entire aggregates
- large collections
- binary data
- duplicated information

Large events increase:

- memory usage
- network traffic
- serialization cost
- storage overhead

Small events move through the platform more efficiently.

---

# Event Frequency

Events should only be published when business state changes.

Avoid publishing events:

- repeatedly for identical state
- for polling behaviour
- for implementation milestones
- simply because another system might find them interesting

If no consumer benefits from an event, that event probably should not exist.

---

# Consumer Performance

Consumers should:

- execute independently
- complete quickly
- remain idempotent
- avoid unnecessary storage access

Consumers should avoid:

- blocking other consumers
- performing excessive computation
- waiting synchronously on external services
- chaining long execution paths

Consumers should process events, not monopolise the Runtime.

---

# Parallel Processing

Independent events should be processed concurrently wherever practical.

The Runtime should allow:

- multiple consumers
- parallel execution
- workload isolation
- independent scaling

Event ordering should only be enforced where required by business rules.

Serial execution should never become the default merely because it is easier to implement.

---

# Event Ordering

Ordering guarantees introduce coordination costs.

Ordering should therefore only be enforced when:

- business correctness depends upon it
- data consistency requires it
- user expectations demand it

Most events do not require global ordering.

Avoid paying for guarantees that nobody actually needs.

---

# Event Routing

Routing should minimise overhead.

The event system should:

- locate subscribers efficiently
- avoid duplicate routing
- minimise dispatch latency
- support dynamic registration

Routing performance should remain stable as the number of capabilities increases.

Adding capabilities should not significantly increase dispatch cost.

---

# Event Fan-Out

One event may legitimately produce multiple consumers.

However, excessive fan-out increases:

- CPU utilisation
- scheduling overhead
- memory pressure
- overall system load

Contributors should question events with unusually large subscriber counts.

Sometimes the architecture is broadcasting because nobody wanted to make a decision.

---

# Serialization

Event serialization should be efficient and predictable.

Serialization formats should:

- minimise allocation
- minimise payload size
- remain deterministic
- avoid unnecessary transformation

Events should be serialized once wherever possible.

Repeated transformation increases processing cost without adding value.

---

# Queue Behaviour

Event queues should remain:

- bounded
- observable
- measurable
- resilient

Queue depth should reflect temporary workload fluctuations rather than permanent overload.

Growing queues are symptoms.

They are not solutions.

---

# Throughput Metrics

The event system should expose metrics including:

- events published
- events processed
- processing latency
- queue depth
- dispatch latency
- consumer duration
- retry count
- failed events
- dropped events

These metrics should integrate with the observability standards defined in MEG-008.

Throughput improvements should always be validated with measurement.

---

# Optimisation Strategy

When improving event throughput, contributors should investigate in the following order:

1. Remove unnecessary events.
2. Reduce event size.
3. Reduce consumer work.
4. Improve routing efficiency.
5. Increase parallelism where appropriate.
6. Reduce serialization overhead.
7. Tune Runtime execution.

Throughput should increase because less work is performed, not because the platform works harder.

---

# Anti-Patterns

The following event behaviours are discouraged:

- event storms
- oversized payloads
- unnecessary fan-out
- synchronous consumer chains
- hidden blocking operations
- duplicate event publication
- unbounded queues
- retry loops without limits
- business workflows dependent upon timing assumptions

These behaviours reduce scalability while making performance increasingly unpredictable.

---

# Expected Outcome

After reading this chapter contributors should understand:

- how event volume affects platform performance
- why event size matters
- how efficient consumers improve throughput
- why routing should remain lightweight
- how queue behaviour influences responsiveness
- how throughput should be measured

A healthy event system moves business information efficiently through the platform without becoming the platform itself.

---

# Next File

`07-scheduling-efficiency.md`
