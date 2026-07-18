<!--
File: docs/design/system/mds-008-component-library/13-contributor-guidance.md
Document: MDS-008
Status: Draft
-->

# Contributor Guidance

---

# Purpose

The Component Library is the only part of Mosaic most frontend engineers will interact with every day.

It is therefore the easiest place for architectural boundaries to erode.

This guidance exists to ensure contributors continue thinking in terms of:

- Behaviour,
- Expressions,
- Tiles,
- Contracts,

rather than:

- widgets,
- callbacks,
- screens,
- application state.

When contributors naturally think in runtime architecture before implementation, the Component Library has achieved its purpose.

---

# Think In Contracts

Never begin with:

> "How should this widget behave?"

Instead ask:

> **"Which Component Contract am I rendering?"**

Good.

```mermaid
flowchart TD

N1["Component Contract"]
N2["Rendering"]

N1 --> N2
```

Poor.

```mermaid
flowchart TD

N1["Widget"]
N2["Behaviour"]

N1 --> N2
```

Components should consume behaviour.

Never invent it.

---

# Think In Tiles

Every Component exists because a Tile exists.

Before implementing anything ask:

> **"Which Tile am I rendering?"**

If the answer is unclear...

The implementation should probably not begin yet.

---

# Components Never Decide

Components should never determine:

- hierarchy,
- colour,
- typography,
- motion,
- interaction,
- behaviour.

Those decisions already exist.

If a Component needs to decide...

The architecture has already drifted.

---

# Preserve Architectural Boundaries

Preferred.

```mermaid
flowchart TD

N1["Behaviour"]
N2["Expression"]
N3["Tile"]
N4["Component"]
N5["Rendering"]

N1 --> N2
N2 --> N3
N3 --> N4
N4 --> N5
```

Avoid.

```mermaid
flowchart TD

N1["Component"]
N2["Behaviour"]
N3["Rendering"]

N1 --> N2
N2 --> N3
```

Dependencies should always flow downward.

Never upward.

---

# Respect Contracts

Component Contracts should be treated as immutable.

Never:

- modify,
- reinterpret,
- extend,
- override

a Contract inside a Component.

If the Contract is insufficient...

Improve the runtime architecture.

Not the Component.

---

# Stay Stateless

Whenever practical...

Components should remain stateless.

Preferred.

```mermaid
flowchart TD

N1["Contract"]
N2["Render"]

N1 --> N2
```

Avoid.

```mermaid
flowchart TD

N1["Component State"]
N2["Behaviour"]
N3["Render"]

N1 --> N2
N2 --> N3
```

State belongs to the Runtime World.

Components simply display it.

---

# Let Runtime Own Updates

Components should respond to:

```text
New Contract
```

They should never poll:

- application state,
- services,
- runtime systems.

The Composition Engine already solved the user's World.

Trust it.

---

# Reuse Components

Before creating a new Component ask:

> Can an existing implementation primitive already render this Contract?

Most new implementation requests should improve:

- Component Composition,
- Component Contracts,

rather than expanding the Component vocabulary.

---

# Respect Accessibility

Accessibility should always originate from Accessibility Contracts.

Components should never invent:

- semantics,
- hierarchy,
- reading order,
- behavioural actions.

Platform APIs implement accessibility.

Runtime defines it.

---

# Respect Platform Independence

Before implementing any Component ask:

> Would another platform be able to render this Contract using an equivalent implementation?

If the answer is no...

The Component is probably too platform-specific.

---

# Performance Comes Last

Optimise only after correctness.

Preferred.

```mermaid
flowchart TD

N1["Correct"]
N2["Optimised"]

N1 --> N2
```

Avoid.

```mermaid
flowchart TD

N1["Optimised"]
N2["Different Behaviour"]

N1 --> N2
```

Behavioural correctness always has higher priority than rendering performance.

---

# Modules Never Render

Modules contribute:

- behaviour,
- Expressions,
- information.

They never contribute:

- Components,
- rendering,
- UI frameworks.

Every module should inherit presentation automatically.

---

# Common Mistakes

Avoid the following.

### Smart Components

Components performing runtime reasoning.

---

### Mutable Contracts

Components changing runtime Contracts.

---

### Platform Logic

Platform-specific Components introducing behavioural differences.

---

### Widget Thinking

Naming Components after application features.

---

### Behavioural Rendering

Rendering frameworks influencing runtime behaviour.

---

### Accessibility Logic

Components independently implementing accessibility policy.

---

# Component Review Questions

Before implementing any Component ask:

- Which Tile does this render?
- Which Contract does it consume?
- Does it remain behaviourally passive?
- Could an existing Component already perform this work?
- Would this implementation work on every Mosaic platform?
- Does it preserve architectural boundaries?

If uncertainty remains...

Return to the Tile before writing implementation.

---

# Component Checklist

Every Component implementation should satisfy the following.

- [ ] Consumes immutable Component Contracts.
- [ ] Contains no behavioural logic.
- [ ] Remains platform independent.
- [ ] Preserves accessibility.
- [ ] Preserves Material behaviour.
- [ ] Preserves Typography behaviour.
- [ ] Preserves Motion behaviour.
- [ ] Remains stateless wherever practical.

---

# Final Guidance

The Component Library should eventually disappear from architectural discussion.

Contributors should stop asking:

> "Which widget should do this?"

and instinctively begin asking:

> **"Which resolved behaviour am I implementing?"**

When every contributor naturally thinks this way, Components become exactly what they should be:

Simple.

Predictable.

Replaceable.

The runtime architecture remains the intelligence of Mosaic.

The Component Library simply gives that intelligence a visible form.
