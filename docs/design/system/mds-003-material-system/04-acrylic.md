<!--
File: docs/design/system/mds-003-material-system/04-acrylic.md
Document: MDS-003
Chapter: 04
Title: Acrylic
Status: Draft
Version: 0.4
-->

# Acrylic

---

# Purpose

Acrylic is the defining material of the Mosaic Design System.

It is the physical medium through which the user's entertainment influences the interface.

Unlike glass, Acrylic should not disappear.

Unlike opaque panels, Acrylic should not isolate itself from its surroundings.

Instead, Acrylic should behave like a premium physical material that:

- possesses depth,
- receives light,
- refracts colour,
- softly diffuses atmosphere,
- remains structurally present.

It is one of the most recognisable characteristics of the Mosaic visual language.

---

# Definition

Within MDS, **Acrylic** is defined as:

> **A semi-translucent material that receives artwork-derived, material-scoped light and transforms it through refraction, absorption and diffusion while preserving hierarchy, readability and physical presence.**

Acrylic is not:

- glass,
- blur,
- transparency,
- opacity,
- frosted panels.

Those are implementation techniques.

Acrylic is a material.

---

# Philosophy

The industry often treats acrylic as:

```

Blur

+

Transparency
```

Mosaic intentionally rejects this.

Instead Acrylic behaves more like a solid object.

Imagine a thick polished acrylic tile placed onto a table.

It possesses:

- edges,
- thickness,
- internal diffusion,
- light transport,
- subtle reflections.

The interface should communicate that same feeling.

The reference Mosaic Acrylic profile behaves conceptually like a polished sheet approximately one centimetre thick.

This thickness is an optical reference for Material behaviour rather than three-dimensional geometry.

Acrylic remains a two-dimensional surface or layered two-dimensional composite positioned within Composition Space.

Implementations may adapt apparent thickness to Composition scale, but they should preserve the diffusion, displacement, edge response and parallax associated with a substantial polished sheet.

---

# Acrylic Is Present

Glass attempts to disappear.

Acrylic should remain visible.

Not because it is visually loud...

but because it physically exists.

Users should perceive:

- depth,
- volume,
- softness,

rather than simply:

- blur.

This distinction creates a much more premium material language.

---

# Acrylic Responsibilities

Acrylic performs five primary responsibilities.

---

## 1. Receive Artwork Light

Acrylic receives a material-scoped light field derived from the current artwork.

The artwork remains visually ordinary within Presentation.

The artwork field is global within the Acrylic transport environment.

Only Acrylic consumes it, but Acrylic may pass transformed light onward to other Acrylic.

---

## 2. Transport Light

Light should appear to travel through Acrylic.

This behaviour is formalised later through the Refraction System.

---

## 3. Preserve Hierarchy

Despite receiving atmospheric colour, Acrylic must remain structurally readable.

Hierarchy always takes precedence over visual richness.

---

## 4. Create Depth

Acrylic communicates physical layering.

It should feel thicker than ordinary interface panels.

---

## 5. Support Continuity

Atmosphere should move naturally through Acrylic during interaction.

Nothing should appear to flash or abruptly recolour.

---

# Acrylic Is Not Transparent

Transparency implies seeing through a material.

Acrylic implies seeing **within** a material.

This distinction is important.

Poor.

```mermaid
flowchart TD

N1["Transparent Blur"]
N2["Background Visible"]

N1 --> N2
```

Preferred.

```mermaid
flowchart TD

N1["Light Enters"]
N2["Diffusion"]
N3["Refraction"]
N4["Soft Reflection"]
N5["Material"]

N1 --> N2
N2 --> N3
N3 --> N4
N4 --> N5
```

The material becomes believable rather than decorative.

Acrylic may distort and diffuse visible Presentation behind its bounds while independently receiving hidden artwork-derived light.

Backdrop participation communicates local translucency.

Artwork-derived light communicates shared pigmentation, glare and edge response.

---

# Runtime Atmosphere

Artwork provides the spatially distributed light source.

Runtime Atmosphere constrains how strongly that source may influence Acrylic within the current World.

Acrylic determines how the constrained light behaves.

Conceptually.

```mermaid
flowchart TD

N1["Artwork"]
N2["Material-Scoped Light Field"]
N3["Runtime Atmosphere Constraints"]
N4["Acrylic"]
N5["Refraction"]
N6["Presentation"]

N1 --> N2
N2 --> N3
N3 --> N4
N4 --> N5
N5 --> N6
```

Acrylic should therefore be considered both a receiver and a secondary transport contributor.

It may redirect existing artwork-derived energy toward other Acrylic, but it must never create additional light energy.

---

# Acrylic-To-Acrylic Transport

Acrylic objects should influence one another when their relative position, orientation, surface bounds, mask and z-order within the three-dimensional Composition permit light transport between them.

```mermaid
flowchart TD

N1["Artwork Primary Source"]
N2["Acrylic A"]
N3["Acrylic B"]
N4["Acrylic C"]

N1 --> N2
N1 --> N3
N2 --> N3
N2 --> N4
N3 --> N4
```

Each interaction may refract, absorb, diffuse or redirect the remaining energy.

Successive responses should become weaker and softer rather than accumulating without limit.

---

# Diffusion

Incoming atmosphere should diffuse naturally.

Examples.

Strong artwork colours.

↓

Soft internal glow.

↓

Neutral readable surface.

The material should smooth environmental changes.

Not amplify them.

---

# Refraction

Unlike ordinary translucent materials...

Acrylic should refract light.

Refraction should create:

- gentle colour movement,
- perceived depth,
- environmental richness.

It should never distort:

- typography,
- interaction,
- hierarchy.

Understanding remains more important than spectacle.

---

# Internal Depth

Acrylic should possess perceived thickness.

Future implementations may communicate this through:

- layered diffusion,
- internal highlights,
- edge lighting,
- soft gradients.

Thickness should be perceived consistently with the reference Acrylic profile rather than exposed as a component-level styling value.

Acrylic does not require an extruded shape, mesh or volumetric scene representation to communicate this depth.

---

# Acrylic Parallax

Acrylic should preserve the feeling that its internal response occupies a different optical depth from its outer surface.

It communicates this through two related behaviours.

| Behaviour | Responsibility |
|-----------|----------------|
| Composition parallax | Moves the complete two-dimensional Acrylic surface according to its Composition depth as the projected viewpoint or Focus relationship changes. |
| Internal optical parallax | Shifts sampled artwork, backdrop, diffusion and glare layers within the fixed Acrylic mask by a smaller bounded amount. |

The apparent-thickness profile constrains internal optical displacement.

The one-centimetre reference establishes the intended perceptual character rather than a universal runtime coefficient.

The governed Acrylic Material profile should define the numerical relationship between apparent thickness, diffusion, displacement and safe sampling margins when that profile is standardised.

Renderers should consume that profile rather than independently hard-code thickness or refractive-index values.

The outer surface, interaction bounds and semantic layout remain stable while internal composite layers move relative to them.

Edge glare may move at a different or opposing rate to strengthen the impression of a polished physical surface.

Parallax must remain restrained, must not distort readable content and must respect accessibility constraints on motion.

It responds to Composition movement, scrolling and Focus transitions rather than pointer, gyroscope or device-tilt input.

---

# Edge Behaviour

Edges define Acrylic.

They communicate:

- structure,
- precision,
- craftsmanship.

Edges should respond more strongly when artwork-derived light exits through an Acrylic boundary than central surfaces.

This creates the feeling that light is travelling through the material rather than simply colouring it.

The artwork itself must not acquire a visible glow, bloom or emission effect.

Visible edge light belongs to Acrylic because Acrylic redirected the hidden incident light.

---

# Hero Acrylic

Hero Materials receive the strongest Acrylic treatment.

Examples include:

- stronger refraction,
- richer environmental light,
- greater perceived thickness.

Importantly...

The Hero should still remain secondary to the entertainment artwork itself.

Artwork remains the emotional centre.

---

# Supporting Acrylic

Supporting materials should receive noticeably less atmospheric influence.

Examples include:

- timeline,
- progress,
- shelves,
- navigation.

Supporting Acrylic should feel related to the Hero without competing with it.

---

# Overlay Acrylic

Overlay Acrylic prioritises readability.

Atmospheric influence should reduce significantly.

Interaction takes precedence over immersion.

Dialogs.

Menus.

Playback controls.

All require stronger separation from the environment.

---

# Movement

Acrylic should respond naturally during interaction.

Changing Focus.

↓

Atmosphere gradually redistributes.

Moving Hero.

↓

Refraction subtly shifts.

Playback begins.

↓

Acrylic influence reduces.

Materials should appear physically consistent throughout every interaction.

---

# Themes

Light Theme.

Acrylic appears:

- brighter,
- softer,
- more diffused.

Dark Theme.

Acrylic appears:

- deeper,
- richer,
- more luminous.

Both remain recognisably the same material.

Only environmental lighting changes.

---

# Accessibility

Accessibility should always constrain Acrylic.

If diffusion or refraction would reduce:

- readability,
- contrast,
- orientation,

their intensity should reduce automatically.

Acrylic exists to enrich understanding.

Not complicate it.

---

# Performance

Future implementations should optimise Acrylic aggressively.

Preferred techniques include:

- cached artwork fields,
- GPU acceleration,
- incremental updates,
- shared material layers.

The client renderer should adapt Acrylic fidelity to measured capability and available presentation budget.

During video playback, Acrylic updates must yield before they delay video presentation.

Users should experience premium materials without perceiving computational cost.

---

# Modules

Modules never define Acrylic.

Modules contribute:

- Information,
- Artwork,
- Relationships.

The Material System determines how Acrylic behaves.

This guarantees every module inherits the same physical language.

---

# Good Examples

## Hero

Poster softly illuminates Acrylic.

Edges gently glow.

Typography remains perfectly readable.

The material feels physically present.

---

## Continue Watching

Timeline receives subtle atmospheric diffusion.

Hero remains dominant.

Nothing feels disconnected.

---

## Playback

Controls float using restrained Acrylic.

Video remains visually dominant.

Interaction feels calm.

---

# Anti-patterns

## Frosted Glass

Heavy blur becomes the defining characteristic.

Material identity disappears.

---

## Fully Transparent Panels

Background dominates foreground.

Depth weakens.

---

## Plastic Shine

Strong specular highlights unrelated to Runtime Atmosphere.

The material feels artificial.

---

## Decorative Refraction

Colour movement exists purely because it looks impressive.

No additional understanding is communicated.

---

# Acrylic Model

```mermaid
flowchart TD

Artwork["Artwork"]
LightField["Material-Scoped Light Field"]
Atmosphere["Runtime Atmosphere Constraints"]
AcrylicA["Acrylic A"]
AcrylicB["Acrylic B"]
SecondaryTransport["Secondary Transport"]
Refraction
Diffusion
EdgeEmission["Edge Emission"]
Presentation

Artwork --> LightField
LightField --> Atmosphere
Atmosphere --> AcrylicA
Atmosphere --> AcrylicB
AcrylicA --> SecondaryTransport
SecondaryTransport --> AcrylicB
AcrylicA --> Refraction
AcrylicB --> Refraction
Refraction --> Diffusion
Diffusion --> EdgeEmission
EdgeEmission --> Presentation
```

Acrylic transforms hidden artwork-derived light into believable physical presence.

---

# Relationship To Future Chapters

The following chapters expand Acrylic into increasingly sophisticated physical behaviour.

Including:

- Hero Material
- Overlay Material
- Refraction
- UV-Indexed Refraction
- Light Transport
- Runtime Material Resolution

These systems all build upon the Acrylic behaviour established here.

---

# Summary

Acrylic is the defining material of Mosaic.

It should feel:

- substantial,
- refined,
- illuminated,
- calm.

It is not glass.

It is not blur.

It is the physical medium through which entertainment quietly reaches into the interface.

When successful, Acrylic should make the interface feel handcrafted rather than rendered.
