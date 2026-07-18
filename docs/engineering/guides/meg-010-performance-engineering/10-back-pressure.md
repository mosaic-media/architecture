<!--
File: docs/engineering/guides/meg-010-performance-engineering/10-back-pressure.md
Document: MEG-010
Status: Draft
-->

# Back-Pressure

---

# Purpose

This chapter defines how the Mosaic platform should respond when workloads exceed available processing capacity.

No system has unlimited resources.

Eventually every platform encounters workloads that exceed what can be processed immediately.

Back-pressure ensures the platform remains stable by slowing the rate at which work enters the system rather than allowing resource consumption to grow without bound.

---

# Back-Pressure Objectives

Back-pressure should be:

- automatic
- predictable
- observable
- proportional
- recoverable
- workload-aware

The objective is not to eliminate overload.

The objective is to survive overload without allowing it to become failure.

---

# Back-Pressure Philosophy

Back-pressure is a safety mechanism.

It prevents the platform from accepting work faster than it can reasonably process it.

Without back-pressure, overload typically results in:

- growing queues
- excessive memory usage
- increasing latency
- resource starvation
- cascading failures

A slower platform is preferable to an unavailable platform.

---

# Design Principles

Back-pressure should:

- activate automatically
- be measurable
- remain bounded
- recover naturally
- avoid cascading effects

Contributors should design workloads assuming that temporary overload is inevitable.

The platform should absorb pressure rather than amplify it.

---

# Sources of Pressure

Back-pressure may be required when:

- request volume increases
- event throughput exceeds processing capacity
- storage systems become slow
- external services become unavailable
- worker pools become saturated
- module execution becomes excessive
- network latency increases

Pressure may originate anywhere within the platform.

Its effects should remain local wherever possible.

---

# Admission Control

The Runtime should control how much work is admitted into the system.

Admission control may include:

- bounded queues
- concurrency limits
- request throttling
- workload prioritisation

Unlimited admission is not scalability.

It is delayed failure.

---

# Queue Management

Queues should absorb temporary bursts rather than sustained overload.

Queues should remain:

- bounded
- observable
- measurable
- workload-specific where appropriate

When queues reach capacity, the Runtime should apply back-pressure rather than continuing to allocate memory indefinitely.

Queues are shock absorbers.

They are not infinite warehouses.

---

# Concurrency Limits

Concurrency should remain explicitly bounded.

Limits should be applied where appropriate to:

- worker pools
- repository operations
- storage connections
- external API calls
- module execution
- background processing

Unlimited parallelism usually produces contention rather than throughput.

---

# Work Rejection

When the platform cannot safely accept additional work, it should reject work predictably.

Rejection strategies may include:

- temporary refusal
- retry recommendations
- deferred execution
- priority reduction

Rejected work should fail quickly rather than consuming resources while waiting indefinitely.

Fast failure is often kinder than slow disappointment.

---

# Graceful Degradation

When back-pressure activates, the platform should degrade gracefully.

Examples include:

- delaying non-essential work
- reducing background processing
- slowing cache refreshes
- postponing analytics
- prioritising user-facing operations

Essential business functionality should receive priority over maintenance activities.

---

# Retry Behaviour

Retries should cooperate with back-pressure.

Retries should:

- be bounded
- use exponential backoff
- include jitter where appropriate
- terminate after reasonable limits

Immediate retries during overload simply increase overload.

The system does not become less busy because another identical request arrived half a millisecond later.

---

# Module Behaviour

Modules must respect Runtime back-pressure.

Modules should:

- honour execution limits
- avoid uncontrolled retries
- avoid creating unbounded background work
- expose retry behaviour

The Module Runtime may suspend or delay modules that ignore platform back-pressure policies.

---

# Recovery

Back-pressure should automatically relax as workload decreases.

Recovery should be:

- gradual
- observable
- predictable

The Runtime should avoid oscillating rapidly between overload and recovery states.

Stable recovery produces more predictable behaviour than aggressive recovery.

---

# Back-Pressure Metrics

The platform should expose metrics including:

- queue depth
- rejected work
- deferred work
- worker utilisation
- concurrency limits
- retry count
- queue wait time
- processing delay
- overload duration

These metrics should integrate with the observability standards defined in [MEG-008](../meg-008-observability/index.md).

Back-pressure should never become an invisible Runtime behaviour.

---

# Optimisation Strategy

When improving back-pressure behaviour, contributors should investigate in the following order:

1. Remove unnecessary work.
2. Reduce queue growth.
3. Improve workload prioritisation.
4. Reduce processing latency.
5. Improve concurrency limits.
6. Optimise retry behaviour.
7. Tune Runtime scheduling.

Back-pressure should reduce pressure rather than merely relocating it elsewhere in the platform.

---

# Anti-Patterns

The following behaviours are discouraged:

- unbounded queues
- unlimited retries
- unlimited concurrency
- retry storms
- hidden overload
- silent request dropping
- infinite buffering
- synchronous waiting under overload
- assuming downstream systems have infinite capacity

These behaviours transform temporary pressure into platform-wide instability.

---

# Expected Outcome

After reading this chapter contributors should understand:

- why back-pressure exists
- how overload should be managed
- why queues must remain bounded
- how graceful degradation protects responsiveness
- why retries require discipline
- how Runtime metrics expose pressure within the platform

A resilient platform is not one that never experiences pressure.

It is one that knows when to stop accepting more work before everything catches fire.
