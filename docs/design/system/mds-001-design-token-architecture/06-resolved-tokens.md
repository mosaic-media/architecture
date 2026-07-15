<!--
File: docs/design/system/mds-001-design-token-architecture/06-resolved-tokens.md
Document: MDS-001
Chapter: 06
Title: Resolved Tokens
Status: Draft
Version: 0.1
-->

# Resolved Tokens

---

# Purpose

Mosaic adapts continuously without allowing runtime state to redefine the Design System.

Resolved Tokens are the generated boundary between stable Semantic Tokens and concrete Presentation.

---

# Definition

Within MDS, a **Resolved Token** is:

> **An immutable client-generated value expressing one Platform Semantic Token for one complete resolution context.**

Resolved Tokens are generated.

They are not authored, registered or extended by Modules.

---

# Resolution Context

The resolver may evaluate:

- Composition role and relationships
- Module domain intent mapped to Platform semantics
- current Focus and interaction Context
- artwork-derived inputs
- approved static brand illumination
- Light, Dark or system appearance preference
- user Refraction-fidelity preference
- accessibility requirements
- renderer capabilities
- current CPU, GPU, memory and compositor budget

Device category is not a resolution input.

A browser on a television and a browser on a phone may select the same result when their measured capabilities and current budgets are equivalent.

---

# Runtime Never Changes Meaning

Resolution may change:

- concrete colour
- contrast
- dimensional value
- motion quantity
- Material fidelity
- renderer technique

Resolution must not change:

- semantic purpose
- hierarchy meaning
- interaction meaning
- accessibility outcome
- Module domain meaning

`Material.Hero` therefore remains Hero at Enhanced, Balanced and Essential fidelity.

---

# Immutable Snapshot

One resolution cycle should publish a complete immutable set.

Consumers must not observe a mixture of old and new theme, accessibility, capability or Focus values.

When resolution fails or is cancelled, the previous stable set remains active.

---

# Capability And Budget

Capability describes what a renderer can perform correctly.

Budget describes what it can perform safely now.

Both are measured client inputs rather than authored token categories.

Quality should reduce quickly under pressure and recover only after sustained headroom.

Accessibility and Presentation deadlines retain higher authority than visual fidelity.

---

# User Preference Boundaries

Users may select Light, Dark or system appearance and supported accessibility preferences such as reduced motion or reduced transparency.

They do not select arbitrary shell colours, Material physics, typography families or renderer techniques.

Refraction preference defines a maximum fidelity:

| Preference | Meaning |
|------------|---------|
| Automatic | Permit resolution up to Enhanced fidelity. |
| Balanced | Never exceed Balanced fidelity. |
| Essential | Prefer static artwork- or brand-derived Acrylic with minimal continuous refinement. |

The effective fidelity is the lowest level permitted by capability, current budget, user maximum and accessibility constraints.

The client may always reduce fidelity further to protect Presentation.

Appearance and accessibility preferences may follow the user or operating system.

Refraction preference may use a synced account value or an explicit local override for one client.

---

# Cache Identity

A Resolved Token Set may be cached using the stable inputs that affect its result, including:

- Semantic Token catalogue revision
- theme revision
- Composition-role signature
- mapped domain-intent signature
- accessibility state
- appearance preference
- synced Refraction maximum and local-override identity
- capability profile
- budget band
- relevant artwork or atmosphere revision

Transient renderer object identity must not become part of semantic cache identity.

---

# Consumer Boundary

Components consume completed resolved values or a resolved profile.

They do not:

- inspect device type
- resolve aliases
- choose accessibility overrides
- generate runtime tokens
- reinterpret Module intent
- select permanent fidelity tiers

---

# Summary

Resolved Tokens make stable Platform semantics adaptive.

They are outputs of resolution, not a third authored namespace and not a route for local design invention.
