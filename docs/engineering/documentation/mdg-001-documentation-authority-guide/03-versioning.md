<!--
File: docs/engineering/documentation/mdg-001-documentation-authority-guide/03-versioning.md
Document: MDG-001
Status: Draft
Version: 0.1
-->

# 03 — Versioning

---

# Purpose

Versioning communicates the maturity of a document rather than the maturity of the implementation it describes.

Documentation versions allow readers to understand:

- how stable the information is
- whether the document is still evolving
- whether architectural review has completed
- whether the document should be considered authoritative

Documentation version numbers are therefore independent of software release versions.

---

# Guiding Principles

Documentation versioning should:

- communicate document maturity
- remain predictable
- encourage deliberate progression
- avoid unnecessary version inflation
- reflect meaningful review milestones

Version numbers should never be incremented solely because time has passed.

---

# Version Progression

Documentation progresses through a defined lifecycle.

| Version | Meaning |
|---------:|---------|
| 0.1 | Initial draft. |
| 0.2 | Editorial review completed. |
| 0.3 | Structural review completed. |
| 0.4 | Cross-reference review completed. |
| 0.5 | Technical review completed. |
| 0.6–0.8 | Iterative refinement. |
| 0.9 | Candidate for approval. |
| 1.0 | Canonical release. |

Each progression represents a measurable improvement in document quality.

---

# Initial Draft (0.1)

Version **0.1** represents the first complete expression of an idea.

The objective is to establish:

- purpose
- scope
- philosophy
- overall direction

Documents at this stage should prioritise clarity of intent over completeness.

Large revisions are expected.

---

# Editorial Review (0.2)

Version **0.2** indicates the document has undergone editorial review.

Typical improvements include:

- improved consistency
- clearer language
- corrected terminology
- improved structure
- removal of duplication
- alignment with documentation standards

Editorial review should not substantially alter architectural intent.

---

# Structural Review (0.3)

Version **0.3** confirms the document structure has been reviewed.

Typical activities include:

- chapter organisation
- navigation improvements
- section ordering
- improved hierarchy
- better separation of concerns

Readers should now find the document significantly easier to navigate.

---

# Cross-Reference Review (0.4)

Version **0.4** focuses on integration with the wider documentation library.

Typical activities include:

- validating references
- removing duplicated concepts
- improving traceability
- linking related specifications
- ensuring glossary consistency

The documentation should increasingly behave as a connected knowledge base rather than isolated documents.

---

# Technical Review (0.5)

Version **0.5** confirms that subject matter experts have reviewed the technical accuracy of the document.

Reviewers should verify:

- architectural correctness
- engineering accuracy
- terminology
- consistency with the Architecture Canon
- consistency with accepted Architecture Decisions

At this stage the document should accurately represent the current understanding of the platform.

---

# Refinement (0.6 – 0.8)

Versions between **0.6** and **0.8** represent iterative improvement.

Typical changes include:

- clarification
- expanded examples
- improved diagrams
- improved explanations
- incorporation of review feedback

These revisions should refine the document rather than redefine it.

Major architectural changes should instead begin with a new Mosaic Design Proposal.

---

# Candidate (0.9)

Version **0.9** indicates the document is considered complete pending final approval.

Only minor changes should occur at this stage.

Examples include:

- typographical corrections
- formatting improvements
- reference validation
- final editorial polish

Architectural changes should generally be avoided.

---

# Canonical Release (1.0)

Version **1.0** represents the first canonical publication of the document.

For Architecture Canon documents this indicates:

- architectural consensus
- editorial completion
- technical approval

Version 1.0 documents become authoritative references for subsequent documentation.

---

# Version Increment Policy

Version numbers should increase only when meaningful improvements occur.

Examples include:

| Change | Version Increment |
|---------|-------------------|
| Editorial improvements | Minor draft progression |
| Structural reorganisation | Minor draft progression |
| New chapters | Minor draft progression |
| Significant architectural revision | New draft cycle or major version |
| Typographical corrections | No version change (unless part of a scheduled review) |

Version inflation should be avoided.

---

# Status Relationship

Document version and document status are related but independent.

For example:

| Status | Typical Versions |
|---------|------------------|
| Draft | 0.1 – 0.9 |
| Approved | 1.x |
| Superseded | Any |
| Archived | Any |

Changing status does not automatically require a version increment.

Likewise, version progression does not imply approval.

---

# Major Versions

Major version increments should represent significant changes to the document itself.

Examples include:

- substantial architectural revision
- restructuring due to accepted Design Proposals
- replacement of obsolete concepts
- changes to governing principles

Major versions should remain relatively rare.

Frequent major version increments indicate architectural instability.

---

# Document History

Every document should maintain version metadata within its Document Control chapter.

Where appropriate, a revision history may also be maintained.

Revision histories should summarise meaningful changes rather than listing every editorial correction.

This preserves the readability of the specification while maintaining appropriate historical traceability.
