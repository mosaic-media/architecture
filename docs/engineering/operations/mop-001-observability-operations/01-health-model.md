<!--
File: docs/engineering/operations/mop-001-observability-operations/01-health-model.md
Document: MOP-001
Status: Draft
-->

# 01 — Health Model

---

# Purpose

Health communicates whether a component can currently fulfil its architectural responsibility.

It does not mean that nothing is wrong.

It means the component can still perform its role.

---

# Health Interpretation

Operators should interpret health through responsibility:

- Platform health reflects execution readiness.
- Runtime health reflects service coordination.
- capability health reflects product behaviour readiness.
- storage health reflects persistence availability.
- infrastructure health reflects environmental dependencies.

---

# Operational Rule

> **Health tells operators whether a responsibility can still be fulfilled. Diagnostics explain why.**
