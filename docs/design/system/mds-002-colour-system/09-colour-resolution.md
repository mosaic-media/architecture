<!--
File: docs/design/system/mds-002-colour-system/09-colour-resolution.md
Document: MDS-002
Status: Draft
-->

# Colour Resolution

---

# Purpose

Previous chapters established:

- Brand Colours
- Semantic Colours
- Runtime Atmosphere
- Theme Architecture
- Accessibility

This chapter defines how those independent systems become a single resolved colour presented to the user.

Colour Resolution is responsible for translating design intent into implementation while preserving every architectural guarantee established by the Mosaic Design Language.

Components should never determine colours themselves.

They should consume resolved semantic intent.

---

# Definition

Within MDS, **Colour Resolution** is defined as:

> **The deterministic process through which semantic colour intent becomes an accessible, context-aware, platform-specific colour value.**

Colour Resolution never creates meaning.

It only implements meaning.

---

# Why Resolution Exists

Without Colour Resolution every component becomes responsible for answering questions such as:

- Which theme is active?
- Which artwork is visible?
- Is accessibility enabled?
- Which device is being used?
- Which atmosphere should apply?

This creates duplication.

Instead:

```mermaid
flowchart TD

N1["Component"]
N2["Semantic Colour"]
N3["Resolved Colour"]

N1 --> N2
N2 --> N3
```

All complexity remains inside the Colour System.

---

# Resolution Pipeline

Every colour should follow the same conceptual resolution pipeline.

```mermaid
flowchart TD

N1["Primitive Palette"]
N2["Semantic Colour"]
N3["Theme"]
N4["Accessibility"]
N5["Runtime Atmosphere"]
N6["Platform Adaptation"]
N7["Resolved Colour"]

N1 --> N2
N2 --> N3
N3 --> N4
N4 --> N5
N5 --> N6
N6 --> N7
```

Each layer contributes one responsibility.

No layer duplicates another.

---

# Resolution Order

Colour Resolution should always occur in the same order.

```mermaid
flowchart TD

N1["1.<br/>Primitive Colour"]
N2["2.<br/>Semantic Colour"]
N3["3.<br/>Theme"]
N4["4.<br/>Accessibility"]
N5["5.<br/>Runtime Atmosphere"]
N6["6.<br/>Device Adaptation"]
N7["7.<br/>Resolved Output"]

N1 --> N2
N2 --> N3
N3 --> N4
N4 --> N5
N5 --> N6
N6 --> N7
```

Changing this order weakens architectural consistency.

---

# Accessibility First

Accessibility should always possess higher authority than atmosphere.

Incorrect.

```mermaid
flowchart TD

N1["Artwork"]
N2["Low Contrast"]
N3["Unreadable Text"]

N1 --> N2
N2 --> N3
```

Correct.

```mermaid
flowchart TD

N1["Artwork"]
N2["Accessibility Validation"]
N3["Adjusted Atmosphere"]
N4["Readable Interface"]

N1 --> N2
N2 --> N3
N3 --> N4
```

Immersion should never reduce comprehension.

---

# Semantic Stability

One of the most important guarantees of the Colour System is:

```mermaid
flowchart TD

N1["Semantic Meaning"]
N2["Never Changes"]

N1 --> N2
```

Example.

```

Surface.Hero
```

may resolve differently depending upon:

- theme
- artwork
- accessibility
- device

The semantic identity remains identical.

Applications should therefore consume only Semantic Colours.

---

# Runtime Refinement

Runtime Atmosphere refines implementation.

It never replaces semantic meaning.

Example.

```mermaid
flowchart TD

N1["Surface.Hero"]
N2["Dark Theme"]
N3["Artwork Reflection"]
N4["Resolved Hero Surface"]

N1 --> N2
N2 --> N3
N3 --> N4
```

---

# Neutral Acrylic Tint Resolution

Acrylic consumes semantic Tint Intent rather than arbitrary colour, opacity or optical coefficients.

```mermaid
flowchart TD

N1["Tint Intent"]
N2["Surface Role"]
N3["Local Luminance"]
N4["Accessibility"]
N5["Clear, Mist, Smoke Or Deep Smoke"]
N6["Fixed Acrylic Material"]

N1 --> N5
N2 --> N5
N3 --> N5
N4 --> N5
N5 --> N6
```

The selected recipe controls neutral pigmentation and transmission.

It does not supply environmental hue and must not change the fixed Acrylic profile defined by [MDS-003 — Material System](../mds-003-material-system/04-acrylic.md#tint-authority).

Recipe values, luminance thresholds and permitted role mappings remain calibration outputs rather than authored application values.

---

# Adaptive Neutral Foregrounds

Text and icons should resolve from calibrated neutral foreground roles rather than absorbing artwork or Brand Illumination colour.

The resolver should evaluate the local resolved luminance behind each foreground region and select a readable light or dark neutral implementation for the requested semantic role.

Foreground switching must include hysteresis.

After selecting a light or dark implementation, the resolver should retain it until local luminance crosses the opposite threshold plus a governed stability margin.

This prevents scrolling, Composition movement and Focus transitions from causing visible foreground flicker near a single contrast boundary.

Contrast validation retains higher authority than the stability margin.

---

# Functional Colour Isolation

Action, focus and status colours resolve independently from Runtime Atmosphere, Acrylic tint and co-brand illumination.

Mosaic Cyan remains the functional action and focus identity.

Success, warning, error and information remain fixed semantic roles with calibrated implementations.

Each status must also communicate through an icon, label, hierarchy or another non-colour signal.

Atmosphere subtly influences the final result.

It never determines it completely.

---

# Device Adaptation

Different displays possess different characteristics.

Examples include:

- OLED
- LCD
- HDR
- SDR
- eInk
- Projection

Device adaptation should compensate for hardware differences while preserving perceived meaning.

Users should experience one Colour System.

Not device-specific colour languages.

---

# Resolution Is Deterministic

Given identical inputs...

Colour Resolution should always produce identical outputs.

Example.

```mermaid
flowchart TD

N1["Dark Theme"]
N2["Current Artwork"]
N3["TV"]
N4["Reduced Motion Disabled"]
N5["Resolved Colour"]

N1 --> N2
N2 --> N3
N3 --> N4
N4 --> N5
```

Every Mosaic client should produce visually equivalent results.

Determinism improves:

- testing
- caching
- accessibility
- predictability

---

# Resolution Inputs

Conceptually, Colour Resolution evaluates:

```mermaid
flowchart TD

N1["Semantic Colour"]
N2["Theme"]
N3["Accessibility"]
N4["Atmosphere"]
N5["Display Characteristics"]
N6["User Preferences"]

N1 --> N2
N2 --> N3
N3 --> N4
N4 --> N5
N5 --> N6
```

These inputs refine implementation.

They do not alter semantic intent.

---

# Fallback Behaviour

Every Semantic Colour should possess a valid fallback.

Example.

```mermaid
flowchart TD

N1["Artwork Missing"]
N2["Brand Neutrals"]
N3["Resolved Surface"]

N1 --> N2
N2 --> N3
```

Components should never receive unresolved colours.

The system should always produce a meaningful visual result.

---

# Caching

Resolved colours should remain cacheable.

Example.

```mermaid
flowchart TD

N1["Artwork"]
N2["Atmosphere"]
N3["Resolved Palette"]
N4["Cache"]

N1 --> N2
N2 --> N3
N3 --> N4
```

The cache should invalidate only when:

- Focus changes
- artwork changes
- theme changes
- accessibility changes

Ordinary interaction should rarely require recolour resolution.

---

# Lazy Resolution

Colour Resolution should occur only when colours are required.

Unused semantic colours should remain unresolved.

This improves runtime performance while preserving identical architectural behaviour.

---

# Components

Components should consume only resolved Semantic Colours.

Correct.

```mermaid
flowchart TD

N1["Hero Tile"]
N2["Surface.Hero"]

N1 --> N2
```

Incorrect.

```mermaid
flowchart TD

N1["Hero Tile"]
N2["Determine Theme"]
N3["Determine Atmosphere"]
N4["Resolve Colour"]

N1 --> N2
N2 --> N3
N3 --> N4
```

Resolution belongs exclusively to the Colour System.

---

# Modules

Modules should never resolve colours.

Modules consume:

- Semantic Colours
- mapped Platform semantic roles

The platform determines final colour values.

This guarantees future compatibility across:

- themes
- accessibility
- runtime atmosphere

without module modification.

---

# Good Examples

```mermaid
flowchart TD

N1["Surface.Canvas"]
N2["Dark Theme"]
N3["Resolved Neutral Surface"]

N1 --> N2
N2 --> N3
```

```mermaid
flowchart TD

N1["Action.Primary"]
N2["Brand Accent"]
N3["Accessibility"]
N4["Resolved Action Colour"]

N1 --> N2
N2 --> N3
N3 --> N4
```

```mermaid
flowchart TD

N1["Surface.Hero"]
N2["Artwork Reflection"]
N3["Adaptive Acrylic"]

N1 --> N2
N2 --> N3
```

Each example preserves semantic intent.

Only implementation changes.

---

# Anti-patterns

## Component Colour Logic

Every component resolving colours independently.

---

## Artwork Overrides

Artwork replacing Semantic Colours entirely.

---

## Platform Resolution

Flutter, CSS or SwiftUI redefining semantic meaning.

---

## Runtime Mutation

Runtime changing the identity of Semantic Colours.

Runtime refines implementation.

It never changes meaning.

---

# Colour Resolution Model

```mermaid
flowchart TD

Primitive
Primitive --> Semantic
Semantic --> Theme
Theme --> Accessibility
Accessibility --> RuntimeAtmosphere["Runtime Atmosphere"]
RuntimeAtmosphere["Runtime Atmosphere"] --> Platform
Platform --> Presentation
```

Meaning flows downward.

Implementation never flows upward.

---

# Relationship To Future Specifications

Future specifications are expected to define:

- palette blending
- atmosphere interpolation
- HDR colour mapping
- GPU colour pipelines
- platform renderers
- colour cache invalidation

This chapter defines the architectural process.

Future specifications define implementation.

---

# Summary

Colour Resolution is the mechanism through which the Mosaic Colour System becomes visible.

Its responsibility is to preserve:

- semantic meaning
- accessibility
- runtime atmosphere
- brand identity

while producing one coherent visual language across every supported platform.

Components should simply ask:

> **"What does this colour mean?"**

The Colour System answers everything else.
