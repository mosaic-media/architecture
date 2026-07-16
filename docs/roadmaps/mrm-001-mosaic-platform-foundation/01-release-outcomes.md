<!--
File: docs/roadmaps/mrm-001-mosaic-platform-foundation/01-release-outcomes.md
Document: MRM-001
Chapter: 01
Status: Draft
Version: 0.1
-->

# 01 — Release Outcomes

MRM-001 plans one foundational release composed of several independently testable outcomes.

## Platform Outcome

Mosaic has a runnable Platform foundation responsible for the core capabilities required by the first product experience, including:

- Mosaic-local authentication, passkeys and session authority,
- remote sign-in and device pairing for limited-input clients,
- local account recovery without email, phone or external identity providers,
- hybrid authorisation through roles, resource relationships, contextual attributes and capability permissions,
- storage and persistence boundaries,
- GraphQL API delivery,
- event-bus integration,
- capability and Module registration,
- configuration and secrets boundaries, and
- health, diagnostics and observability hooks.

The exact capability list remains owned by the Platform Architecture and its implementation guides. This Roadmap records the outcome, not the internal service decomposition.

## Supervisor Outcome

Mosaic has a Supervisor that can assemble, launch, monitor, diagnose and recover the first Mosaic binary using the Platform contracts.

The Supervisor must exist before the first Module is considered complete. This creates an executable integration target for Module development rather than testing Modules only in isolation.

## SDK Outcome

Mosaic has an SDK derived from the Platform contracts that allows the Shell and Modules to:

- authenticate and establish sessions,
- access typed Platform capabilities,
- consume GraphQL data,
- publish and subscribe to supported events,
- register Module capabilities, and
- report health and lifecycle state.

The SDK is a consumer-facing contract and must not become a second source of Platform authority.

## Shell Outcome

Mosaic has a Shell that renders the first Mosaic experience through the client-side Mosaic Design Language and Design System implementation.

The Shell should provide the stable host for navigation, identity, loading, errors, Module surfaces and accessibility preferences. It consumes semantic data and capabilities through the SDK rather than embedding Module-specific backend logic.

## Module Outcomes

The first Module set is delivered against the SDK and Shell contracts:

| Module | First-release role |
|--------|--------------------|
| `mosaic-jellyfin-api-module` | Reference integration for Jellyfin-backed media discovery and playback metadata. |
| `mosaic-remote-media-module` | Remote media capability and source integration. |
| `mosaic-anime-module` | Anime-specific discovery, metadata and experience capability. |

The Jellyfin API Module should be the first reference Module because it provides an external integration target against which the SDK, Supervisor and Shell contracts can be exercised.
