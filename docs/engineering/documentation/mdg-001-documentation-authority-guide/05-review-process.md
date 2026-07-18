<!--
File: docs/engineering/documentation/mdg-001-documentation-authority-guide/05-review-process.md
Document: MDG-001
Status: Active
-->

# 05 — Review Process

---

# Purpose

Every Mosaic document should undergo review before it is considered authoritative.

Documentation review is an architectural activity rather than a proofreading exercise.

The objective of review is to ensure that documentation remains:

- technically accurate
- internally consistent
- architecturally aligned
- understandable
- maintainable

Review should improve the quality of both the document and the architecture it describes.

---

# Review Philosophy

Documentation should evolve deliberately.

Review should identify:

- ambiguity
- inconsistency
- duplication
- obsolete concepts
- architectural drift
- incorrect terminology

Review should not introduce unnecessary complexity or stylistic variation.

Consistency across the documentation library is more valuable than individual author preference.

---

# Review Responsibilities

Every review should consider three independent perspectives.

## Editorial Review

Editorial review focuses on readability.

Typical activities include:

- grammar
- spelling
- sentence structure
- clarity
- formatting
- consistency

Editorial review should not alter architectural meaning.

---

## Structural Review

Structural review focuses on organisation.

Typical activities include:

- chapter ordering
- navigation
- section hierarchy
- document flow
- information grouping

Readers should be able to navigate documents predictably regardless of author.

---

## Technical Review

Technical review validates correctness.

Typical activities include:

- architectural accuracy
- engineering correctness
- terminology
- implementation alignment
- references
- diagrams

Technical review should be performed by individuals familiar with the subject matter.

---

# Architecture Review

Documents describing architecture require additional review.

Architecture review should verify:

- consistency with the Architecture Canon
- consistency with accepted Architecture Decisions
- compatibility with existing protocols
- consistency of terminology
- conceptual integrity

Where architectural disagreement exists, documentation should not be updated until consensus has been reached.

---

# Documentation Checklist

Before approval, authors should confirm the following.

## General

- Purpose is clearly stated.
- Scope is defined.
- Audience is appropriate.
- Terminology is consistent.

## Structure

- Chapters follow the standard structure.
- Headings are descriptive.
- Navigation is logical.
- Information progresses naturally.

## Content

- Concepts are explained before use.
- Duplication has been minimised.
- References are accurate.
- Diagrams support the text.

## Quality

- Markdown renders correctly.
- Tables are readable.
- Code examples compile where applicable.
- References and glossary are complete.

---

# Cross-Document Review

Documentation should never be reviewed in isolation.

Reviewers should verify:

- referenced documents still exist
- terminology matches related specifications
- duplicated concepts have not diverged
- architectural relationships remain correct

Where inconsistencies are discovered, the authoritative document should be updated rather than introducing additional explanation elsewhere.

---

# Review Outcomes

A review should conclude with one of the following outcomes.

| Outcome | Description |
|----------|-------------|
| Accepted | Document satisfies review objectives. |
| Accepted with Minor Changes | Minor corrections required before publication. |
| Requires Revision | Significant changes required before approval. |
| Superseded | Document should be replaced by another specification. |
| Archived | Document retained for historical purposes only. |

Review outcomes describe the conclusion of a review. They are not Status values. An outcome of Superseded results in `Status: Superseded`, and an outcome of Archived results in `Status: Deprecated` or `Status: Superseded` according to whether a replacement exists.

Review outcomes should be constructive and documented.

---

# Architectural Drift

One of the primary responsibilities of review is detecting architectural drift.

Architectural drift occurs when:

- implementation evolves beyond the documented architecture
- documentation evolves independently of implementation
- terminology changes inconsistently
- duplicated concepts diverge

When architectural drift is identified, the preferred resolution is to update the authoritative document rather than introducing local corrections elsewhere.

---

# Review Milestones And Status

Review milestones are recorded as completed review activities rather than as a numeric progression.

A document does not advance a version as each review completes. It remains `Status: Review` until every required review has concluded, and then becomes `Status: Active`.

| Review Activity | Effect On Status |
|-----------------|------------------|
| Editorial Review | No change. Recorded as a completed review activity. |
| Structural Review | No change. Recorded as a completed review activity. |
| Cross-reference Review | No change. Recorded as a completed review activity. |
| Technical Review | No change. Recorded as a completed review activity. |
| All required reviews complete | Review → Active. |
| Review requires substantial rewriting | Review → Draft. |

Review completion is therefore traceable through Git history and through the document revision history rather than through a version number.

The Status lifecycle is defined within [03 — Status And Versioning](03-versioning.md).

---

# Continuous Improvement

Publication is not the end of review.

As the Mosaic platform evolves, documentation should be revisited to ensure it continues to represent the current understanding of the architecture.

Reviews should therefore be viewed as an ongoing engineering responsibility rather than a one-time publishing activity.

High-quality documentation is maintained through continuous refinement rather than occasional large-scale rewrites.
