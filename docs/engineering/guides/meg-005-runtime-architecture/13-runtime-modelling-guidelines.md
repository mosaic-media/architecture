<!--
File: docs/engineering/guides/meg-005-runtime-architecture/13-runtime-modelling-guidelines.md
Document: MEG-005
Status: Draft
Version: 0.4
-->

# Runtime Modelling Guidelines

> *A Runtime should grow by adding capabilities, not by increasing complexity.*

---

# Purpose

The previous chapters introduced the structural building blocks of the Mosaic Runtime:

- Runtime Kernel
- Capability Registry
- Dependency Graph
- Execution Engine
- Worker Manager
- Scheduler
- Resource Manager

This document brings those concepts together into practical modelling guidance.

Its purpose is to help engineers answer one question.

> **"Where does this Runtime component belong?"**

---

# Philosophy

Within Mosaic:

> **The Runtime should provide execution, not accumulate business behaviour.**

Every Runtime component should exist because it enables capabilities.

Not because it implements them.

As the platform grows, the Runtime should become more capable.

It should not become more complicated.

---

# Start With Responsibility

Before introducing a new Runtime component ask:

> **What single Runtime responsibility does this component own?**

Examples include:

- scheduling
- worker allocation
- capability discovery
- dependency validation

Avoid introducing components that own multiple unrelated responsibilities.

Small Runtime Services compose more effectively than large ones.

---

# Distinguish Runtime From Business

A useful question is:

> **Would this concept still exist if every business capability disappeared?**

If the answer is:

```
Yes
```

it probably belongs in the Runtime.

Examples.

- Worker Pool
- Scheduler
- Resource Manager

If the answer is:

```
No
```

it probably belongs to a capability.

Examples.

- Playback
- Library
- Metadata
- Recommendations

This distinction should remain one of the strongest modelling heuristics within Mosaic.

---

# Prefer Runtime Services

Whenever new operational behaviour appears ask:

> **Can this become an independent Runtime Service?**

Preferred.

```
Runtime Kernel

↓

Scheduler

↓

Execution Engine

↓

Resource Manager
```

Avoid.

```
Runtime Kernel

↓

Everything
```

The Kernel should coordinate.

Runtime Services should perform work.

---

# Protect The Kernel

The Runtime Kernel should remain intentionally small.

Before adding functionality ask:

> **Does the Kernel really need to know this?**

If another Runtime Service could own the responsibility:

Move it there.

The Kernel should evolve slowly.

Runtime Services should evolve freely.

---

# Model Capabilities

The Runtime executes capabilities.

It should never execute arbitrary business objects.

Preferred.

```
Capability

↓

Operation

↓

Execution Engine
```

Avoid.

```
Random Function

↓

Runtime
```

Everything executable within Mosaic should ultimately belong to a registered capability.

This reinforces the platform's capability-oriented architecture.

---

# Runtime Contracts

Every Runtime interaction should occur through explicit contracts.

Examples include:

- Lifecycle
- Scheduling
- Execution
- Resource Allocation
- Capability Registration

Avoid hidden communication between Runtime Services.

Contracts should make Runtime relationships obvious.

---

# Avoid Runtime Shortcuts

Suppose:

```
Scheduler

↓

Needs Worker
```

Poor.

```
Scheduler

↓

Worker Pool
```

Preferred.

```
Scheduler

↓

Execution Engine

↓

Worker Manager
```

The Runtime architecture should remain layered.

Bypassing Runtime Services usually creates long-term coupling.

---

# Dependency Direction

Every Runtime dependency should point towards the Runtime Kernel.

Conceptually.

```
Worker Manager

↓

Kernel
```

```
Scheduler

↓

Kernel
```

```
Execution Engine

↓

Kernel
```

Runtime Services should not form complex dependency meshes.

The Dependency Graph should remain understandable.

---

# Runtime State

Before introducing new Runtime state ask:

> **Who owns this information?**

Examples.

Worker utilisation.

↓

Worker Manager.

Capability metadata.

↓

Capability Registry.

Execution progress.

↓

Execution Engine.

Ownership should always remain singular.

---

# Build For Replacement

Every Runtime Service should be replaceable.

Ask:

> **Could another implementation satisfy the same contract?**

Examples.

```
Scheduler V1

↓

Scheduler V2
```

```
Worker Pool A

↓

Worker Pool B
```

If replacing the component requires changing the Runtime Kernel:

The abstraction probably needs refinement.

---

# Runtime Growth

The preferred Runtime growth pattern is:

```
Existing Runtime

↓

New Runtime Service

↓

Register

↓

Dependency Graph

↓

Ready
```

Avoid modifying existing Runtime Services unnecessarily.

Growth should occur primarily through composition.

Not modification.

---

# Runtime Services Should Not Discover Each Other

Poor.

```
Scheduler

↓

Find Worker Manager

↓

Execute
```

Preferred.

```
Scheduler

↓

Kernel Contract

↓

Execution Engine
```

The Runtime should remain explicitly composed.

Hidden service discovery weakens architectural clarity.

---

# Prefer Determinism

Runtime behaviour should remain deterministic.

Given identical:

- configuration
- capabilities
- dependency graph

the Runtime should produce identical startup, execution and shutdown behaviour.

Determinism dramatically simplifies:

- debugging
- testing
- operations

---

# Runtime Models

Every Runtime component should answer:

- What do I own?
- What do I expose?
- What do I require?
- Who depends upon me?

If these questions cannot be answered clearly:

The Runtime model probably requires refinement.

---

# Runtime Diagrams

Before implementing a Runtime Service:

Draw it.

Example.

```
Capability Registry

↓

Dependency Graph

↓

Execution Engine

↓

Worker Manager
```

Simple diagrams frequently reveal:

- circular dependencies
- ownership confusion
- unnecessary coupling

Architecture should become obvious before code exists.

Good architecture documentation should clearly communicate component responsibilities and interactions while remaining easy to evolve alongside the system.  [Qt](https://www.qt.io/software-insights/best-practices-for-architecture-documentation)

---

# Runtime Review Checklist

Before implementing a Runtime Service ask:

- [ ] Does it own one Runtime responsibility?
- [ ] Does it remain business agnostic?
- [ ] Could it become its own Runtime Service?
- [ ] Does it expose explicit contracts?
- [ ] Does it preserve dependency direction?
- [ ] Is ownership obvious?
- [ ] Is Runtime state clearly owned?
- [ ] Can it be replaced independently?
- [ ] Does it strengthen the Runtime rather than complicate it?

If any answer is "no":

Continue modelling.

Implementation should wait.

---

# Common Runtime Modelling Mistakes

Avoid:

- adding business behaviour to the Runtime
- creating "manager" services that own unrelated responsibilities
- introducing hidden dependencies
- bypassing Runtime Services
- centralising every operational concern inside the Kernel
- sharing Runtime state between components

These patterns inevitably produce Runtime monoliths.

---

# Mosaic Guidelines

Within Mosaic:

- Every Runtime component MUST own one responsibility.
- Runtime growth SHOULD occur through composition.
- The Runtime Kernel MUST remain small.
- Runtime Services SHOULD communicate through contracts.
- Runtime state MUST have explicit ownership.
- Capabilities MUST remain separate from Runtime infrastructure.
- Runtime behaviour SHOULD remain deterministic.
- Architectural clarity SHOULD always outweigh implementation convenience.

---

# Relationship to MEG

This chapter completes the practical Runtime Architecture guidance of MEG-005.

The remaining documents describe:

- supervisor authority
- architectural reasoning (ADRs)
- contributor expectations
- terminology
- references

The next specification, **MEG-006 – Module Platform**, will build directly upon this Runtime Architecture by defining how third-party capabilities integrate into the Runtime without modifying it.

---

# Summary

A well-designed Runtime should disappear into the background.

Engineers should spend their time building capabilities.

Not extending the Runtime itself.

Within Mosaic, every Runtime component should make one thing easier:

> **Building independently evolving capabilities.**

When that remains the guiding principle, the Runtime grows into a platform rather than a framework.

---

# Review Status

**Status**

Draft

**Owner**

Lead Software Architect

**Previous File**

`12-runtime-state.md`

**Next File**

`14-supervisor-model.md`
