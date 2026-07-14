<!--
File: docs/design/system/mds-003-material-system/10-runtime-material-resolution.md
Document: MDS-003
Chapter: 10
Title: Runtime Material Resolution
Status: Draft
Version: 0.4
-->

# Runtime Material Resolution

---

# Purpose

The previous chapters established the conceptual behaviour of the Material System.

They defined:

- Material Hierarchy
- Acrylic
- Hero Material
- Overlay Material
- Refraction
- UV-Indexed Refraction
- Light Transport

This chapter defines how those independent systems become a resolved material at runtime.

Runtime Material Resolution is the bridge between architectural intent and rendered surfaces.

It ensures that every Mosaic client presents identical material behaviour regardless of rendering technology.

---

# Definition

Within MDS, **Runtime Material Resolution** is defined as:

> **The deterministic process through which conceptual material behaviour is transformed into concrete runtime material properties suitable for rendering.**

Runtime Material Resolution never changes material identity.

It only determines how that identity is expressed in the current environment.

---

# Why Resolution Exists

A Hero Tile should never decide:

- blur strength
- acrylic depth
- edge lighting
- atmosphere intensity
- translucency
- refraction strength

Instead it simply requests:

```text
Material.Hero
```

The Runtime Material Resolver determines everything else.

This dramatically reduces component complexity.

---

# Resolution Pipeline

Every material follows the same conceptual pipeline.

```mermaid
flowchart TD

N1["Material Identity"]
N2["Semantic Tokens"]
N3["Runtime Atmosphere"]
N4["UV Field"]
N5["Light Transport"]
N6["Accessibility"]
N7["Device Capability"]
N8["Resolved Material"]

N1 --> N2
N2 --> N3
N3 --> N4
N4 --> N5
N5 --> N6
N6 --> N7
N7 --> N8
```

Each stage contributes exactly one responsibility.

---

# Resolution Inputs

The Runtime Material Resolver evaluates:

```mermaid
flowchart TD

N1["Current World"]
N2["Current Focus"]
N3["Current Context"]
N4["Composition"]
N5["Material Identity"]
N6["Runtime Atmosphere"]
N7["Accessibility"]
N8["Theme"]
N9["Device"]

N1 --> N2
N2 --> N3
N3 --> N4
N4 --> N5
N5 --> N6
N6 --> N7
N7 --> N8
N8 --> N9
```

No single input should dominate.

The resolver balances all inputs according to architectural priority.

---

# Resolution Priority

Material Resolution follows a strict evaluation order.

```mermaid
flowchart TD

N1["1.<br/>Material Identity"]
N2["2.<br/>Composition"]
N3["3.<br/>Runtime Atmosphere"]
N4["4.<br/>Accessibility"]
N5["5.<br/>Device Capability"]
N6["6.<br/>Rendering Backend"]

N1 --> N2
N2 --> N3
N3 --> N4
N4 --> N5
N5 --> N6
```

Meaning always precedes implementation.

Accessibility always precedes aesthetics.

---

# Material Identity Never Changes

One of the strongest guarantees within Mosaic is:

```mermaid
flowchart TD

N1["Hero Material"]
N2["Always Hero Material"]

N1 --> N2
```

Regardless of:

- device
- theme
- accessibility
- artwork

Only its physical implementation changes.

The conceptual identity remains constant.

---

# Runtime Adaptation

Runtime Material Resolution adapts implementation.

Examples include:

Hero.

↓

Greater perceived thickness.

Playback.

↓

Reduced atmosphere.

Reading.

↓

Softer diffusion.

Administration.

↓

Calmer materials.

The same Material Identity behaves differently because the user's World changed.

Not because components changed.

---

# Accessibility Resolution

Accessibility possesses higher authority than physical realism.

Examples.

High Contrast.

↓

Reduced translucency.

Reduced Motion.

↓

Simplified atmosphere interpolation.

Low Vision.

↓

Reduced refraction.

Every adaptation should preserve:

- hierarchy
- readability
- interaction

before preserving material richness.

---

# Device Resolution

Different devices possess different rendering capabilities.

Desktop.

↓

Full Acrylic.

Television.

↓

Enhanced depth.

Phone.

↓

Reduced shader complexity.

Low Power Device.

↓

Simplified diffusion.

Despite implementation differences...

Users should continue perceiving the same Material System.

---

# Material Profiles

Future implementations may internally generate Material Profiles.

Conceptually.

```mermaid
flowchart TD

N1["Material.Hero"]
N2["Runtime Profile"]
N3["Blur"]
N4["Refraction"]
N5["Thickness"]
N6["Edge Behaviour"]
N7["Lighting"]
N8["Resolved Material"]

N1 --> N2
N2 --> N3
N3 --> N4
N4 --> N5
N5 --> N6
N6 --> N7
N7 --> N8
```

Components consume only the completed profile.

---

# Runtime Caching

Resolved Materials should be aggressively cached.

Typical cache invalidation events include:

- Hero changes
- Focus changes
- artwork changes
- theme changes
- accessibility changes

Ordinary scrolling should not invalidate material resolution.

The environment should remain visually stable.

---

# Incremental Updates

Material Resolution should favour incremental refinement.

Preferred.

```mermaid
flowchart TD

N1["Atmosphere Changes"]
N2["Update Hero"]
N3["Update Nearby Acrylic"]
N4["Canvas Stable"]

N1 --> N2
N2 --> N3
N3 --> N4
```

Avoid.

```mermaid
flowchart TD

N1["Atmosphere Changes"]
N2["Rebuild Entire Material Tree"]

N1 --> N2
```

Incremental updates preserve continuity while reducing computational cost.

---

# Composition Awareness

Material Resolution should remain Composition-aware.

Example.

Primary Composition.

↓

High-quality Acrylic.

Peripheral Composition.

↓

Simplified Acrylic.

Material fidelity should follow compositional importance.

Rendering effort should therefore support user understanding.

---

# Module Behaviour

Modules never resolve materials.

Modules contribute:

- artwork
- information
- relationships

The platform resolves:

- Material Identity
- Atmosphere
- Refraction
- Lighting

This guarantees every module inherits identical physical behaviour.

---

# Good Examples

## Hero

Current artwork.

↓

Atmosphere.

↓

Hero Profile.

↓

Premium Acrylic.

↓

Rendered Surface.

---

## Timeline

Supporting Composition.

↓

Supporting Acrylic.

↓

Reduced refraction.

↓

Consistent hierarchy.

---

## Playback Overlay

Overlay Material.

↓

Reduced atmosphere.

↓

Maximum readability.

↓

Interaction remains effortless.

---

# Anti-patterns

## Component Materials

Components constructing materials independently.

The Material System fragments.

---

## Device Materials

Every client inventing its own material hierarchy.

Consistency disappears.

---

## Runtime Identity

Runtime changing Hero into Surface.

Meaning has leaked into implementation.

---

## Complete Rebuild

Every runtime update regenerates every material.

Continuity weakens.

Performance decreases.

---

# Runtime Material Model

```mermaid
flowchart TD

MaterialIdentity
MaterialIdentity --> Composition
Composition --> RuntimeAtmosphere
RuntimeAtmosphere --> LightTransport
LightTransport --> Accessibility
Accessibility --> DeviceCapability
DeviceCapability --> ResolvedMaterial
ResolvedMaterial --> Presentation
```

Material behaviour is resolved once.

Components simply consume the result.

---

# Relationship To Future Specifications

Future specifications are expected to formalise:

- Material Resolver
- GPU Material Pipeline
- Shader Profiles
- Material Cache
- Acrylic Renderer
- Refraction Engine
- Cross-platform Material Backends

These systems implement the architecture defined by this chapter.

---

# Summary

Runtime Material Resolution transforms conceptual materials into physical experience.

It preserves:

- hierarchy
- atmosphere
- accessibility
- continuity
- performance

while hiding implementation complexity from the rest of the platform.

Components should never know:

- how Acrylic is rendered,
- how light was transported,
- how atmosphere was generated.

They should simply receive:

> **Material.Hero**

The Material System does everything else.
