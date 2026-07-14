<!--
File: docs/engineering/documentation/mdg-001-documentation-authority-guide/09-governance.md
Document: MDG-001
Status: Draft
Version: 0.1
-->

# 09 — Governance

---

# Purpose

Documentation governance ensures that the Mosaic documentation library remains authoritative, coherent and maintainable throughout the lifetime of the project.

Governance establishes ownership, responsibility and accountability for documentation while encouraging contributions from the wider community.

Without governance, documentation inevitably diverges from implementation and gradually loses authority.

---

# Documentation as Authority

Within the Mosaic Architecture repository, documentation is considered the authoritative description of the platform.

Implementation should realise the documented architecture.

Where implementation and documentation differ, one of the following actions should occur:

- the implementation should be updated to match the documented architecture; or
- the documentation should be formally revised following the lifecycle defined within this guide.

Architecture should never silently evolve through implementation alone.

---

# Ownership

Every specification should have an identified owner.

Ownership is responsible for:

- maintaining technical accuracy
- reviewing proposed changes
- ensuring consistency with related specifications
- preserving architectural intent

Ownership does not imply exclusive authorship.

Contributors are encouraged to improve documentation while respecting the governing principles established within this guide.

---

# Responsibilities

Document owners should:

- review proposed changes
- maintain document quality
- approve editorial improvements
- ensure references remain valid
- maintain terminology consistency
- identify obsolete information

Ownership should focus upon stewardship rather than control.

---

# Contributors

Any contributor may propose improvements to documentation.

Examples include:

- correcting inaccuracies
- improving clarity
- fixing references
- updating diagrams
- improving navigation
- correcting terminology

Contributors should avoid introducing architectural changes directly into authoritative documentation.

Architectural change should instead follow the documented proposal process.

---

# Architectural Changes

Changes affecting architectural behaviour should follow the established documentation lifecycle.

Typically:

```text
Proposal

↓

Architecture Review

↓

Architecture Decision

↓

Architecture Canon

↓

Supporting Documentation
```

Direct modification of accepted architectural documents without appropriate review should be avoided.

---

# Editorial Changes

Editorial improvements may be made without initiating a Design Proposal provided they do not alter architectural meaning.

Examples include:

- spelling corrections
- grammar improvements
- formatting
- improved readability
- improved examples
- navigation improvements

Editorial review should preserve technical intent.

---

# Review Authority

Different review activities require different expertise.

| Review Type | Typical Reviewer |
|-------------|------------------|
| Editorial | Documentation author or reviewer |
| Structural | Documentation maintainer |
| Technical | Subject matter expert |
| Architectural | Architecture owner or maintainers |

Large architectural changes should receive architectural review before becoming authoritative.

---

# Consistency

Consistency is considered a governance responsibility.

Reviewers should actively identify:

- duplicated concepts
- conflicting terminology
- inconsistent diagrams
- conflicting guidance
- obsolete references

Where inconsistency exists, the authoritative specification should be updated rather than introducing additional explanation elsewhere.

---

# Deprecation

When documentation becomes obsolete it should not normally be removed immediately.

Instead it should be:

1. marked as **Superseded**;
2. linked to the replacement specification;
3. retained until historical value no longer exists.

Maintaining architectural history improves long-term traceability.

---

# Repository Health

The documentation library should be treated as a maintained engineering asset.

Regular review should identify:

- broken references
- inconsistent terminology
- missing glossaries
- outdated diagrams
- incomplete specifications
- orphaned documents

Documentation health should improve continuously alongside the platform itself.

---

# Automation

Where practical, documentation governance should be supported by automation.

Future tooling should validate:

- document metadata
- document numbering
- version consistency
- repository organisation
- reference integrity
- glossary completeness
- duplicate terminology
- Markdown formatting

Automation should reduce repetitive review work while allowing reviewers to focus upon architectural quality.

---

# Long-Term Stewardship

The Mosaic Architecture repository is intended to remain valuable throughout the lifetime of the platform.

Governance should therefore prioritise:

- clarity over novelty;
- consistency over personal preference;
- architectural integrity over implementation convenience;
- long-term maintainability over short-term expedience.

Good documentation should allow future contributors to understand not only how Mosaic is built, but why it was designed that way.

Maintaining that understanding is the primary responsibility of documentation governance.
