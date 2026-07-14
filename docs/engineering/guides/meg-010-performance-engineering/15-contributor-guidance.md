<!--
File: docs/engineering/guides/meg-010-performance-engineering/15-contributor-guidance.md
Document: MEG-010
Status: Draft
Version: 0.1
-->

# Contributor Guidance

---

# Purpose

This chapter provides practical guidance for contributors working within the performance architecture defined by MEG-010.

Performance is not the responsibility of a dedicated optimisation phase or a specialist engineering team.

Every contributor influences the performance characteristics of the platform through the decisions they make during design, implementation and review.

This chapter explains how contributors should approach those decisions.

---

# Engineering Mindset

Performance begins with good engineering rather than clever engineering.

Contributors should strive to build systems that are:

- simple
- understandable
- measurable
- maintainable
- efficient

Complexity should only be introduced when it demonstrably improves the platform.

Complexity introduced "just in case" usually becomes technical debt disguised as ambition.

---

# Think in Systems

Contributors should evaluate the impact of changes across the entire platform rather than within individual components.

Questions worth asking include:

- Does this reduce total work?
- Does this increase event volume?
- Does this introduce additional storage access?
- Does this increase allocation?
- Does this affect Runtime scheduling?
- Does this change observability?

Local optimisation should never come at the expense of global behaviour.

---

# Respect Architectural Boundaries

Performance improvements should preserve the architectural boundaries established throughout previous MEGs.

Avoid allowing performance concerns to leak:

- into the Domain
- into business logic
- into capability contracts
- into extension APIs

Architecture should remain clean even when optimisation becomes necessary.

A fast architecture that nobody can evolve eventually becomes a slow organisation.

---

# Measure First

Before attempting optimisation, contributors should:

- establish a baseline
- collect relevant metrics
- profile representative workloads
- understand the bottleneck

Engineering effort should focus on measured problems rather than perceived ones.

Assumptions are valuable starting points.

Measurements determine whether they survive contact with reality.

---

# Keep Optimisations Small

Optimisations should be:

- targeted
- isolated
- measurable
- reviewable

Large-scale optimisation changes are difficult to validate and often introduce unintended regressions.

Small improvements are easier to understand and easier to reverse if necessary.

---

# Prefer Simplicity

When two implementations provide comparable performance, contributors should prefer the simpler design.

Simple systems are:

- easier to review
- easier to profile
- easier to optimise
- easier to maintain

Future contributors should be able to understand *why* an optimisation exists.

If an optimisation requires a presentation to explain, it is probably worth questioning.

---

# Review Performance Continuously

Performance should be considered during normal engineering review.

Reviewers should ask questions such as:

- Is this work necessary?
- Can storage access be reduced?
- Are allocations reasonable?
- Is concurrency justified?
- Is this observable?
- Is this measurable?
- Does this preserve architectural boundaries?

Performance review should become routine rather than exceptional.

---

# Document Significant Decisions

Performance decisions with architectural impact should be documented.

Examples include:

- introducing new caches
- changing scheduling behaviour
- modifying execution models
- changing storage strategies
- altering concurrency limits

Future contributors should understand not only *what* changed, but *why* it changed.

---

# Avoid Cargo Cult Optimisation

Contributors should avoid introducing techniques simply because they are considered best practice elsewhere.

Every optimisation should have:

- a measurable problem
- a documented rationale
- an observable improvement

Practices that improve one system may reduce the performance of another.

Architecture is contextual.

Performance engineering is no different.

---

# Learn From Production

Production telemetry should inform future engineering decisions.

Performance investigations should make use of:

- Runtime metrics
- profiling data
- benchmark history
- operational dashboards
- incident reports

Real workloads provide better guidance than synthetic assumptions.

Production has a remarkable ability to expose weaknesses that laboratory conditions politely ignore.

---

# Continuous Improvement

Performance engineering is an ongoing process.

Contributors should continually:

- simplify implementations
- remove unnecessary work
- investigate regressions
- validate assumptions
- refine benchmarks
- improve observability

Small improvements applied consistently produce more durable results than occasional heroic optimisation efforts.

---

# Performance Checklist

Before completing significant work, contributors should consider the following checklist.

- Has unnecessary work been removed?
- Is storage access proportional?
- Is allocation reasonable?
- Is concurrency justified?
- Is data movement minimised?
- Are caches appropriate?
- Is the change observable?
- Is the behaviour measurable?
- Have benchmarks or profiles been reviewed where appropriate?
- Does the implementation remain architecturally consistent?

Not every item will apply to every change.

Each should, however, be considered deliberately.

---

# Next File

`glossary.md`
