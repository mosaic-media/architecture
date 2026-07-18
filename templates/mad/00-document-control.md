<!--
File: docs/engineering/architecture/mad-nnn-<decision-slug>/00-document-control.md
Document: MAD-NNN
Status: Draft
-->

<!--
Guidance
- Status describes this record's own documentation lifecycle (MDG-001 chapter 03).
- Decision Status describes the decision it captures, which is a different thing. A record may be
  Status: Draft while the decision it preserves is already Accepted.
- Authority states plainly what this record does not own. A MAD never defines architecture and
  never provides implementation guidance.
- Affected Specifications names every document the decision touches and what it did to each,
  including the documents it deliberately left unchanged.
-->

# Document Control

---

# Document Information

| Field | Value |
|-------|-------|
| Document | MAD-NNN |
| Title | <Decision Title> |
| Status | Draft |
| Decision Status | Accepted |
| Owner | <git-username> |
| Audience | <who needs to read this> |
| Classification | Architecture decision record |

`Status` describes this record's own documentation lifecycle. `Decision Status` describes the decision it captures.

---

# Authority

MAD-NNN records a single accepted decision. It does not define architecture and it does not provide implementation guidance.

- The accepted architecture it depends upon is owned by [<ID> — <Canonical Title>](<relative/path/index.md>).
- The contract shape it changes is owned by [<ID> — <Canonical Title>](<relative/path/index.md>).

Per [MDG-001 — Documentation Authority Guide](../../documentation/mdg-001-documentation-authority-guide/02-document-types.md), a decision record preserves reasoning and alternatives that must not live inside Canon or Engineering Guides. This record should remain effectively immutable; a later change of direction should be captured as a new decision rather than by rewriting this one.

---

# Affected Specifications

| Specification | Effect |
|---------------|--------|
| [<ID> — <Canonical Title>](<relative/path/index.md>) | <What changed. Which document carries the decision.> |
| [<ID> — <Canonical Title>](<relative/path/index.md>) | Unchanged. <Which principle is honoured rather than altered.> |

---

# Required Reading

<!-- The minimum a reader needs to evaluate this decision. Link chapters, not just index pages. -->

- [<ID> — <Canonical Title>](<relative/path/NN-chapter.md>)
