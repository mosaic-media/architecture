<!--
File: docs/engineering/guides/meg-008-observability/09-alerting.md
Document: MEG-008
Status: Draft
Version: 0.4
-->

# Alerting

> *Alerting is engineered restraint: notify humans only when human judgement is required.*

---

# Purpose

[MOP-001](../../operations/mop-001-observability-operations/index.md) defines operational alert handling.

This chapter explains how engineers should produce actionable alert signals.

---

# Engineering Guidance

Alerting should be driven by evidence from health, metrics, traces and diagnostics.

Logs alone should rarely raise alerts.

Alert implementations should avoid notifying people about conditions the Platform can recover automatically.

---

# Implementation Expectations

Alerts should include:

- affected responsibility
- severity
- observed evidence
- probable impact
- relevant diagnostic links or identifiers
- recommended first operator action

---

# Reference

Operational authority is provided by:

- [MOP-001 — Observability Operations](../../operations/mop-001-observability-operations/index.md)
