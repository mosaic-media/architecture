<!--
File: docs/design/system/mds-006-composition-engine/01-supersession.md
Document: MDS-006
Status: Superseded
-->

# 01 — Supersession

---

# What Changed

MDS-006 — Composition Engine was published as an active Design System specification and later withdrawn.

Its content was not discarded. It was moved into the deferred proposal [MDP-001 — Adaptive Composition Runtime](../../../engineering/architecture/mdp-001-adaptive-composition-runtime/index.md), where it is preserved in full as research.

Separately, the parts of the subject that Mosaic v1 genuinely needs were taken up by [MDS-008 — Component Library](../mds-008-component-library/index.md), which is authoritative for the v1 implementation.

---

# Reading Guidance

The two destinations answer different questions, and confusing them is the risk this record exists to prevent.

- **Building Mosaic today.** Read [MDS-008](../mds-008-component-library/index.md). It is authoritative, current, and describes what the platform actually implements.
- **Understanding where the adaptive model was heading.** Read [MDP-001](../../../engineering/architecture/mdp-001-adaptive-composition-runtime/index.md). It is explicitly non-authoritative and unscheduled, and it must not be used to establish implementation requirements.

A term may appear in both with different meanings. The v1 definition governs.

---

# Traceability

| Aspect | Record |
|--------|--------|
| Decision to ship v1 as a component library | ADR-204 in [MDS-008](../mds-008-component-library/12-adrs.md) |
| Decision to defer the adaptive runtime | ADR-205 in [MDS-008](../mds-008-component-library/12-adrs.md) |
| Preserved research | [MDP-001 — Adaptive Composition Runtime](../../../engineering/architecture/mdp-001-adaptive-composition-runtime/index.md) |
| Retired identifier registry | `chapter-registry.yml` at the repository root |

---

# Identifier Reuse

The MDS-006 identifier is retired permanently. A future Design System specification takes the next free number rather than reoccupying this one, so that every reference written against MDS-006 keeps resolving to the same subject.
