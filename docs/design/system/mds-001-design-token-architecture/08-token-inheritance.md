<!--
File: docs/design/system/mds-001-design-token-architecture/08-token-inheritance.md
Document: MDS-001
Chapter: 08
Title: Token Inheritance
Status: Draft
Version: 0.1
-->

# Token Inheritance

---

# Purpose

Inheritance permits stable Semantic Tokens to reuse Platform definitions without duplicating values or allowing consumers to bypass meaning.

---

# Permitted Relationships

Primitive Tokens terminate an inheritance chain.

Semantic Tokens may reference:

- one Primitive Token
- another compatible Semantic Token
- a governed composite of compatible Semantic Tokens

Resolved Tokens inherit the completed meaning and value selected by resolution.

Composition roles, Module intent and component identities do not participate in token inheritance.

They influence resolution through explicit inputs and mappings.

---

# Type Compatibility

Every inheritance relationship must preserve value type and unit compatibility.

A colour token cannot inherit a duration.

A relative length must not silently inherit an absolute physical value when their scaling rules differ.

Composite tokens must declare the type of every member.

---

# Alias Direction

Aliases must resolve toward an authoritative definition.

```mermaid
flowchart LR

S1["Semantic Alias"] --> S2["Semantic Authority"]
S2 --> P["Primitive Value"]
```

Aliases must not:

- form cycles
- cross incompatible token families
- point to renderer artefacts
- depend on Module namespaces
- bypass deprecation metadata

---

# Theme Variation

A theme may change the permitted Primitive or Semantic mapping used during resolution.

It must not change what a Semantic Token means.

For example, `Colour.Content.Primary` may resolve to different accessible colours in light and dark themes while retaining its responsibility.

---

# Local Overrides

Modules and components cannot locally override token inheritance.

Permitted customisation occurs through:

- mapped domain intent
- governed recipes
- Composition inputs
- user preferences
- accessibility requirements

If a required expression cannot be achieved through those inputs, it requires Platform review rather than a local alias.

---

# Resolution And Inheritance

Inheritance is resolved before contextual constraints are applied.

```text
validate token
    → resolve aliases
    → evaluate context
    → enforce accessibility and budget
    → publish Resolved Token
```

The renderer receives no unresolved inheritance graph.

---

# Validation

Automated validation should reject:

- circular aliases
- missing targets
- incompatible value types
- Module-defined Primitive or Semantic targets
- aliases to generated renderer names
- unresolved deprecated targets without migration paths

---

# Summary

Inheritance exists only within the Platform-owned Primitive and Semantic hierarchy.

Runtime and domain concepts influence resolution without becoming inheritance layers.
