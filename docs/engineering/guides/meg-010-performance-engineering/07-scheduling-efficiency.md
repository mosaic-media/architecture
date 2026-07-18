<!--
File: docs/engineering/guides/meg-010-performance-engineering/07-scheduling-efficiency.md
Document: MEG-010
Status: Draft
-->

# Scheduling Efficiency

---

# Purpose

This chapter defines how work should be scheduled efficiently throughout the Mosaic Runtime.

Scheduling determines when work executes, how resources are shared and how fairly competing workloads are handled.

Poor scheduling can make an otherwise efficient system appear slow.

Efficient scheduling allows the platform to remain responsive under changing workloads without requiring contributors to understand the underlying execution mechanics.

---

# Scheduling Objectives

Scheduling should be:

- fair
- predictable
- responsive
- observable
- workload-aware
- resource-efficient

The scheduler exists to maximise useful work while preventing individual tasks from degrading the performance of the entire platform.

---

# Scheduling Philosophy

Scheduling should optimise platform responsiveness rather than individual task completion.

The Runtime should ensure that:

- small tasks are not delayed by large tasks
- background work does not interfere with user requests
- unrelated workloads remain isolated
- execution resources remain balanced

The goal is not to finish one task as quickly as possible.

The goal is to keep the entire platform making forward progress.

---

# Runtime Ownership

Scheduling is owned exclusively by the Runtime.

Capabilities should never:

- manage worker allocation
- create scheduling policies
- prioritise themselves
- assume execution order
- manipulate execution queues

Business logic should describe what needs to happen.

The Runtime decides when and where it happens.

---

# Work Classification

The Runtime should classify work according to its characteristics.

Typical categories include:

- user-facing requests
- event processing
- background maintenance
- scheduled jobs
- storage operations
- module execution

Different workloads may require different scheduling behaviour.

Treating every task identically usually produces equally mediocre results.

---

# Prioritisation

Scheduling priority should reflect business value.

Higher priority should generally be given to:

- interactive requests
- user-visible operations
- latency-sensitive execution

Lower priority should generally be assigned to:

- maintenance tasks
- cache warming
- cleanup operations
- analytics
- background synchronisation

Priority should improve responsiveness without introducing starvation.

---

# Fairness

Every workload should receive an appropriate opportunity to execute.

The Runtime should prevent:

- long-running tasks monopolising workers
- individual capabilities consuming disproportionate resources
- modules degrading Platform behaviour

Fair scheduling produces more predictable performance than aggressive scheduling.

---

# Bounded Execution

Work should complete within reasonable limits.

Long-running execution should be:

- divided into smaller units
- delegated to background processing
- made observable
- monitored for excessive duration

The Runtime should avoid allowing individual tasks to occupy execution resources indefinitely.

---

# Cooperative Scheduling

Tasks should cooperate with the Runtime.

Long-running operations should naturally yield opportunities for other work to execute.

Execution models that require continuous exclusive ownership of workers should be avoided wherever practical.

Cooperation generally produces better platform responsiveness than competition.

---

# Queue Management

Scheduling queues should remain:

- bounded
- measurable
- observable
- workload-specific where appropriate

Growing queues indicate increasing pressure within the platform.

Queues should absorb temporary workload spikes rather than permanently accumulating work.

A queue is a buffer.

It is not long-term storage with optimistic branding.

---

# Starvation Prevention

The Runtime should prevent starvation of lower-priority work.

Even background operations must eventually execute.

Scheduling policies should balance:

- responsiveness
- fairness
- throughput
- resource utilisation

Starvation simply moves today's latency into tomorrow's outage.

---

# Load Distribution

Available execution resources should be utilised evenly.

The scheduler should minimise:

- idle workers
- overloaded workers
- uneven workload distribution
- unnecessary contention

Balanced execution generally produces more stable performance than attempting to maximise utilisation of individual workers.

---

# Scheduling Metrics

Scheduling behaviour should expose metrics including:

- scheduling latency
- queue depth
- worker utilisation
- active workers
- waiting time
- execution duration
- task completion rate
- rejected work
- deferred work

These metrics should integrate with the observability standards defined in [MEG-008](../meg-008-observability/index.md).

Scheduling behaviour should always be measurable.

---

# Optimisation Strategy

When improving scheduling efficiency, contributors should investigate in the following order:

1. Remove unnecessary scheduled work.
2. Reduce execution duration.
3. Improve workload classification.
4. Improve queue behaviour.
5. Improve workload distribution.
6. Reduce scheduling overhead.
7. Tune Runtime scheduling policies.

Scheduling should become simpler before it becomes faster.

---

# Anti-Patterns

The following scheduling behaviours are discouraged:

- blocking workers unnecessarily
- unbounded execution queues
- scheduler-aware business logic
- priority inversion
- long-running foreground tasks
- excessive background scheduling
- hidden execution delays
- starvation of low-priority work
- manual workload balancing

These behaviours reduce responsiveness while making Runtime behaviour increasingly difficult to predict.

---

# Expected Outcome

After reading this chapter contributors should understand:

- how scheduling influences platform responsiveness
- why execution ownership belongs to the Runtime
- how workloads should be prioritised
- why fairness matters
- how queue behaviour affects performance
- how scheduling metrics support optimisation

A well-designed scheduler is rarely noticed.

It quietly ensures that the right work happens at the right time, allowing contributors to focus on business behaviour instead of negotiating peace treaties between goroutines.
