<!--
File: docs/design/system/mds-001-design-token-architecture/10-module-intent.md
Document: MDS-001
Chapter: 10
Title: Module Intent
Status: Draft
Version: 0.1
-->

# Module Intent

---

# Purpose

Modules require creative and domain freedom without gaining authority to fragment the Mosaic Design Language.

They participate by declaring intent and optional domain layout extensions rather than by creating Design Tokens.

---

# Governing Principle

> **Modules may create expression, but they may not redefine meaning.**

The Platform owns:

- Primitive Tokens
- Semantic Tokens
- core Materials
- typography and motion mechanics
- interaction meaning
- accessibility rules
- token resolution
- renderer adaptation

Modules own domain content, domain meaning and valid domain structure.

---

# Domain Intent

A Module may declare a namespaced domain intent when the Platform vocabulary does not express the domain fact directly.

Examples include:

```text
Calendar.Today
Calendar.OutsideCurrentMonth
Sports.Live
Music.NowPlaying
```

These are intent identifiers, not Design Tokens.

Each identifier must declare:

- its domain meaning
- the existing Platform Semantic Token or role to which it maps
- a safe fallback
- any permitted state transitions

---

# Extension Rule

A Module may introduce a domain intent without prior Platform catalogue expansion when:

1. the intent is namespaced to the Module domain
2. its meaning is genuinely domain-specific
3. it maps to an existing Platform semantic role
4. it supplies a valid fallback
5. it does not alter locked Platform behaviour

An intent requiring entirely new cross-product semantic meaning requires Platform review.

---

# Creative Control

Modules may provide:

- semantic emphasis and relationship intent
- atmosphere or energy intent within governed ranges
- governed recipes composed from Platform semantics
- domain-specific Composition invariants
- valid domain presentation modes

Modules may not provide:

- raw colours, blur radii or physical values as design authority
- padding, spacing, radius, density or concrete geometry
- new Primitive or Semantic Tokens
- new Material physics
- renderer code through SDUI
- device-category branches
- component-local accessibility exceptions

---

# Mosaic Shell And Module Content

The Mosaic shell retains Platform navigation, Focus, typography hierarchy, interaction meaning and accessibility behaviour.

A Module may become visually dominant inside its governed content area through content, artwork, domain intent and Composition.

The underlying Material, motion and rendering behaviours remain Platform-owned.

---

# Domain Layout Extensions

When the Platform lacks a required layout, a Module may provide a layout extension contract.

The contract declares domain invariants, valid presentation modes, adaptation permissions, priority rules and overflow behaviour.

The [MDS-006 — Composition Engine](../mds-006-composition-engine/index.md) remains responsible for selecting a valid mode and calculating Tile location and size.

The extension does not create shape or geometry tokens.

---

# Validation And Fallback

The client should validate Module intent before resolution.

```text
Is the identifier namespaced?
Is its domain meaning declared?
Does it map to Platform semantics?
Does it preserve accessibility and locked behaviour?
Does it provide a fallback?
```

Invalid or unknown intent uses the declared fallback.

It must not create a local design interpretation.

---

# Promotion

Repeated equivalent intent across several Modules may indicate missing Platform semantic vocabulary.

Promotion requires Platform review, migration guidance and compatibility treatment.

It is not automatic.

---

# Summary

Modules extend Mosaic through domain intent and domain Composition, not through Design Tokens.

This preserves creative freedom inside one coherent Platform-owned design system.
