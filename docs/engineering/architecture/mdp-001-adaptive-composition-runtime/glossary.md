<!--
File: docs/engineering/architecture/mdp-001-adaptive-composition-runtime/glossary.md
Document: MDP-001
Status: Draft
-->

# Glossary

---

# Purpose

This glossary defines the terminology introduced by **MDP-001 — Adaptive Composition Runtime**.

Unlike previous glossaries, these definitions describe the runtime architecture responsible for constructing the user's World.

These terms intentionally remain independent from:

- UI frameworks,
- rendering engines,
- platforms,
- programming languages.

Future specifications should reuse these definitions consistently.

---

# A

## Airspace Reserve

A projected hard or soft settlement constraint extending through a governed range of Composition Planes above a lower-plane Expression.

Tiles may transit through the reserve but must resolve to a valid settled footprint outside hard exclusions and within the permitted soft occlusion budget.

---

## Acrylic Assembly

A Composition grouping of separate rigid Acrylic Tiles that may coordinate layout, movement and renderer compositing while retaining distinct Material boundaries.

One Tile, rather than one Assembly, defines a continuous Acrylic surface.

---

## Adaptive Layout

The client-side runtime process that projects one solved Composition into different presentation environments using current constraints and private Platform primitives.

Adaptive Layout changes:

- spatial organisation,
- density,
- presentation.

It never changes:

- behaviour,
- hierarchy,
- understanding.

---

## Authored Layout

A client layout mode for documentation, administration, dashboards and conventional application pages built with CSS or native layout using public Mosaic Semantic Tokens.

Authored Layout complements rather than replaces Adaptive Composition.

---

# B

## Behavioural Cost

A proposed normalised measure of transition significance derived from Focus change, Domain boundaries, Composition topology and continuity credit.

Behavioural Cost may govern the breadth and settlement character of future adaptive choreography without delaying initial response.

---

## Behaviour Orchestration

The coordinated execution of every runtime subsystem following behavioural change.

Behaviour Orchestration ensures:

- Composition,
- Materials,
- Typography,
- Motion,

all evolve together.

---

# C

## Capability Profile

The current set of Presentation constraints used by Adaptive Layout.

It may include available extent, orientation, viewing distance, input methods, accessibility, renderer features and measured runtime budget.

A Capability Profile is not a permanent device category.

Registered Device Capability Envelopes provide stable discovery input while Live Presentation Profiles resolve the effective current constraints.

---

## Composition

The solved understanding of the user's current World.

Composition exists independently from:

- layouts,
- components,
- rendering.

---

## Composition Plane

A governed persistent logical \(z\)-level with an independent two-dimensional occupancy solution.

Tiles on separate Composition Planes may overlap in projected \(x,y\) space.

A Tile's current Composition Plane is resolved state rather than identity.

---

## Composition Profile

A private client-side arrangement used to resolve semantic intent into deterministic presentation slots during reference, fallback or early implementation stages.

SDUI and Modules cannot address Composition Profile identifiers or slots.

---

## Composition Solver

The deterministic runtime system responsible for transforming the Runtime World into a solved Composition.

The Solver determines:

- hierarchy,
- priority,
- grouping,
- Expressions.

It never determines rendering.

---

## Critically Damped Motion

A proposed second-order spatial response with damping ratio \(\zeta=1\), intended to return rigid geometry to equilibrium without bounce or overshoot.

---

# D

## Domain Boundary Cost

The proposed Behavioural Cost contribution introduced when a transition crosses conceptual Domains and changes the relevant information model.

---

# E

## Expression

A runtime representation of one conceptual responsibility.

Examples include:

- Hero
- Timeline
- Progress
- Relationships
- Actions

Expressions are presentation independent.

---

## Expression Resolution

The deterministic process that transforms solved Composition into reusable runtime Expressions.

Expression Resolution bridges runtime understanding and presentation.

---

# H

## HD ClearLogo

A high-resolution transparent media-identity asset intended for placement within verified negative space in landscape or backdrop artwork.

An HD ClearLogo replaces the visible typographic title only while it remains legible and does not obscure the artwork focal subject.

---

## Hierarchy Profile

A conceptual runtime artefact representing the resolved behavioural hierarchy of the current Composition.

Hierarchy Profiles improve:

- determinism,
- caching,
- incremental updates.

---

# L

## Live Presentation Profile

The client-owned, session-local resolution of current viewport, safe area, accessibility, input and measured renderer-budget constraints used to project a Composition.

It may change while one registered device remains the same.

---

# N

## Normalised Composition Space

A resolution-independent logical coordinate system in which projected \(x\) and \(y\) share a width-derived scale while \(z\) represents bounded logical depth.

It remains distinct from Tile-local and artwork UV coordinate spaces.

---

# P

## Presentation Model

The platform-independent runtime description consumed by rendering engines.

The Presentation Model contains:

- Expressions,
- Materials,
- Typography,
- Motion,
- Interaction metadata.

Components are generated afterwards.

---

# R

## Registered Device Capability Envelope

A reusable description of relatively stable renderer, input, application and platform capabilities discovered during device registration or first sign-in.

It may seed Presentation resolution but never determines final Composition geometry by itself.

---

## Runtime World

The continuously evolving behavioural model representing the user's current reality.

The Runtime World is the single source of truth for:

- Focus,
- Context,
- Behaviour,
- Relationships.

Every runtime subsystem consumes it.

---

## Runtime Pipeline

A deterministic execution stage within the Composition Engine.

Pipelines transform:

Behaviour

↓

Understanding

↓

Presentation

Each pipeline owns one architectural responsibility.

---

## Runtime Snapshot

An immutable representation of the Runtime World used during one orchestration cycle.

Snapshots improve:

- replay,
- testing,
- caching,
- deterministic execution.

---

# S

## Saliency Mask

A normalised low-resolution importance field derived from focal subjects, faces, identity marks or editorial safe regions and used to resolve Airspace Reserve cost.

---

## Solver

See **Composition Solver**.

Within Mosaic, "Solver" always refers to runtime understanding rather than layout computation.

## Spatial Rhythm

The relationship created by internal, group, region and Hero separation across a resolved Composition.

Adaptive Layout derives Spatial Rhythm from semantic relationships and the private spatial scale rather than equal gaps or public spacing choices.

---

# W

## World

The user's current behavioural reality.

A World contains:

- Focus,
- Context,
- Relationships,
- Behaviour,
- Information.

The Composition Engine continuously solves this World into understandable presentation.

---

# Cross References

| Specification | Primary Concepts |
|---------------|------------------|
| [MDL-001 — Mosaic Design Language Vision](../../../design/language/mdl-001-vision/index.md) | Companion |
| [MDL-002 — Principles](../../../design/language/mdl-002-principles/index.md) | Behaviour First |
| [MDL-003 — Mental Model](../../../design/language/mdl-003-mental-model/index.md) | World, Focus |
| [MDL-004 — Interaction Model](../../../design/language/mdl-004-interaction-model/index.md) | Behaviour |
| [MDL-005 — Composition Model](../../../design/language/mdl-005-composition-model/index.md) | Hero, Hierarchy |
| [MDS-001 — Design Token Architecture](../../../design/system/mds-001-design-token-architecture/index.md) | Runtime Resolution |
| [MDS-002 — Colour System](../../../design/system/mds-002-colour-system/index.md) | Runtime Atmosphere |
| [MDS-003 — Material System](../../../design/system/mds-003-material-system/index.md) | Material Resolution |
| [MDS-004 — Typography System](../../../design/system/mds-004-typography-system/index.md) | Editorial Hierarchy |
| [MDS-005 — Motion System](../../../design/system/mds-005-motion-system/index.md) | Behavioural Motion |

---

# Terminology Rules

Future contributors should:

- describe Worlds before screens,
- describe behaviour before rendering,
- describe Expressions before components,
- distinguish Composition from presentation,
- avoid platform-specific terminology inside architectural specifications.

Runtime terminology should remain independent from implementation technology.
