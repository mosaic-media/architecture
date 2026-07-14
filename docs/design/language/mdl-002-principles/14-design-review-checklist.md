<!--
File: docs/design/language/mdl-002-principles/14-design-review-checklist.md
Document: MDL-002
Chapter: 14
Title: Design Review Checklist
Status: Draft
Version: 0.1
-->

# Design Review Checklist

---

# Purpose

The Mosaic Design Language is intended to reduce subjective design discussions.

This checklist provides a repeatable review process that evaluates proposals against MDL rather than individual preference.

Every significant proposal should complete this checklist before implementation begins.

The objective is not to block change.

The objective is to ensure that change strengthens Mosaic rather than gradually fragmenting it.

Structured review checklists improve consistency, reduce omissions and help teams evaluate work against agreed standards rather than personal taste.  [oai_citation:0‡WPDean](https://wpdean.com/design-system-documentation/?utm_source=chatgpt.com)

---

# When To Use This Checklist

This checklist should be completed for:

- New features
- New interaction patterns
- New components
- New navigation models
- New extension capabilities
- Material System changes
- Motion changes
- Composition changes
- Major refactors

Editorial documentation changes do not normally require a full review.

---

# Review Outcome

Every review should produce one of the following outcomes.

| Outcome | Meaning |
|----------|---------|
| Accepted | Ready for implementation |
| Accepted with Revisions | Minor changes required |
| Deferred | Requires additional research or prototyping |
| Rejected | Conflicts with MDL |
| Superseded | Replaced by another proposal |

Every rejected proposal should reference the relevant MDL principle or ADR.

---

# Section A

## Vision

### A1

Does the proposal strengthen the Vision defined by MDL-001?

- [ ] Yes
- [ ] No

---

### A2

Does it reduce friction?

- [ ] Yes
- [ ] No

---

### A3

Does it preserve immersion?

- [ ] Yes
- [ ] No

---

### A4

Would the product feel more like Mosaic if this proposal became standard everywhere?

- [ ] Yes
- [ ] No

---

# Section B

## Principle Alignment

### B1

Supports **Context Before Prediction**

- [ ] Yes
- [ ] No

---

### B2

Supports **Enhancement Before Persuasion**

- [ ] Yes
- [ ] No

---

### B3

Supports **Content Leads**

- [ ] Yes
- [ ] No

---

### B4

Supports **Movement Preserves Understanding**

- [ ] Yes
- [ ] No

---

### B5

Supports **Every Feature Earns Its Place**

- [ ] Yes
- [ ] No

---

### B6

Supports **The Platform Enables**

- [ ] Yes
- [ ] No

---

### B7

Supports **Be A Companion**

- [ ] Yes
- [ ] No

---

# Section C

## User Experience

### C1

Does the proposal reduce cognitive effort?

- [ ] Yes
- [ ] No

---

### C2

Does the proposal preserve the user's current context?

- [ ] Yes
- [ ] No

---

### C3

Will users understand what changed?

- [ ] Yes
- [ ] No

---

### C4

Does the proposal remove unnecessary decisions?

- [ ] Yes
- [ ] No

---

### C5

Would this interaction still feel understandable with animations disabled?

- [ ] Yes
- [ ] No

---

# Section D

## System Design

### D1

Can an existing Mosaic system solve this problem?

- [ ] Yes
- [ ] No

---

### D2

If "No", has a new system been justified?

- [ ] Yes
- [ ] No

---

### D3

Does the proposal introduce new terminology?

- [ ] Yes
- [ ] No

If yes:

Has existing terminology been evaluated first?

- [ ] Yes
- [ ] No

---

### D4

Does the proposal duplicate existing capability?

- [ ] Yes
- [ ] No

---

### D5

Does this increase long-term maintainability?

- [ ] Yes
- [ ] No

---

# Section E

## Platform

### E1

Does this capability belong in the core platform?

- [ ] Yes
- [ ] No

---

### E2

Would an extension provide a better solution?

- [ ] Yes
- [ ] No

---

### E3

Does the proposal strengthen the extension ecosystem?

- [ ] Yes
- [ ] No

---

### E4

Does the proposal expose implementation details?

- [ ] Yes
- [ ] No

If yes:

Redesign before implementation.

---

# Section F

## Accessibility

### F1

Does the proposal maintain keyboard accessibility?

- [ ] Yes
- [ ] No

---

### F2

Does it remain understandable using reduced motion?

- [ ] Yes
- [ ] No

---

### F3

Does it maintain visual hierarchy?

- [ ] Yes
- [ ] No

---

### F4

Does it improve accessibility rather than merely preserve it?

- [ ] Yes
- [ ] No

---

# Section G

## Companion Behaviour

### G1

Would a trusted companion behave this way?

- [ ] Yes
- [ ] No

---

### G2

Does this interrupt unnecessarily?

- [ ] Yes
- [ ] No

---

### G3

Does this increase trust?

- [ ] Yes
- [ ] No

---

### G4

Once the proposal has completed its purpose, does the interface quietly step back?

- [ ] Yes
- [ ] No

---

# Automatic Rejection Criteria

The proposal should normally be rejected if it:

- introduces unnecessary friction
- weakens immersion
- duplicates an existing system
- competes with entertainment for attention
- introduces new terminology without justification
- exposes implementation details
- optimises engagement over understanding
- requires explanation before becoming understandable

---

# Principle Traceability

Every proposal should explicitly reference:

```
Relevant Principles

Relevant ADRs

Affected Specifications

Migration Impact

Future Work
```

Traceability ensures future contributors understand not only what changed, but why it changed.

---

# Final Question

Before approval, every reviewer should answer the following question.

> **If every future feature behaved like this proposal, would Mosaic become a better entertainment companion?**

If the answer is uncertain, further iteration is recommended before implementation.

---

# Review Record

```text
Specification:

Reviewer(s):

Date:

Outcome:

Relevant Principles:

Relevant ADRs:

Follow-up Actions:

Implementation Notes:

Comments:
```

---

# Review Status

**Status**

Draft

**Next File**

`glossary.md`
