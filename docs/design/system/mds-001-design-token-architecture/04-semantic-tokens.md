<!--
File: docs/design/system/mds-001-design-token-architecture/04-semantic-tokens.md
Document: MDS-001
Chapter: 04
Title: Semantic Tokens
Status: Draft
Version: 0.2
-->

# Semantic Tokens

---

# Purpose

Primitive Tokens describe physical values.

Semantic Tokens describe **meaning**.

This distinction is the single most important architectural separation within the Mosaic Design System.

If Primitive Tokens answer:

> **"What value exists?"**

Semantic Tokens answer:

> **"Why does this value exist?"**

Applications should think almost exclusively in Semantic Tokens.

Primitive Tokens should rarely appear outside the Design System itself.

---

# Definition

Within MDS, a **Semantic Token** is defined as:

> **A platform-independent design decision expressed in terms of meaning rather than physical implementation.**

Semantic Tokens deliberately avoid describing:

- colour
- spacing
- radius
- typography
- blur

Instead they describe:

- purpose
- responsibility
- role

---

# Why Semantic Tokens Exist

Imagine the following implementation.

```css
.button {
    background: #06b6d4;
}
```

This immediately creates several problems.

- Why cyan?
- Can it change?
- Should every button use it?
- Does another component depend on it?

Now compare.

```text
Action.Primary
```

The implementation becomes:

```
Action.Primary

↓

Primitive.Colour.Cyan.500
```

The reason survives.

The value may evolve.

---

# Semantic Tokens Are Design Decisions

A Semantic Token represents a deliberate design decision.

Examples include:

```
Text.Primary

Surface.Canvas

Action.Primary

Border.Subtle

Status.Success
```

Each communicates:

- purpose
- intention
- responsibility

rather than implementation.

---

# Semantic Categories

The Mosaic Design System currently defines the following semantic categories.

```
Semantic

├── Brand

├── Surface

├── Text

├── Border

├── Icon

├── Action

├── Status

├── Material

├── Atmosphere

├── Elevation

├── Motion

└── Focus
```

Future categories should remain intentionally limited.

Semantic Tokens describe concepts.

Not features.

---

# Brand

Purpose.

Communicate Mosaic identity.

Examples.

```
Brand.Primary

Brand.Secondary

Brand.Accent
```

Brand Tokens should remain stable regardless of:

- artwork
- runtime
- themes

Brand communicates Mosaic.

Not media.

---

# Surface

Purpose.

Describe compositional surfaces.

Examples.

```
Surface.Canvas

Surface.Primary

Surface.Secondary

Surface.Overlay

Surface.Hero
```

Notice that these describe **roles**.

Not colours.

---

# Text

Purpose.

Communicate reading hierarchy.

Examples.

```
Text.Primary

Text.Secondary

Text.Tertiary

Text.Disabled

Text.Inverse
```

Text Tokens describe information hierarchy.

Not typography values.

---

# Border

Purpose.

Communicate separation.

Examples.

```
Border.Subtle

Border.Strong

Border.Focus
```

The implementation may change.

The conceptual role remains stable.

---

# Action

Purpose.

Communicate user intent.

Examples.

```
Action.Primary

Action.Secondary

Action.Destructive

Action.Passive
```

Buttons consume Action Tokens.

The tokens do not belong to buttons.

This significantly improves reuse.

---

# Status

Purpose.

Communicate state.

Examples.

```
Status.Success

Status.Warning

Status.Error

Status.Information
```

Status Tokens intentionally avoid implementation colours.

Accessibility and presentation are resolved later.

---

# Material

Purpose.

Describe the conceptual role of physical materials.

Examples.

```
Material.Canvas

Material.Acrylic

Material.Hero

Material.Overlay
```

Material Tokens intentionally avoid:

- blur values
- opacity
- colours

Those belong to Primitive Tokens.

---

# Atmosphere

Purpose.

Communicate artwork-derived environmental intent.

Examples.

```
Atmosphere.Primary

Atmosphere.Secondary

Atmosphere.Supporting
```

Unlike Brand Tokens...

Atmosphere Tokens are expected to resolve differently at runtime.

---

# Focus

Purpose.

Communicate emphasis.

Examples.

```
Focus.Primary

Focus.Secondary

Focus.Background
```

These Tokens should influence:

- hierarchy
- composition
- emphasis

rather than presentation directly.

---

# Semantic Tokens Never Reference Components

Incorrect.

```
Button.Primary

Card.Background

Sidebar.Border
```

Correct.

```
Action.Primary

Surface.Primary

Border.Subtle
```

Components consume Semantic Tokens.

Semantic Tokens should never know components exist.

---

# Semantic Tokens Consume Primitive Tokens

Example.

```
Semantic.Surface.Primary

↓

Primitive.Colour.Slate.900
```

Future themes may resolve the same Semantic Token differently.

Consumers remain unchanged.

---

# Runtime Independence

Semantic Tokens intentionally remain independent from runtime.

Incorrect.

```
Surface.CurrentArtwork
```

Correct.

```
Surface.Hero

↓

Runtime.Atmosphere.Primary
```

Runtime adapts implementation.

Semantic meaning remains stable.

---

# Naming Convention

Semantic Tokens should follow the same hierarchy.

```
Category

↓

Role

↓

Variant
```

Examples.

```
Text.Primary

Surface.Canvas

Action.Destructive

Status.Warning
```

Naming should always communicate meaning.

Never implementation.

---

# Semantic Stability

Semantic Tokens should change significantly less frequently than Primitive Tokens.

Expected lifetime.

| Layer | Lifetime |
|--------|----------|
| Primitive Values | Years |
| Semantic Meaning | Many Years |

Changing Semantic Tokens potentially affects the conceptual language of the Design System.

Such changes should therefore be rare.

---

# Good Examples

```
Surface.Canvas

↓

Primitive.Colour.Slate.950
```

```
Action.Primary

↓

Primitive.Colour.Cyan.500
```

```
Text.Secondary

↓

Primitive.Colour.Slate.400
```

Meaning remains completely independent from implementation.

---

# Anti-patterns

## Component Semantics

```
Button.Blue
```

Meaning depends upon implementation.

---

## Colour Semantics

```
Blue.Primary
```

Meaning depends upon colour.

---

## Platform Semantics

```
CSS.Primary
```

Architecture becomes implementation dependent.

---

## Runtime Semantics

```
Artwork.Background
```

Runtime concepts belong elsewhere.

---

# Semantic Model

```mermaid
flowchart TD

Primitive
Primitive --> Semantic
Semantic --> Composition
Composition --> Component
Component --> Runtime
Runtime --> Presentation
```

Semantic Tokens introduce meaning.

Everything above them should reason about that meaning.

Everything below them should implement it.

---

# Litmus Test

Contributors should ask:

> **If every Primitive value changed tomorrow, would this token still make sense?**

If the answer is yes...

It probably belongs within the Semantic layer.

If the answer is no...

It probably belongs within Primitive Tokens instead.

---

# Summary

Semantic Tokens represent the language of the Design System.

They intentionally separate:

meaning

from

implementation.

This separation allows Mosaic to:

- evolve themes
- support runtime adaptation
- preserve accessibility
- maintain consistency
- remain implementation independent

Every future MDS specification should consume Semantic Tokens rather than physical values whenever practical.

---

# Review Status

**Status**

Draft

**Next File**

`05-composition-tokens.md`
