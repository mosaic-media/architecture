<!--
File: docs/engineering/guides/meg-008-observability/13-adrs.md
Document: MEG-008
Status: Draft
Version: 0.4
-->

# Architectural Decision Guidance

> *Decision history belongs in decision records. This chapter identifies when MEG-008 needs them and where readers should look for the governing process.*

---

# Purpose

MEG-008 may require architecture decisions when changes alter long-lived engineering direction, compatibility expectations or responsibility boundaries.

The decision process itself is governed by **[MDG-001 — Documentation Authority Guide](../../documentation/mdg-001-documentation-authority-guide/index.md)**.

This chapter avoids repeating ADR process rules so the documentation library has one authoritative home for decision practice.

---

# Decision Areas

Create or update a decision record when a change affects:

- Structured Logging
- Architecture-Owned Metrics
- Distributed Tracing Strategy
- Health Model
- Runtime Diagnostics
- OpenTelemetry Integration
- Alerting Strategy
- Capability Telemetry Ownership

---

# Relationship To [MDG-001](../../documentation/mdg-001-documentation-authority-guide/index.md)

[MDG-001](../../documentation/mdg-001-documentation-authority-guide/index.md) defines ADR structure, review expectations, lifecycle and cross-reference rules.

This guide should reference decisions that affect it, but should not redefine the decision process.

---

# Review Guidance

During review, confirm that the guide and any related decision record agree.

If a decision changes the meaning of this guide, update the affected chapter and reference the decision from this page.
