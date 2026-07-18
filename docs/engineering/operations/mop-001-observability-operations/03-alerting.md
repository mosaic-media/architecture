<!--
File: docs/engineering/operations/mop-001-observability-operations/03-alerting.md
Document: MOP-001
Status: Draft
-->

# 03 — Alerting

---

# Purpose

Alerting identifies conditions that require human attention.

It should not notify people about every failure.

Automation should handle recoverable conditions.

Humans should be alerted when automation cannot preserve availability, correctness or safety.

---

# Severity

Alert severity should reflect operational impact.

Use severity to communicate urgency, not implementation difficulty.

---

# Alert Context

Every actionable alert should explain:

- affected responsibility
- observed evidence
- probable impact
- relevant diagnostics
- immediate operator action

---

# Operational Rule

> **Alert people only when human judgement is required.**
