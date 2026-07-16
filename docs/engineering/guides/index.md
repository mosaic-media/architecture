<!--
File: docs/engineering/guides/index.md
Document: Guides
Status: Draft
Version: 0.3
-->

# Guides

Engineering guidelines describe implementation-facing standards, architectural patterns, and quality expectations for Mosaic software.

## Engineering Guides in Brief

The guides form a deliberate progression from code-level foundations to cross-cutting Platform qualities.

| Specification | In one sentence |
|---------------|-----------------|
| [MEG-001 — Go Engineering Standards](meg-001-go-engineering-standards/index.md) | Establishes the engineering philosophy and Go practices used across Mosaic software. |
| [MEG-002 — Event-Driven Runtime](meg-002-event-driven-runtime/index.md) | Explains how autonomous capabilities coordinate work through events. |
| [MEG-003 — Domain-Driven Design](meg-003-domain-driven-design/index.md) | Explains how Mosaic models independent business capabilities and protects domain language. |
| [MEG-004 — Hexagonal Architecture](meg-004-hexagonal-architecture/index.md) | Defines dependency boundaries that keep the Domain independent of external technology. |
| [MEG-005 — Runtime Architecture](meg-005-runtime-architecture/index.md) | Explains the internal components that discover, compose, schedule and supervise capabilities. |
| [MEG-006 — Module Platform](meg-006-module-platform/index.md) | Explains how Modules extend Mosaic through safe, deterministic composition. |
| [MEG-007 — Storage Architecture](meg-007-storage-architecture/index.md) | Explains how storage responsibilities are separated by information type and lifecycle. |
| [MEG-008 — Observability](meg-008-observability/index.md) | Defines how the running Platform explains its behaviour through telemetry and diagnostics. |
| [MEG-009 — Security Architecture](meg-009-security-architecture/index.md) | Defines how trust, authority and protection are designed into an extensible Platform. |
| [MEG-010 — Performance Engineering](meg-010-performance-engineering/index.md) | Defines how performance is designed, measured and protected as an architectural property. |
| [MEG-014 — Refraction Engine](meg-014-refraction-engine/index.md) | Explains how clients resolve artwork light, local backdrop and two-dimensional Composition state into stable Acrylic rendering. |
| [MEG-015 — Platform Foundation Implementation](meg-015-platform-foundation-implementation/index.md) | Defines the first implementation-grade build path for the Mosaic Platform foundation. |

New readers should follow the guides in numerical order. Readers solving a focused problem may start with the owning guide, but should follow its references back to [MAC-001 — Platform Architecture](../architecture/mac-001-platform-architecture/index.md) and preceding guides.

The following identifiers remain reserved:

- MEG-011 — Deployment Architecture *(planned; not yet published)*
- MEG-012 — API Architecture *(planned; not yet published)*
- MEG-013 — Event Architecture *(planned; not yet published)*

The linked MEG specifications own the implementation guidance; this page is a catalogue and reading path.
