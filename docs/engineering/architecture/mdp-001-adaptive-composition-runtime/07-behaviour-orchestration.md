<!--
File: docs/engineering/architecture/mdp-001-adaptive-composition-runtime/07-behaviour-orchestration.md
Document: MDP-001
Status: Draft
-->

# Behaviour Orchestration

> **Proposal status:** Deferred and non-authoritative. This chapter preserves post-v1 research; it is not a Mosaic v1 requirement.

---

# Purpose

The Runtime World evolves continuously.

Every behavioural change affects multiple systems simultaneously.

Examples include:

- Composition
- Motion
- Materials
- Typography
- Atmosphere

If each subsystem reacted independently, the platform would feel fragmented.

Behaviour Orchestration ensures every subsystem evolves as one coherent behavioural experience.

The user should never perceive separate systems updating.

They should perceive one World continuing naturally.

---

# Definition

Within MDS, **Behaviour Orchestration** is defined as:

> **The coordinated execution of every runtime subsystem in response to behavioural change while preserving continuity, determinism and understanding.**

Orchestration is responsible for sequencing.

Not solving.

The Composition Solver determines *what* should happen.

Behaviour Orchestration determines *how every subsystem evolves together*.

---

# Why Orchestration Exists

Traditional interfaces frequently behave like this.

```mermaid
flowchart TD

N1["State Changes"]
N2["Layout Updates"]
N3["Animation"]
N4["Theme Updates"]
N5["Done"]

N1 --> N2
N2 --> N3
N3 --> N4
N4 --> N5
```

Each subsystem behaves independently.

Mosaic intentionally behaves differently.

```mermaid
flowchart TD

N1["Behaviour"]
N2["Composition"]
N3["Expressions"]
N4["Materials"]
N5["Motion"]
N6["Presentation"]
N7["Understanding"]

N1 --> N2
N2 --> N3
N3 --> N4
N4 --> N5
N5 --> N6
N6 --> N7
```

The runtime behaves as one coordinated organism.

---

# Behaviour Is The Trigger

Every orchestration cycle begins with behaviour.

Examples include:

```text
Playback Started

Playback Paused

Focus Changed

Episode Completed

Search Opened

Chapter Changed
```

Rendering events should never initiate orchestration.

Behaviour always possesses the highest authority.

---

# Orchestration Pipeline

Every behavioural event should follow the same conceptual pipeline.

```mermaid
flowchart TD

N1["Behaviour"]
N2["Runtime World"]
N3["Composition Solver"]
N4["Expression Resolution"]
N5["Hierarchy Update"]
N6["Presentation Model"]
N7["Motion"]
N8["Rendering"]

N1 --> N2
N2 --> N3
N3 --> N4
N4 --> N5
N5 --> N6
N6 --> N7
N7 --> N8
```

Each stage contributes one responsibility.

No stage should bypass another.

---

# World Snapshot

Every orchestration cycle begins from one immutable Runtime World snapshot.

```mermaid
flowchart TD

N1["Runtime World"]
N2["Snapshot"]
N3["Entire Pipeline"]

N1 --> N2
N2 --> N3
```

This guarantees that every subsystem responds to identical behavioural information.

No subsystem should observe partially updated state.

---

# Sequential Consistency

Subsystems should evolve in a predictable order.

Preferred order.

```mermaid
flowchart TD

N1["Behaviour"]
N2["Composition"]
N3["Expressions"]
N4["Materials"]
N5["Typography"]
N6["Motion"]
N7["Presentation"]

N1 --> N2
N2 --> N3
N3 --> N4
N4 --> N5
N5 --> N6
N6 --> N7
```

This ordering mirrors the architectural dependency chain established throughout MDL and MDS.

---

# Atomic Behaviour

One behavioural event should produce one coherent runtime update.

Poor.

```mermaid
flowchart TD

N1["Playback"]
N2["Composition"]
N3["Later..."]
N4["Materials"]
N5["Later..."]
N6["Motion"]

N1 --> N2
N2 --> N3
N3 --> N4
N4 --> N5
N5 --> N6
```

Preferred.

```mermaid
flowchart TD

N1["Playback"]
N2["Entire Runtime Evolves Together"]

N1 --> N2
```

Users should never perceive intermediate states.

---

# Incremental Evolution

Behaviour Orchestration should minimise unnecessary work.

Example.

Progress updates.

↓

Timeline Expression updates.

↓

Timeline Material updates.

↓

Timeline Motion updates.

The Hero remains unchanged.

Local behavioural changes should remain local.

---

# Dependency Graph

Future implementations may internally construct a dependency graph.

Conceptually.

```mermaid
flowchart TD

N1["Behaviour"]
N2["Dependency Graph"]
N3["Affected Systems"]
N4["Presentation"]

N1 --> N2
N2 --> N3
N3 --> N4
```

The graph remains an implementation detail.

Behavioural ordering remains architecturally defined by this specification.

---

# Behaviour Categories

Different behaviours naturally produce different orchestration paths.

Examples.

## Focus Change

Updates:

- Composition
- Hero
- Expressions
- Materials
- Atmosphere
- Motion

---

## Playback Progress

Updates:

- Timeline
- Progress
- Motion

Only.

---

## Search

Updates:

- Overlay
- Navigation
- Interaction

The Runtime World itself remains largely unchanged.

Behaviour determines orchestration scope.

---

# Material Coordination

Material systems should never update independently.

Preferred.

```mermaid
flowchart TD

N1["Composition"]
N2["Hero Material"]
N3["Atmosphere"]
N4["Refraction"]
N5["Presentation"]

N1 --> N2
N2 --> N3
N3 --> N4
N4 --> N5
```

Every Material subsystem should receive identical behavioural inputs.

---

# Typography Coordination

Typography should participate after Composition has stabilised.

Reasons.

Editorial hierarchy depends upon:

- Hero
- Expressions
- Runtime Hierarchy

Typography should therefore respond.

Never lead.

---

# Motion Coordination

Motion begins only after the behavioural model has been solved.

Motion communicates change.

It never determines change.

The Motion System therefore consumes the resolved Presentation Model.

---

# Rendering Boundary

Rendering begins only after orchestration completes.

Conceptually.

```mermaid
flowchart TD

N1["Behaviour"]
N2["Runtime Systems"]
N3["Presentation Model"]
N4["Renderer"]

N1 --> N2
N2 --> N3
N3 --> N4
```

Rendering frameworks should remain passive consumers.

They should never influence orchestration.

---

# Failure Behaviour

If one subsystem cannot update.

Preferred.

```mermaid
flowchart TD

N1["Behaviour"]
N2["Graceful Degradation"]
N3["Presentation Continues"]

N1 --> N2
N2 --> N3
```

Avoid.

```mermaid
flowchart TD

N1["Behaviour"]
N2["Entire Runtime Stops"]

N1 --> N2
```

The Composition Engine should remain resilient.

Individual subsystem failures should not prevent behavioural continuity wherever practical.

---

# Deterministic Orchestration

Given identical:

- Runtime World
- Behaviour
- Context

the orchestration pipeline should always produce identical outputs.

Deterministic behaviour enables:

- replay
- debugging
- testing
- caching
- synchronisation

Every client should therefore experience equivalent runtime behaviour.

---

# Multi-Device Behaviour

Different devices may render differently.

They should orchestrate identically.

Desktop.

↓

Same Behaviour Pipeline.

Phone.

↓

Same Behaviour Pipeline.

Television.

↓

Same Behaviour Pipeline.

Presentation differs.

Behaviour does not.

---

# Modules

Modules contribute:

- behaviours
- information
- relationships

Modules never orchestrate runtime systems.

The Composition Engine determines:

- sequencing
- hierarchy
- subsystem execution

Every module therefore inherits one coherent runtime architecture.

---

# Good Examples

## Playback

Playback begins.

↓

Composition updates.

↓

Timeline resolves.

↓

Hero remains stable.

↓

Motion communicates change.

↓

Presentation updates.

Everything feels continuous.

---

## Reading

Chapter changes.

↓

Progress updates.

↓

Bookmarks evolve.

↓

Typography remains stable.

↓

Reader continues naturally.

---

## Music

Track changes.

↓

Hero updates.

↓

Playback queue adapts.

↓

Atmosphere redistributes.

↓

Environment settles.

The World quietly evolves.

---

# Anti-patterns

## Independent Systems

Every subsystem updates independently.

---

## Renderer Ownership

Rendering engine driving behavioural updates.

---

## Partial State

Subsystems observing different Runtime Worlds.

---

## Behaviour Duplication

Multiple systems attempting to solve the same behavioural problem.

---

# Behaviour Orchestration Model

```mermaid
flowchart TD

Behaviour
Behaviour --> RuntimeWorld
RuntimeWorld --> CompositionSolver
CompositionSolver --> ExpressionResolution
ExpressionResolution --> RuntimeHierarchy
RuntimeHierarchy --> PresentationModel
PresentationModel --> Motion
Motion --> Renderer
Renderer --> Understanding
```

One behavioural event.

One coordinated runtime evolution.

---

# Relationship To Future Chapters

The next chapter defines **Runtime Pipelines**.

Behaviour Orchestration explains:

> **How runtime systems evolve together.**

Runtime Pipelines explain:

> **How those coordinated stages are executed efficiently inside the Composition Engine.**

Together they establish the execution architecture of the Mosaic runtime.

---

# Summary

Behaviour Orchestration is the conductor of the Mosaic runtime.

Every subsystem:

- Composition,
- Materials,
- Typography,
- Motion,
- Presentation,

should evolve together from one shared behavioural understanding.

Users should never perceive multiple systems updating.

They should simply feel that their World naturally continued.
