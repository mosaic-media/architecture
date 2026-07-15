<!--
File: docs/design/system/mds-006-composition-engine/12-adrs.md
Document: MDS-006
Chapter: 12
Title: Architectural Decision Records
Status: Draft
Version: 0.4
-->

# Architectural Decision Records

---

# Purpose

The Architectural Decision Records (ADRs) contained within MDS-006 preserve the architectural reasoning behind the Mosaic Composition Engine.

Every previous specification established:

- Vision
- Behaviour
- Design Language
- Runtime Systems

MDS-006 establishes how those systems become one continuously evolving runtime experience.

These ADRs explain why Mosaic treats runtime composition as a behavioural solving process rather than a rendering process.

Future contributors should understand these decisions before modifying the Composition Engine.

---

# Decision Format

Decision format, lifecycle and review expectations are governed by **[MDG-001 — Documentation Authority Guide](../../../engineering/documentation/mdg-001-documentation-authority-guide/index.md)**.

This chapter records decisions specific to this specification and avoids redefining the shared ADR process.

# ADR-154

## Title

Treat The Runtime World As The Primary Runtime Model

### Status

Accepted

### Context

Traditional applications frequently build interfaces from application state.

Founder workshops consistently favoured modelling the user's current World rather than interface state.

### Decision

The Runtime World becomes the single behavioural source of truth.

### Consequences

Every runtime subsystem consumes identical behavioural information.

Presentation becomes deterministic.

---

# ADR-155

## Title

Composition Is Solved Rather Than Authored

### Status

Accepted

### Context

Static interface templates struggle to communicate changing behavioural priorities.

### Decision

The Composition Solver continuously constructs understanding from the Runtime World.

### Consequences

The interface evolves naturally as behaviour changes.

---

# ADR-156

## Title

Introduce Expressions As A Runtime Abstraction

### Status

Accepted

### Context

Directly generating components tightly couples runtime behaviour to rendering frameworks.

### Decision

Expressions become the stable contract between runtime understanding and presentation.

### Consequences

Future clients remain implementation independent while sharing one conceptual runtime.

---

# ADR-157

## Title

Runtime Hierarchy Is Behavioural

### Status

Accepted

### Context

Traditional interfaces frequently derive hierarchy from layout.

### Decision

Hierarchy is continuously solved from behaviour rather than geometry.

### Consequences

Adaptive layouts preserve understanding across every device.

---

# ADR-158

## Title

Behaviour Orchestrates Every Runtime System

### Status

Accepted

### Context

Independent runtime subsystems frequently produce fragmented user experiences.

### Decision

Every runtime subsystem evolves from one coordinated behavioural pipeline.

### Consequences

Users experience one coherent World rather than multiple independent interface updates.

---

# ADR-159

## Title

Presentation Is A Runtime Product

### Status

Accepted

### Context

Traditional frameworks often treat presentation as the runtime model.

### Decision

Presentation becomes the output of runtime solving.

### Consequences

Rendering technologies remain replaceable without affecting runtime behaviour.

---

# ADR-160

## Title

Adaptive Layout Never Changes Behaviour

### Status

Accepted

### Context

Responsive layouts frequently alter behavioural meaning across devices.

### Decision

Adaptive Layout projects solved understanding rather than redefining it.

### Consequences

Every device communicates identical behavioural intent.

---

# ADR-161

## Title

Runtime Pipelines Must Remain Deterministic

### Status

Accepted

### Context

Predictable runtime behaviour is essential for replay, testing and synchronisation.

### Decision

Every pipeline stage consumes immutable inputs and produces deterministic outputs.

### Consequences

Caching, replay and multi-device synchronisation become reliable architectural capabilities.

---

# ADR-162

## Title

Modules Enrich The Runtime World

### Status

Amended by ADR-163

### Context

Allowing modules to construct presentation fragments runtime consistency.

### Decision

Modules contribute behaviour, relationships, information and governed domain layout constraints.

They do not provide final Presentation geometry or private Platform values.

The Composition Engine owns runtime solving.

### Consequences

Community modules inherit every future runtime improvement automatically.

---

# ADR-163

## Title

Resolve Presentation Geometry In The Client From Capability And Constraints

### Status

Accepted

### Context

SDUI must support browsers and native clients with widely different extents, input contexts, accessibility settings and rendering budgets.

Device categories do not reliably describe those constraints, while server-authored coordinates would couple semantic intent to one Presentation.

### Decision

Composition and Runtime SDUI provide semantic hierarchy, relationships, Expressions and permitted domain layout modes.

The client-side Adaptive Layout implementation calculates final location, size, depth ordering, padding, spacing, density and typography from private Platform primitives and the current capability profile.

Modules may provide governed domain invariants, but cannot provide final Presentation geometry or select private primitives.

Intrinsic domain coordinates, such as those in an authored diagram or spatial canvas, remain content data and are projected into Presentation space by the client.

### Consequences

Web and native clients share one semantic contract while adapting to their actual runtime conditions.

Mosaic retains control of visual rhythm without exposing controls such as `Spacing.Large` to SDUI, Modules or users.

---

# ADR Relationships

```mermaid
flowchart TD

ADR154["Runtime World"]

ADR155["Composition Solver"]

ADR156["Expressions"]

ADR157["Runtime Hierarchy"]

ADR158["Behaviour Orchestration"]

ADR159["Presentation"]

ADR160["Adaptive Layout"]

ADR161["Deterministic Pipelines"]

ADR162["Modules"]

ADR163["Client Geometry Resolution"]

ADR154 --> ADR155
ADR155 --> ADR156
ADR156 --> ADR157
ADR157 --> ADR160
ADR155 --> ADR158
ADR158 --> ADR161
ADR156 --> ADR159
ADR161 --> ADR162
ADR160 --> ADR163
ADR162 --> ADR163
```

Together these decisions establish the Composition Engine as a behavioural runtime architecture rather than a rendering framework.

---

# Future ADRs

Future Composition Engine ADRs are expected to formalise:

- Predictive Composition
- AI-assisted Expression Selection
- Distributed Runtime Worlds
- Collaborative Runtime Sessions
- Spatial Composition
- Incremental Graph Solving
- Runtime Behaviour Personas
- Cloud-assisted Composition Pipelines

These intentionally remain outside the scope of MDS-006 Version 0.1.

---

# ADR Governance

Composition Engine ADRs should change only when:

- behavioural research identifies deficiencies,
- runtime architecture fundamentally evolves,
- deterministic guarantees require refinement,
- the Mosaic Design Language itself changes.

Implementation technology alone should never justify architectural changes.

The runtime model should remain recognisably Mosaic regardless of future execution environments.

---

# Summary

The ADRs contained within MDS-006 define the architectural heart of Mosaic.

Rather than constructing interfaces...

The Composition Engine constructs understanding.

Everything else:

- layouts,
- materials,
- typography,
- motion,
- rendering,

emerges naturally from that solved understanding.
