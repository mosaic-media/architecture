<!--
File: docs/design/language/mdl-001-vision/10-design-review-checklist.md
Document: MDL-001
Chapter: 10
Title: Design Review Checklist
Status: Draft
Version: 0.1
-->

# Design Review Checklist

---

# Purpose

The purpose of this checklist is to provide a consistent framework for reviewing design proposals against the Mosaic Design Language.

The checklist exists to remove subjectivity from design discussions.

Rather than asking:

> "Do we like this?"

Reviewers should ask:

> "Does this align with MDL?"

Every significant feature, interaction, component, motion system or architectural proposal should be reviewed against this checklist before implementation.

Structured design review checklists are widely used because they improve consistency, reduce omissions and encourage objective discussions over subjective preference.  [oai_citation:0‡Smartsheet](https://www.smartsheet.com/content/design-review-checklist-templates?utm_source=chatgpt.com)

---

# Review Philosophy

Design reviews exist to answer one question.

> **Does this proposal make Mosaic feel more like Mosaic?**

Reviews are not intended to:

- approve personal preferences
- optimise visual novelty
- reward technical complexity

Instead they protect the long-term integrity of the design language.

---

# Review Levels

Every proposal should be classified before review.

| Level | Examples | Review Required |
|--------|----------|-----------------|
| Editorial | Documentation, wording | Maintainer |
| Minor Design | Small UI improvement | Design Review |
| Major Design | New interaction or component | Design Review + Founder |
| Philosophical | Changes to MDL | Design Authority |

The higher the impact on the product identity, the higher the level of review required.

---

# Section A
## Vision

### A1

Does the proposal strengthen the vision established in MDL-001?

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

Does it strengthen Mosaic as an entertainment companion?

- [ ] Yes
- [ ] No

---

# Section B
## Product Beliefs

### B1

Does the proposal respect the user's current context?

- [ ] Yes
- [ ] No

---

### B2

Does it deepen the current experience rather than redirect attention?

- [ ] Yes
- [ ] No

---

### B3

Would a knowledgeable companion behave this way?

- [ ] Yes
- [ ] No

---

### B4

Does the proposal earn the user's attention rather than demand it?

- [ ] Yes
- [ ] No

---

# Section C
## User Experience

### C1

Can the user understand what changed?

- [ ] Yes
- [ ] No

---

### C2

Is the interface calmer after this change?

- [ ] Yes
- [ ] No

---

### C3

Has unnecessary cognitive effort been removed?

- [ ] Yes
- [ ] No

---

### C4

Is artwork still the primary emotional focus?

- [ ] Yes
- [ ] No

---

# Section D
## Systems

### D1

Does the proposal reuse an existing MDL or MDS system?

- [ ] Yes
- [ ] No

---

### D2

If a new system is introduced, has it been justified?

- [ ] Yes
- [ ] No

---

### D3

Can this capability be expressed through existing composition rules?

- [ ] Yes
- [ ] No

---

### D4

Does this reduce long-term design complexity?

- [ ] Yes
- [ ] No

---

# Section E
## Engineering

### E1

Does the proposal expose implementation details to users?

- [ ] Yes
- [ ] No

If **Yes**, redesign.

---

### E2

Does the proposal remain platform independent?

- [ ] Yes
- [ ] No

---

### E3

Will this behave consistently across supported devices?

- [ ] Yes
- [ ] No

---

### E4

Can future extensions participate naturally?

- [ ] Yes
- [ ] No

---

# Section F
## Accessibility

### F1

Does this improve accessibility?

- [ ] Yes
- [ ] No

---

### F2

Does movement remain understandable with reduced motion enabled?

- [ ] Yes
- [ ] No

---

### F3

Can this interaction be completed without relying on animation?

- [ ] Yes
- [ ] No

---

### F4

Does this preserve readability and visual hierarchy?

- [ ] Yes
- [ ] No

---

# Automatic Rejection Criteria

A proposal should normally be rejected if it:

- introduces unnecessary friction
- competes with entertainment for attention
- exposes implementation details
- duplicates an existing system
- weakens established MDL principles
- requires explanation before becoming understandable
- prioritises novelty over clarity

These criteria intentionally bias Mosaic towards restraint rather than feature accumulation.

---

# Review Outcome

Every review should conclude with one of the following outcomes.

| Outcome | Meaning |
|----------|---------|
| Accepted | Ready for implementation |
| Accepted with Revisions | Minor changes required |
| Deferred | Requires additional investigation |
| Rejected | Conflicts with MDL |
| Superseded | Proposal replaced by another approach |

Rejected proposals should always reference the relevant MDL section or ADR rather than relying on subjective reasoning.

---

# Review Record

Every completed review should record:

```text
Specification:

Reviewer(s):

Date:

Decision:

Relevant ADRs:

Relevant MDL Sections:

Follow-up Actions:

Review Notes:
```

This creates a permanent audit trail explaining why significant design decisions were accepted or rejected.

---

# One Final Question

Before approving any proposal, every reviewer should ask:

> **If this became the standard across every part of Mosaic, would the product become stronger or weaker?**

If the answer is uncertain, the proposal should remain in review.

---

# Architectural Decisions

| ADR | Decision |
|------|----------|
| ADR-034 | Design reviews evaluate alignment with MDL rather than personal preference. |
| ADR-035 | Every significant proposal must leave a documented review trail. |
| ADR-036 | Existing systems are preferred over introducing isolated exceptions. |

---

# Review Status

**Status**

Draft

**Outstanding Questions**

None.

**Next File**

`11-future-considerations.md`