<!--
File: docs/engineering/architecture/mac-001-platform-architecture/01-platform-model.md
Document: MAC-001
Status: Draft
-->

# 01 — Platform Model

---

# Purpose

The Platform is the stable runtime on which Mosaic capabilities execute.

It provides the environment in which independently evolving capabilities can be discovered, composed, executed, observed and governed.

The Platform should evolve slowly.

Most user-facing functionality should evolve outside the Platform.

---

# Definition

Within Mosaic, the Platform is the combination of:

- Runtime
- Capability Managers
- Event Bus
- permissions
- identity and session authority
- policy decision point and permission enforcement
- storage
- scheduler
- configuration
- GraphQL
- Service Registry
- capability registry
- module admission
- execution services
- resource ownership
- observability surfaces
- security and permission enforcement

The Platform does not own product behaviour. Its infrastructure implementations also remain behind ports: the Platform core defines the contract, while built-in infrastructure Modules provide the adapters.

It owns the execution environment in which product behaviour can run together coherently.

The Platform also does not own Mosaic's public HTTP entry point, Shell lifecycle, installation, updates, rollback or recovery.

Those host-level responsibilities belong to the Supervisor.

---

# Platform Responsibilities

The Platform owns responsibilities that must remain consistent across all capabilities.

These include:

- execution
- lifecycle
- dependency composition
- scheduling
- capability discovery
- capability orchestration
- module admission
- contract definition
- provider routing
- event transport
- API assembly
- Runtime SDUI production
- operational visibility
- fault isolation
- permission enforcement

These responsibilities are architectural infrastructure.

They allow capabilities to focus on behaviour rather than hosting themselves.

---

# Product Responsibilities

Product behaviour belongs outside the Platform.

Examples include:

- playback
- metadata
- Jellyfin integration
- AniList integration
- TMDB integration
- recommendations
- search providers
- artwork providers
- transcoding
- domain-specific media behaviour

These behaviours may be delivered by first-party modules, third-party modules or built-in capabilities.

They should still execute through the same Platform model.

---

# Architectural Rule

> **The Platform becomes stronger by standardising how capabilities run, not by absorbing what capabilities do.**

This rule prevents Mosaic from becoming a monolith as new product areas are added.

---

# Design Goals

The Platform should remain:

- stable,
- lightweight,
- long-lived,
- domain independent,
- extensible,
- testable,
- deterministic.

Architecture should evolve far more slowly than Modules.

## Infrastructure adapters

The Platform core follows hexagonal architecture. Storage, analytical processing, event persistence, cryptography, scheduling and other infrastructure concerns are ports owned by Platform contracts; their concrete implementations are Modules compiled into the Platform binary. Because these are ports, the Platform mandates the capability rather than the engine that provides it — analytical processing, for example, is satisfied by the storage engine today and may gain a dedicated engine as a further essential Module without changing the contract.

Some adapters are mandatory and are not user-selectable. For example, the PostgreSQL adapter is a built-in storage Module required by the first Platform distribution. It remains replaceable at the contract boundary, allowing a future compatible database adapter without allowing arbitrary runtime provider selection.
