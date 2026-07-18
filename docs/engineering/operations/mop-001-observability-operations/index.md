<!--
File: docs/engineering/operations/mop-001-observability-operations/index.md
Document: MOP-001
Status: Draft
-->

# MOP-001 — Observability Operations

> *Observability becomes operational value only when it helps people understand when to act, why to act and what to inspect first.*

---

# Purpose

MOP-001 defines operational expectations for Mosaic health, diagnostics, alerting and debugging.

[MEG-008](../../guides/meg-008-observability/index.md) explains observability engineering guidance.

MOP-001 defines how Mosaic should be operated using those observability surfaces.

---

# Operations Statement

Within Mosaic:

> **Operations should intervene only when the Platform can explain why intervention is required.**

Logs, metrics, traces, health, diagnostics and alerts should form one operational story.

---

# Scope

This playbook defines:

- health interpretation
- diagnostic expectations
- alert handling
- debugging boundaries
- operational review expectations

It does not define telemetry implementation, observability vendor configuration or code-level instrumentation patterns.
