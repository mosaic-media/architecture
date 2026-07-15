<!--
File: docs/design/system/mds-002-colour-system/04-runtime-atmosphere.md
Document: MDS-002
Chapter: 04
Title: Runtime Atmosphere
Status: Draft
Version: 0.4
-->

# Runtime Atmosphere

---

# Purpose

Runtime Atmosphere is one of the defining characteristics of the Mosaic Design System.

It is the mechanism through which the interface quietly reflects the emotional tone of the user's current entertainment without surrendering its own identity.

Unlike themes, which are selected by users...

or branding, which remains constant...

Runtime Atmosphere continuously adapts.

Its purpose is not to decorate the interface.

Its purpose is to increase immersion.

---

# Definition

Within MDS, **Runtime Atmosphere** is defined as:

> **The adaptive environmental colour system generated from the user's current World and applied subtly throughout the interface.**

Atmosphere exists to create emotional continuity between:

- artwork
- content
- interface

while preserving:

- accessibility
- semantic meaning
- brand identity

---

# Why Runtime Atmosphere Exists

Entertainment already possesses atmosphere.

Examples include:

- album artwork
- anime key visuals
- film posters
- book covers
- promotional art

Traditional applications typically ignore this.

Every title appears inside the same interface.

Mosaic intentionally embraces the emotional identity already present in media.

Instead of recolouring the interface...

It reflects the media.

---

# Reflection

Runtime Atmosphere should be thought of as **reflection** rather than **replacement**.

Incorrect.

```mermaid
flowchart TD

N1["Artwork"]
N2["Entire Interface"]
N3["Artwork Colours"]

N1 --> N2
N2 --> N3
```

Correct.

```mermaid
flowchart TD

N1["Artwork"]
N2["Atmosphere"]
N3["Subtle Reflection"]
N4["Interface"]

N1 --> N2
N2 --> N3
N3 --> N4
```

The interface should feel illuminated by the artwork.

Not painted with it.

This distinction is fundamental.

---

# Atmosphere Is Environmental

Atmosphere belongs to the environment.

Not individual components.

Example.

Poor.

```mermaid
flowchart TD

N1["Button"]
N2["Artwork Colour"]

N1 --> N2
```

Preferred.

```mermaid
flowchart TD

N1["Environment"]
N2["Artwork Reflection"]
N3["Components Inherit Atmosphere"]

N1 --> N2
N2 --> N3
```

Components should remain semantically stable.

Atmosphere surrounds them.

---

# Inputs

Runtime Atmosphere may evaluate:

```mermaid
flowchart TD

N1["Current Focus"]
N2["Current Artwork"]
N3["Dominant Palette"]
N4["Luminance"]
N5["Contrast"]
N6["Theme"]
N7["Accessibility"]

N1 --> N2
N2 --> N3
N3 --> N4
N4 --> N5
N5 --> N6
N6 --> N7
```

These inputs collectively determine the environmental atmosphere.

No single input possesses authority.

---

# Outputs

Runtime Atmosphere produces conceptual outputs.

Examples include:

```

Atmosphere.Primary

Atmosphere.Secondary

Atmosphere.Highlight

Atmosphere.Glow

Atmosphere.Reflection
```

Future Material specifications determine how these outputs become visible.

---

# Atmosphere Is Contextual

The same artwork may produce different Atmospheres depending upon Context.

Example.

Browsing.

```mermaid
flowchart TD

N1["Artwork"]
N2["Subtle Reflection"]

N1 --> N2
```

Playback.

```mermaid
flowchart TD

N1["Artwork"]
N2["Reduced Reflection"]

N1 --> N2
```

Reading.

```mermaid
flowchart TD

N1["Artwork"]
N2["Soft Reflection"]

N1 --> N2
```

The artwork remains identical.

The user's activity changes.

Atmosphere should respect that activity.

---

# Atmosphere Never Becomes Brand

Brand and Atmosphere intentionally remain separate.

Example.

```mermaid
flowchart TD

N1["Brand"]
N2["Stable Identity"]

N1 --> N2
```

```mermaid
flowchart TD

N1["Atmosphere"]
N2["Adaptive Emotion"]

N1 --> N2
```

Artwork should never redefine:

- Brand.Primary
- Brand.Secondary
- Brand.Accent

Those tokens belong exclusively to Mosaic.

Atmosphere enhances.

Brand identifies.

---

# Atmosphere Should Be Peripheral

Users should rarely consciously notice Runtime Atmosphere.

Instead they should simply feel:

- warmer
- calmer
- brighter
- darker
- more immersive

Atmosphere should exist primarily within peripheral vision.

The entertainment remains the emotional centre.

---

# Adaptive Intensity

Atmosphere intensity should vary according to Context.

Examples.

```mermaid
flowchart TD

N1["Playback"]
N2["Low Intensity"]

N1 --> N2
```

```mermaid
flowchart TD

N1["Browsing"]
N2["Medium Intensity"]

N1 --> N2
```

```mermaid
flowchart TD

N1["Hero"]
N2["Highest Intensity"]

N1 --> N2
```

Atmosphere should never reduce readability.

Understanding always possesses higher priority than immersion.

---

# Atmosphere Regions

Future implementations may divide Atmosphere into conceptual regions.

```mermaid
flowchart TD

N1["Hero"]
N2["Primary Reflection<br/>Canvas"]
N3["Supporting Reflection<br/>Navigation"]
N4["Minimal Reflection<br/>Overlay"]
N5["Neutral"]

N1 --> N2
N2 --> N3
N3 --> N4
N4 --> N5
```

This regional approach prevents atmosphere from overwhelming the interface.

---

# Atmosphere And Materials

Atmosphere should normally appear through Materials.

Examples include:

- acrylic
- translucency
- glow
- subtle gradients
- reflected highlights

Flat colour replacement should generally be avoided.

Atmosphere should feel like light interacting with materials.

Not paint replacing them.

This directly supports the Refraction System defined elsewhere within Mosaic.

---

# Atmosphere And Refraction

The Runtime Atmosphere becomes one of the primary inputs into the Mosaic Refraction System.

Conceptually.

```mermaid
flowchart TD

N1["Artwork"]
N2["Colour Extraction"]
N3["Runtime Atmosphere"]
N4["Material Refraction"]
N5["Rendered Surface"]

N1 --> N2
N2 --> N3
N3 --> N4
N4 --> N5
```

Notice that artwork never directly colours interface elements.

Instead it influences how light appears to travel through the interface.

This distinction gives Mosaic a recognisable visual identity that remains independent of any particular artwork.

---

# Atmosphere Persistence

Atmosphere should evolve gradually.

Poor.

```mermaid
flowchart TD

N1["Artwork Changes"]
N2["Entire Interface Changes"]

N1 --> N2
```

Preferred.

```mermaid
flowchart TD

N1["Artwork Changes"]
N2["Atmosphere Blends"]
N3["Materials Adapt"]
N4["Composition Continues"]

N1 --> N2
N2 --> N3
N3 --> N4
```

Users should experience atmosphere as environmental change.

Not theme switching.

---

# No-Artwork Atmosphere

When focused and Hero artwork are both unavailable, Runtime Atmosphere should derive from the approved static Mosaic pair or deterministically resolved co-brand pair.

If that pair is missing or invalid, the default Mosaic illumination pair becomes authoritative.

The static source preserves environmental colour continuity without pretending that administrative, settings or dashboard content contains artwork.

---

# Accessibility

Runtime Atmosphere must never reduce accessibility.

Accessibility always overrides atmosphere.

If an atmosphere would reduce:

- contrast
- readability
- recognisability

its intensity should reduce automatically.

Accessibility is considered a higher-order design constraint.

---

# Performance

Atmosphere should be computationally inexpensive.

Future implementations should:

- cache extracted palettes
- reuse generated atmosphere
- update only when Focus changes
- avoid recomputation during ordinary interaction

Atmosphere should never noticeably impact interaction performance.

Immersion should not come at the expense of responsiveness.

---

# Good Examples

## Hero Artwork

Artwork subtly illuminates surrounding acrylic surfaces.

Brand remains unchanged.

Typography remains readable.

Atmosphere feels natural.

---

## Dark Science Fiction

Cool blue reflections appear within Hero materials.

The rest of the interface remains restrained.

The experience feels cohesive.

---

## Warm Fantasy Novel

Soft amber reflections appear behind the Hero.

Supporting surfaces remain largely neutral.

Attention remains on the book cover.

---

# Anti-patterns

## Full Recolour

Every interface element adopts artwork colours.

Brand identity disappears.

---

## Saturated UI

Atmosphere becomes more visually interesting than the entertainment itself.

The interface now competes with content.

---

## Instant Theme Switching

Artwork changes produce abrupt colour changes.

Continuity is lost.

---

## Accessibility Compromise

Atmosphere reduces readability.

Immersion should never weaken usability.

---

# Atmosphere Model

```mermaid
flowchart TD

Artwork
Artwork --> PaletteExtraction["Palette Extraction"]
PaletteExtraction["Palette Extraction"] --> RuntimeAtmosphere["Runtime Atmosphere"]
RuntimeAtmosphere["Runtime Atmosphere"] --> MaterialSystem["Material System"]
MaterialSystem["Material System"] --> Presentation
Presentation
Presentation --> Immersion
```

Atmosphere exists between artwork and materials.

It does not bypass the Material System.

---

# Relationship To Future Specifications

Future specifications will formalise:

- palette extraction
- UV refraction
- acrylic rendering
- glow synthesis
- adaptive blending
- material shaders

MDS-002 defines only the conceptual role of Runtime Atmosphere.

Future MDS specifications define how it is implemented.

---

# Summary

Runtime Atmosphere is one of the defining innovations of the Mosaic Design System.

Rather than colouring the interface...

It allows the user's entertainment to illuminate it.

Brand remains stable.

Meaning remains stable.

Accessibility remains stable.

Only the atmosphere evolves.

When successful, users should feel that the interface belongs to their current entertainment without ever feeling that it has stopped being unmistakably Mosaic.
