<!--
File: docs/design/language/mdl-002-principles/08-principle-06-the-platform-enables.md
Document: MDL-002
Chapter: 08
Principle: 06
Title: The Platform Enables
Status: Draft
Version: 0.1
-->

# Principle 06 — The Platform Enables

---

# Principle Statement

> **The core Mosaic platform should solve universal problems. Specialised experiences should emerge through extension rather than expansion of the core.**

Mosaic is designed as a platform.

Not because plugins are fashionable.

Because no core team can anticipate every way people wish to enjoy entertainment.

The responsibility of the core platform is therefore to provide excellent foundations rather than infinite features.

---

# Why This Principle Exists

Software inevitably grows.

Without clear architectural boundaries, every successful feature request becomes another permanent responsibility of the core application.

Eventually:

- navigation expands
- settings multiply
- interactions diverge
- maintenance slows
- innovation becomes more difficult

A platform avoids this by distinguishing between:

- universal capabilities
- specialised capabilities

Universal capabilities belong in the core.

Specialised capabilities belong at extension points.

Extensible platform architectures consistently favour a stable core with well-defined extension points, allowing innovation without increasing coupling or destabilising the platform.  [oai_citation:0‡arc42 Quality Model](https://quality.arc42.org/approaches/plugin-architecture?utm_source=chatgpt.com)

---

# Definition

Within MDL, **the platform** is defined as:

> The collection of systems that every Mosaic experience depends upon.

Examples include:

- authentication
- composition
- playback
- navigation
- search
- materials
- design language
- extension framework

Everything else should justify why it belongs inside the core.

---

# The Responsibility Of The Core

The core platform owns:

- consistency
- composition
- accessibility
- interaction
- terminology
- behaviour
- quality

The core should not attempt to own every possible entertainment experience.

Instead, it provides the environment within which those experiences can exist.

---

# The Responsibility Of Extensions

Extensions exist to provide:

- new domains
- specialised metadata
- community integrations
- experimental capabilities
- niche workflows

Extensions should extend Mosaic.

They should not become independent applications running inside Mosaic.

---

# Core First

When evaluating a proposal, contributors should first ask:

> **Is this solving a universal problem?**

If the answer is yes...

The capability probably belongs in the core.

Examples:

- playback
- progress
- collections
- navigation
- accessibility

---

# Extension First

If the proposal instead answers:

> **Only some users need this.**

The default assumption should become:

Extension.

Examples include:

- manga providers
- audiobook integrations
- torrent health
- franchise-specific metadata
- community statistics

The burden of proof lies with moving functionality into the core.

Not the extension ecosystem.

---

# The Platform Contract

The platform promises:

- consistency
- stability
- accessibility
- composition
- behaviour

Extensions promise:

- knowledge
- capability
- integration
- specialisation

Neither should attempt to perform the other's responsibilities.

---

# The UI Belongs To Mosaic

One of the most important architectural consequences of this principle is ownership of the interface.

Plugins should not create arbitrary interface.

Plugins should contribute capability.

The platform decides presentation.

This ensures:

- consistency
- accessibility
- device independence
- future evolution

Future MDS specifications are expected to formalise this separation through the Composition Engine and Information Model.

---

# Example

## Good

Anime extension contributes:

```
Episode Release

Tomorrow
```

Book extension contributes:

```
Chapter Progress

12 / 18
```

The platform determines:

- composition
- hierarchy
- movement
- materials
- interaction

Every extension therefore feels native.

---

## Poor

Anime extension renders:

- custom navigation
- custom cards
- custom animations
- custom spacing
- custom typography

The platform has lost ownership of the experience.

Users now experience multiple competing design languages.

---

# Platform Growth

Growth should occur through stronger systems.

Not larger systems.

Good platform evolution looks like:

```
Core System

↓

Extension Point

↓

Community Capability
```

Poor platform evolution looks like:

```
Feature

↓

Feature

↓

Feature

↓

Feature

↓

Settings

↓

Configuration

↓

Complexity
```

The objective is sustainable growth.

Not unlimited growth.

---

# Relationship To Other Principles

This principle reinforces:

- Every Feature Earns Its Place
- Be A Companion
- Content Leads

It also provides the architectural foundation for:

- Extension Framework
- Composition Engine
- Runtime Systems
- Information Model

---

# Review Questions

Before approving a proposal ask:

- Does every Mosaic user require this capability?
- Can the existing platform already support it?
- Would an extension provide the same value?
- Does this strengthen the platform or enlarge it?
- Is the proposal introducing a capability or a dependency?

If uncertainty remains, contributors should default towards extension rather than core implementation.

---

# Litmus Test

A proposal belongs in the platform if removing it would fundamentally weaken Mosaic.

A proposal belongs in an extension if removing it only affects a particular audience or workflow.

The platform should remain intentionally small.

Its capabilities should remain intentionally powerful.

---

# Summary

Platforms do not become successful because they contain every feature.

They become successful because they enable others to build features without weakening the foundation.

Mosaic should grow by strengthening its systems.

Not by endlessly expanding its core.

---

# Related Specifications

- MDL-001 Vision
- MDL-005 Composition Model
- MDS-003 Composition Engine
- MDS-011 Extension Design Specification

---

# Architectural Decisions

| ADR | Decision |
|------|----------|
| ADR-020 | The core platform owns behaviour, consistency and presentation. |
| ADR-021 | Extensions own specialised capability rather than interface. |
| ADR-022 | Platform growth should occur through extension points before core expansion. |

---

# Review Status

**Status**

Draft

**Next File**

`09-principle-07-be-a-companion.md`
