<!--
File: docs/engineering/architecture/mdp-001-adaptive-composition-runtime/24-runtime-tile-resolution.md
Document: MDP-001
Status: Draft
-->

# Runtime Tile Resolution

> **Proposal status:** Deferred and non-authoritative. This chapter preserves post-v1 research; it is not a Mosaic v1 requirement.

---

# Purpose

The Tile Framework defines:

- Tile identities,
- Tile behaviour,
- Tile interaction,
- Tile composition.

This chapter defines how those concepts become concrete runtime presentation objects.

Runtime Tile Resolution transforms behavioural Tiles into fully resolved presentation primitives ready for implementation by the Component Library.

Components should never decide:

- Material
- Typography
- Motion
- Interaction
- Layout

They receive already resolved Tiles.

---

# Definition

Within MDS, **Runtime Tile Resolution** is defined as:

> **The deterministic process through which behavioural Tile identities become fully resolved runtime presentation objects while preserving behavioural meaning and platform independence.**

Runtime Tile Resolution resolves presentation.

It never changes behaviour.

---

# Why Resolution Exists

Without Runtime Tile Resolution, every component would need to understand:

- Runtime Hierarchy
- Material Intent
- Typography Intent
- Motion Intent
- Adaptive behaviour
- Accessibility

Instead.

```mermaid
flowchart TD

N1["Tile"]
N2["Runtime Tile Resolver"]
N3["Resolved Tile"]
N4["Component"]

N1 --> N2
N2 --> N3
N3 --> N4
```

Components remain extremely simple.

---

# Resolution Pipeline

Every Tile follows the same conceptual pipeline.

```mermaid
flowchart TD

N1["Tile Identity"]
N2["Runtime Hierarchy"]
N3["Material Intent"]
N4["Typography Intent"]
N5["Motion Intent"]
N6["Accessibility"]
N7["Adaptive Behaviour"]
N8["Resolved Tile"]

N1 --> N2
N2 --> N3
N3 --> N4
N4 --> N5
N5 --> N6
N6 --> N7
N7 --> N8
```

Each stage contributes one responsibility.

---

# Resolution Inputs

Runtime Tile Resolution evaluates:

```mermaid
flowchart TD

N1["Tile Identity"]
N2["Expression"]
N3["Runtime Hierarchy"]
N4["Current Context"]
N5["Device Profile"]
N6["Accessibility"]
N7["Capabilities"]

N1 --> N2
N2 --> N3
N3 --> N4
N4 --> N5
N5 --> N6
N6 --> N7
```

Rendering technology remains intentionally absent.

---

# Resolution Outputs

Resolved Tiles contain:

```mermaid
flowchart TD

N1["Material"]
N2["Typography"]
N3["Motion"]
N4["Interaction"]
N5["Adaptive Variant"]
N6["Presentation Metadata"]

N1 --> N2
N2 --> N3
N3 --> N4
N4 --> N5
N5 --> N6
```

These objects become the direct input to the Component Library.

---

# Tile Identity Is Stable

One of the strongest guarantees within Mosaic is:

```mermaid
flowchart TD

N1["Hero Tile"]
N2["Always Hero Tile"]

N1 --> N2
```

Runtime Resolution may alter:

- material richness,
- layout,
- interaction affordances,
- typography.

It never alters Tile identity.

---

# Material Resolution

Material Intent resolves into runtime Materials.

Example.

```mermaid
flowchart TD

N1["Hero Tile"]
N2["Hero Material"]
N3["Resolved Hero Material"]

N1 --> N2
N2 --> N3
```

Components should never determine Material behaviour independently.

---

# Typography Resolution

Typography Intent resolves similarly.

Example.

```mermaid
flowchart TD

N1["Metadata Tile"]
N2["Supporting Typography"]
N3["Resolved Typography"]

N1 --> N2
N2 --> N3
```

Editorial hierarchy therefore remains entirely runtime driven.

---

# Motion Resolution

Motion Intent resolves into runtime behaviour.

Example.

```mermaid
flowchart TD

N1["Timeline Tile"]
N2["Supporting Motion"]
N3["Resolved Motion Profile"]

N1 --> N2
N2 --> N3
```

Components consume motion.

They never construct it.

---

# Interaction Resolution

Interaction Intent also resolves.

Examples.

```mermaid
flowchart TD

N1["Primary"]
N2["Touch"]
N3["Mouse"]
N4["Remote"]
N5["Voice"]

N1 --> N2
N2 --> N3
N3 --> N4
N4 --> N5
```

Interaction methods adapt.

Behavioural intent remains unchanged.

---

# Adaptive Resolution

Runtime Tile Resolution also determines adaptive variants.

Example.

Desktop.

↓

Expanded Hero Tile.

Phone.

↓

Compact Hero Tile.

Voice.

↓

Conversational Hero Tile.

The Tile remains behaviourally identical.

---

# Accessibility Resolution

Accessibility refines resolved Tiles.

Examples.

Large Text.

↓

Typography.

Reduced Motion.

↓

Motion.

High Contrast.

↓

Materials.

Behaviour remains identical.

Only presentation adapts.

---

# Runtime Profiles

Future implementations may internally generate Tile Profiles.

Conceptually.

```mermaid
flowchart TD

N1["Hero Tile"]
N2["Tile Profile"]
N3["Material"]
N4["Typography"]
N5["Motion"]
N6["Interaction"]
N7["Resolved Tile"]

N1 --> N2
N2 --> N3
N3 --> N4
N4 --> N5
N5 --> N6
N6 --> N7
```

Components consume Tile Profiles.

They remain unaware of runtime solving.

---

# Runtime Caching

Resolved Tiles should be aggressively cacheable.

Typical invalidation events include:

- behaviour changes,
- hierarchy changes,
- accessibility changes,
- device changes.

Ordinary rendering should reuse existing Tile Profiles whenever practical.

---

# Incremental Resolution

Preferred.

```mermaid
flowchart TD

N1["Timeline Tile"]
N2["Resolved"]
N3["Updated"]

N1 --> N2
N2 --> N3
```

Avoid.

```mermaid
flowchart TD

N1["Every Tile"]
N2["Resolved Again"]

N1 --> N2
```

Incremental resolution preserves runtime performance and behavioural continuity.

---

# Platform Independence

Runtime Tile Resolution should remain completely platform independent.

Flutter.

↓

Consumes Resolved Tile.

Web.

↓

Consumes Resolved Tile.

SwiftUI.

↓

Consumes Resolved Tile.

Compose.

↓

Consumes Resolved Tile.

Presentation differs.

Resolved behavioural intent remains identical.

---

# Deterministic Resolution

Given identical:

- Tile Identity,
- Runtime World,
- Hierarchy,
- Accessibility,

Runtime Tile Resolution should always produce identical resolved Tiles.

Determinism improves:

- caching,
- replay,
- testing,
- cross-platform consistency.

---

# Modules

Modules contribute:

- Expressions,
- behaviour,
- relationships.

Modules never resolve Tiles.

The Tile Framework owns:

- Tile Resolution,
- adaptive behaviour,
- runtime presentation.

Every module therefore automatically inherits future Tile improvements.

---

# Good Examples

## Playback

Timeline Tile.

↓

Runtime Resolution.

↓

Resolved Timeline.

↓

Component.

Behaviour remains preserved.

---

## Reading

Relationship Tile.

↓

Adaptive Resolution.

↓

Phone Presentation.

↓

Reader continues naturally.

---

## Television

Hero Tile.

↓

Immersive Variant.

↓

Hero Material.

↓

Presentation.

One behavioural identity.

---

# Anti-patterns

## Component Resolution

Components selecting Materials independently.

---

## Platform Resolution

Each client inventing Tile behaviour.

---

## Widget Resolution

Rendering technology influencing behavioural presentation.

---

## Module Resolution

Modules bypassing the Tile Framework.

---

# Runtime Tile Resolution Model

```mermaid
flowchart TD

TileIdentity
TileIdentity --> RuntimeTileResolver
RuntimeTileResolver --> Material
RuntimeTileResolver
RuntimeTileResolver --> Typography
RuntimeTileResolver
RuntimeTileResolver --> Motion
RuntimeTileResolver
RuntimeTileResolver --> Interaction
Material --> ResolvedTile
Typography --> ResolvedTile
Motion --> ResolvedTile
Interaction --> ResolvedTile
ResolvedTile
ResolvedTile --> Component
```

The Runtime Tile Resolver transforms behavioural presentation into implementation-ready runtime objects.

---

# Relationship To Future Chapters

The next chapter defines **Module Tiles**.

Runtime Tile Resolution explains:

> **How Tiles become runtime presentation.**

Module Tiles explain:

> **How third-party runtime contributions participate in the Tile Framework while remaining indistinguishable from native Mosaic presentation.**

Together they complete the runtime architecture of the Tile Framework.

---

# Summary

Runtime Tile Resolution ensures every behavioural Tile becomes one fully resolved presentation object before rendering begins.

Components therefore remain implementation details.

Behaviour remains the architectural authority.

Tiles remain the presentation language of Mosaic.

That separation allows the platform to evolve indefinitely while preserving one coherent runtime experience.
