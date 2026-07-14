<!--
File: docs/engineering/guides/meg-010-performance-engineering/11-benchmarking.md
Document: MEG-010
Status: Draft
Version: 0.1
-->

# Benchmarking

---

# Purpose

This chapter defines how benchmarking should be performed throughout the Mosaic platform.

Benchmarking provides objective measurements of system performance under controlled conditions.

Its purpose is not to produce impressive numbers for documentation or social media.

Its purpose is to provide repeatable evidence that engineering decisions improve the platform.

---

# Benchmarking Objectives

Benchmarking should be:

- repeatable
- measurable
- representative
- automated
- comparable
- reproducible

A benchmark should provide confidence that a change genuinely improves performance rather than merely changing it.

---

# Benchmarking Philosophy

Benchmarks exist to answer engineering questions.

Examples include:

- Is this implementation faster?
- Does this allocate less memory?
- Has latency improved?
- Has throughput increased?
- Has scalability changed?

Benchmarks should never exist solely because every respectable project has a benchmark directory.

Numbers without context are surprisingly effective at misleading people.

---

# Benchmark Scope

Benchmarking should cover:

- Runtime scheduling
- capability execution
- repository behaviour
- storage access
- event throughput
- serialization
- memory allocation
- caching behaviour

Benchmarks should focus on components that materially influence platform performance.

---

# Representative Workloads

Benchmarks should simulate realistic workloads.

Representative scenarios include:

- common API requests
- event processing
- repository operations
- metadata retrieval
- cache hits
- cache misses
- background processing
- concurrent execution

Artificial workloads may be useful for investigation but should not replace representative testing.

---

# Isolation

Benchmarks should isolate the component being measured.

External influences should be minimised wherever practical, including:

- network variability
- unrelated background work
- logging overhead
- external dependencies

The objective is to measure the behaviour under investigation rather than the behaviour of the surrounding environment.

---

# Repeatability

Benchmarks should produce consistent results across multiple executions.

Contributors should:

- execute benchmarks multiple times
- compare averages
- consider variance
- identify anomalies

One unusually fast benchmark result is rarely evidence of improvement.

It is often evidence that statistics have temporarily given up.

---

# Metrics

Benchmarks should record metrics including:

- execution time
- throughput
- memory allocation
- allocation count
- garbage collection impact
- CPU utilisation where appropriate

Measurements should focus upon outcomes that directly influence platform behaviour.

---

# Comparative Testing

Benchmark results should always be compared against a baseline.

Useful comparisons include:

- before and after changes
- alternative implementations
- previous releases
- regression detection

Benchmarks without a comparison provide limited engineering value.

Improvement requires something to improve upon.

---

# Automation

Performance benchmarks should be automated wherever practical.

Automation improves:

- consistency
- repeatability
- regression detection
- contributor confidence

Performance regressions should be detected as early as possible during development.

---

# Regression Detection

Benchmarks should be retained over time.

Historical results allow contributors to identify:

- gradual degradation
- unexpected regressions
- scaling issues
- architectural improvements

Small regressions often accumulate into significant platform problems if left unnoticed.

---

# Interpreting Results

Benchmark results should be interpreted carefully.

Contributors should consider:

- workload realism
- statistical variation
- architectural impact
- maintainability
- complexity introduced

A five percent improvement that doubles implementation complexity is rarely a good trade.

---

# Limitations

Benchmarks measure isolated behaviour.

They do not measure:

- production workloads
- user experience
- operational complexity
- architectural quality

Benchmarking should therefore complement, rather than replace:

- profiling
- observability
- load testing
- production telemetry

Fast code inside an inefficient architecture remains part of an inefficient architecture.

---

# Optimisation Strategy

When using benchmark results to guide optimisation, contributors should:

1. Confirm the benchmark reflects a real workload.
2. Compare against a baseline.
3. Measure memory allocation.
4. Measure throughput.
5. Investigate regressions.
6. Validate architectural impact.
7. Retain benchmark history.

Benchmarks should guide engineering decisions rather than dictate them.

---

# Anti-Patterns

The following benchmarking behaviours are discouraged:

- benchmarking unrealistic workloads
- chasing insignificant improvements
- ignoring allocation metrics
- deleting historical benchmarks
- comparing unrelated measurements
- optimising exclusively for benchmark scores
- drawing conclusions from single executions
- benchmarking without understanding the workload

These behaviours produce attractive graphs while providing very little useful engineering information.

---

# Expected Outcome

After reading this chapter contributors should understand:

- why benchmarking exists
- how benchmarks should be designed
- why realistic workloads matter
- how benchmark results should be interpreted
- why regression detection is important
- how benchmarking complements observability and profiling

Good benchmarks answer meaningful engineering questions.

Great benchmarks prevent contributors from confidently optimising the wrong thing.

---

# Next File

`12-profiling.md`
