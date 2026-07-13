<!--
File: engineering/meg/MEG-001 Go Engineering Standards/00-document-control.md
Document: MEG-001
Status: Draft
Version: 0.1
-->

# Document Control

---

# Document Information

| Field | Value |
|---------|--------|
| Document ID | MEG-001 |
| Title | Go Engineering Standards |
| File | 00-document-control.md |
| Status | Draft |
| Version | 0.1 |
| Owner | Lead Software Architect |
| Classification | Internal Architecture Specification |

---

# Purpose

This document establishes the governance, authority and lifecycle of the Mosaic Engineering Guidelines (MEG).

It defines how engineering standards are created, reviewed and maintained throughout the Mosaic ecosystem.

Unlike implementation documentation, MEG specifications are considered **normative architectural standards**.

Where guidance within this specification conflicts with implementation, the discrepancy must be resolved rather than ignored.

---

# Authority

MEG specifications define the canonical engineering standards for every Go codebase within Mosaic.

This includes, but is not limited to:

- Backend services
- APIs
- Workers
- Background jobs
- SDKs
- CLI applications
- Infrastructure tooling
- Shared libraries

Individual repositories may introduce additional standards provided they do not conflict with this specification.

---

# Normative Language

Unless explicitly stated otherwise, the keywords below are interpreted using the definitions established by RFC 2119.

| Keyword | Meaning |
|----------|---------|
| **MUST** | Mandatory requirement. |
| **MUST NOT** | Behaviour that is prohibited. |
| **SHOULD** | Strong recommendation. Deviation requires clear justification. |
| **SHOULD NOT** | Generally discouraged. Exceptions should be documented. |
| **MAY** | Optional behaviour determined by engineering judgement. |

Examples and code samples contained within this specification are **informative**, unless explicitly stated otherwise. This mirrors common standards-writing practice where examples explain intent rather than introduce mandatory behaviour.  [oai_citation:0‡W3C](https://w3c.github.io/manual-of-style/?utm_source=chatgpt.com)

---

# Document Lifecycle

Every MEG specification progresses through the following lifecycle.

```
Draft

↓

Review

↓

Accepted

↓

Implemented

↓

Maintained

↓

Superseded (optional)
```

Engineering standards are expected to evolve alongside the Mosaic platform.

The handbook is therefore considered a living specification.

---

# Change Management

Changes to accepted engineering standards SHOULD be made through an Architectural Decision Record (ADR).

Minor improvements may be made directly when they:

- improve clarity
- correct mistakes
- expand examples
- add references
- improve terminology

Changes that alter engineering philosophy, architectural direction or implementation expectations MUST be accompanied by an ADR.

---

# Compliance

All Go repositories within the Mosaic organisation SHOULD comply with this specification.

Where deviation is necessary, the repository SHOULD document:

- the reason
- the expected impact
- why the standard cannot reasonably be followed

Temporary deviations should eventually be removed.

Permanent deviations should result in an update to the handbook if they represent a better engineering approach.

---

# Engineering Philosophy

The purpose of these standards is not to maximise theoretical purity.

The purpose is to produce software that is:

- understandable
- maintainable
- predictable
- testable
- observable
- performant
- enjoyable to work on

Engineering judgement always takes precedence over blindly following rules.

A rule that consistently makes software worse should be challenged through architecture review rather than ignored.

---

# External References

The MEG builds upon established Go guidance rather than replacing it.

Primary references include:

- Effective Go
- Go Code Review Comments
- Go Documentation Guidelines

Where Mosaic introduces additional conventions, those conventions exist to improve consistency across the project rather than redefine the Go language itself. The Go project itself describes the Code Review Comments as a supplement to *Effective Go*, not a complete style guide, which is the philosophy adopted here.  [oai_citation:1‡Google Source](https://go.googlesource.com/wiki/%2B/6fe9f52ac7c4d92cb8fc878d8dee1bda0c63c8a5/CodeReviewComments.md?utm_source=chatgpt.com)

---

# Review Status

**Status**

Draft

**Owner**

Lead Software Architect

**Previous File**

`README.md`

**Next File**

`01-engineering-philosophy.md`
