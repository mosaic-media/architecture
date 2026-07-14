<!--
File: docs/engineering/guides/meg-010-performance-engineering/02-runtime-performance.md
Document: MEG-010
Status: Draft
Version: 0.1
-->

# Runtime Performance

---

# Purpose

This chapter defines how performance should be achieved within the Mosaic Runtime.

The Runtime is responsible for executing work across the platform.

Every capability, event, repository operation and background task ultimately depends upon the Runtime behaving efficiently.

A slow Runtime affects every feature.

An efficient Runtime improves every feature.

Runtime performance is therefore considered a platform concern rather than a capability concern.

---

# Runtime Objectives

The Runtime should be:

- responsive
- predictable
- scalable
- observable
- resource-efficient
- resilient under load

Its primary objective is not maximum throughput.

Its objective is maintaining predictable execution while the workload changes.

---

# Performance Responsibilities

The Runtime is responsible for:

- scheduling work
- executing asynchronous tasks
- managing worker utilisation
- preventing resource starvation
- maintaining fairness
- limiting contention
- exposing execution metrics
- supporting graceful degradation

Capabilities should never implement their own execution model.

The Runtime owns execution.

Capabilities own behaviour.

---

# Execution Philosophy

The Runtime should maximise useful work while minimising unnecessary coordination.

Execution should favour:

- asynchronous operations
- message passing
- ownership transfer
- bounded concurrency
- cooperative scheduling

Execution should avoid:

- unnecessary blocking
- excessive synchronisation
- busy waiting
- long-lived locks
- shared mutable state

The fastest lock is the one that never needs to exist.

---

# Scheduling Principles

Scheduling should prioritise:

- fairness
- responsiveness
- bounded latency
- workload isolation

No capability should be capable of monopolising Runtime resources.

Long-running work should not prevent short-running work from executing.

Background work should never delay user-facing operations unnecessarily.

---

# Concurrency Model

Concurrency exists to improve throughput, not to increase complexity.

The Runtime should:

- execute independent work concurrently
- isolate unrelated workloads
- avoid unnecessary serial execution
- minimise coordination overhead

Concurrency should never be introduced simply because multiple CPU cores exist.

More goroutines do not automatically produce more performance.

Occasionally they simply produce a faster route to exhaustion.

---

# Blocking Operations

Blocking operations reduce Runtime utilisation.

Contributors should minimise:

- synchronous network calls
- blocking storage access
- long-running computation
- unnecessary waiting
- idle polling

Where blocking work cannot be avoided, it should be isolated from latency-sensitive execution.

---

# Worker Utilisation

Workers should spend the majority of their lifetime performing useful work.

The Runtime should minimise time spent:

- waiting
- spinning
- retrying
- sleeping unnecessarily
- competing for locks

Idle workers represent unused capacity.

Overloaded workers represent insufficient capacity.

Balanced workers represent healthy scheduling.

---

# Work Distribution

Incoming work should be distributed evenly across available execution resources.

Distribution mechanisms should:

- avoid hotspots
- minimise contention
- preserve fairness
- support scaling

Work distribution should remain transparent to capabilities.

A capability should not need to understand where it executes.

---

# Latency Targets

The Runtime should prioritise low scheduling latency.

Execution delays introduced by the Runtime itself should remain small relative to the work being executed.

Scheduling overhead should not become a measurable percentage of total request time.

If scheduling costs become visible in profiling data, they should be investigated.

The Runtime should facilitate work, not become the work.

---

# Resource Management

The Runtime should use system resources efficiently.

This includes:

- CPU
- memory
- goroutines
- network connections
- storage connections
- timers

Resources should be:

- reused where appropriate
- released promptly
- monitored continuously
- bounded wherever possible

Unbounded resource growth is considered a Runtime defect.

---

# Graceful Degradation

As workload increases, the Runtime should degrade gracefully rather than catastrophically.

Preferred responses include:

- increased queue depth
- controlled back-pressure
- reduced throughput
- prioritised scheduling

Avoid:

- deadlocks
- starvation
- cascading failures
- uncontrolled memory growth
- scheduler collapse

A slower Runtime is preferable to one that stops making progress entirely.

---

# Runtime Metrics

The Runtime should expose metrics including:

- active workers
- queued work
- scheduling latency
- task execution duration
- goroutine count
- worker utilisation
- queue depth
- retry rates
- rejected work
- execution failures

These metrics should integrate with the observability platform defined in MEG-008.

Performance that cannot be observed cannot be managed.

---

# Runtime Optimisation

Optimisation efforts should focus on:

- reducing unnecessary scheduling
- reducing contention
- reducing allocation pressure
- reducing idle time
- improving workload distribution
- shortening critical paths

Optimisation should not compromise:

- correctness
- observability
- architectural boundaries
- maintainability

A Runtime that is impossible to understand is eventually impossible to optimise.

---

# Anti-Patterns

The following Runtime behaviours are discouraged:

- unbounded goroutine creation
- blocking event handlers
- shared global locks
- synchronous capability chains
- busy polling
- unnecessary retries
- scheduler-aware business logic
- manual thread management
- hidden background execution

These patterns reduce predictability and make Runtime behaviour increasingly difficult to reason about.

---

# Expected Outcome

After reading this chapter contributors should understand:

- how the Runtime contributes to platform performance
- why execution ownership belongs to the Runtime
- how scheduling affects responsiveness
- how concurrency should be applied
- why fairness is more valuable than raw parallelism
- how Runtime metrics support optimisation

A well-designed Runtime should disappear into the background.

If contributors spend their time thinking about business capabilities instead of fighting execution behaviour, the Runtime is doing its job.

---

# Next File

`03-capability-performance.md`
