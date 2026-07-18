<!--
File: docs/design/system/mds-001-design-token-architecture/13-contributor-guidance.md
Document: MDS-001
Status: Draft
-->

# Contributor Guidance

---

# Begin With Meaning

Before requesting a value, identify the stable design responsibility it serves.

Prefer:

```text
Colour.Content.Primary
```

Avoid:

```text
Primitive.Colour.Slate.950
```

Primitive Tokens remain a Platform implementation foundation.

---

# Do Not Turn Context Into Tokens

Hero, Supporting, Focused, Calendar.Today and renderer capability may affect resolution.

They do not automatically become Design Tokens.

Use the owning contract:

- Composition role for hierarchy
- Module intent for domain meaning
- accessibility state for user requirements
- capability and budget for implementation limits

---

# Components Render

Components consume completed resolved values or profiles.

They must not:

- choose Primitive Tokens
- infer their Composition role
- inspect device category
- remap Module domain meaning
- override accessibility constraints
- create component-specific token namespaces

If a component needs unresolved design logic, responsibility has leaked across the boundary.

---

# Modules Declare Intent

Modules may declare domain facts such as:

```text
Calendar.Today
Sports.Live
Music.NowPlaying
```

Every intent requires an explicit Platform semantic mapping and fallback.

Modules may combine governed recipes and provide domain layout invariants.

They may not create Design Tokens or renderer values.

---

# Domain Layouts

A layout extension describes relationships and valid modes rather than concrete pixels.

For a calendar month view, describe weeks, days, chronology, Focus, overflow and acceptable adaptation.

Allow the Composition Engine to calculate Tile location and size.

---

# Runtime Resolution

Runtime resolution belongs to the client resolver.

Use measured capability and current budget rather than mobile, television, desktop or tablet branches.

Preserve semantic presence and accessibility when fidelity reduces.

Publish complete immutable sets and retain the previous stable set when new work fails.

---

# Recipes

A recipe coordinates existing Semantic Tokens and constrained inputs.

It cannot:

- define a new Primitive
- redefine a Semantic Token
- alter locked Material or motion mechanics
- bypass accessibility
- send renderer code through SDUI

Recipes express governed creative combinations, not local design systems.

---

# Review Questions

- Is this value stable Platform meaning or current context?
- Does an existing Semantic Token already express it?
- Is a Module proposing intent or attempting to create a token?
- Is Composition still responsible for role and geometry?
- Does the component receive a complete resolved value?
- Are capability and budget measured?
- Is the fallback deterministic and accessible?
- Could this change fragment Mosaic across clients?

---

# Checklist

- [ ] Primitive and Semantic ownership remains Platform-only.
- [ ] Runtime state remains outside the authored hierarchy.
- [ ] Module intent is namespaced, mapped and has a fallback.
- [ ] Components render rather than resolve.
- [ ] Renderer artefacts contain no semantic authority.
- [ ] Device categories do not select fidelity.
- [ ] Accessibility remains authoritative.
- [ ] Aliases are type-compatible and cycle-free.
- [ ] Deprecation includes migration guidance.

---

# Final Guidance

Use Design Tokens for durable Platform design decisions.

Use intent and Composition contracts for current meaning.

Use resolution for adaptation.

Use renderer adapters for implementation.
