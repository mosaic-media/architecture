<!--
File: docs/engineering/guides/meg-010-performance-engineering/12-profiling.md
Document: MEG-010
Status: Draft
-->

# Profiling

---

# Purpose

This chapter defines how profiling should be used throughout the Mosaic platform.

While benchmarking measures performance under controlled conditions, profiling explains **why** performance behaves the way it does.

Profiling provides visibility into how the platform actually spends its time and resources.

Optimisation without profiling is little more than educated guesswork.

---

# Profiling Objectives

Profiling should be:

- evidence-driven
- repeatable
- targeted
- representative
- measurable
- actionable

The purpose of profiling is not to find activity.

It is to identify activity that meaningfully affects platform performance.

---

# Profiling Philosophy

Profiling exists to explain system behaviour.

It should answer questions such as:

- Where is execution time spent?
- Which functions allocate the most memory?
- What causes garbage collection pressure?
- Which operations block execution?
- Which components scale poorly?

Profiling should always precede significant optimisation work.

Assumptions are useful for forming hypotheses.

Profiles exist to prove or disprove them.

---

# When to Profile

Profiling should be performed when:

- performance regressions are detected
- benchmarks unexpectedly change
- latency increases
- throughput decreases
- memory usage grows unexpectedly
- CPU utilisation becomes excessive
- scaling behaviour changes
- contributors suspect inefficient execution

Profiling should investigate observed behaviour rather than hypothetical concerns.

---

# Types of Profiling

The platform should make use of several complementary profiling techniques.

These include:

- CPU profiling
- memory profiling
- allocation profiling
- blocking profiling
- mutex profiling
- goroutine profiling
- execution tracing

Each provides visibility into different aspects of Runtime behaviour.

No single profile explains the entire system.

---

# CPU Profiling

CPU profiling identifies where execution time is spent.

CPU investigations should focus on:

- expensive algorithms
- repeated computation
- unnecessary work
- inefficient loops
- serialization overhead

High CPU utilisation is not automatically a problem.

Unexpected CPU utilisation usually is.

---

# Memory Profiling

Memory profiling identifies:

- allocation hotspots
- retained objects
- heap growth
- excessive object lifetime
- allocation-heavy code paths

The objective is to reduce unnecessary allocation rather than simply reducing memory usage.

Healthy memory usage is preferable to constant allocation churn.

---

# Allocation Profiling

Allocation profiling should identify:

- frequently allocated objects
- repeated temporary structures
- unnecessary copying
- inefficient data movement

Allocation rate often influences performance more than absolute memory consumption.

Reducing allocation pressure typically benefits both latency and garbage collection.

---

# Blocking Profiling

Blocking profiles identify execution that waits unnecessarily.

Common causes include:

- lock contention
- synchronous I/O
- channel contention
- long-running storage operations
- external service latency

Blocking often produces greater performance improvements than CPU optimisation because waiting contributes no useful work.

---

# Goroutine Profiling

Goroutine profiles should identify:

- excessive goroutine creation
- blocked goroutines
- leaked goroutines
- unexpected execution patterns

Large numbers of goroutines are not inherently problematic.

Large numbers of idle or permanently blocked goroutines usually are.

---

# Execution Tracing

Execution tracing provides visibility into Runtime behaviour over time.

Tracing should help explain:

- scheduling behaviour
- execution ordering
- concurrent workloads
- latency propagation
- Runtime utilisation

Tracing complements profiling by showing how work flows through the system rather than merely where resources are consumed.

---

# Representative Workloads

Profiles should be captured using representative workloads.

Suitable scenarios include:

- common user interactions
- metadata synchronisation
- event processing
- module execution
- repository operations
- concurrent requests

Profiling an unrealistic workload frequently produces unrealistic conclusions.

---

# Comparing Profiles

Profiles should be compared over time.

Useful comparisons include:

- before and after optimisation
- previous releases
- regression investigations
- scaling evaluations

Historical profiles often reveal gradual degradation that individual measurements fail to expose.

---

# Profiling Workflow

Contributors should follow a consistent workflow:

1. Observe the problem.
2. Capture relevant profiles.
3. Identify bottlenecks.
4. Form a hypothesis.
5. Implement a targeted improvement.
6. Profile again.
7. Confirm measurable improvement.

Skipping directly from observation to optimisation risks solving the wrong problem.

---

# Optimisation Decisions

Profiling should influence engineering decisions.

However, contributors should also consider:

- architectural consistency
- maintainability
- readability
- correctness
- observability

A profile may justify optimisation.

It does not justify damaging the architecture.

---

# Anti-Patterns

The following profiling behaviours are discouraged:

- profiling synthetic workloads exclusively
- profiling after optimisation rather than before
- ignoring allocation profiles
- treating CPU usage as the only metric
- drawing conclusions from incomplete profiles
- optimising without validating results
- deleting historical profile data
- assuming today's bottleneck will remain tomorrow's bottleneck

These behaviours produce misleading conclusions and frequently encourage unnecessary optimisation.

---

# Expected Outcome

After reading this chapter contributors should understand:

- why profiling is essential
- when profiling should occur
- how different profile types complement each other
- how profiling guides optimisation
- why representative workloads matter
- how profiling validates engineering decisions

Profiling turns performance from opinion into evidence.

Evidence, unlike intuition, has the useful habit of being measurable.
