<!--
File: docs/engineering/guides/meg-014-refraction-engine/07-temporal-scheduling.md
Document: MEG-014
Status: Draft
-->

# 07 — Temporal Scheduling

---

# Scheduling Authority

The Refraction Engine should schedule work only inside budget remaining after video presentation, interaction and core UI Composition.

Asynchronous execution does not make expensive work safe by itself.

The scheduler should account for CPU, GPU, memory-transfer and compositor contention.

---

# Video Sidecar

Video analysis should operate as a sidecar to playback.

It may inspect periodically offered decoded samples but must not require every presented frame.

The pipeline should:

- prefer the latest useful sample
- discard stale analysis work
- publish immutable frames
- retain the last stable field when work is skipped
- avoid cache or upload work on the presentation critical path

---

# Update Triggers

The engine should resolve incrementally when one of these changes:

- focused or Hero artwork identity
- approved or default Brand Illumination Pair
- `UVLightField` epoch or sequence
- Acrylic transform, bounds or mask
- Composition movement or scroll position
- Focus transition state
- accessibility constraints
- Renderer Capability Profile
- Dynamic Material Budget
- User Fidelity Maximum or local-override selection

Pointer movement, gyroscope data and device tilt are not Refraction update triggers.

---

# Playback Protection

The engine must not cause a video presentation deadline miss.

When work does not fit, it should reduce or defer in this order:

1. additional secondary-transport depth
2. secondary update frequency
3. backdrop and distortion refinement
4. optical-parallax refinement
5. edge-response refinement
6. direct source sampling precision

The renderer should reuse the last stable state before it risks the deadline.

---

# Temporal Stability

Source transitions, edge movement and parallax should use bounded smoothing.

Recovery from a reduced profile should be gradual.

The engine should avoid independent per-frame exposure changes, oscillating quality profiles and late application of stale source states.
