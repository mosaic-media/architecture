<!--
File: docs/engineering/operations/mop-001-observability-operations/04-debugging.md
Document: MOP-001
Status: Draft
-->

# 04 — Debugging

---

# Purpose

Debugging provides controlled investigation when ordinary observability cannot explain behaviour.

It should be deterministic, safe, observable and non-invasive.

---

# Debugging Boundary

Debugging should not become a normal operational workflow.

If operators routinely require debugging to understand production behaviour, the observability model should improve.

---

# Debugging Safety

Debugging mechanisms should avoid:

- changing production behaviour
- bypassing permissions
- exposing secrets
- relying on private implementation state
- creating hidden operational APIs

---

# Operational Rule

> **Debugging should explain behaviour without changing it.**
