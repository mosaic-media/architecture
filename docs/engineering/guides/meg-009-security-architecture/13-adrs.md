<!--
File: docs/engineering/guides/meg-009-security-architecture/13-adrs.md
Document: MEG-009
Status: Draft
-->

# Architectural Decision Guidance

> *Decision history belongs in decision records. This chapter identifies when MEG-009 needs them and where readers should look for the governing process.*

---

# Purpose

MEG-009 may require architecture decisions when changes alter long-lived engineering direction, compatibility expectations or responsibility boundaries.

The decision process itself is governed by **[MDG-001 — Documentation Authority Guide](../../documentation/mdg-001-documentation-authority-guide/index.md)**.

This chapter avoids repeating ADR process rules so the documentation library has one authoritative home for decision practice.

---

# Decision Areas

Create or update a decision record when a change affects:

- Zero Trust Runtime
- Capability Permission Model
- Runtime-Owned Secrets
- Module Trust Pipeline
- Security Observability
- Network Trust Boundaries
- Cryptographic Strategy
- Authentication Architecture
- Registered Device And Session Revocation Architecture

---

# Relationship To [MDG-001](../../documentation/mdg-001-documentation-authority-guide/index.md)

[MDG-001](../../documentation/mdg-001-documentation-authority-guide/index.md) defines ADR structure, review expectations, lifecycle and cross-reference rules.

This guide should reference decisions that affect it, but should not redefine the decision process.

---

# Review Guidance

During review, confirm that the guide and any related decision record agree.

If a decision changes the meaning of this guide, update the affected chapter and reference the decision from this page.
