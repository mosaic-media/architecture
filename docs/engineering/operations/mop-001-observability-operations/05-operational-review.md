<!--
File: docs/engineering/operations/mop-001-observability-operations/05-operational-review.md
Document: MOP-001
Status: Draft
-->

# 05 — Operational Review

---

# Purpose

Operational review keeps observability useful as Mosaic evolves.

Every meaningful Platform, Runtime, capability or module change should consider whether operations remain clear.

---

# Review Questions

Operational review should ask:

- Can operators identify whether the component is healthy?
- Can diagnostics explain the component's current structure?
- Are alerts actionable and sparse?
- Can debugging occur safely when needed?
- Are secrets and sensitive data protected?
- Does the operational story reference the authoritative architecture and protocols?

---

# Review Rule

> **A component is not operationally ready until it can explain failure without requiring implementation knowledge.**
