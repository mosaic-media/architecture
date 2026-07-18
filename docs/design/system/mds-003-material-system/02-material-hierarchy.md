<!--
File: docs/design/system/mds-003-material-system/02-material-hierarchy.md
Document: MDS-003
Status: Draft
-->

# Material Hierarchy

---

# Purpose

Every physical object communicates importance.

A sheet of paper does not feel the same as polished acrylic.

Glass does not feel the same as carved stone.

Likewise, every material within Mosaic should communicate its role through its physical behaviour.

The Material Hierarchy defines the architectural relationship between every material used throughout the platform.

It answers one question.

> **"How physically present should this part of the interface feel?"**

---

# Definition

Within MDS, **Material Hierarchy** is defined as:

> **The ordered system through which materials communicate hierarchy using physical behaviour rather than decoration.**

Material Hierarchy is independent from:

- colour
- typography
- components
- layout

It is an environmental system.

---

# Why Hierarchy Exists

Without Material Hierarchy:

Every surface behaves identically.

Every object appears equally important.

Users must rely entirely upon colour or layout to understand hierarchy.

Mosaic intentionally distributes hierarchy across multiple systems.

Including:

- Composition
- Colour
- Typography
- Motion
- Materials

Materials reinforce understanding.

They never create it independently.

---

# Material Layers

The Mosaic Material System defines five primary layers.

```mermaid
flowchart TD

N1["Canvas"]
N2["Surface"]
N3["Acrylic"]
N4["Hero"]
N5["Overlay"]

N1 --> N2
N2 --> N3
N3 --> N4
N4 --> N5
```

Each layer increases perceived physical presence.

---

# Layer 01

## Canvas

Purpose.

Represent the environment.

The Canvas should feel:

- calm
- stable
- neutral
- distant

It should receive only subtle influence from Runtime Atmosphere.

The Canvas exists to support everything above it.

It should rarely attract attention itself.

---

# Layer 02

## Surface

Purpose.

Group related understanding.

Examples include:

- tiles
- panels
- collections
- shelves

Surfaces should possess:

- gentle separation
- minimal elevation
- restrained material response

Surfaces organise information.

They should not dominate it.

---

# Layer 03

## Acrylic

Purpose.

Create physical presence.

Acrylic introduces:

- translucency
- refraction
- environmental lighting
- perceived depth

Acrylic should feel:

- premium
- contemporary
- substantial

Importantly...

Acrylic is **not glass**.

Glass disappears.

Acrylic possesses presence.

It occupies space while remaining connected to its surroundings.

This distinction forms one of the defining visual characteristics of Mosaic.

---

# Layer 04

## Hero

Purpose.

Communicate current importance.

Hero Materials receive the highest compositional and scheduling priority for:

- Runtime Atmosphere
- Artwork
- Refraction

Hero Materials should feel:

- illuminated
- immersive
- emotionally connected

without becoming visually dominant.

Priority does not alter the fixed Acrylic profile.

The entertainment remains the emotional centre.

The Hero Material quietly supports it.

---

# Layer 05

## Overlay

Purpose.

Temporarily communicate interaction.

Examples include:

- playback controls
- dialogs
- search
- menus

Overlay Materials should prioritise:

- readability
- separation
- focus

Runtime Atmosphere influence should reduce while overlays remain active.

Interaction always has higher priority than atmosphere.

---

# Physical Presence

Every material possesses perceived physical weight.

Conceptually.

```mermaid
flowchart TD

N1["Canvas"]
N2["Very Light<br/>Surface"]
N3["Light<br/>Acrylic"]
N4["Medium<br/>Hero"]
N5["High<br/>Overlay"]
N6["Highest"]

N1 --> N2
N2 --> N3
N3 --> N4
N4 --> N5
N5 --> N6
```

Physical weight influences:

- depth
- refraction
- diffusion
- translucency
- environmental response

It should not be confused with visual brightness.

---

# Material Relationships

Materials should behave like members of the same physical family.

Poor.

```

Glass

Metal

Paper

Plastic
```

Each behaves independently.

Preferred.

```mermaid
flowchart TD

N1["Canvas"]
N2["Surface"]
N3["Acrylic"]
N4["Hero"]
N5["Overlay"]

N1 --> N2
N2 --> N3
N3 --> N4
N4 --> N5
```

Every material shares:

- lighting model
- refraction language
- environmental response

The differences are gradual.

Not absolute.

---

# Hierarchy Is Behaviour

Material Hierarchy should evolve alongside Composition.

Example.

```mermaid
flowchart TD

N1["Hero Changes"]
N2["Material Importance Changes"]
N3["Lighting Changes"]
N4["Refraction Changes"]

N1 --> N2
N2 --> N3
N3 --> N4
```

Materials should never change independently from behavioural hierarchy.

They respond to understanding.

Not interface events.

---

# Hierarchy Across Themes

The hierarchy remains identical across themes.

Light Theme.

```mermaid
flowchart TD

N1["Canvas"]
N2["Paper-like"]

N1 --> N2
```

Dark Theme.

```mermaid
flowchart TD

N1["Canvas"]
N2["Slate-like"]

N1 --> N2
```

Hero remains Hero.

Acrylic remains Acrylic.

Only physical interpretation changes.

---

# Hierarchy Across Devices

Different rendering technologies may communicate Material Hierarchy differently.

Desktop.

↓

High-quality acrylic.

Mobile.

↓

Reduced translucency.

Television.

↓

Greater perceived depth.

The behavioural hierarchy remains unchanged.

---

# Runtime Behaviour

Runtime Atmosphere should influence each layer differently.

| Material | Atmosphere Influence |
|-----------|---------------------:|
| Canvas | Very Low |
| Surface | Low |
| Acrylic | Medium |
| Hero | High |
| Overlay | Minimal |

This prevents atmosphere from overwhelming the interface.

The user's attention naturally remains on current content.

---

# Modules

Modules never define materials.

Modules contribute:

- Information
- Relationships
- Expressions

The Material System determines:

- physical presence
- lighting
- hierarchy
- atmosphere

Every module therefore inherits one coherent physical language.

---

# Good Examples

## Continue Watching

Canvas remains neutral.

Hero gently illuminated.

Supporting tiles receive subtle acrylic.

Navigation remains restrained.

The hierarchy is immediately understandable.

---

## Playback

Video dominates.

Controls appear using Overlay Material.

Atmosphere reduces.

Readability increases.

Interaction feels effortless.

---

## Administration

Canvas becomes calmer.

Atmosphere becomes minimal.

Materials remain recognisably Mosaic while supporting productivity rather than immersion.

---

# Anti-patterns

## Everything Acrylic

Every surface possesses identical material.

Hierarchy disappears.

---

## Decorative Depth

Elevation exists purely because it looks modern.

No additional understanding is communicated.

---

## Theme Materials

Different themes invent different material hierarchies.

Users lose physical consistency.

---

## Module Materials

Modules introducing their own material behaviour.

The physical language fragments.

---

# Material Hierarchy Model

```mermaid
flowchart TD

Canvas
Canvas --> Surface
Surface --> Acrylic
Acrylic --> Hero
Hero --> Overlay
Overlay
Overlay --> Presentation
```

Each material increases physical presence while remaining part of one coherent environmental system.

---

# Relationship To Future Chapters

The following chapters define each material individually.

Including:

- Canvas
- Acrylic
- Hero Material
- Overlay Material
- Refraction
- UV-indexed Refraction
- Light Transport

This chapter establishes only the hierarchy connecting them.

---

# Summary

Material Hierarchy defines how physical presence communicates importance.

It allows users to understand hierarchy before consciously analysing colour or layout.

Every material belongs to one coherent physical family.

The interface should feel constructed from one environmental language rather than several unrelated visual effects.

That physical coherence is one of the defining characteristics of the Mosaic Material System.
