<!--
File: docs/design/system/mds-001-design-token-architecture/11-governance.md
Document: MDS-001
Status: Draft
-->

# Token Governance

---

# Purpose

Governance protects Mosaic from duplicated meaning, local primitives, device-specific forks and Module-owned design systems.

---

# Ownership

| Artefact | Owner |
|----------|-------|
| Primitive Token | Platform Design System |
| Semantic Token | Platform Design System |
| Module domain intent | Owning Module, subject to Platform mapping rules |
| Composition role and layout resolution | Composition Engine |
| Resolved Token Set | Client runtime |
| Renderer artefact | Client adapter |

Only the Platform Design System may create Primitive or Semantic Tokens.

---

# Protected Core

Modules and clients must not redefine:

- semantic hierarchy
- brand meaning
- Material behaviour
- typography roles
- motion mechanics
- Focus and interaction meaning
- accessibility outcomes
- performance degradation policy

Implementation may adapt while these meanings remain invariant.

---

# Introducing A Primitive Token

A proposed Primitive Token should be accepted only when:

1. it represents a reusable foundational value
2. no existing Primitive can express it accurately
3. its type and unit are explicit
4. it contains no usage or renderer meaning
5. downstream Semantic ownership is identified

Primitive Tokens must not be created merely to avoid an existing semantic constraint.

---

# Introducing A Semantic Token

A proposed Semantic Token should be accepted only when:

1. the meaning applies across more than one local implementation
2. no existing Semantic Token expresses the responsibility
3. its distinction is semantic rather than visual
4. accessibility behaviour is defined
5. fallback and migration behaviour are defined
6. downstream owning specifications agree with the meaning

Repeated Module intent may reveal a missing Semantic Token but does not create one automatically.

---

# Module Governance

A Module may register domain intent without creating Design Tokens when the intent:

- is namespaced
- describes domain meaning
- maps to an existing Platform semantic role
- supplies a safe fallback
- preserves locked Platform behaviour

Entirely new cross-product meaning requires Platform review.

Module layout extensions are governed by [MDP-001 — Adaptive Composition Runtime](../../../engineering/architecture/mdp-001-adaptive-composition-runtime/index.md) and must preserve Platform rendering authority.

A Module or application implementing Authored Layout may consume existing public Semantic Tokens.

It may not create local Primitive values, redefine token meaning or publish new cross-Platform Semantic Tokens without Platform review.

---

# Capability Governance

Resolution must use measured capability and current budget.

Permanent branches based on mobile, television, desktop, tablet or similar product categories are prohibited.

Capability inputs must describe observable support or cost, such as backdrop availability, shader support, measured frame headroom or memory pressure.

---

# Automated Validation

Tooling should validate:

- unique token identifiers
- permitted token ownership
- value type and unit compatibility
- alias targets and cycle freedom
- Semantic Token documentation
- Module intent namespace and fallback
- absence of renderer names in authored tokens
- absence of device-category resolution branches
- deprecation and migration metadata

Invalid extension data should fail closed to a declared Platform fallback.

---

# Review Checklist

- [ ] Is this artefact actually a Design Token?
- [ ] Is ownership explicit?
- [ ] Does the name communicate stable meaning?
- [ ] Can an existing Semantic Token or mapped intent solve it?
- [ ] Are Primitive values hidden from ordinary consumers?
- [ ] Is runtime context kept outside the token hierarchy?
- [ ] Are accessibility constraints preserved?
- [ ] Is capability measured rather than inferred from device type?
- [ ] Is fallback behaviour deterministic?
- [ ] Are compatibility and deprecation effects documented?

---

# Success Criteria

Governance succeeds when Modules remain expressive, clients remain adaptive and the Platform retains one coherent Design Token API.
