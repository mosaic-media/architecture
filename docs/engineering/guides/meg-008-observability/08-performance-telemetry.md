<!--
File: docs/engineering/guides/meg-008-observability/08-performance-telemetry.md
Document: MEG-008
Status: Draft
Version: 0.1
-->

# Performance Telemetry

> *Performance should be measured as an architectural property, not as a collection of isolated benchmarks.*

---

# Purpose

Performance is frequently treated as a late-stage optimisation exercise.

Within Mosaic, performance is an observable property of the architecture itself.

Every Runtime component contributes to overall platform performance.

Examples include:

- Runtime scheduling
- worker allocation
- capability execution
- repository access
- storage latency
- event propagation

Performance Telemetry exists to measure these architectural behaviours continuously.

Optimisation should always be driven by evidence.

Never intuition.

---

# Philosophy

Within Mosaic:

> **Measure the platform where architectural responsibility exists.**

The Runtime should never ask:

> **Which function is slow?**

Instead it should ask:

> **Which architectural responsibility is consuming time?**

Performance follows ownership.

So should telemetry.

---

# Performance Hierarchy

Performance naturally follows the Runtime Architecture.

```text
Platform

↓

Runtime

↓

Capabilities

↓

Repositories

↓

Storage
```

Every architectural layer exposes performance telemetry independently.

Platform performance emerges from these combined measurements.

---

# Performance Objectives

Performance telemetry exists to answer questions such as:

- Where is latency increasing?
- Which capability is consuming the most CPU?
- Which storage system is the bottleneck?
- Are workers saturated?
- Is startup becoming slower?
- Is the platform scaling as expected?

Without requiring:

- profiling
- production debugging
- source code inspection

---

# Runtime Performance

The Runtime SHOULD expose:

- startup duration
- shutdown duration
- scheduling latency
- execution latency
- queue latency
- dependency resolution time

These measurements describe Runtime behaviour.

Not business behaviour.

---

# Capability Performance

Every capability SHOULD expose:

- execution duration
- invocation count
- success rate
- failure rate
- average latency

Capabilities own business execution.

Performance ownership follows that boundary.

Capabilities should never expose Runtime implementation timings.

---

# Repository Performance

Repositories SHOULD expose:

- load duration
- save duration
- cache utilisation
- transaction latency

Repository telemetry measures:

Persistence behaviour.

Not database internals.

---

# Storage Performance

Every storage engine SHOULD expose metrics appropriate to its workload.

Examples.

PostgreSQL.

- transaction latency
- commit duration

DuckDB.

- analytical query duration
- aggregation throughput

Blob Storage.

- retrieval latency
- streaming throughput

MOS Cache.

- cache lookup latency
- rebuild duration

Storage should be evaluated according to its architectural responsibility.

---

# Event Performance

Runtime Events SHOULD expose:

- publication latency
- delivery latency
- subscriber execution duration
- retry duration

The Runtime should answer:

> **How efficiently does work move through the platform?**

Event throughput becomes an architectural performance characteristic.

---

# Worker Performance

Worker Manager telemetry SHOULD expose:

- worker utilisation
- queue wait time
- execution duration
- idle percentage
- replacement frequency

The Worker Manager owns execution resources.

It therefore owns worker performance telemetry.

---

# Scheduler Performance

The Scheduler SHOULD expose:

- scheduling precision
- delayed execution
- scheduling backlog
- recurring execution latency

Operators should understand:

> **Is the Runtime keeping accurate time?**

Scheduling performance is distinct from execution performance.

---

# Startup Performance

Startup SHOULD expose stage timings.

Examples include:

```text
Configuration

↓

Runtime Kernel

↓

Capability Registration

↓

Dependency Resolution

↓

Activation
```

Slow startup should identify:

The architectural stage responsible.

Not merely:

```
Startup Slow
```

---

# Shutdown Performance

Shutdown SHOULD expose:

- cooldown duration
- draining duration
- disposal duration
- total shutdown time

Graceful shutdown should remain measurable.

Performance includes:

How efficiently the platform stops.

Not only how quickly it starts.

---

# Resource Utilisation

Resource Manager telemetry SHOULD expose:

- CPU utilisation
- memory utilisation
- worker saturation
- queue saturation
- connection utilisation

Resource metrics explain:

Why performance changes.

Not merely that it changed.

---

# Throughput

Throughput SHOULD be measured explicitly.

Examples include:

- Runtime Events per second
- capability executions per second
- repository operations per second
- blob transfers per second

Latency explains one execution.

Throughput explains platform capacity.

Both should remain observable.

---

# Capacity

Capacity differs from utilisation.

Example.

```text
Worker Pool

↓

32 Workers

↓

27 Active
```

Utilisation.

↓

84%.

Capacity.

↓

5 Workers Remaining.

Capacity planning requires both measurements.

---

# Percentiles

Latency SHOULD generally be reported using percentiles.

Examples include:

- P50
- P95
- P99

Average latency frequently hides operational problems.

Percentiles better represent real user experience.

---

# Baselines

Performance should always be interpreted relative to historical baselines.

Example.

```
Capability Activation

↓

180 ms

↓

Normally 60 ms
```

Raw numbers rarely explain behaviour.

Historical comparison provides operational context.

---

# Performance Budgets

Major Runtime components SHOULD define performance budgets.

Examples.

Startup.

```
<10 Seconds
```

Capability activation.

```
<250 ms
```

Repository load.

```
<50 ms
```

Budgets provide operational expectations.

They should remain architectural rather than implementation specific.

---

# Regression Detection

Performance telemetry SHOULD support regression detection.

Examples include:

- startup slowing
- worker utilisation increasing
- storage latency growing
- cache effectiveness decreasing

Operators should discover regressions before users do.

---

# Performance Correlation

Performance telemetry should correlate naturally with:

- traces
- logs
- metrics

Example.

```
High Repository Latency

↓

Trace

↓

Storage Span

↓

PostgreSQL
```

Performance should explain architecture.

Not isolated implementation.

---

# Profiling

Profiling remains an engineering activity.

Performance telemetry identifies:

Where profiling should begin.

It should not replace profiling.

Profilers answer:

> **Which code consumed CPU?**

Telemetry answers:

> **Which architectural responsibility became slower?**

---

# Cost

Performance telemetry SHOULD remain inexpensive.

Avoid:

- excessive sampling
- unnecessary aggregation
- expensive calculations

Observability should not become the platform's largest performance problem.

---

# Anti-Patterns

The following practices are prohibited.

## Function Timings

Publishing latency for every helper function.

---

## Average Only

Reporting only average latency.

---

## Missing Ownership

Performance measurements without architectural ownership.

---

## Duplicate Metrics

Multiple Runtime Services measuring identical behaviour.

---

## Technology Metrics

Organising performance exclusively around implementation technologies.

---

## Reactive Optimisation

Optimising implementation before understanding architectural bottlenecks.

---

# Mosaic Guidelines

Within Mosaic:

- Performance telemetry MUST follow architectural ownership.
- Runtime Services SHOULD expose latency and throughput.
- Capabilities SHOULD expose execution performance.
- Storage SHOULD expose workload-specific performance.
- Percentiles SHOULD be preferred over averages.
- Performance budgets SHOULD be defined for major Runtime components.
- Performance telemetry SHOULD integrate naturally with traces.
- Optimisation SHOULD be evidence driven.

---

# Relationship to MEG

Storage Observability explains:

> **How information systems are behaving.**

Performance Telemetry explains:

> **How efficiently every architectural responsibility is being fulfilled.**

The next chapter introduces **Alerting**, defining how Mosaic converts observable platform behaviour into meaningful operational notifications without overwhelming operators with noise.

---

# Summary

Performance is not one number.

It is the combined behaviour of:

- Runtime
- Capabilities
- Storage
- Resources

Within Mosaic, every performance measurement should reinforce architectural ownership, allowing optimisation to improve the design itself rather than merely accelerating isolated pieces of implementation.

Performance should become understandable.

Not mysterious.

---

# Review Status

**Status**

Draft

**Owner**

Lead Software Architect

**Previous File**

`07-storage-observability.md`

**Next File**

`09-alerting.md`
