<!--
File: docs/engineering/guides/meg-006-extension-platform/01-extension-philosophy.md
Document: MEG-006
Status: Draft
Version: 0.1
-->

# Extension Philosophy

> *The Runtime should never need to know what tomorrow's capabilities look like. It should simply know how to host them.*

---

# Purpose

Traditional software grows by modifying its core.

Every new feature requires:

- new services
- new modules
- new dependencies
- new deployment

Over time, the core becomes increasingly complex.

Mosaic intentionally rejects this approach.

Instead:

The Runtime remains small.

The platform grows by adding capabilities.

This document establishes the architectural philosophy behind the Mosaic Extension Platform.

---

# Philosophy

Within Mosaic:

> **The platform evolves through capabilities, not through Runtime modification.**

Every new business feature should ideally be introduced by:

- adding a capability
- registering it
- allowing the Runtime to execute it

Rather than modifying the Runtime itself.

The Runtime should become increasingly capable without becoming increasingly complicated.

---

# Why Extensions Exist

Consider adding support for:

- Books
- Comics
- Audiobooks
- Music
- Podcasts
- IPTV

Traditional architecture.

```
Core

↓

Books

↓

Music

↓

Podcasts

↓

IPTV
```

Eventually:

The Core owns every business concept.

Instead.

```
Runtime

↓

Capability

↓

Capability

↓

Capability

↓

Capability
```

The Runtime remains unchanged.

Only capabilities increase.

---

# Capabilities Before Features

Within Mosaic:

Features are not architectural units.

Capabilities are.

Example.

Poor.

```
Add Podcast Feature
```

Preferred.

```
Podcast Capability
```

The distinction matters.

Capabilities possess:

- lifecycle
- dependencies
- contracts
- manifests
- ownership

Features do not.

---

# The Runtime Is Complete

One of the most important ideas within Mosaic is:

The Runtime should already contain everything required to execute future capabilities.

Adding a capability should **not** require:

- Runtime modification
- Runtime recompilation
- Runtime redesign

Only:

```
Capability

↓

Manifest

↓

Registration
```

The Runtime should simply recognise it.

---

# Core Is Just Another Capability

Architecturally:

Core capabilities should be treated exactly like extension capabilities.

Example.

```
Playback
```

```
Metadata
```

```
Library
```

All are capabilities.

The only distinction is:

Delivery.

Core capabilities ship with the Runtime.

Extensions ship independently.

Execution should remain identical.

This plugin-first philosophy, where core functionality and extensions share the same architectural model, is increasingly common in extensible platforms because it keeps the core small and stable.  [oai_citation:0‡Bifrost](https://docs.getbifrost.ai/architecture/core/plugins?utm_source=chatgpt.com)

---

# Runtime Neutrality

The Runtime should remain neutral.

It should not know:

- Anime
- Movies
- Books
- Jellyfin
- Stremio
- TMDB

It should know only:

```
Capability
```

Everything else belongs to the capability itself.

---

# Platform Growth

The preferred growth model is:

```
Runtime

↓

New Capability
```

Not:

```
Runtime

↓

Modify Runtime

↓

Add Feature
```

The platform grows by composition.

Not accumulation.

---

# Discovery Before Execution

One of the defining characteristics of the Extension Platform is:

```
Discover

↓

Validate

↓

Register

↓

Activate

↓

Execute
```

The Runtime should completely understand a capability before executing any of its code.

Discovery should be metadata driven.

Execution should come later.

Modern plugin systems increasingly separate **manifest discovery** from **runtime loading**, allowing validation before executable code is activated.  [oai_citation:1‡OpenClaw](https://docs.openclaw.ai/plugins/architecture?utm_source=chatgpt.com)

---

# Manifest First

Every capability begins with a manifest.

The manifest describes:

- identity
- dependencies
- permissions
- contracts
- configuration
- capabilities

The Runtime should understand the manifest before it understands the implementation.

The manifest becomes the Runtime's architectural contract.

---

# Capabilities Are Products

Capabilities should be developed as independently evolving products.

Each capability owns:

- business behaviour
- documentation
- lifecycle
- testing
- versioning

Capabilities should not depend upon private Runtime implementation.

The Runtime provides the platform.

Capabilities provide value.

---

# Runtime Contracts

Every interaction with the Runtime should occur through stable contracts.

Examples include:

- lifecycle
- execution
- configuration
- scheduling
- permissions

Capabilities should never depend upon Runtime internals.

This allows the Runtime to evolve independently.

---

# Replaceability

Capabilities should remain replaceable.

Suppose:

```
Metadata Capability

↓

Version 2
```

The Runtime should require:

```
Manifest Validation

↓

Activation

↓

Ready
```

Nothing else.

Capabilities should be interchangeable wherever practical.

---

# Capability Isolation

Every capability should execute independently.

Suppose:

```
Recommendation Capability

↓

Failure
```

The Runtime should ensure:

```
Playback Capability

↓

Unaffected
```

Capability failures should never destabilise the platform.

Isolation is one of the defining responsibilities of the Runtime.

---

# Runtime Evolution

The Runtime evolves by improving execution.

Capabilities evolve by improving business behaviour.

These concerns should remain independent.

Examples.

Runtime.

- faster scheduler
- improved worker pools
- better observability

Capabilities.

- better metadata
- improved playback
- smarter recommendations

Neither should require modifying the other.

---

# Extension Equality

The Runtime should never distinguish between:

- Core
- First-party
- Third-party

Every capability should satisfy the same Runtime contracts.

Every capability should participate in:

- lifecycle
- discovery
- execution
- observability

Architectural equality greatly simplifies the platform.

---

# Marketplace Thinking

The Runtime should eventually support an ecosystem.

That ecosystem depends upon:

- predictable contracts
- stable manifests
- capability discovery
- version compatibility

The Runtime should therefore be designed for capabilities that have not yet been written.

Platform ecosystems thrive when the host defines stable extension points and capabilities register through manifests rather than bespoke integration code.  [oai_citation:2‡arc42 Quality Model](https://quality.arc42.org/approaches/plugin-architecture?utm_source=chatgpt.com)

---

# Simplicity

The Extension Platform should remain conceptually simple.

Everything reduces to one sentence.

```
Capability

↓

Manifest

↓

Runtime

↓

Execution
```

Everything else is implementation.

---

# Mosaic Principles

Within Mosaic:

- The Runtime grows through capabilities.
- Capabilities are first-class architectural units.
- Core and extensions are architectural equals.
- Discovery precedes execution.
- Manifests define Runtime contracts.
- Runtime neutrality must be preserved.
- Capabilities remain independently deployable.
- Runtime evolution and capability evolution remain independent.

These principles define the identity of the Extension Platform.

---

# Relationship to MEG

MEG-005 defined:

> **How the Runtime executes capabilities.**

MEG-006 now begins defining:

> **How capabilities become part of the Runtime.**

The next chapter introduces the **Capability Manifest**, the machine-readable contract through which every capability describes itself to the platform.

---

# Summary

The Extension Platform exists for one purpose.

> **Allow the platform to grow forever without growing the Runtime.**

The Runtime should become increasingly powerful by hosting more capabilities.

Not by accumulating more business behaviour.

That distinction is what transforms Mosaic from an application into a platform.

---

# Review Status

**Status**

Draft

**Owner**

Lead Software Architect

**Previous File**

`00-document-control.md`

**Next File**

`02-capability-manifest.md`
