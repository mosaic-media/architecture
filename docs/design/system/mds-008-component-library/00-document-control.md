<!--
File: docs/design/system/mds-008-component-library/00-document-control.md
Document: MDS-008
Status: Draft
-->

# Document Control

---

# Document Information

| Property | Value |
|----------|-------|
| Document ID | MDS-008 |
| Title | Mosaic Design System — Component Library |
| Classification | Internal |
| Status | Draft |
| Owner | AdamNi-7080 |
| Parent Specifications | [MDL-001](../../language/mdl-001-vision/index.md) → [MDL-005](../../language/mdl-005-composition-model/index.md), [MDS-001](../mds-001-design-token-architecture/index.md) → [MDS-005](../mds-005-motion-system/index.md) |
| Repository | `/design/mds/MDS-008 Component Library/` |

---

# Purpose

MDS-008 defines the Component Library used throughout Mosaic.

The Component Library is the final implementation layer of the entire Mosaic Design Language.

Everything before this specification determines:

- behaviour,
- hierarchy,
- materials,
- typography,
- motion,
- presentation.

The Component Library determines only:

> **How those solved decisions become visible.**

Unlike conventional component libraries, Mosaic Components intentionally possess almost no behavioural responsibility.

Components are implementation.

Not architecture.

---

# Authority

MDS-008 governs:

- Component philosophy
- Component taxonomy
- Component contracts
- Component lifecycle
- Component composition
- Tile structural components
- Rendering architecture
- Client rendering
- Runtime SDUI
- Mosaic v1 Web Component Library
- SDUI Structural Component Vocabulary
- Optional HTMX Web Adapter
- Refreshable Compiled SDUI
- SDUI Patch Stream
- Continuity Keys
- Recovery SDUI
- Platform-specific MDL libraries
- Platform components
- Accessibility contracts
- Runtime rendering
- Component optimisation

This specification intentionally does **not** govern:

- Behaviour
- Runtime World
- Composition
- Expressions
- Design Tokens

The deferred adaptive Tile solver belongs to [MDP-001 — Adaptive Composition Runtime](../../../engineering/architecture/mdp-001-adaptive-composition-runtime/index.md).

The Design Language and semantic structure already establish runtime understanding.

Components simply render it.

---

# Relationship To MDS

The Component Library sits at the very end of the runtime architecture.

```mermaid
flowchart TD

Vision
Vision --> Principles
Principles --> MentalModel
MentalModel --> Interaction
Interaction --> Composition
Composition --> Tokens
Tokens --> Colour
Colour --> Materials
Materials --> Typography
Typography --> Motion
Motion --> CompositionEngine
CompositionEngine --> TileFramework
TileFramework --> ComponentLibrary
ComponentLibrary --> Rendering
Rendering --> User
```

Every previous specification influences Components.

Components influence nothing upstream.

---

# Design Intent

Traditional UI frameworks frequently behave like this.

```mermaid
flowchart TD

N1["Components"]
N2["State"]
N3["Behaviour"]
N4["Rendering"]

N1 --> N2
N2 --> N3
N3 --> N4
```

Mosaic intentionally reverses this dependency.

```mermaid
flowchart TD

N1["Behaviour"]
N2["Composition"]
N3["Semantic Structure"]
N4["Components"]
N5["Rendering"]

N1 --> N2
N2 --> N3
N3 --> N4
N4 --> N5
```

Components become passive renderers of behavioural presentation.

---

# Reader Expectations

Before reading this specification contributors should already understand:

- [MDL-001 — Mosaic Design Language Vision](../../language/mdl-001-vision/index.md)
- [MDL-002 — Principles](../../language/mdl-002-principles/index.md)
- [MDL-003 — Mental Model](../../language/mdl-003-mental-model/index.md)
- [MDL-004 — Interaction Model](../../language/mdl-004-interaction-model/index.md)
- [MDL-005 — Composition Model](../../language/mdl-005-composition-model/index.md)
- [MDS-001 — Design Token Architecture](../mds-001-design-token-architecture/index.md) through [MDS-005 — Motion System](../mds-005-motion-system/index.md)

MDS-008 assumes every architectural decision has already been made.

Its responsibility is implementation.

---

# Architectural Scope

The Component Library defines:

- component contracts
- rendering behaviour
- platform implementation
- platform-specific MDL library boundaries
- accessibility implementation
- runtime rendering
- client rendering responsibilities
- component optimisation

It intentionally avoids implementation-specific frameworks becoming architectural concepts.

Web and native clients remain implementation targets.

Native clients may include Flutter, Windows, macOS, Linux, Android TV or Apple TV.

Not design abstractions.

The Platform and Supervisor emit SDUI contracts.

Clients implement those contracts as native presentation.

The Component Library owns the rendering responsibility, not the upstream runtime decisions.

Version 0.4 records the Presentation Architecture boundary between Platform semantic UI, client renderers and platform-specific MDL libraries.

---

# Stability

Expected lifetime.

| Artefact | Expected Lifetime |
|----------|-------------------|
| Platform Widgets | Months |
| Rendering APIs | Months |
| Framework Integrations | Years |
| Component Contracts | Years |
| Component Philosophy | Decades |

Frameworks evolve.

Component philosophy should remain recognisably Mosaic.

---

# Success Criteria

MDS-008 succeeds when:

- Components remain behaviourally simple
- platform implementations remain replaceable
- accessibility is automatically inherited
- rendering remains deterministic
- contributors naturally think in Tiles rather than Components
- the runtime architecture remains invisible beneath implementation
- semantic objects retain perceptual identity across snapshots, patches and route changes

Users should never perceive Components.

They should simply experience a Companion that always behaves consistently.
