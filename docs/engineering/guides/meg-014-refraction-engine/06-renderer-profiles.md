<!--
File: docs/engineering/guides/meg-014-refraction-engine/06-renderer-profiles.md
Document: MEG-014
Status: Draft
-->

# 06 — Renderer Profiles

---

# Selection Principle

Renderer paths should be selected from measured cost and available frame headroom.

They must not be assigned permanently by browser, television, mobile or device category.

---

# Web Profiles

| Profile | Techniques | Intended role |
|---------|------------|---------------|
| Basic CSS | Tint, gradients, borders, opacity and transforms. | Minimum stable Acrylic identity. |
| CSS Composite | Pseudo-elements, masks, blend modes and limited backdrop filters. | Default web path. |
| Two-Dimensional Shader | WebGL2 or equivalent fragment processing over rectangular surfaces. | Consolidated or enhanced dynamic response. |
| WebGPU | Optional two-dimensional compute or fragment path. | Use only when measured benefit justifies it. |

TypeScript should decode source data, resolve spatial state and set renderer inputs.

CSS may remain responsible for all visible painting in Basic CSS and CSS Composite profiles.

Example adapter output:

```css
--acrylic-light-r: 0.72;
--acrylic-light-g: 0.31;
--acrylic-light-b: 0.18;
--acrylic-light-strength: 0.64;
--acrylic-parallax-x: -1.2px;
--acrylic-parallax-y: 0.8px;
--acrylic-edge-top: 0.18;
--acrylic-edge-right: 0.73;
```

---

# Flutter Profiles

| Profile | Techniques | Intended role |
|---------|------------|---------------|
| Flutter Composite | `Stack`, `Transform`, clipping, gradients, backdrop filters and `CustomPainter`. | Default native path. |
| Flutter Fragment | `FragmentProgram` over two-dimensional surfaces. | Enhanced fidelity or pass consolidation. |

Flutter adapters may unpack canonical RGBA source data into renderer-friendly textures when necessary.

Peak luminance must not accidentally become visual transparency.

---

# Three-Layer Adaptation

Renderer profiles implement one logical Rear Optical Plane, Acrylic Volume and Front Surface Response.

They do not have to allocate three physical render passes.

| Renderer path | Expected adaptation |
|---------------|---------------------|
| Basic CSS | Pre-composed rear approximation, governed Volume gradient and thin directional contour response. |
| CSS Composite | Shared mask with stacked rear sample, Volume pigmentation and surface pseudo-elements. |
| Flutter Composite | `Stack` or `CustomPainter` with shared clipping and bounded transforms. |
| Two-Dimensional Shader or Flutter Fragment | One consolidated fragment pass retaining logically separate layer inputs. |

Layer consolidation must not turn the Material into backdrop blur plus a border.

Fidelity reduction should simplify sampling and temporal refinement before changing the fixed apparent-thickness relationship.

---

# Profile Switching

The engine should preserve `ResolvedAcrylicState` semantics when switching profiles.

It should avoid switching repeatedly near a performance threshold.

Quality should reduce quickly under pressure and recover only after sustained headroom.

---

# Fidelity Levels

Renderer technique and fidelity are separate decisions.

A CSS, Flutter or shader renderer may operate at any fidelity level it can implement safely.

| Fidelity level | Required behaviour | Optional refinement |
|----------------|--------------------|---------------------|
| Enhanced | Artwork-field sampling, directional edge response, bounded optical parallax and readable foreground content. | Local backdrop distortion and bounded secondary transport. |
| Balanced | Artwork-derived colour, directional edge response, restrained parallax and readable foreground content. | Reduced local backdrop refinement. |
| Essential | Stable flat or gently graded Acrylic derived from a cached artwork field. | Static edge emphasis. |

Essential fidelity should continue using precomputed artwork-light data when it is available.

It reduces continuous sampling, backdrop work, parallax and secondary transport rather than discarding the artwork relationship.

When artwork is absent, Essential fidelity should use the approved Brand Illumination Pair or the default Mosaic pair as a stable synthetic source.

Neutral Acrylic is reserved for invalid or unavailable artwork and brand source data.

Fidelity levels must be selected from measured cost and current frame headroom rather than device category.

Automatic permits selection up to Enhanced, Balanced caps selection at Balanced and Essential caps selection at Essential.

Accessibility, capability and budget may always reduce below the user's maximum.

---

# Backdrop And Overdraw Governance

Backdrop filtering may allocate intermediate surfaces and amplify compositor work across every covered pixel.

Renderer adapters should therefore:

- avoid nested or recursively compounded backdrop filters
- consolidate compatible Acrylic backdrop work where the renderer supports it
- bound filtered pixel area, blur radius, layer count and backdrop-pass count
- flatten decorative Acrylic sublayers into one logical backdrop operation
- reuse an eligible captured backdrop within one Composition resolution cycle
- disable backdrop refinement before threatening a Presentation deadline

One `ResolvedAcrylicState` should request no more than one logical backdrop operation for one receiver.

An adapter may fulfil several compatible requests through one shared pass.

When nested Acrylic cannot be consolidated safely, the deeper receiver should use artwork-derived tint and edge response without another backdrop filter.

Overdraw pressure should move fidelity from Enhanced to Balanced and then Essential.

It must not be compensated for by unbounded main-thread painting or repeated offscreen capture.

---

# Unsupported Features

When a technique is unavailable or too expensive, the renderer should omit it explicitly rather than emulate it with unbounded main-thread work.

Fallback order should preserve:

1. Material presence and readability
2. direct artwork-derived colour
3. directional edge response
4. bounded optical parallax
5. backdrop refinement
6. secondary transport
