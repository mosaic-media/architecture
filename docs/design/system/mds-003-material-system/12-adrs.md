<!--
File: docs/design/system/mds-003-material-system/12-adrs.md
Document: MDS-003
Status: Draft
-->

# Architectural Decision Records

---

# Purpose

The Architectural Decision Records (ADRs) contained within MDS-003 preserve the reasoning behind the Mosaic Material System.

Where previous specifications established:

- Design Tokens
- Colour
- Runtime Atmosphere

this specification establishes the physical language through which those systems become a believable environment.

These ADRs explain why Mosaic deliberately models materials as physical behaviours rather than decorative effects.

Future contributors should consult these records before proposing changes to the Material System.

---

# Decision Format

Decision format, lifecycle and review expectations are governed by **[MDG-001 — Documentation Authority Guide](../../../engineering/documentation/mdg-001-documentation-authority-guide/index.md)**.

This chapter records decisions specific to this specification and avoids redefining the shared ADR process.

# ADR-111

## Title

Treat Materials As Physical Behaviours

### Status

Accepted

### Context

Most UI frameworks model materials as visual styles.

Founder workshops consistently described the desired experience as physical rather than decorative.

### Decision

Materials become behavioural objects.

Rendering becomes their implementation.

### Consequences

Future rendering technologies may evolve without changing the perceived physical language of Mosaic.

---

# ADR-112

## Title

Adopt Acrylic As The Primary Interactive Material

### Status

Accepted

### Context

Glass interfaces frequently disappear into the background while opaque panels isolate themselves from surrounding content.

Neither behaviour aligned with the desired Mosaic experience.

### Decision

Premium Acrylic becomes the primary interactive material.

### Consequences

The interface gains:

- presence
- depth
- environmental lighting
- restrained translucency

without competing with entertainment.

---

# ADR-113

## Title

Treat Artwork As Environmental Light

### Status

Accepted

### Context

Direct artwork recolouring weakens hierarchy and brand identity.

Visible artwork glow would turn a material relationship into a scene-wide lighting effect.

### Decision

Artwork becomes a spatially distributed, material-scoped light source rather than a colour palette.

The source is available only to Acrylic transport and remains independent from the ordinary visible presentation of the artwork.

### Consequences

Runtime Atmosphere constrains the artwork-derived field rather than directly colouring components.

Visible illumination appears within Acrylic without making the artwork glow or illuminate the wider Composition.

---

# ADR-114

## Title

Introduce UV-Indexed Refraction

### Status

Accepted

### Context

Screen-space atmospheric effects become inconsistent across devices and layouts.

The Composition itself is three-dimensional even though artwork is naturally parameterised using two-dimensional UV coordinates.

### Decision

Artwork-derived relative radiance is represented in normalised artwork UV space.

The artwork world transform projects that emitter surface into the three-dimensional Composition, where Acrylic samples it according to spatial relationship.

### Consequences

The source field becomes:

- device independent
- reusable across Compositions
- runtime efficient

while preserving one coherent Acrylic lighting model.

---

# ADR-115

## Title

Separate Refraction From Colour

### Status

Accepted

### Context

Many rendering systems treat refraction as colour overlays or decorative bloom.

### Decision

Refraction becomes light transport rather than colour replacement.

### Consequences

Materials appear physically illuminated rather than digitally tinted.

---

# ADR-116

## Title

Material Resolution Owns Rendering Decisions

### Status

Accepted

### Context

Allowing components to construct their own material behaviour fragments the Material System.

### Decision

Components request Material Identity.

The Runtime Material Resolver determines implementation.

### Consequences

Applications remain simple while rendering technology evolves independently.

---

# ADR-117

## Title

Accessibility Overrides Material Fidelity

### Status

Accepted

### Context

Highly expressive material systems frequently reduce readability.

### Decision

Accessibility possesses higher authority than physical realism.

### Consequences

Material richness automatically adapts whenever readability would otherwise decrease.

---

# ADR-118

## Title

Maintain One Global Acrylic Transport Environment

### Status

Amended by ADR-127

### Context

Per-component lighting and independently resolved Acrylic create inconsistent physical behaviour.

### Decision

One active Material-light source governs one shared Acrylic transport environment.

Artwork remains preferred; ADR-127 defines the governed static source used when artwork is absent.

Spatially related Acrylic resolves direct source transport and secondary Acrylic-to-Acrylic transport as one coupled system.

Canvas, Surface, typography, icons and components do not sample that field.

### Consequences

Acrylic behaves as one coherent physical family rather than a collection of unrelated effects or independent source samples.

Other materials remain free to respond to Runtime Atmosphere through their own governed behaviours.

---

# ADR-119

## Title

Modules Inherit The Material System

### Status

Accepted

### Context

Allowing modules to implement independent materials fragments product identity.

### Decision

Modules contribute:

- artwork
- information
- relationships

The platform owns every material behaviour.

### Consequences

Community modules automatically inherit future material improvements.

---

# ADR-120

## Title

Bound Acrylic-To-Acrylic Light Transport

### Status

Accepted

### Context

Acrylic objects occupying the same three-dimensional Composition should influence one another when light can travel between them.

Unbounded transport would amplify or recirculate energy and could become computationally or visually unstable.

### Decision

Acrylic may redirect artwork-derived light toward other Acrylic according to relative position, distance, orientation, surface bounds, masks and visibility.

Projected overlap is not required when two Acrylic surfaces remain within a bounded projected-distance radius and possess a visible transport path.

Opaque Composition surfaces occlude the hidden transport field according to bounds, masks and z-order.

Every interaction preserves or reduces the remaining energy, and further transport terminates when its contribution becomes negligible.

### Consequences

Neighbouring Acrylic gains a coherent knock-on response without becoming an independent light source.

Implementations may approximate termination through transport-depth limits, energy thresholds or equivalent bounded strategies.

---

# ADR-121

## Title

Resolve Material Quality From Measured Client Capability

### Status

Accepted

### Context

Mosaic clients include browsers and native renderers with widely varying capabilities and performance characteristics.

Device categories do not predict rendering performance reliably, and feature availability does not prove that a technique is affordable.

Runtime SDUI communicates semantic intent rather than native rendering instructions.

### Decision

Each client renderer discovers available capabilities, calibrates their measured cost and continuously adapts Material quality to the current presentation budget.

Quality varies across independent dimensions rather than fixed device tiers.

The client renderer owns this resolution without requiring device-specific Runtime SDUI.

### Consequences

Different renderers may use different techniques while preserving the same Material invariants.

Secondary transport and negligible detail reduce before direct artwork-to-Acrylic coherence.

Quality reduces quickly under pressure and recovers gradually after sustained headroom.

---

# ADR-122

## Title

Protect Video Presentation From Refraction Work

### Status

Accepted

### Context

Video decode, composition and Refraction may compete for shared CPU, GPU and memory resources.

Asynchronous execution alone cannot guarantee that Refraction will not delay video presentation.

### Decision

The Refraction Engine must never cause a video presentation deadline to be missed.

Video decode and presentation possess higher priority than every Refraction operation.

When insufficient safe budget remains, the renderer skips or defers Material work and reuses the last stable Material state.

### Consequences

Material updates, secondary transport and edge refinement are disposable under playback pressure.

Video presentation never waits for light-field generation, cache access, transport updates or quality recovery.

The guarantee applies to frame drops attributable to Refraction rather than independent decoding, delivery or operating-environment failures.

---

# ADR-123

## Title

Standardise UVLightFrame As The Artwork-Light Exchange Unit

### Status

Accepted

### Context

Static artwork and video require one compatible representation of their primary material light.

Static sources need a reusable cached result, while video needs periodic analysis that remains independent from presentation cadence.

Without a standard logical unit, producers and client renderers may derive incompatible light-field meanings.

### Decision

`UVLightFrame` becomes the immutable, normalised and downscaled snapshot exchanged between artwork analysis, caching and Refraction.

Its source payload preserves spatially varying mean linear colour and relative brightness.

An optional local peak-luminance measure may preserve concentrated highlights that would otherwise disappear during downscaling.

The frame does not imply that source artwork is HDR and must not invent absolute luminance for an SDR source.

Successive moving-source frames preserve a stable intensity relationship rather than applying independent per-frame exposure normalisation.

Emission direction is artwork-local and defaults to the artwork surface normal when no more specific information is available.

The direction from artwork to an Acrylic receiver is derived from their transforms in the three-dimensional Composition and is not stored as receiver-relative frame data.

Static artwork normally produces one `UVLightFrame`.

Moving artwork and video produce an ordered, timestamped `UVLightStream` through periodic sampling.

The renderer reconstructs the active `UVLightField` consumed by Acrylic transport.

MDS-003 owns visual meaning and lifecycle, while [MIP-003 — UVLightFrame Protocol](../../../engineering/protocols/mip-003-uv-light-frame-protocol/index.md) owns the exact schema and compatibility rules.

### Consequences

Static and moving sources share one conceptual pipeline.

Video analysis does not need to run for every presented frame and may skip polls under playback pressure.

The exact channel encodings, serialisation, compression and compatibility rules are defined by [MIP-003 — UVLightFrame Protocol](../../../engineering/protocols/mip-003-uv-light-frame-protocol/index.md).

Polling intervals and platform-specific GPU layouts remain implementation choices subject to technical validation.

---

# ADR-124

## Title

Resolve Acrylic Parallax Outside UVLightFrame

### Status

Accepted

### Context

Acrylic must feel physically substantial while remaining a two-dimensional surface or layered composite.

Composition depth provides spatial relationships but does not imply mesh geometry or an extruded Acrylic object.

Parallax depends upon a particular Acrylic receiver, its apparent thickness and the current projected viewpoint or Focus relationship.

### Decision

Acrylic uses both whole-surface Composition parallax and bounded internal optical parallax.

The complete two-dimensional Acrylic surface may move according to Composition depth.

Sampled artwork, backdrop, diffusion and glare layers may move by smaller relative offsets inside the stable Acrylic mask.

The Refraction Engine derives receiver-specific optical offsets from Composition transforms and the apparent-thickness profile.

`UVLightFrame` remains receiver-independent and does not carry parallax offsets.

No mesh, extrusion or volumetric scene representation is required.

Composition movement, scrolling and Focus transitions may drive parallax.

Pointer position, gyroscope data, device tilt and unrelated ambient motion do not drive it.

### Consequences

CSS, Flutter composites and two-dimensional fragment renderers may implement the same Material behaviour.

Parallax can reduce or become static under accessibility or playback pressure without invalidating the source field.

The one-centimetre Acrylic reference governs optical character rather than physical geometry.

---

# ADR-125

## Title

Select Focused Artwork Before Hero Artwork

### Status

Accepted

### Context

Several artworks may be visible while Acrylic requires one coherent global primary source.

Using every visible artwork simultaneously would weaken Focus and produce competing Material environments.

### Decision

Artwork associated with current Focus becomes the active global primary source.

When Focus is not associated with artwork, Hero artwork becomes the source.

Source changes transition between fields without an abrupt Material reset.

### Consequences

Acrylic lighting follows user attention while retaining a deterministic fallback.

Components do not select or reinterpret the primary source independently.

---

# ADR-126

## Title

Separate Local Backdrop Participation From Artwork Light

### Status

Accepted

### Context

Acrylic must feel locally translucent while artwork remains the hidden global source of its pigmentation and illumination.

Treating visible backdrop pixels as the global field would couple the source contract to a particular Composition and renderer.

### Decision

Acrylic distorts and diffuses actual Presentation behind its two-dimensional bounds and mask.

This backdrop sample remains local to the receiver.

The hidden artwork-derived `UVLightField` independently supplies primary pigmentation, intensity, edge emission and shared environmental coherence.

Backdrop data does not enter `UVLightFrame` and does not become another global primary source.

### Consequences

CSS, Flutter and two-dimensional shader renderers may use native backdrop mechanisms while consuming the same artwork-light source contract.

Backdrop distortion may simplify under performance or accessibility pressure without changing source identity.

---

# ADR-127

## Title

Use Governed Brand Illumination When Artwork Is Absent

### Status

Accepted

### Context

Settings, administration and dashboard experiences may have no focused or Hero artwork but must retain Mosaic Acrylic identity.

### Decision

Primary source priority is focused artwork, Hero artwork, a resolved co-brand Brand Illumination Pair, then the default Mosaic pair.

The pair resolves into one stable synthetic Material-light field using Platform-owned placement, intensity and transition rules.

It does not recolour components directly, create new Material physics or require a partner-owned `UVLightFrame` format.

### Consequences

No-artwork experiences preserve Acrylic and Refraction with low continuous rendering cost.

Governed co-branding may influence illumination without replacing Mosaic identity.

---

# ADR-128

## Title

Treat User Refraction Preference As A Fidelity Maximum

### Status

Accepted

### Context

Users may prefer a calmer or less expensive Acrylic experience even when the client can render Enhanced fidelity.

### Decision

Automatic, Balanced and Essential define the maximum fidelity permitted by the user.

The preference may be synced or locally overridden for one client.

Accessibility, capability, current budget and Presentation deadlines may reduce further and must never be overridden by the preference.

### Consequences

Users can select a stable lower-refinement experience without controlling individual Refraction mechanics.

---

# ADR-129

## Title

Derive Rigid Acrylic Edges From Resolved Geometry

### Status

Amended by ADR-131

### Context

Exposed radius choices would fragment Mosaic geometry, while automatically fusing neighbouring Tiles would make Acrylic behave like liquid glass.

Several Tiles may still need shared layout and renderer work without losing their rigid material identity.

### Decision

The Material System derives corner curvature and edge-band width continuously from the shortest resolved Tile side.

The provisional alpha profile uses:

```text
cornerRadius = clamp(s × 0.045, 8, 32)
edgeBand     = clamp(s × 0.022, 4, 12)
seam         = clamp(s × 0.006, 2, 4)
```

An Acrylic Assembly may share layout, rendering and transported light while preserving visible precision seams and distinct rigid panels.

Proximity never causes material fusion.

One continuous Acrylic surface exists only when Composition creates one Tile.

### Consequences

Mosaic gains continuous geometry and efficient compositing without adopting liquid, blob-like behaviour.

The alpha Design System must validate the numerical coefficients before they become a stable Material profile.

---

# ADR-130

## Title

Generate A Composition-Anchored Static Brand Field Without MOS

### Status

Accepted

### Context

Documentation, administration and dashboard experiences may have no artwork but still require positioned Brand illumination and live Acrylic response during scroll and Focus changes.

Requiring artwork analysis or a serialised MOS cache for a deterministic colour-pair source would add unnecessary work and coupling.

### Decision

Artwork-free Authored Layout may define one Static Brand Emitter using normalised `x`, `y` and bounded logical `z` coordinates in its Composition Space parent.

The client generates or pre-bakes one deterministic low-resolution procedural `UVLightField` from the approved Brand Illumination Pair and governed Material profile.

The field remains fixed while Acrylic receivers move across it during scrolling and Focus transitions.

Receiver projection updates do not regenerate the source field.

The procedural source does not require `.mos` serialisation or [MIP-003 — UVLightFrame Protocol](../../../engineering/protocols/mip-003-uv-light-frame-protocol/index.md) interchange.

### Consequences

Conventional Mosaic pages receive positioned, coherent Refraction at low continuous cost.

Page authors control source placement while Mosaic retains energy, falloff, diffusion, accessibility and degradation authority.

---

# ADR-131

## Title

Compose One Fixed Acrylic Material From Three Optical Layers

### Status

Accepted

### Context

Representing apparent thickness as a visibly wide edge band makes Acrylic resemble a thick bezel.

Collapsing backdrop sampling, pigmentation and surface reflection into one translucent layer instead makes the Material resemble glass or uniform frost.

The one-centimetre reference needs to govern optical transport while every Acrylic surface retains one stable Material identity.

### Decision

Mosaic Acrylic uses three conceptual two-dimensional layers sharing one surface mask:

1. Rear Optical Plane
2. Acrylic Volume
3. Front Surface Response

The Rear Optical Plane provides relatively sharp, world-anchored and safely overscanned backdrop sampling with fixed bounded displacement.

The Acrylic Volume transforms incident artwork light through tint, absorption and scattering; receives directional contour ingress; and carries source hue inward as pigmentation.

The Front Surface provides only the polished Fresnel, reflection, specular and thin contour response.

The one-centimetre reference defines one fixed apparent-thickness profile across surface size, semantic role and renderer.

Tint is the only authored Acrylic Material parameter.

Artwork or a Static Brand Emitter remains an environmental input rather than a Material control.

The provisional `edgeBand` width in ADR-129 is superseded.

Corner-radius and Assembly-seam decisions in ADR-129 remain active.

Renderer fidelity may consolidate, pre-compose or omit optional refinement while preserving the same resolved three-layer meaning.

### Consequences

Acrylic thickness is communicated through optical displacement, internal pigmentation, parallax and contour response rather than a physical-looking bezel.

Modules and components cannot create custom glass, frost or stronger Hero Acrylic variants.

Alpha implementation must calibrate private displacement, transmission, scattering, contour, Fresnel, parallax, overscan and peak-energy relationships before technical review.

Those values remain private Material Profile data rather than public tokens or SDUI fields.

---

# ADR Relationships

```mermaid
flowchart TD

ADR111["Physical Behaviour"]

ADR112["Acrylic"]

ADR113["Artwork Light"]

ADR114["UV Refraction"]

ADR115["Light Transport"]

ADR116["Material Resolver"]

ADR117["Accessibility"]

ADR118["Shared Environment"]

ADR119["Modules"]

ADR120["Bounded Secondary Transport"]

ADR121["Measured Client Quality"]

ADR122["Playback Protection"]

ADR123["UVLightFrame Standard"]

ADR124["Acrylic Parallax"]

ADR125["Focused Artwork Selection"]

ADR126["Local Backdrop Participation"]

ADR127["Static Brand Illumination"]

ADR128["User Fidelity Maximum"]

ADR129["Rigid Derived Edges"]

ADR130["Static Brand Emitter"]

ADR131["Three-Layer Fixed Acrylic"]

ADR111 --> ADR112

ADR112 --> ADR115

ADR113 --> ADR114

ADR114 --> ADR115

ADR115 --> ADR118

ADR115 --> ADR120

ADR120 --> ADR118

ADR118 --> ADR121

ADR121 --> ADR122

ADR114 --> ADR123

ADR123 --> ADR118

ADR123 --> ADR122

ADR112 --> ADR124

ADR114 --> ADR124

ADR124 --> ADR116

ADR113 --> ADR125

ADR125 --> ADR123

ADR112 --> ADR126

ADR123 --> ADR126

ADR126 --> ADR116

ADR125 --> ADR127

ADR127 --> ADR116

ADR121 --> ADR128

ADR128 --> ADR116

ADR112 --> ADR129

ADR129 --> ADR116

ADR127 --> ADR130

ADR130 --> ADR116

ADR112 --> ADR131

ADR126 --> ADR131

ADR129 --> ADR131

ADR131 --> ADR116

ADR118 --> ADR116

ADR117 --> ADR116

ADR116 --> ADR119
```

Together these decisions establish one coherent physical model for the entire Mosaic interface.

---

# Future ADRs

Future Material ADRs are expected to formalise:

- Spectral Refraction
- HDR Material Response

These intentionally remain outside the scope of MDS-003 Version 0.4.

---

# ADR Governance

Material ADRs should change only when:

- architectural inconsistencies emerge,
- runtime evolution requires refinement,
- accessibility research identifies deficiencies,
- the Design Language itself evolves.

Implementation techniques should never drive architectural changes.

Rendering engines evolve.

Material behaviour should remain recognisably Mosaic.

---

# Summary

The ADRs contained within MDS-003 define the physical identity of Mosaic.

Rather than treating materials as visual styling, Mosaic treats them as environmental behaviours.

Light moves.

Materials respond.

Entertainment quietly illuminates the interface.

Together these decisions create a material language that feels:

- premium,
- restrained,
- believable,
- unmistakably Mosaic.
