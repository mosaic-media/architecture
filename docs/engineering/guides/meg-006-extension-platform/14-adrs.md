<!--
File: docs/engineering/guides/meg-006-extension-platform/14-adrs.md
Document: MEG-006
Status: Draft
Version: 0.1
-->

# Architectural Decision Records (ADRs)

> *The Extension Platform defines how the Mosaic ecosystem grows. Decisions affecting that ecosystem should always be deliberate, documented and historically traceable.*

---

# Purpose

The Extension Platform defines how capabilities:

- are discovered
- are registered
- integrate with the Runtime
- evolve over time
- interact safely

Changes to these mechanisms affect:

- every capability
- every extension author
- every SDK consumer
- every marketplace

Architectural Decision Records (ADRs) preserve the reasoning behind these platform decisions.

Future contributors should understand not only:

> **How the platform works**

but also:

> **Why it was designed that way.**

---

# Philosophy

Within Mosaic:

> **The platform should evolve through architectural intent rather than implementation convenience.**

Every Extension Platform decision introduces long-term ecosystem consequences.

Those consequences should be documented before they become implementation.

---

# Why Extension ADRs Matter

Unlike business capabilities, platform decisions affect everyone.

Changing:

- manifest schema
- SDK contracts
- permissions
- activation lifecycle

may require changes across hundreds of capabilities.

Without ADRs, future contributors eventually ask:

- Why are manifests mandatory?
- Why are permissions declared rather than inferred?
- Why is discovery separated from activation?
- Why is the SDK intentionally small?

Architectural knowledge should not disappear with the original authors.

---

# When An ADR Is Required

An Extension Platform ADR SHOULD be created whenever a decision changes:

- capability manifests
- Runtime contracts
- SDK design
- dependency resolution
- activation model
- permission model
- capability lifecycle
- marketplace integration
- compatibility strategy

If the decision changes how capabilities integrate with the platform, it deserves an ADR.

---

# Examples

Examples of Extension Platform ADRs include:

```
ADR-001

Manifest-Driven Platform
```

```
ADR-002

Capability-Oriented Architecture
```

```
ADR-003

SDK Stability Policy
```

```
ADR-004

Permission Model
```

```
ADR-005

Capability Lifecycle
```

```
ADR-006

Dependency Resolution Strategy
```

```
ADR-007

Marketplace Compatibility
```

```
ADR-008

Extension Isolation
```

These decisions influence every extension ever written for Mosaic.

They should remain permanently discoverable.

---

# Platform Stability

The Extension Platform should evolve conservatively.

Changing:

```
Marketplace UI
```

is relatively inexpensive.

Changing:

```
Capability Manifest
```

affects:

- every extension
- every SDK
- every Runtime
- every marketplace
- every development tool

Platform contracts should therefore change rarely and deliberately.

---

# ADR Structure

Every Extension Platform ADR SHOULD contain:

```
Title

↓

Status

↓

Context

↓

Architectural Problem

↓

Options

↓

Decision

↓

Consequences

↓

Migration

↓

Related Specifications
```

Migration guidance is especially important because platform decisions frequently affect third-party developers outside the Runtime itself.

A consistent ADR structure centred on context, decision and consequences is widely regarded as a software architecture best practice because it preserves architectural reasoning rather than implementation detail.  [oai_citation:0‡AWS Documentation](https://docs.aws.amazon.com/prescriptive-guidance/latest/architectural-decision-records/adr-process.html?utm_source=chatgpt.com)

---

# Context

The Context section should describe:

- current platform behaviour
- ecosystem requirements
- Runtime constraints
- compatibility concerns

Readers unfamiliar with the Extension Platform should understand:

> **Why did this architectural discussion become necessary?**

---

# Architectural Problem

The problem statement should describe the platform.

Good.

```
Capabilities currently expose Runtime implementation details.
```

Poor.

```
The SDK feels awkward.
```

The problem should remain architectural.

Not implementation specific.

---

# Options

Every significant platform decision SHOULD evaluate alternatives.

Example.

```
Manifest Discovery
```

versus

```
Reflection Discovery
```

or

```
Explicit Permissions
```

versus

```
Automatic Permission Detection
```

Each option should document:

- advantages
- disadvantages
- ecosystem impact
- maintenance implications

Rejected alternatives remain valuable architectural knowledge.

---

# Decision

The Decision section answers:

> **Which platform architecture becomes the Mosaic standard?**

Implementation details belong elsewhere.

The ADR records the architectural commitment.

---

# Consequences

Every platform decision introduces trade-offs.

Example.

Choosing:

```
Manifest First
```

Benefits.

- deterministic discovery
- better tooling
- stronger validation
- improved security

Costs.

- additional authoring effort
- manifest maintenance
- schema evolution

Trade-offs should always be documented honestly.

No architectural decision is free.

---

# Migration

Platform evolution frequently requires migration.

Migration guidance SHOULD explain:

- affected capabilities
- SDK compatibility
- manifest changes
- Runtime compatibility
- marketplace impact

Migration planning should exist before implementation begins.

---

# SDK Evolution

Changes affecting the SDK SHOULD always receive ADRs.

The SDK is the public contract between:

- Runtime
- Extension Authors

Breaking SDK behaviour without documented reasoning damages ecosystem stability.

SDK evolution deserves particularly careful review.

---

# Manifest Evolution

Manifest schema changes SHOULD always be documented.

Examples include:

- new required fields
- permission changes
- contract changes
- lifecycle changes

The Runtime and tooling both depend upon the manifest.

Schema evolution therefore affects the entire platform.

---

# Marketplace Impact

Platform ADRs SHOULD explicitly describe marketplace implications.

Examples include:

- installation
- compatibility
- upgrades
- discovery
- diagnostics

Marketplace behaviour should naturally follow platform architecture.

Not redefine it.

---

# Repository Structure

Recommended layout.

```text
architecture/

    adrs/

        ADR-001-capability-manifests.md

        ADR-002-sdk-contracts.md

        ADR-003-permission-model.md

        ADR-004-capability-lifecycle.md

        ADR-005-marketplace-architecture.md
```

Extension Platform ADRs should remain close to the specifications governing the platform itself.

---

# Review Process

Extension Platform ADRs SHOULD receive architectural review.

Review should consider:

- ecosystem stability
- SDK compatibility
- Runtime integration
- extension author experience
- operational impact
- long-term evolution

Platform decisions should favour stability over novelty.

---

# Documentation

Accepted Extension Platform ADRs SHOULD eventually be reflected within:

- MEG specifications
- SDK documentation
- marketplace documentation
- extension author guides
- tooling documentation

Platform documentation should evolve alongside the platform itself.

---

# Mosaic Guidelines

Within Mosaic:

- Significant platform changes SHOULD have ADRs.
- SDK changes MUST be documented.
- Manifest evolution MUST be documented.
- Platform alternatives SHOULD be evaluated explicitly.
- Trade-offs MUST be acknowledged.
- Migration guidance SHOULD accompany platform evolution.
- Historical ADRs MUST remain available.
- Platform architecture SHOULD evolve deliberately.

---

# Relationship to MEG

MEG-006 defines:

> **How capabilities integrate with the Runtime today.**

Extension Platform ADRs explain:

> **Why the platform integrates capabilities that way.**

Together they preserve the architectural intent of the Mosaic ecosystem.

---

# Summary

The Extension Platform is the foundation of the Mosaic ecosystem.

Every architectural decision made here affects not only the Runtime but every capability written in the future.

Architectural Decision Records ensure that this ecosystem grows through conscious engineering judgement rather than accidental implementation.

The platform should continue evolving.

Its architectural reasoning should never be lost.

---

# Review Status

**Status**

Draft

**Owner**

Lead Software Architect

**Previous File**

`13-platform-guidelines.md`

**Next File**

`15-contributor-guidance.md`
