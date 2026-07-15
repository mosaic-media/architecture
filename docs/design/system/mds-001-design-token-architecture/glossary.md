<!--
File: docs/design/system/mds-001-design-token-architecture/glossary.md
Document: MDS-001
Status: Draft
Version: 0.1
-->

# Glossary

---

# A

## Authored Layout

A conventional CSS or native layout constructed by a Design System consumer using public Semantic Tokens rather than Adaptive Composition geometry.

Authored Layout remains governed by Mosaic typography, spacing, sizing, Material, accessibility and rendering contracts.

---

## Appearance Preference

The user or operating-system choice of Light, Dark or system-controlled appearance.

Appearance Preference does not permit arbitrary shell recolouring.

---

# C

## Capability Input

Observable client support or measured renderer behaviour used to constrain token resolution.

Capability Input describes what can be performed correctly and does not classify the device.

## Composition Input

A role, relationship, priority or constraint supplied by the Composition Engine to token resolution.

Composition Input is runtime context rather than a Design Token.

---

# D

## Domain Intent

A namespaced Module-owned identifier describing a domain fact that maps to existing Platform semantic meaning.

Domain Intent is not a Primitive or Semantic Token.

## Dynamic Budget

The client-owned estimate of CPU, GPU, memory, transfer and compositor work safely available for optional Presentation refinement now.

---

# F

## Fidelity Maximum

The highest Refraction fidelity the user permits: Automatic, Balanced or Essential.

Capability, budget and accessibility may resolve to a lower level.

---

# L

## Local Override

A preference stored for one client that takes precedence over the corresponding synced account preference on that client only.

---

# P

## Presentation Artefact

A generated renderer-specific value such as a CSS custom property, Flutter value, SwiftUI environment value or shader uniform.

Presentation Artefacts do not own semantic meaning.

## Primitive Token

A Platform-owned foundational value without usage meaning.

Primitive Tokens may define colours, dimensions, type metrics, motion curves or Material coefficients and are not consumed directly by Modules or ordinary components.

## Private Spatial Scale

The Platform-owned sequence of internal spacing values used by client Adaptive Layout.

The scale is not a public semantic API and cannot be selected by SDUI, Modules, users or ordinary components.

---

# R

## Recipe

A governed combination of existing Semantic Tokens and constrained inputs used to coordinate an expression.

A Recipe is not another token layer and cannot introduce new Primitive or Semantic Tokens.

## Resolved Token

An immutable client-generated value expressing one Semantic Token for one complete resolution context.

## Resolved Token Set

The complete atomic collection of Resolved Tokens published for one resolution cycle.

## Resolution Context

The captured set of governed inputs evaluated by Token Resolution, including Composition, mapped Module intent, Focus, theme, artwork, accessibility, capability and budget.

## Runtime Resolver

The client-owned subsystem that transforms Platform Semantic Tokens and Resolution Context into a Resolved Token Set.

---

# S

## Semantic Token

A Platform-owned token representing stable design meaning independently from implementation technology and current runtime state.

Semantic Tokens form the public Design System API.

Public layout examples include spatial relationships, typography roles and dimensional responsibilities.

---

# T

## Theme

A governed variation in permitted Primitive or Semantic mappings that preserves Semantic Token meaning.

## Token

A machine-readable Platform design decision with a stable identifier, type, value or reference, ownership and lifecycle metadata.

Within Mosaic, authored Design Tokens are Primitive Tokens or Semantic Tokens.

## Token Alias

A type-compatible reference from one Platform token to another authoritative Platform token.

## Token Drift

The gradual loss of semantic consistency through duplication, local overrides, device forks or implementation leakage.

## Token Resolution

The deterministic client-owned process that evaluates Semantic Tokens against a governed Resolution Context and publishes an immutable Resolved Token Set.

---

# Cross References

| Specification | Related concepts |
|---------------|------------------|
| [MDL-005 — Composition Model](../../language/mdl-005-composition-model/index.md) | Composition and hierarchy |
| [MDS-002 — Colour System](../mds-002-colour-system/index.md) | Colour semantics and runtime atmosphere |
| [MDS-003 — Material System](../mds-003-material-system/index.md) | Material profiles and capability-driven fidelity |
| [MDS-006 — Composition Engine](../mds-006-composition-engine/index.md) | Composition inputs and domain layout selection |
| [MDS-008 — Component Library](../mds-008-component-library/index.md) | Resolved-value consumption |

---

# Terminology Rules

Use **Platform** for the owner of Primitive and Semantic Tokens.

Use **Module** for an extensibility participant providing domain intent or layout contracts.

Do not use Composition Token, Component Token, Runtime Token, Module Token or Platform Token as current architectural categories.
