<!--
File: docs/engineering/protocols/mip-nnn-subject-protocol/04-versioning-and-compatibility.md
Document: MIP-NNN
Status: Draft
-->

<!--
Guidance
- This chapter is what makes a MIP a MIP. It states what may change without breaking implementations
  and what forces a new major version.
- Major integer versions only. No minor or patch component anywhere, per MDG-001 chapter 03.
- Name which side of the contract carries the compatibility burden. Unassigned burden is how
  protocols break.
-->

# 04 — Versioning And Compatibility

---

# Version Ownership

This document defines **Subject Protocol v1**.

The version describes the contract. It does not describe this document, which carries a Status like every other Mosaic specification.

---

# Compatible Changes

Changes that do not require a new major version:

- additions that a conforming implementation can ignore safely

---

# Breaking Changes

Changes that require a new major version:

- anything that would break an existing conforming implementation

---

# Compatibility Responsibilities

| Party | Responsibility |
|-------|----------------|
| Producer | what it must preserve |
| Consumer | what it must tolerate |
