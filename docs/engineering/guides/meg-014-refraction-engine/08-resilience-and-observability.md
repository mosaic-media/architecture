<!--
File: docs/engineering/guides/meg-014-refraction-engine/08-resilience-and-observability.md
Document: MEG-014
Status: Draft
-->

# 08 — Resilience And Observability

---

# Failure Policy

Refraction is presentation refinement and must fail safely.

| Failure | Required response |
|---------|-------------------|
| Missing source artwork | Use the approved Brand Illumination Pair or default Mosaic pair. |
| Invalid artwork and brand source data | Resolve neutral Acrylic. |
| Invalid `UVLightFrame` | Reject it and retain the last stable field. |
| Cache miss | Regenerate asynchronously or continue without source refinement. |
| Unsupported compression | Request or generate an unsupercompressed frame. |
| Renderer context loss | Fall back to a supported composite profile. |
| Backdrop unavailable | Preserve tint, edge response and material presence. |
| Budget exhaustion | Reuse stable state and continue Presentation. |

No failure should block video presentation or remove semantic foreground content.

---

# Diagnostics

The client should expose diagnostics for:

- active source identity and revision
- field epoch, sequence and age
- selected renderer profile
- active mip level
- Acrylic receiver count
- direct and secondary relationship counts
- analysis and resolution duration
- GPU or compositor duration where measurable
- filtered pixel area and maximum backdrop nesting depth
- skipped updates and reasons
- fallback transitions
- rejected-frame reasons

---

# Metrics

Useful metrics include:

| Metric | Purpose |
|--------|---------|
| Refraction-attributable deadline misses | Guard the playback invariant. |
| Resolution time percentile | Detect expensive engine states. |
| Stable-state reuse rate | Identify sustained budget pressure. |
| Renderer-profile residency | Understand real capability distribution. |
| Source-frame age | Detect stale analysis. |
| Secondary relationship count | Bound coupled-work growth. |
| Backdrop-pass count | Detect compositor amplification. |
| Filtered pixel area | Detect expensive large-surface effects. |
| Fidelity-level residency | Understand time spent at Enhanced, Balanced and Essential fidelity. |

Telemetry should describe renderer behaviour without capturing artwork pixels or user-viewing content.

---

# Logging

Routine quality reduction should not produce error logs.

Invalid protocol data, repeated context loss and violated invariants should produce structured diagnostics with bounded frequency.
