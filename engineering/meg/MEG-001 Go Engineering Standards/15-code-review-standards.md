<!--
File: engineering/meg/MEG-001 Go Engineering Standards/15-code-review-standards.md
Document: MEG-001
Status: Draft
Version: 0.1
-->

# Code Review Standards

> *The purpose of code review is not to find fault with engineers. It is to improve the quality, consistency and longevity of the software.*

---

# Purpose

Every change made to the Mosaic codebase should improve the software.

Code review exists to ensure that changes are:

- technically correct
- architecturally consistent
- maintainable
- understandable
- testable
- aligned with the Mosaic Engineering Guidelines

Reviews are collaborative engineering activities.

They are not approval ceremonies.

---

# Philosophy

Within Mosaic:

> **Review the code. Never the author.**

Engineering discussions should focus upon:

- design
- maintainability
- correctness
- readability
- architecture

Personal preference should never outweigh established engineering standards.

When disagreement exists, the MEG should be considered the source of truth.

---

# Objectives

Every code review should answer five questions.

## 1. Is it Correct?

Does the implementation solve the intended problem?

Does it introduce bugs?

Does it handle failures correctly?

---

## 2. Is it Understandable?

Would another engineer immediately understand:

- what the code does
- why it exists
- how it behaves

without additional explanation?

---

## 3. Is it Maintainable?

Will this implementation remain understandable in:

- six months
- one year
- five years

Can future requirements be accommodated without major rewrites?

---

## 4. Is it Consistent?

Does the implementation follow:

- Go conventions
- Mosaic conventions
- repository conventions

Consistency reduces cognitive load.

---

## 5. Is it Simpler?

Does this change reduce complexity?

Or merely move it somewhere else?

Every review should seek opportunities to simplify.

---

# Review Mindset

Reviews should begin with the assumption that:

> The author made the best decision they could with the information available.

The objective is to improve the software together.

Not to prove someone wrong.

---

# Review Checklist

Every review SHOULD consider the following.

---

## Correctness

- Does the implementation satisfy the requirements?
- Are edge cases handled?
- Are errors propagated correctly?
- Are resources cleaned up?
- Does cancellation work?
- Are concurrent operations safe?

---

## Architecture

- Does the package own this responsibility?
- Are dependencies flowing correctly?
- Is abstraction appropriate?
- Is composition preferred?
- Has coupling increased?
- Does this align with the MEG?

---

## Readability

- Can names be improved?
- Are functions too large?
- Is the control flow obvious?
- Are comments necessary?
- Would another engineer understand this quickly?

---

## Simplicity

Ask:

> Can this become smaller?

> Can this become clearer?

> Can this become more explicit?

Complexity should always justify itself.

---

## Testing

- Are tests present?
- Do tests verify behaviour?
- Are edge cases covered?
- Are failures tested?
- Does concurrency have tests?
- Would race detection pass?

---

## Performance

- Is optimisation justified?
- Has performance been measured?
- Does complexity outweigh the benefit?
- Is allocation behaviour reasonable?

Premature optimisation should be challenged.

---

## Documentation

- Are exported APIs documented?
- Does architecture documentation require updating?
- Are comments explaining *why* rather than *what*?

Documentation should evolve alongside implementation.

---

# What Reviews Should Not Discuss

The following SHOULD NOT dominate review discussions.

- personal formatting preferences
- preferred variable names without objective improvement
- favourite libraries
- editor configuration
- personal coding style

Automated tooling should handle formatting.

Reviews should focus on engineering.

---

# Review Comments

Comments should be:

- respectful
- specific
- actionable
- educational

Good:

> This dependency appears to create coupling between playback and metadata. Could the interface belong to the consumer instead?

Poor:

> This is wrong.

Explain the reasoning.

Not merely the conclusion.

Google's Go Code Review Comments encourage reviewers to explain the principle behind requested changes so future code improves as well. ([go.dev](https://go.dev/wiki/CodeReviewComments?utm_source=chatgpt.com))

---

# The Boy Scout Review

Every review should ask one additional question.

> **Did this pull request leave the surrounding code better than it was before?**

Examples include:

- improved naming
- removed duplication
- simplified logic
- additional tests
- better documentation
- dead code removal

Small improvements accumulate over time.

---

# Review Categories

Review feedback should naturally fall into one of four categories.

| Category | Description |
|----------|-------------|
| Defect | Incorrect behaviour that must be fixed |
| Architecture | Violates engineering standards or design principles |
| Suggestion | Improvement that is optional |
| Question | Clarification requested before approval |

Not every comment blocks a merge.

Distinguishing between categories improves collaboration.

---

# Blocking Issues

The following SHOULD block approval.

- Incorrect behaviour
- Race conditions
- Resource leaks
- Security issues
- Broken tests
- Architectural violations
- Hidden dependencies
- Missing error handling
- Unsafe concurrent access
- Significant maintainability concerns

---

# Non-Blocking Issues

The following generally SHOULD NOT block approval.

- Minor naming preferences
- Small formatting issues
- Future optimisation ideas
- Stylistic differences already accepted by the repository

These may be addressed separately.

---

# Self Review

Before requesting review, every engineer SHOULD review their own changes.

Suggested checklist:

- Read every changed line.
- Remove temporary code.
- Remove debugging statements.
- Run formatting.
- Run static analysis.
- Execute tests.
- Read the diff as another engineer would.

The best time to find defects is before someone else has to.

---

# Automated Review

Automation should perform repetitive tasks.

Examples include:

- formatting
- linting
- static analysis
- dependency scanning
- vulnerability detection
- test execution
- race detection

Humans should review:

- architecture
- design
- readability
- maintainability
- intent

Do not spend human attention on problems that tooling can solve reliably.

---

# Large Pull Requests

Large pull requests are difficult to review.

Where practical:

- separate refactoring from feature work
- separate formatting from behaviour changes
- separate infrastructure from business logic

Smaller reviews produce higher quality feedback.

---

# Receiving Feedback

Review feedback should be viewed as an opportunity to improve the software.

Avoid defending implementations automatically.

Instead ask:

- Is the reviewer correct?
- Does this improve the design?
- Is there a simpler solution?

Engineering discussions should optimise for the codebase.

Not individual opinions.

---

# Review Culture

A healthy review culture encourages:

- curiosity
- discussion
- learning
- consistency
- shared ownership

It discourages:

- ego
- blame
- gatekeeping
- personal criticism

The quality of a codebase is directly influenced by the quality of its reviews.

---

# Mosaic Guidelines

Within Mosaic:

- Every significant change SHOULD be reviewed.
- Reviews MUST focus on engineering rather than personal preference.
- Automated tooling SHOULD handle formatting.
- Blocking comments MUST explain the underlying concern.
- Engineers SHOULD perform self-review before requesting review.
- Every review SHOULD leave the surrounding code better than before.
- Architecture discussions SHOULD reference the MEG where applicable.

---

# Summary

Code review is one of the highest leverage engineering activities.

It spreads knowledge.

It maintains consistency.

It prevents architectural drift.

Most importantly, it protects the long-term health of the codebase.

Within Mosaic, the objective of review is simple:

> **Leave both the software and the engineer better than you found them.**

---

# Review Status

**Status**

Draft

**Owner**

Lead Software Architect

**Previous File**

`14-anti-patterns.md`

**Next File**

`16-boy-scout-rule.md`
