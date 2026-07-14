<!--
File: docs/engineering/guides/meg-005-runtime-architecture/05-dependency-graph.md
Document: MEG-005
Status: Draft
Version: 0.1
-->

# Dependency Graph

> *The Runtime should understand every dependency before execution begins. Execution order should emerge from the graph, not from hard-coded startup sequences.*

---

# Purpose

The Mosaic Runtime is composed of many Runtime Services and Capabilities.

Examples include:

- Capability Registry
- Execution Engine
- Scheduler
- Worker Manager
- Metadata
- Playback
- Library
- Recommendations

These components frequently depend upon one another.

Without an explicit dependency model:

- startup becomes fragile
- shutdown becomes unpredictable
- cycles emerge
- architectural drift becomes inevitable

This document defines the Dependency Graph that governs the construction, startup and shutdown of the Runtime.

---

# Philosophy

Within Mosaic:

> **Dependencies should be declared. The Runtime should determine execution order.**

No component should manually decide:

> "Start this service first."

Instead, every component declares its dependencies.

The Runtime constructs a dependency graph.

Execution order naturally follows.

---

# What Is The Dependency Graph?

The Dependency Graph is a directed graph describing relationships between Runtime components.

Conceptually.

```
Capability Registry

↓

Execution Engine

↓

Scheduler

↓

Worker Manager
```

Every node represents a Runtime component.

Every edge represents a dependency.

The Runtime uses this graph to determine:

- startup order
- shutdown order
- readiness
- dependency validation

---

# Runtime Source Of Truth

The Dependency Graph is the authoritative description of Runtime relationships.

It answers questions such as:

- What depends on this service?
- What must start first?
- What can start in parallel?
- What must stop last?

No Runtime Service should independently answer these questions.

---

# Declared Dependencies

Every Runtime component SHOULD explicitly declare its dependencies.

Example.

```
Scheduler

↓

Execution Engine
```

Rather than:

```
Scheduler

↓

Calls Execution Engine

↓

Dependency Hidden
```

Dependencies should be visible before execution begins.

---

# Directed Graph

Dependencies are directional.

```
Scheduler

↓

Execution Engine
```

means:

The Scheduler depends upon the Execution Engine.

Not the reverse.

Direction should always communicate dependency.

Never execution.

---

# Directed Acyclic Graph

The Runtime Dependency Graph MUST remain acyclic.

```
Capability Registry

↓

Execution Engine

↓

Scheduler

↓

Worker Manager
```

is valid.

```
Scheduler

↓

Worker Manager

↓

Scheduler
```

is prohibited.

Cycles prevent deterministic startup.

A dependency graph without cycles forms a Directed Acyclic Graph (DAG), allowing a valid execution order to be derived using topological sorting.  [oai_citation:0‡Wikipedia](https://en.wikipedia.org/wiki/Dependency_graph?utm_source=chatgpt.com)

---

# Topological Startup

Startup order should be derived automatically.

Conceptually.

```
Dependency Graph

↓

Topological Sort

↓

Startup Order
```

The Runtime should never rely upon manually maintained startup sequences.

The graph should determine ordering.

---

# Parallel Startup

Independent components SHOULD start in parallel.

Example.

```
Capability Registry

↓

Execution Engine
```

and

```
Observability
```

may initialise simultaneously if no dependency exists.

The Runtime should maximise parallelism without violating dependency order.

This naturally improves startup performance.

---

# Shutdown Order

Shutdown follows the reverse dependency order.

Example.

Startup.

```
Capability Registry

↓

Execution Engine

↓

Scheduler
```

Shutdown.

```
Scheduler

↓

Execution Engine

↓

Capability Registry
```

Components should never outlive their dependencies.

---

# Capability Dependencies

Capabilities participate in the same graph.

Example.

```
Recommendations

↓

Playback

↓

Metadata
```

The Runtime should validate capability dependencies before activation.

Missing dependencies should prevent startup.

Rather than failing later during execution.

---

# Runtime Services

Runtime Services also participate.

Example.

```
Worker Manager

↓

Execution Engine
```

```
Execution Engine

↓

Capability Registry
```

The graph contains both:

- Runtime Services
- Capabilities

The Runtime should reason about both uniformly.

---

# Dependency Validation

Before startup, the Runtime SHOULD validate:

- missing dependencies
- duplicate registrations
- circular dependencies
- incompatible versions

Invalid dependency graphs should fail during startup.

Not during execution.

Early validation dramatically reduces operational complexity.

---

# Optional Dependencies

Some dependencies may be optional.

Example.

```
Recommendations

↓

Machine Learning Extension

(Optional)
```

If unavailable:

Recommendations continue.

Capabilities should explicitly distinguish between:

- required dependencies
- optional dependencies

The Runtime should never guess.

---

# Dynamic Dependencies

Dependencies SHOULD remain stable during execution.

Runtime mutation of the dependency graph should be rare.

Examples where it may occur include:

- extension installation
- extension removal
- runtime upgrades

Even then:

The Runtime should validate the resulting graph before activating new components.

---

# Dependency Metadata

Edges within the graph MAY contain metadata.

Examples include:

- required
- optional
- version constraints
- lifecycle relationship

This allows the Runtime to reason about compatibility as well as ordering.

---

# Observability

The Dependency Graph SHOULD be observable.

Operators should be able to answer:

- Which services depend upon this capability?
- What prevents startup?
- Which components are blocked?
- What will stop if this service fails?

The graph should become an operational tool.

Not merely an implementation detail.

---

# Runtime Diagnostics

The Runtime should expose the Dependency Graph through diagnostics.

Example.

```
Runtime

↓

Dependency Graph

↓

Visualisation
```

This greatly simplifies:

- debugging
- onboarding
- architecture reviews
- operational support

Understanding the Runtime should not require reading source code.

---

# Dependency Ownership

Every component owns only its outgoing dependencies.

Example.

```
Scheduler

↓

Execution Engine
```

The Scheduler declares the dependency.

The Execution Engine does not maintain a list of dependants.

The Runtime derives reverse relationships automatically.

This keeps ownership simple.

---

# Dependency Resolution

The Runtime Kernel resolves dependencies before startup.

Conceptually.

```
Register Components

↓

Build Graph

↓

Validate Graph

↓

Topological Order

↓

Start Runtime
```

Resolution occurs once.

Execution simply follows the resulting graph.

---

# Anti-Patterns

The following practices are prohibited.

## Manual Startup Order

```go
startRegistry()

startExecution()

startScheduler()
```

Hard-coded ordering should be replaced by graph resolution.

---

## Hidden Dependencies

Components discovering dependencies during execution.

---

## Circular Dependencies

Any cycle between Runtime components or Capabilities.

---

## Runtime Service Locator

Resolving arbitrary dependencies dynamically instead of declaring them.

---

## Startup Guesswork

Starting components without validating dependency availability.

---

## Duplicate Dependency Graphs

Multiple Runtime components maintaining separate dependency models.

The Runtime should own exactly one dependency graph.

---

# Mosaic Guidelines

Within Mosaic:

- Every Runtime component MUST declare its dependencies.
- The Runtime MUST construct one dependency graph.
- The Dependency Graph MUST remain acyclic.
- Startup order MUST be derived from the graph.
- Shutdown order MUST be the reverse of startup.
- Independent components SHOULD start in parallel.
- Dependency validation MUST occur before execution.
- The Dependency Graph SHOULD remain observable.
- Components MUST NOT discover hidden dependencies at runtime.

---

# Relationship to MEG

The Capability Registry answers:

> **What exists?**

The Dependency Graph answers:

> **How do those things depend upon one another?**

The next chapter introduces the **Execution Engine**, the Runtime subsystem responsible for turning this validated dependency graph into running capability execution.

---

# Summary

The Dependency Graph transforms Runtime startup from a collection of hard-coded initialisation steps into a deterministic architectural process.

By making dependencies:

- explicit
- observable
- validated
- acyclic

the Runtime becomes easier to:

- understand
- evolve
- debug
- extend

Most importantly, startup order becomes a property of the architecture itself rather than an implementation detail hidden inside bootstrap code.

---

# Review Status

**Status**

Draft

**Owner**

Lead Software Architect

**Previous File**

`04-service-lifecycle.md`

**Next File**

`06-execution-engine.md`
