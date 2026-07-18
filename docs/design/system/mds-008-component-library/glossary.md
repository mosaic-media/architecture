<!--
File: docs/design/system/mds-008-component-library/glossary.md
Document: MDS-008
Status: Draft
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

## Client Renderer

A client-owned implementation layer that transforms Mosaic SDUI contracts into native presentation.

Client Renderers may exist for:

- Web
- Flutter
- Windows
- macOS
- TV

Client Renderers implement presentation.

They do not produce runtime behaviour.

---

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

## Continuity Key

A stable domain identity carried by Runtime SDUI so a Client Renderer can recognise one semantic object across snapshots, patches, route changes, resizing, reparenting and Composition-plane movement.

A Continuity Key is independent from component-instance, render-tree and transaction identities.

---

# E

## Embedded Recovery Renderer

A self-contained Web fallback renderer served by the Supervisor when the Shell or normal Web Renderer cannot run.

The Embedded Recovery Renderer renders Recovery SDUI using one HTML document with inline CSS and JavaScript only.

It must not depend on external assets, bundles, fonts, images, frameworks or build pipeline output.

---

# F

## Flutter Renderer

A specific Native Client Renderer that transforms Runtime SDUI or Recovery SDUI into native Flutter presentation.

The Flutter Renderer uses the Flutter MDL library rather than browser fallback rendering.

It is an example native renderer, not the required native-client architecture.

---

# H

## HTMX Web Adapter

An optional Web integration that uses HTMX for transport or progressive enhancement while resolving responses through the governed Mosaic component library.

HTMX is not the canonical Runtime SDUI contract.

---

# L

## Live State Binding

A semantic relationship between a stable SDUI node and changing Platform data.

The binding communicates meaning and freshness intent without prescribing endpoint, transport, polling or renderer implementation.

---

# M

## MDL Algorithm

A platform-independent design-language calculation implemented by each platform-specific MDL library.

Examples include:

- light intensity,
- refraction strength,
- colour extraction,
- elevation calculations,
- motion curves.

MDL Algorithms preserve design-language equivalence across different rendering technologies.

---

## MDL Library

A platform-specific implementation of the Mosaic Design Language.

Examples include:

- `mdl-web`
- `mdl-flutter`
- future `mdl-windows`
- future `mdl-macos`
- future `mdl-linux`
- future `mdl-android-tv`
- future `mdl-apple-tv`
- future `mdl-tv`

MDL Libraries own presentation behaviour.

They do not own Mosaic business logic.

---

## MDL Runtime

A rejected architecture in which the Mosaic Design Language existed as a runtime presentation service between SDUI and client renderers.

Mosaic does not use an MDL Runtime.

MDL is implemented as platform-specific libraries linked into client renderers.

---

## MDL Specification

The platform-independent source of truth for Mosaic visual language behaviour.

The MDL Specification defines design-language concepts that platform-specific MDL libraries implement.

It may be represented as a dedicated `mdl-spec` project.

---

## Material Profile

The resolved Material behaviour supplied to Components through Component Contracts.

Material Profiles describe implementation behaviour.

Components execute them.

---

## Native Client Renderer

A non-Web client renderer that transforms Runtime SDUI or Recovery SDUI into native application presentation.

Flutter is the clearest current example, but native clients may also include Windows, macOS, Linux, Android TV and Apple TV implementations.

Native Client Renderers should not depend on the Web Shell, browser fallback rendering or CSS as their normal presentation contract.

---

# P

## Presentation Architecture

The architectural separation between semantic intent, design-language behaviour and native rendering implementation.

Presentation Architecture separates:

- Platform-owned Semantic UI,
- MDL-owned presentation behaviour,
- renderer-owned native implementation.

---

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

## Product Identity

The brand-specific assets and choices that identify Mosaic as a product.

Product Identity includes:

- logos,
- product colours,
- icons,
- favicons,
- brand imagery.

Product Identity is separate from the Mosaic Design Language, which owns presentation behaviour.

---

# R

## Recovery SDUI

The deliberately small SDUI contract emitted by the Supervisor for Shell bootstrap status, onboarding, build progress, diagnostics, updates, maintenance and recovery states.

Recovery SDUI supports only the recovery component vocabulary.

Its purpose is to keep an intelligent interface available when the Platform does not exist, has failed or is being replaced.

Recovery SDUI is owned by the Supervisor.

MDL does not modify Recovery SDUI.

Recovery SDUI also supports onboarding before the Platform exists; the Supervisor does not emit Runtime SDUI for that flow.

---

## Refreshable Compiled SDUI

An immutable, versioned SDUI snapshot produced before or independently of a live presentation session.

The active site may refresh by atomically adopting a newer bundle, while live values may update separately through Live State Bindings.

---

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

## Runtime SDUI

The SDUI contract emitted by the Platform for normal Mosaic presentation.

Runtime SDUI may express the full Mosaic presentation model and is rendered by client renderers through Shell or native client implementations.

Runtime SDUI is the normal Mosaic form of Semantic UI.

Runtime SDUI is owned by the Platform.

MDL does not modify Runtime SDUI.

---

# S

## SDUI Driver

The Platform-owned producer that supplies initial Runtime SDUI state, ordered semantic transactions and Live State Binding updates to a Client Renderer.

The SDUI Driver owns semantic intent and never supplies client presentation values.

---

## SDUI Patch Stream

The ordered stream of atomic semantic transactions used to update Runtime SDUI during a connected session without replacing the document or application root.

The stream is renderer-independent and does not make HTML fragments its canonical payload.

---

## Semantic UI

An SDUI contract that describes business intent and interface structure without visual implementation details.

Semantic UI may describe:

- business logic,
- navigation structure,
- component hierarchy,
- actions,
- state,
- permissions.

Semantic UI must not describe:

- CSS,
- colours,
- spacing,
- animation,
- refraction,
- layout coordinates,
- native widget classes.

---

# T

## Tile

A behavioural presentation primitive defined by the semantic structure resolver.

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

# W

## Web Component Library

The Mosaic v1 client-side implementation of governed semantic components using HTML, CSS and TypeScript for authored and SDUI-driven Web experiences.

---

## Web Renderer

The Web client renderer responsible for transforming Runtime SDUI or Recovery SDUI into browser presentation when the Shell is available.

The Web Renderer is distinct from the Embedded Recovery Renderer.

---

# Cross References

| Specification | Primary Concepts |
|---------------|------------------|
| [MDL-001 — Mosaic Design Language Vision](../../language/mdl-001-vision/index.md) | Companion |
| [MDL-002 — Principles](../../language/mdl-002-principles/index.md) | Behaviour Before Interface |
| [MDL-003 — Mental Model](../../language/mdl-003-mental-model/index.md) | World |
| [MDL-004 — Interaction Model](../../language/mdl-004-interaction-model/index.md) | Behaviour |
| [MDL-005 — Composition Model](../../language/mdl-005-composition-model/index.md) | Hierarchy |
| [MDP-001 — Adaptive Composition Runtime](../../../engineering/architecture/mdp-001-adaptive-composition-runtime/index.md) | Expressions, Presentation Model |
| [MDP-001 — Adaptive Composition Runtime](../../../engineering/architecture/mdp-001-adaptive-composition-runtime/14-adaptive-tile-model.md) | Tiles, semantic Tile resolution |

---

# Terminology Rules

Future contributors should:

- describe Tiles before Components,
- describe Contracts before rendering,
- distinguish implementation from behaviour,
- distinguish rendering from runtime architecture,
- avoid framework-specific terminology within architectural documentation.

Component terminology should remain independent from implementation technologies.
