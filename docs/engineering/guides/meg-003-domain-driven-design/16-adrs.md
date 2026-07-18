<!--
File: docs/engineering/guides/meg-003-domain-driven-design/16-adrs.md
Document: MEG-003
Status: Draft
-->

# Architectural Decision Guidance

> *Decision history belongs in decision records. This chapter identifies when MEG-003 needs them and where readers should look for the governing process.*

---

# Purpose

MEG-003 may require architecture decisions when changes alter long-lived engineering direction, compatibility expectations or responsibility boundaries. The decision process itself is governed by **[MDG-001 — Documentation Authority Guide](../../documentation/mdg-001-documentation-authority-guide/index.md)**, and this chapter avoids repeating those ADR process rules so that the documentation library retains one authoritative home for decision practice.

---

# Decision Areas

Each of the following areas fixes a responsibility boundary that chapters of this guide depend upon, so create or update a decision record when a change affects:

- Library Is The Core Aggregate
- Playback As Independent Context
- Metadata Ownership
- Continue Watching Model
- Recommendation Domain
- Media Identity Strategy
- Collection Ownership

Because a decision in any of these areas can change what this guide means, the record and the affected chapter have to move together.

---

# Relationship To [MDG-001](../../documentation/mdg-001-documentation-authority-guide/index.md)

[MDG-001](../../documentation/mdg-001-documentation-authority-guide/index.md) defines ADR structure, review expectations, lifecycle and cross-reference rules, which means this guide should reference the decisions that affect it but should not redefine the decision process itself.

---

# Review Guidance

During review, confirm that the guide and any related decision record agree. Where a decision changes the meaning of this guide, update the affected chapter and reference the decision from this page.
