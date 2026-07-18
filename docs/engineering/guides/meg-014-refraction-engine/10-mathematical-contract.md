<!--
File: docs/engineering/guides/meg-014-refraction-engine/10-mathematical-contract.md
Document: MEG-014
Status: Draft
-->

# 10 — Mathematical Contract

---

# Purpose

This chapter defines the minimum coordinate and numerical conventions required for consistent Refraction across CSS, Flutter and two-dimensional shader renderers.

It standardises observable results rather than requiring one matrix library or implementation language.

---

# Coordinate Spaces

The engine uses three distinct spaces.

| Space | Responsibility |
|-------|----------------|
| Artwork UV space | Stable normalised coordinates stored by `UVLightFrame`. |
| Composition Space | Spatial relationship between artwork, Acrylic and occluding surfaces. |
| Receiver-local space | Two-dimensional coordinates used to paint one Acrylic surface. |

`UVLightFrame` is anchored to artwork UV space rather than a Composition parent or receiver.

The artwork transform anchors that stable field within Composition Space at resolution time.

For a receiver-local point `pR`, the sampling relationship is conceptually:

```text
pC = receiverToComposition(pR)
pA = compositionToArtwork(pC)
uv = normaliseArtworkPosition(pA)
```

The receiver therefore behaves as a moving window over the artwork field.

Changing receiver position, scrolling or Composition movement changes the window transform without invalidating the source frame.

---

# Receiver-Local Direction Basis

Every receiver should expose a projected tangent basis:

- `right`: positive receiver-local x
- `down`: positive receiver-local y
- `normal`: outward artwork-facing surface normal

The basis is derived from the receiver transform in Composition Space.

Renderer adapters must convert native coordinate conventions into this basis before applying Refraction mathematics.

---

# Highlight Rotation

Let `sourceVector` point from the resolved receiver sample toward the corresponding artwork source sample in Composition Space.

The projected receiver-local direction is:

```text
dx = dot(sourceVector, right)
dy = dot(sourceVector, down)
```

The canonical highlight rotation is:

```text
highlightRotation = atan2(dy, dx)
```

The result is expressed in radians in the interval `[-pi, pi]`.

Zero points toward receiver-local right and positive rotation proceeds clockwise in the receiver-local presentation plane.

Adapters accepting degrees may convert only after this calculation.

When `abs(dx) + abs(dy)` falls below the active numeric epsilon, the engine should retain the previous stable rotation.

If no previous state exists, it should use zero.

Transitions should interpolate through the shortest wrapped angular distance to avoid a full rotation at the `-pi` and `pi` boundary.

---

# Moving-Window Continuity

The artwork-UV sampling transform should change continuously with a continuous receiver transform.

An engine should preserve the previous stable field while calculating a changed sampling window.

It must not clear Acrylic state, regenerate a static `UVLightFrame` or restart source exposure solely because a receiver moved.

Focus transitions may blend between two source fields while each field retains its own artwork-UV anchoring.

---

# Apparent Thickness Input

The engine consumes a governed `ApparentThicknessProfile` from the Material System.

The profile should provide renderer-independent limits for:

- optical-offset scale
- maximum optical offset
- diffusion contribution
- required sampling margin
- edge-spread contribution

The approximately one-centimetre Acrylic reference defines perceptual intent.

MEG-014 does not prescribe its final refractive index, physical-to-pixel conversion or platform scaling.

A future Material-profile revision may refine those private values without changing the coordinate contract.

The profile represents one fixed Material across receiver size, semantic role and renderer.

Platform scaling maps that fixed profile safely into Presentation; it must not reinterpret apparent thickness.

The Rear Optical Plane, Acrylic Volume and Front Surface Response may apply different bounded offsets from the same profile.

Their relative ratios require alpha calibration and must remain renderer-equivalent once standardised.

---

# Safe Optical Offset

A practical receiver-specific offset begins with:

```text
unclampedOffset = projectedRelationshipDelta * profile.opticalOffsetScale
```

The renderer must then constrain its magnitude by both the Material limit and available expanded sampling region:

```text
availableOffset = max(
    0,
    samplingMargin - diffusionRadius - edgeSpread
)

maximumSafeOffset = min(
    profile.maximumOpticalOffset,
    availableOffset
)

opticalOffset = clampMagnitude(
    unclampedOffset,
    maximumSafeOffset
)
```

If the required sampling margin is unavailable, the renderer must reduce optical displacement or related refinement before painting.

It must not reveal transparent, uncaptured or unrelated pixels inside the Acrylic mask.

---

# Peak-Energy Response

The canonical `UVLightFrame` fourth component is relative peak luminance.

A runtime may call it `E` or `peakEnergy` while retaining the [MIP-003 — UVLightFrame Protocol](../../protocols/mip-003-uv-light-frame-protocol/index.md) semantics.

Given mean linear RGB:

```text
meanY = 0.2627 R + 0.6780 G + 0.0593 B
peakRatio = E / max(meanY, epsilon)
```

A high `meanY` with a peak ratio near one represents broad brightness.

A materially higher peak ratio indicates a concentrated highlight that may strengthen bounded glare or bloom response.

The renderer must not treat `E` as transparency, additional integrated energy or evidence that an SDR source is HDR.

---

# Numerical Safety

All derived values should remain finite.

The engine should:

- clamp dot products before inverse trigonometric functions
- define and test one implementation epsilon per numeric precision
- reject or neutralise non-finite transforms
- clamp offsets before renderer adaptation
- preserve the last stable state when a new calculation is invalid

Numerical failure must not block Presentation or invalidate a valid `UVLightField`.
