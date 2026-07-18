<!--
File: docs/engineering/architecture/mdp-001-adaptive-composition-runtime/06-adaptive-layout.md
Document: MDP-001
Status: Draft
-->

# Adaptive Layout

> **Proposal status:** Deferred and non-authoritative. This chapter preserves post-v1 research; it is not a Mosaic v1 requirement.

---

# Purpose

The Composition Solver determines:

- what should exist,
- what deserves attention,
- how understanding should be organised.

Adaptive Layout determines how that solved understanding is expressed within the physical constraints of a device.

Unlike responsive design, Adaptive Layout does **not** solve geometry first.

It solves understanding first.

Layout becomes a consequence.

> **Release applicability:** Mathematical Adaptive Layout is reserved for the post-v1 Adaptive Composition Runtime. Mosaic v1 uses governed components and responsive CSS or equivalent native layout primitives.

---

# Definition

Within MDS, **Adaptive Layout** is defined as:

> **The deterministic client-side projection of a solved Composition into a spatial arrangement while preserving behavioural hierarchy and understanding.**

Adaptive Layout changes:

- spatial organisation,
- density,
- presentation.

It never changes:

- hierarchy,
- behaviour,
- meaning.

---

# Why Adaptive Layout Exists

Traditional responsive systems generally behave like this.

```mermaid
flowchart TD

N1["Viewport"]
N2["Breakpoints"]
N3["Different Layout"]

N1 --> N2
N2 --> N3
```

Meaning frequently changes because layout changed.

Mosaic intentionally follows:

```mermaid
flowchart TD

N1["Composition"]
N2["Hierarchy"]
N3["Expressions"]
N4["Adaptive Layout"]
N5["Presentation"]

N1 --> N2
N2 --> N3
N3 --> N4
N4 --> N5
```

Understanding remains constant.

Only spatial expression changes.

---

# Behaviour Before Geometry

Adaptive Layout should never ask:

> How much space exists?

before asking:

> What must remain understandable?

Behaviour always possesses higher authority than geometry.

---

# One Composition

Every device should consume the same solved Composition.

Desktop.

↓

Expanded Presentation.

Tablet.

↓

Editorial Presentation.

Phone.

↓

Compact Presentation.

Television.

↓

Immersive Presentation.

The Composition never changes.

Only layout.

---

# Layout Modes

Mosaic supports two client layout modes.

| Mode | Use |
|------|-----|
| v1 Component Layout | Every Mosaic v1 experience, including media, documentation, administration and dashboards, built from governed components using CSS or native layout and public Semantic Tokens. |
| Post-v1 Adaptive Composition | Selected future experiences where the client mathematically resolves Tile geometry from Composition, artwork, Focus, content and current constraints. |

Both modes use the same typography, spacing, sizing, Material, accessibility and Refraction systems.

v1 Component Layout does not require the Composition Engine to replace CSS Grid, Flexbox or native layout primitives.

Adaptive Composition does not require authors to select spacing or geometry values manually.

A future client may combine both modes while preserving one Mosaic design language.

---

# Layout Inputs

Adaptive Layout evaluates:

```mermaid
flowchart TD

N1["Expression Tree"]
N2["Hierarchy"]
N3["Available Extent"]
N4["Orientation And Viewing Context"]
N5["Typography And Accessibility"]
N6["Capability And Runtime Budget"]

N1 --> N2
N2 --> N3
N3 --> N4
N4 --> N5
N5 --> N6
```

Notice that Behaviour has already been solved.

Adaptive Layout communicates.

It does not decide.

---

# Layout Outputs

Adaptive Layout produces:

```mermaid
flowchart TD

N1["Spatial Regions"]
N2["Expression Placement"]
N3["Density"]
N4["Presentation Constraints"]

N1 --> N2
N2 --> N3
N3 --> N4
```

These outputs remain independent from components.

Future rendering systems consume them directly.

The client-side Mosaic design runtime calculates concrete Presentation geometry from these outputs and private Platform primitives.

Runtime SDUI does not provide final coordinates, dimensions, padding, spacing, radius or typography values.

---

# Regions

Adaptive Layout organises Expressions into conceptual regions.

Examples.

```mermaid
flowchart TD

N1["Hero"]
N2["Primary Region"]
N3["Supporting Region"]
N4["Peripheral Region"]
N5["Navigation"]

N1 --> N2
N2 --> N3
N3 --> N4
N4 --> N5
```

Regions communicate behavioural organisation.

Not implementation.

---

# Composition-Plane Occupancy

Adaptive Layout projects semantic depth intent into governed persistent Composition Planes.

Each plane owns an independent two-dimensional occupancy solution.

A Tile's current plane is resolved Composition state rather than part of its identity. Every Tile may settle on any valid governed plane, and may move between planes when the solved hierarchy changes.

For ordinary Tile footprints \(F_i\) and \(F_j\):

\[
z_i=z_j
\quad\Longrightarrow\quad
F_i\cap F_j=\varnothing
\]

Tiles on different planes may overlap in projected space:

\[
z_i\ne z_j
\quad\Longrightarrow\quad
F_i\cap F_j\text{ may be non-empty}
\]

When a Tile gains or releases capacity, the solver should first move related Tiles on the same plane.

Other planes retain their independent occupancy, although occlusion, parallax, interaction priority and Material relationships may update.

A Tile may remain on its newly resolved plane after its semantic hierarchy changes.

SDUI and Modules provide roles and relationships rather than final \(z\) coordinates.

---

# Projected Text Legibility

Cross-plane overlap does not permit readable text to overlap other readable text.

For the projected text-protection regions \(T_i\) and \(T_j\) of any two settled Tiles:

\[
T_i \cap T_j = \varnothing
\]

This constraint applies even when:

\[
z_i \ne z_j
\]

Text-protection regions should include governed legibility clearance rather than only glyph bounds.

Artwork, atmosphere and non-semantic Material responses may overlap across planes when readability, hierarchy and accessibility remain valid.

---

# Breathable Composition Extent

The viewport is a moving window over a vertically extensible Composition rather than a fixed container into which every relevant Tile must fit.

For neighbouring settled footprints \(F_i\) and \(F_j\):

\[
\operatorname{distance}(F_i,F_j) \ge g_{\min}
\]

If no valid candidate satisfies the governed minimum clearance inside the current extent, the solver should extend the Composition vertically and place lower-priority relevant content farther along the scroll path.

The provisional layout objective is:

\[
C_{\mathrm{layout}}
=
w_m C_{\mathrm{movement}}
+ w_r C_{\mathrm{resize}}
+ w_z C_{\mathrm{plane}}
+ w_o C_{\mathrm{occlusion}}
+ w_h C_{\mathrm{hierarchy}}
+ w_s C_{\mathrm{scroll}}
- w_c C_{\mathrm{continuity}}
\]

Hard accessibility, minimum-size, same-plane collision, text-legibility, hard-Airspace and Breathing Space constraints are evaluated before this score. An invalid candidate cannot compensate for a violation by receiving a lower weighted cost elsewhere.

The weights remain private alpha-calibration data. Density maximisation is not an objective.

---

# Airspace Reserve Resolution

A lower-plane Expression may provide or derive a normalised importance mask \(M_a(x,y)\in[0,1]\) and a governed protected depth interval.

The mask may represent:

- focal subjects
- recognised faces
- identity marks
- editorial safe regions
- weighted visual saliency

For candidate footprint \(F\) settling on plane \(z\), the normalised occlusion cost is:

\[
O(F,z)
=
w_z(z)
\frac{
\displaystyle\iint_F M_a(x,y)\,\mathrm{d}x\,\mathrm{d}y
}{
\operatorname{area}(F)
}
\]

The plane weighting function \(w_z(z)\) determines how strongly the reserve applies across governed depth.

A hard-reserve mask invalidates a settled footprint when:

\[
\operatorname{area}\left(F\cap H_a\right)>0
\]

A soft reserve contributes to placement cost:

\[
C_p
=
C_m
+ \lambda_o O(F,z)
+ C_h
+ C_c
\]

| Term | Meaning |
|------|---------|
| \(C_p\) | Total candidate placement cost. |
| \(C_m\) | Movement and continuity cost. |
| \(\lambda_o\) | Governed occlusion weight. |
| \(C_h\) | Hierarchy cost. |
| \(C_c\) | Same-plane collision and capacity cost. |

Airspace Reserve constraints apply to settled placement rather than transit.

Motion paths may cross the reserve, but interruption handling must still continue toward a valid settled footprint.

The client may evaluate rectangular footprints from a low-resolution summed-area table \(P\):

\[
\Sigma_F
=
P(x_2,y_2)
-P(x_1,y_2)
-P(x_2,y_1)
+P(x_1,y_1)
\]

This makes candidate evaluation independent from the number of source pixels inside the footprint.

Exact mask resolution, thresholds, depth weighting and cost coefficients remain alpha-calibration data.

---

# Density

Adaptive Layout resolves density continuously from available extent, viewing distance, input context, typography, accessibility and current content pressure.

It must not select density from a device category.

The provisional relationship bands are:

| Private values | Relationship |
|---------------:|--------------|
| `2–8` | Optical and internal detail |
| `12–16` | Tightly related content |
| `24–32` | Component groups |
| `48–64` | Major regions |
| `64–96` | Hero and artwork breathing space |

These bands guide the resolver; they are not SDUI or Module controls.

Related items must sit visibly closer together than unrelated items.

Separation between groups should normally be at least twice the separation within a group.

Artwork receives more surrounding space than utility controls.

Dense administration and calendar expressions may reduce internal separation without flattening hierarchy or removing region-level breathing space.

Accessibility may increase separation or restructure the Composition.

It must not solve pressure by squeezing content below readable or operable limits.

---

# Acrylic Topology

Composition determines material topology before the Material System resolves Acrylic edges.

One Tile represents one continuous Acrylic surface even when it contains several internal content regions.

An Acrylic Assembly represents several rigid Tiles that share a governed group relationship while retaining distinct material boundaries.

Adaptive Layout may align and move Assembly members together and the renderer may composite them in one pass.

It must not fuse separate Tile silhouettes because their projected bounds touch or become close.

Modules express content relationships and valid domain layout modes.

They do not select continuous-surface, seam, radius or edge-band values directly.

The visual and optical Assembly behaviour is owned by [MDS-003 — Material System](../../../design/system/mds-003-material-system/04-acrylic.md#acrylic-assemblies).

---

# Progressive Disclosure

Smaller devices should prefer progressive disclosure over hierarchy reduction.

Incorrect.

```text
Remove Relationships
```

Preferred.

```mermaid
flowchart TD

N1["Relationships"]
N2["Collapsed"]
N3["Expandable"]

N1 --> N2
N2 --> N3
```

Understanding remains available.

Presentation simply becomes more compact.

---

# Hero Preservation

The Hero should remain visually dominant across every layout.

Examples.

Desktop.

↓

Large Hero region.

Phone.

↓

Compact Hero.

Television.

↓

Immersive Hero.

The Hero should always remain immediately recognisable.

---

# Artwork Title Treatment

Composition selects the visible media-title treatment from the available artwork role and safe placement.

For landscape or backdrop artwork:

1. use an HD ClearLogo when one is available and a verified negative-space region can contain it without obscuring the focal subject
2. otherwise use the semantic Mona Sans title on an Acrylic information plane

For portrait poster artwork, preserve the image without text overlays and place the semantic title and metadata below it.

The ClearLogo and typographic fallback must not appear together.

The semantic text title remains available for accessibility, search, voice output and asset failure even when the ClearLogo is visible.

ClearLogos preserve their aspect ratio and must not be cropped, stretched or reduced below a legible presentation size.

Asset aspect ratio and artwork role determine this treatment.

Device category does not.

---

# Anchor Preservation

Anchors should remain behaviourally stable.

Examples include:

- Navigation
- Search
- Playback
- Current Focus

Adaptive Layout may reposition Anchors.

It should never redefine them.

---

# Expression Integrity

Expressions should never fragment because layout changes.

Example.

Timeline.

↓

Timeline.

Not.

Timeline Header.

↓

Timeline Progress.

↓

Timeline Footer.

Expressions remain conceptually whole even when visually rearranged.

---

# Material Awareness

Adaptive Layout should preserve Material Hierarchy.

Hero Region.

↓

Hero Material.

Supporting Region.

↓

Acrylic.

Canvas.

↓

Environment.

Layout should never weaken physical hierarchy.

---

# Typography Awareness

Editorial hierarchy should remain stable.

Heading.

↓

Heading.

Body.

↓

Body.

Supporting.

↓

Supporting.

Adaptive Layout may alter line length and spacing.

It should never alter editorial roles.

---

# Motion Awareness

Adaptive Layout should preserve behavioural sequencing.

Examples.

Hero moves first.

↓

Supporting Expressions respond.

↓

Environment settles.

Changing layout should never create a different Motion language.

---

# Capability-Driven Layout

Adaptive Layout must not select a permanent strategy from a product category such as phone, tablet, desktop or television.

Those labels do not reliably describe the available extent, input method, viewing distance, typography scale, renderer capability or current workload.

The same solved Composition is projected from measured and declared constraints.

Clients with equivalent effective constraints should produce equivalent spatial behaviour even when their product categories differ.

---

# Runtime Adaptation

Adaptive Layout should respond to:

- orientation changes,
- window resizing,
- foldable devices,
- accessibility scaling.

These changes should preserve continuity.

Users should feel the interface adapting.

Not rebuilding.

---

# Incremental Layout

Small environmental changes should produce small layout changes.

Preferred.

```mermaid
flowchart TD

N1["Window Slightly Wider"]
N2["Additional Supporting Expression Appears"]

N1 --> N2
```

Avoid.

```mermaid
flowchart TD

N1["Window Slightly Wider"]
N2["Entire Layout Rebuilt"]

N1 --> N2
```

Incremental adaptation preserves orientation.

The current valid layout should remain selected until a candidate is meaningfully better:

\[
C_{\mathrm{new}} + \Delta_{\mathrm{switch}} < C_{\mathrm{current}}
\]

where \(\Delta_{\mathrm{switch}}\) is a governed stability margin.

This hysteresis prevents measurement noise from repeatedly changing layout. It must not delay direct Focus, navigation or accessibility intent; those changes invalidate the relevant current-state assumptions and resolve immediately.

---

# Accessibility

Accessibility should influence layout.

Examples.

Larger text.

↓

Greater spacing.

Reduced vision.

↓

Simpler layout.

High contrast.

↓

Unchanged hierarchy.

Accessibility modifies spatial expression.

Not behavioural meaning.

---

# Modules

Modules contribute Expressions and may declare governed domain layout constraints or valid presentation modes.

Modules do not provide final Presentation coordinates, Material radius values or arbitrary Primitive values.

A Module implementing Authored Layout may consume the public Semantic Tokens defined by [MDS-001 — Design Token Architecture](../../../design/system/mds-001-design-token-architecture/04-semantic-tokens.md).

Adaptive Layout remains Platform-owned and chooses how the Module contract is projected through Mosaic primitives.

Every module therefore automatically inherits future layout improvements.

---

# Good Examples

## Desktop

Hero.

↓

Expanded supporting regions.

↓

Peripheral collections.

Everything breathes.

---

## Phone

Hero.

↓

Primary actions.

↓

Progressive disclosure.

Understanding remains intact.

---

## Television

Large Hero.

↓

Generous spacing.

↓

Minimal interface.

Entertainment remains dominant.

---

# Anti-patterns

## Breakpoint Thinking

Entire interface changes because width crossed an arbitrary value.

---

## Hierarchy Loss

Smaller devices removing behavioural importance.

---

## Component Layout

Widgets determining spatial organisation.

---

## Module Layout

Modules introducing independent layout systems.

---

# Adaptive Layout Model

```mermaid
flowchart TD

Composition
Composition --> ExpressionTree
ExpressionTree --> AdaptiveLayout
AdaptiveLayout --> PresentationModel
PresentationModel --> Rendering
```

Composition determines understanding.

Adaptive Layout determines spatial expression.

---

# Relationship To Future Chapters

The next chapter defines **Behaviour Orchestration**.

Adaptive Layout explains:

> **Where Expressions should appear.**

Behaviour Orchestration explains:

> **How every runtime subsystem evolves together as behaviour changes.**

Together they transform solved understanding into one continuously evolving runtime experience.

---

# Summary

Adaptive Layout is not responsive design.

It is behavioural projection.

The user's World remains identical across:

- phones,
- desktops,
- televisions,
- future devices.

Only the physical arrangement changes.

That distinction allows Mosaic to remain one coherent Companion regardless of where users choose to experience it.
