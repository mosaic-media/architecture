<!--
File: docs/engineering/guides/meg-008-observability/05-health-model.md
Document: MEG-008
Status: Draft
-->

# Health Model

> *Health is an operational contract. Engineering should make that contract observable and reliable.*

---

# Purpose

MEG-008 explains how engineers build observability into Mosaic.

Operational health interpretation is defined by **[MOP-001 — Observability Operations](../../operations/mop-001-observability-operations/index.md)**.

This chapter describes the engineering work required to support that model.

---

# Engineering Guidance

Every component that owns an architectural responsibility should expose health that answers one question:

> **Can this component currently fulfil its responsibility?**

Health should not become a log stream, metric dashboard or business correctness signal.

---

# Implementation Expectations

Health implementations should be:

- cheap to evaluate
- deterministic
- safe to expose
- tied to explicit responsibility
- useful for diagnostics and alerting

---

# Reference

Operational authority is provided by:

- [MOP-001 — Observability Operations](../../operations/mop-001-observability-operations/index.md)
