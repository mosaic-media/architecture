<!--
File: docs/design/system/mds-001-design-token-architecture/08-token-inheritance.md
Document: MDS-001
Chapter: 08
Title: Token Inheritance
Status: Draft
Version: 0.4
-->

# Token Inheritance

---

# Purpose

One of the primary responsibilities of the Mosaic Design Token Architecture is allowing design decisions to evolve without requiring widespread implementation changes.

Token Inheritance provides this capability.

Instead of every component defining its own values, components inherit increasingly specialised design intent from higher layers of the architecture.

Inheritance therefore allows the Design System to express:

- consistency
- adaptability
- maintainability

through one coherent hierarchy.

---

# Definition

Within MDS, **Token Inheritance** is defined as:

> **The process by which a token derives its meaning or implementation from another token while preserving a single responsibility at each layer.**

Inheritance exists to preserve meaning.

Not duplicate values.

---

# Why Inheritance Exists

Without inheritance, every component becomes responsible for resolving its own appearance.

Example.

```mermaid
flowchart TD

N1["Hero Tile"]
N2["Colour"]
N3["Spacing"]
N4["Radius"]
N5["Blur"]
N6["Elevation"]

N1 --> N2
N2 --> N3
N3 --> N4
N4 --> N5
N5 --> N6
```

Every component repeats identical decisions.

Instead.

```mermaid
flowchart TD

N1["Hero Tile"]
N2["Composition.Hero"]
N3["Surface.Hero"]
N4["Primitive Values"]

N1 --> N2
N2 --> N3
N3 --> N4
```

Responsibility becomes centralised.

Consistency naturally follows.

---

# Inheritance Hierarchy

Inheritance always follows the same architectural direction.

```mermaid
flowchart TD

N1["Primitive"]
N2["Semantic"]
N3["Composition"]
N4["Component"]
N5["Runtime"]
N6["Platform"]

N1 --> N2
N2 --> N3
N3 --> N4
N4 --> N5
N5 --> N6
```

No layer should inherit directly from a lower layer.

Each layer inherits only the responsibilities it requires.

---

# Primitive Inheritance

Primitive Tokens do not inherit.

They represent the physical foundation of the Design System.

Example.

```

Primitive.Space.16
```

This value is absolute.

Primitive Tokens terminate the inheritance chain.

---

# Semantic Inheritance

Semantic Tokens inherit physical implementation.

Example.

```mermaid
flowchart TD

N1["Surface.Primary"]
N2["Primitive.Colour.Slate.950"]

N1 --> N2
```

The Semantic Token gains:

- colour
- contrast
- physical implementation

while preserving semantic meaning.

---

# Composition Inheritance

Composition Tokens inherit semantic meaning.

Example.

```mermaid
flowchart TD

N1["Composition.Hero"]
N2["Surface.Hero"]
N3["Text.Primary"]
N4["Elevation.Primary"]

N1 --> N2
N2 --> N3
N3 --> N4
```

Composition therefore combines multiple semantic concepts into one compositional role.

Importantly...

It still does not know anything about components.

---

# Component Inheritance

Components inherit compositional responsibilities.

Example.

```mermaid
flowchart TD

N1["Hero Tile"]
N2["Composition.Hero"]
N3["Semantic.Surface.Hero"]
N4["Primitive Values"]

N1 --> N2
N2 --> N3
N3 --> N4
```

The component consumes design intent.

It does not create it.

---

# Runtime Inheritance

Runtime Tokens inherit the complete conceptual chain.

Example.

```mermaid
flowchart TD

N1["Runtime.Atmosphere.Primary"]
N2["Composition.Hero"]
N3["Surface.Hero"]
N4["Primitive Colour"]

N1 --> N2
N2 --> N3
N3 --> N4
```

Runtime then resolves implementation according to:

- artwork
- accessibility
- device
- user preferences

Meaning remains unchanged.

---

# Platform Inheritance

Platform implementations inherit fully resolved Runtime Tokens.

Examples include:

- CSS Variables
- Flutter Theme
- SwiftUI Environment
- Compose Theme

Platform code should never reconstruct inheritance.

It should consume the completed result.

---

# Multiple Inheritance

A token may inherit from multiple parent tokens.

Example.

```mermaid
flowchart TD

N1["Composition.Hero"]
N2["Surface.Hero"]
N3["Text.Primary"]
N4["Elevation.Primary"]
N5["Spacing.Section"]

N1 --> N2
N2 --> N3
N3 --> N4
N4 --> N5
```

The resulting role communicates:

- hierarchy
- material
- typography
- rhythm

without duplicating implementation.

Multiple inheritance should remain intentional and predictable.

---

# Override Rules

Inheritance should support controlled overrides.

Permitted.

```mermaid
flowchart TD

N1["Runtime"]
N2["Accessibility Override"]

N1 --> N2
```

Not permitted.

```mermaid
flowchart TD

N1["Component"]
N2["Primitive Override"]

N1 --> N2
```

Bypassing semantic layers weakens the architecture.

Overrides should occur as high in the hierarchy as practical.

---

# Local Overrides

Occasionally local overrides are necessary.

These should remain exceptional.

Before introducing an override ask:

1. Can an existing Semantic Token solve this?
2. Can Composition solve this?
3. Is Runtime the correct place?
4. Is a new token required?

Overrides should be the exception.

Not the default workflow.

---

# Inheritance And Themes

Themes should never redefine semantic meaning.

Instead.

```mermaid
flowchart TD

N1["Surface.Primary"]
N2["Dark Theme"]
N3["Slate 950"]

N1 --> N2
N2 --> N3
```

```mermaid
flowchart TD

N1["Surface.Primary"]
N2["Light Theme"]
N3["Slate 50"]

N1 --> N2
N2 --> N3
```

The consuming component remains identical.

Only implementation changes.

---

# Inheritance And Modules

Modules should inherit the complete Design System.

Modules should consume:

- Semantic Tokens
- Composition Tokens

They should never redefine:

- Primitive values
- Runtime resolution
- Platform implementation

This guarantees ecosystem consistency.

---

# Good Examples

```mermaid
flowchart TD

N1["Button"]
N2["Action.Primary"]
N3["Primitive Colour"]

N1 --> N2
N2 --> N3
```

```mermaid
flowchart TD

N1["Hero Tile"]
N2["Composition.Hero"]
N3["Surface.Hero"]
N4["Primitive Values"]

N1 --> N2
N2 --> N3
N3 --> N4
```

```mermaid
flowchart TD

N1["Timeline"]
N2["Composition.Supporting"]
N3["Surface.Secondary"]
N4["Primitive Values"]

N1 --> N2
N2 --> N3
N3 --> N4
```

Meaning accumulates.

Implementation remains centralised.

---

# Anti-patterns

## Primitive Consumption

```mermaid
flowchart TD

N1["Component"]
N2["Primitive"]

N1 --> N2
```

Semantic meaning has been bypassed.

---

## Circular Inheritance

```mermaid
flowchart TD

N1["Semantic"]
N2["Component"]
N3["Semantic"]

N1 --> N2
N2 --> N3
```

Inheritance should always remain directional.

---

## Component Overrides

Components redefining inherited values locally.

Consistency weakens.

---

## Runtime Mutation

Runtime changing semantic identity.

Runtime resolves implementation.

It never changes meaning.

---

# Inheritance Model

```mermaid
flowchart TD

Primitive
Primitive --> Semantic
Semantic --> Composition
Composition --> Component
Component --> Runtime
Runtime --> Platform
Platform --> Rendering
```

Every layer contributes additional understanding.

No layer duplicates responsibilities owned elsewhere.

---

# Relationship To Future Specifications

Future specifications should inherit from this architecture.

Examples include:

- Colour System
- Material System
- Typography
- Motion
- Component Library

None of these specifications should redefine inheritance.

They should extend it.

---

# Litmus Test

Contributors should ask:

> **Can this change be made higher in the hierarchy?**

If the answer is yes...

The change should almost always occur there.

Higher-level inheritance generally produces:

- fewer overrides
- stronger consistency
- easier maintenance

---

# Summary

Token Inheritance allows Mosaic to express one coherent Design System across:

- multiple devices
- multiple themes
- runtime adaptation
- accessibility
- future implementations

Every layer inherits meaning from the layer above it while adding exactly one new responsibility.

This deliberate separation is what allows the Design System to evolve without losing conceptual integrity.
