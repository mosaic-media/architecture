<!--
File: docs/engineering/protocols/mip-001-event-protocol/index.md
Document: MIP-001
Status: Draft
Version: 0.4
-->

# MIP-001 — Event Protocol

> *Events are the shared language of Mosaic. The Protocol keeps that language stable as capabilities evolve independently.*

---

# Purpose

MIP-001 defines the canonical event contract used by Mosaic capabilities, modules, Runtime Services and observability tooling.

[MEG-002](../../guides/meg-002-event-driven-runtime/index.md) explains how engineers build event-driven behaviour.

MIP-001 defines the protocol those implementations must preserve.

---

# Protocol Statement

Within Mosaic:

> **The Platform transports events. Modules give events meaning.**

Every event consists of an immutable Platform envelope surrounding an immutable payload.

The SDK defines the envelope.

The Platform owns transport, routing, delivery and reliability.

Modules own domain event names, payloads, semantics, documentation and versioning.

---

# Scope

This protocol defines:

- event model
- event envelope
- naming rules
- versioning rules
- compatibility expectations
- event ownership
- public and private Module event visibility

It does not define:

- subscriber implementation
- event bus internals
- retry strategy
- storage implementation
- business payload schemas for individual domains
