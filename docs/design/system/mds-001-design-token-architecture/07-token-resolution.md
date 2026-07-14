<!--
File: docs/design/system/mds-001-design-token-architecture/07-token-resolution.md
Document: MDS-001
Chapter: 07
Title: Token Resolution
Status: Draft
Version: 0.4
-->

# Token Resolution

---

# Purpose

Previous chapters defined the layers of the Design Token Architecture.

This chapter defines **how those layers become usable design values at runtime**.

Token Resolution is responsible for transforming abstract design intent into concrete values without exposing implementation complexity to components.

Components should never ask:

> **"Which colour should I use?"**

Instead they should ask:

> **"Which token represents my responsibility?"**

The Design System resolves everything else.

---

# Definition

Within MDS, **Token Resolution** is defined as:

> **The deterministic process by which an abstract design token is resolved into a platform-specific implementation value.**

Resolution is an implementation process.

The Design Language remains unchanged throughout.

---

# Why Resolution Exists

Consider the following component.

```

Hero Tile
```

Without token resolution, the component would need to understand:

- theme
- artwork
- accessibility
- platform
- device
- colour palette
- contrast
- motion

The component becomes responsible for far too many decisions.

Instead.

```mermaid
flowchart TD

N1["Hero Tile"]
N2["Surface.Hero"]

N1 --> N2
```

Everything else becomes the responsibility of the Design System.

---

# One Direction

Token Resolution always flows in one direction.

```mermaid
flowchart TD

N1["Primitive"]
N2["Semantic"]
N3["Composition"]
N4["Runtime"]
N5["Platform"]
N6["Rendering"]

N1 --> N2
N2 --> N3
N3 --> N4
N4 --> N5
N5 --> N6
```

Tokens should never resolve backwards.

Presentation should never redefine semantic meaning.

---

# Resolution Pipeline

Every token should pass through the same conceptual pipeline.

```mermaid
flowchart TD

Primitive
Primitive --> Semantic
Semantic --> Composition
Composition --> Runtime
Runtime --> Platform
Platform --> Renderer
```

Every layer contributes one responsibility.

No layer duplicates another.

---

# Resolution Inputs

Resolution may evaluate:

- current World
- current Focus
- current Context
- artwork
- accessibility
- user preferences
- device class
- platform theme

Importantly...

These inputs never change the semantic meaning of a token.

They only influence its implementation.

---

# Deterministic Resolution

Given identical inputs...

Resolution should always produce identical outputs.

Example.

```mermaid
flowchart TD

N1["Surface.Hero"]
N2["Current Artwork"]
N3["Dark Theme"]
N4["Desktop"]
N5["Resolved Surface"]

N1 --> N5
N2 --> N5
N3 --> N5
N4 --> N5
```

The same request should always produce the same result.

Deterministic behaviour is essential for:

- predictability
- testing
- caching
- accessibility
- consistency

---

# Resolution Order

The Runtime Resolver should evaluate inputs in a consistent order.

```mermaid
flowchart TD

N1["1.<br/>Primitive Values"]
N2["2.<br/>Semantic Meaning"]
N3["3.<br/>Composition Role"]
N4["4.<br/>Runtime Inputs"]
N5["5.<br/>Accessibility"]
N6["6.<br/>Platform"]
N7["7.<br/>Resolved Value"]

N1 --> N2
N2 --> N3
N3 --> N4
N4 --> N5
N5 --> N6
N6 --> N7
```

Earlier stages establish meaning.

Later stages refine implementation.

---

# Resolution Never Changes Intent

One of the most important architectural guarantees of Mosaic is:

> **Resolution changes implementation.**

> **Resolution never changes meaning.**

Example.

```

Surface.Hero
```

Dark Mode.

↓

Slate Background.

Light Mode.

↓

White Background.

Artwork Mode.

↓

Artwork-derived Acrylic.

The semantic meaning remains:

```

Surface.Hero
```

Meaning survives.

Implementation evolves.

---

# Resolution Context

The Runtime Resolver should understand current context.

Example.

```mermaid
flowchart TD

N1["Playback"]
N2["Surface.Hero"]

N1 --> N2
```

may resolve differently from:

```mermaid
flowchart TD

N1["Browsing"]
N2["Surface.Hero"]

N1 --> N2
```

because runtime atmosphere changes.

The token itself remains identical.

Only resolution differs.

---

# Resolution Priority

Multiple runtime influences may exist simultaneously.

Example.

```

Artwork

Accessibility

Dark Mode

Television
```

The Runtime Resolver should evaluate them using a defined priority.

Recommended conceptual priority.

```mermaid
flowchart TD

N1["Accessibility"]
N2["User Preferences"]
N3["Composition"]
N4["Artwork"]
N5["Device"]
N6["Platform Defaults"]

N1 --> N2
N2 --> N3
N3 --> N4
N4 --> N5
N5 --> N6
```

Accessibility should always take precedence over aesthetics.

---

# Fallback Resolution

Every token must possess a valid fallback.

Poor.

```mermaid
flowchart TD

N1["Artwork Missing"]
N2["Failure"]

N1 --> N2
```

Preferred.

```mermaid
flowchart TD

N1["Artwork Missing"]
N2["Brand Tokens"]
N3["Resolved Value"]

N1 --> N2
N2 --> N3
```

Components should never receive unresolved tokens.

The Design System should always produce a meaningful result.

---

# Lazy Resolution

Resolution should occur only when required.

Example.

```mermaid
flowchart TD

N1["Unused Token"]
N2["Not Resolved"]

N1 --> N2
```

The platform should avoid resolving values that will never be rendered.

This improves runtime efficiency while preserving identical behaviour.

---

# Resolution Cache

Runtime resolution is expected to be cacheable.

Example.

```mermaid
flowchart TD

N1["Current Artwork"]
N2["Atmosphere"]
N3["Resolved Surface"]
N4["Cache"]

N1 --> N2
N2 --> N3
N3 --> N4
```

As long as the runtime inputs remain unchanged, the resolved value should remain stable.

Future Composition Engines may invalidate this cache when:

- Focus changes
- Context changes
- artwork changes
- accessibility changes

---

# Resolution Is Invisible

Components should never know:

- how tokens were resolved
- where values originated
- whether runtime adaptation occurred

Components consume:

```

Resolved Tokens
```

Nothing else.

This dramatically simplifies component implementation.

---

# Good Examples

```mermaid
flowchart TD

N1["Surface.Hero"]
N2["Runtime.Atmosphere"]
N3["Resolved Acrylic Surface"]

N1 --> N2
N2 --> N3
```

```mermaid
flowchart TD

N1["Text.Primary"]
N2["Accessibility"]
N3["Higher Contrast"]

N1 --> N2
N2 --> N3
```

```mermaid
flowchart TD

N1["Spacing.Section"]
N2["Television"]
N3["Expanded Physical Spacing"]

N1 --> N2
N2 --> N3
```

Every example preserves semantic meaning.

Only implementation changes.

---

# Anti-patterns

## Component Resolution

```mermaid
flowchart TD

N1["Component"]
N2["Determine Theme"]
N3["Determine Colours"]

N1 --> N2
N2 --> N3
```

Resolution responsibility has leaked.

---

## Platform Resolution

```mermaid
flowchart TD

N1["Flutter"]
N2["Invent Semantic Meaning"]

N1 --> N2
```

Meaning belongs above implementation.

---

## Runtime Mutation

```mermaid
flowchart TD

N1["Runtime"]
N2["Change Token Identity"]

N1 --> N2
```

Runtime should only resolve.

Never redefine.

---

## Partial Resolution

Components receiving unresolved token chains.

Every rendered value should be fully resolved before presentation.

---

# Resolution Model

```mermaid
flowchart TD

Semantic
Semantic --> Composition
Composition --> Runtime
Runtime --> Resolution
Resolution --> PlatformTheme["Platform Theme"]
PlatformTheme["Platform Theme"] --> Rendering
```

Resolution exists to remove implementation complexity from the rest of the Design System.

---

# Relationship To Future Specifications

Future specifications are expected to define:

- Runtime Resolver
- Theme Resolver
- Atmosphere Generator
- Accessibility Resolver
- Platform Adapters

These systems collectively implement the conceptual process defined by this chapter.

---

# Summary

Token Resolution is the implementation bridge between design intent and rendered interface.

Its responsibility is to ensure that every component receives the correct implementation value while remaining completely unaware of:

- runtime adaptation
- artwork analysis
- accessibility
- platform differences
- device capabilities

The Design System owns complexity.

Components consume clarity.
