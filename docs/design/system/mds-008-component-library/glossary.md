<!--
File: docs/design/system/mds-008-component-library/glossary.md
Document: MDS-008
Title: Glossary
Status: Draft
Version: 0.1
-->

# Glossary

---

# Purpose

This glossary defines the terminology introduced by **MDS-008 — Component Library**.

Unlike previous glossaries, these definitions describe the final implementation layer of the Mosaic architecture.

These terms intentionally remain independent from:

- UI frameworks,
- rendering engines,
- graphics APIs,
- programming languages.

Future specifications should reuse these definitions consistently.

---

# A

## Accessibility Contract

An immutable runtime contract describing the accessibility behaviour a Component must implement.

Accessibility Contracts include:

- semantic roles,
- accessible names,
- focus behaviour,
- interaction actions,
- motion preferences.

Accessibility Contracts are produced by the runtime.

Components consume them.

---

# C

## Component

A platform-specific implementation primitive responsible for rendering a resolved Tile.

Components are implementation artefacts.

They do not own:

- behaviour,
- hierarchy,
- Materials,
- Typography,
- Motion.

---

## Component Contract

The immutable runtime description consumed by a Component.

Component Contracts contain:

- Material Profile,
- Typography Profile,
- Motion Profile,
- Interaction Profile,
- Accessibility Profile.

Components render Contracts.

They never modify them.

---

## Component Composition

The deterministic assembly of Components required to render one resolved Tile.

Component Composition concerns implementation only.

---

## Component Lifecycle

The implementation lifecycle through which Components are:

- created,
- bound,
- rendered,
- updated,
- detached,
- released.

This lifecycle is intentionally separate from Tile lifecycle.

---

# M

## Material Profile

The resolved Material behaviour supplied to Components through Component Contracts.

Material Profiles describe implementation behaviour.

Components execute them.

---

# P

## Platform Component

A framework-specific implementation of a Mosaic Component Contract.

Examples include:

- Flutter Component,
- React Component,
- SwiftUI Component,
- Compose Component.

Platform Components preserve identical behavioural presentation.

---

## Presentation

The visible result produced by rendering Components.

Presentation is the final architectural output of the Mosaic Design Language.

---

# R

## Rendering

The implementation process that transforms Platform Components into visible presentation.

Rendering is behaviourally passive.

It never determines runtime understanding.

---

## Runtime Rendering

The deterministic execution of Component Contracts into continuously updated presentation.

Runtime Rendering performs:

- scheduling,
- compositing,
- drawing,
- accessibility integration.

It does not perform behavioural reasoning.

---

# T

## Tile

A behavioural presentation primitive defined by the Tile Framework.

Components render Tiles indirectly through Component Contracts.

---

## Typography Profile

The resolved typography behaviour supplied to Text Components.

Typography Profiles determine:

- hierarchy,
- scale,
- rhythm,
- accessibility.

Components simply render them.

---

# V

## Virtualisation

An implementation optimisation allowing Components to be created only when required.

Virtualisation affects implementation only.

Behaviour remains identical.

---

# Cross References

| Specification | Primary Concepts |
|---------------|------------------|
| MDL-001 Vision | Companion |
| MDL-002 Principles | Behaviour Before Interface |
| MDL-003 Mental Model | World |
| MDL-004 Interaction Model | Behaviour |
| MDL-005 Composition Model | Hierarchy |
| MDS-006 Composition Engine | Expressions, Presentation Model |
| MDS-007 Tile Framework | Tiles, Runtime Tile Resolution |

---

# Terminology Rules

Future contributors should:

- describe Tiles before Components,
- describe Contracts before rendering,
- distinguish implementation from behaviour,
- distinguish rendering from runtime architecture,
- avoid framework-specific terminology within architectural documentation.

Component terminology should remain independent from implementation technologies.

---

# Review Status

**Status**

Draft

**Next File**

`references.md`
