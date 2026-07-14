<!--
File: docs/design/system/mds-001-design-token-architecture/05-composition-tokens.md
Document: MDS-001
Chapter: 05
Title: Composition Tokens
Status: Draft
Version: 0.4
-->

# Composition Tokens

---

# Purpose

Primitive Tokens describe physical values.

Semantic Tokens describe design intent.

Composition Tokens describe **compositional roles**.

This distinction is unique to the Mosaic Design System.

Traditional design systems frequently stop at Semantic Tokens.

Mosaic introduces an additional layer because the platform's interface is not static.

It is continuously reorganised by the Composition Model.

Composition Tokens provide the implementation bridge between:

- [MDL-005 — Composition Model](../../language/mdl-005-composition-model/index.md)

and

- runtime presentation.

---

# Definition

Within MDS, a **Composition Token** is defined as:

> **A token describing the compositional responsibility of an element independently from its presentation.**

Composition Tokens answer:

> **"What role does this thing play inside the current Composition?"**

They intentionally avoid answering:

> **"What should it look like?"**

---

# Why Composition Tokens Exist

Imagine two pieces of information.

```mermaid
flowchart TD

N1["Continue Watching"]
N2["Next Episode"]

N1 --> N2
```

Both may consume:

```

Surface.Primary
```

Both may consume:

```

Text.Primary
```

Yet one is significantly more important.

Semantic Tokens cannot express this difference.

Composition Tokens can.

---

# Composition Before Components

Composition Tokens intentionally exist before Components.

```mermaid
flowchart TD

N1["Composition"]
N2["Component"]
N3["Presentation"]

N1 --> N2
N2 --> N3
```

This allows:

- Hero
- Timeline
- Navigation
- Progress

to share identical compositional behaviour while using completely different components.

---

# Composition Categories

The current Composition Token taxonomy consists of:

```mermaid
flowchart TD

N1["Composition"]
N2["Hero"]
N3["Anchor"]
N4["Primary"]
N5["Supporting"]
N6["Contextual"]
N7["Peripheral"]
N8["Overlay"]
N9["Navigation"]
N10["Modal"]
N11["Background"]

N1 --> N2
N1 --> N3
N1 --> N4
N1 --> N5
N1 --> N6
N1 --> N7
N1 --> N8
N1 --> N9
N1 --> N10
N1 --> N11
```

These categories are conceptual.

They intentionally avoid implementation terminology.

---

# Hero

Purpose.

Communicate the primary concept within the current Composition.

Example.

```

Composition.Hero
```

The Hero token should influence:

- emphasis
- visual weight
- breathing space
- movement priority

It should not define:

- colour
- typography
- dimensions

Those responsibilities belong elsewhere.

---

# Anchor

Purpose.

Preserve orientation.

Example.

```

Composition.Anchor
```

Anchors intentionally remain behaviourally stable.

Future runtime systems should preferentially preserve Anchors during adaptive recomposition.

---

# Primary

Purpose.

Represent information directly supporting the Hero.

Examples include:

- progress
- next episode
- current chapter

Primary Tokens communicate conceptual proximity to the Hero.

---

# Supporting

Purpose.

Strengthen understanding without competing for attention.

Examples include:

- timeline
- queue
- continuation
- bookmarks

Supporting Tokens should remain visible while allowing the Hero to dominate.

---

# Contextual

Purpose.

Provide explanation.

Examples include:

- cast
- author
- soundtrack
- reviews
- relationships

Contextual Tokens enrich understanding.

They should rarely become the visual centre of a Composition.

---

# Peripheral

Purpose.

Represent information valuable but not immediately relevant.

Examples include:

- collections
- history
- statistics
- diagnostics

Peripheral Tokens should naturally compress before higher-priority compositional roles.

---

# Overlay

Purpose.

Temporarily communicate information requiring immediate interaction.

Examples include:

- playback controls
- search
- confirmations

Overlay Tokens intentionally possess temporary behavioural ownership.

They should relinquish emphasis once interaction completes.

---

# Navigation

Purpose.

Represent navigational anchors.

Unlike Hero Tokens...

Navigation Tokens should optimise:

- stability
- predictability
- orientation

rather than attention.

---

# Background

Purpose.

Communicate supporting environmental information.

Examples include:

- atmospheric materials
- decorative relationships
- passive artwork

Background Tokens should never compete with active understanding.

---

# Composition Tokens Are Behavioural

Unlike Semantic Tokens, Composition Tokens intentionally change.

Example.

```mermaid
flowchart TD

N1["Timeline"]
N2["Supporting"]

N1 --> N2
```

After playback completes.

```mermaid
flowchart TD

N1["Timeline"]
N2["Primary"]

N1 --> N2
```

Nothing about the Timeline changed.

Only its compositional role.

Composition Tokens therefore describe **behavioural intent** rather than permanent identity.

---

# Composition Tokens Consume Semantic Tokens

Example.

```mermaid
flowchart TD

N1["Composition.Hero"]
N2["Semantic.Surface.Hero"]
N3["Primitive Values"]

N1 --> N2
N2 --> N3
```

Composition Tokens should never reference Primitive Tokens directly.

Meaning should remain layered.

---

# Runtime Adaptation

Composition Tokens are expected to participate heavily in runtime adaptation.

Example.

```mermaid
flowchart TD

N1["Composition.Supporting"]
N2["Composition.Primary"]

N1 --> N2
```

This promotion occurs because:

- Context changed
- Priority changed
- Behaviour changed

The component itself remains identical.

Only its compositional responsibility changes.

---

# Component Consumption

Components should consume Composition Tokens.

Not infer them.

Poor.

```mermaid
flowchart TD

N1["Timeline"]
N2["If Important..."]

N1 --> N2
```

Preferred.

```mermaid
flowchart TD

N1["Composition.Primary"]
N2["Timeline"]

N1 --> N2
```

The Composition Engine owns compositional reasoning.

Components communicate it.

---

# Composition Independence

Composition Tokens intentionally remain independent from:

- devices
- layouts
- frameworks
- rendering engines

Desktop.

```

Composition.Hero
```

Television.

```

Composition.Hero
```

Voice.

```

Composition.Hero
```

The role remains identical.

Presentation changes.

---

# Good Examples

```mermaid
flowchart TD

N1["Composition.Hero"]
N2["Surface.Hero"]
N3["Tile.Hero"]

N1 --> N2
N2 --> N3
```

```mermaid
flowchart TD

N1["Composition.Supporting"]
N2["Surface.Secondary"]
N3["Timeline"]

N1 --> N2
N2 --> N3
```

```mermaid
flowchart TD

N1["Composition.Peripheral"]
N2["Surface.Canvas"]
N3["Collection Shelf"]

N1 --> N2
N2 --> N3
```

Each layer contributes one responsibility.

---

# Anti-patterns

## Component Composition

```

Timeline.Primary
```

Component owns composition.

Incorrect.

---

## Colour Composition

```

BlueHero
```

Presentation has leaked into composition.

---

## Device Composition

```

MobileHero
```

Composition should remain device independent.

---

## Static Composition

Composition Tokens never change.

Adaptive behaviour becomes impossible.

---

# Composition Token Model

```mermaid
flowchart TD

Semantic
Semantic --> Composition
Composition --> Component
Component --> Runtime
Runtime --> Presentation
```

Composition Tokens bridge:

design intent

and

runtime behaviour.

---

# Litmus Test

Contributors should ask:

> **If this component disappeared tomorrow, would this compositional role still exist?**

If the answer is yes...

It belongs within Composition Tokens.

If the answer is no...

It probably belongs within Component Tokens instead.

---

# Summary

Composition Tokens are one of the defining innovations of the Mosaic Design System.

They allow runtime systems to reorganise understanding without requiring components to understand behaviour.

This separation enables:

- adaptive composition
- runtime hierarchy
- device independence
- module consistency
- future evolution

Every future runtime implementation should treat Composition Tokens as behavioural intent rather than visual styling.
