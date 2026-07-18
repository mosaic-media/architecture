<!--
File: docs/engineering/architecture/mdp-002-tile-framework/index.md
Document: MDP-002
Status: Deferred
-->

# MDP-002 — Tile Framework

> *A Tile is what a behaviour looks like when it becomes visible.*

> **Status: Deferred.** MDP-002 is non-authoritative, unscheduled research. It is not a Mosaic v1 requirement. The v1 Tile is a governed Container Component owned by [MDS-008 — Component Library](../../../design/system/mds-008-component-library/index.md).

---

# Purpose

MDP-002 preserves the behavioural Tile model researched for a future Adaptive Composition release.

It was previously published as [MDS-007 — Tile Framework](../../../design/system/mds-007-tile-framework/index.md), and then carried as the second half of [MDP-001 — Adaptive Composition Runtime](../mdp-001-adaptive-composition-runtime/index.md). It is separated here because the Tile model and the Composition Engine are distinct subjects that were reviewed, deferred and can be reactivated independently.

The research describes Tiles as a behavioural layer sitting between an Expression and a rendered Component: the Tile carries identity and intent, and something else renders it.

---

# Relationship To Mosaic v1

Mosaic v1 uses the word **Tile** for a narrower thing, and that narrower definition is the authoritative one.

| Concept | Owner | Status |
|---------|-------|--------|
| Tile as a governed Container Component | [MDS-008 — Component Library](../../../design/system/mds-008-component-library/02-component-taxonomy.md) | Authoritative for v1 |
| Tile as a behavioural presentation primitive, with runtime resolution, lifecycle and orchestration | MDP-002 | Deferred research |

A reader implementing Mosaic today wants [MDS-008](../../../design/system/mds-008-component-library/index.md). A reader studying where the adaptive model was heading wants this proposal.

The decisions that established this boundary are [ADR-204 and ADR-205](../../../design/system/mds-008-component-library/12-adrs.md), recorded in [MDS-008](../../../design/system/mds-008-component-library/index.md) and accepted. This proposal does not restate them.

---

# Proposal Objectives

MDP-002 preserves research intended to determine whether a future client runtime can:

- give a presented unit a stable identity that survives layout change
- map solved behavioural Expressions onto that identity deterministically
- evolve a presented unit through a defined lifecycle rather than rebuilding it
- let Module-provided Expressions resolve through the same path as native ones
- coordinate many presented units after a single behavioural change

None of these are Mosaic v1 conformance requirements.

---

# Scope

This proposal covers:

- Tile philosophy, taxonomy and identity
- deterministic Expression to Tile mapping
- Tile lifecycle, composition, interaction and orchestration
- Module-provided Tiles and the resolution pipeline
- the research governance and decision history behind the model

It does not cover:

- the v1 component library, which is owned by [MDS-008 — Component Library](../../../design/system/mds-008-component-library/index.md)
- the Composition Engine, solver and layout mathematics, which are preserved by [MDP-001 — Adaptive Composition Runtime](../mdp-001-adaptive-composition-runtime/index.md)
- Design Language composition intent, which is owned by [MDL-005 — Composition Model](../../../design/language/mdl-005-composition-model/index.md)

---

# Reading Path

1. [01 — Tile Philosophy](01-tile-philosophy.md)
2. [02 — Tile Taxonomy](02-tile-taxonomy.md)
3. [03 — Expression Mapping](03-expression-mapping.md)
4. [04 — Tile Lifecycle](04-tile-lifecycle.md)
5. [05 — Adaptive Tiles](05-adaptive-tiles.md)
6. [06 — Tile Composition](06-tile-composition.md)
7. [07 — Tile Interaction](07-tile-interaction.md)
8. [08 — Runtime Tile Resolution](08-runtime-tile-resolution.md)
9. [09 — Module Tiles](09-module-tiles.md)
10. [10 — Tile Orchestration](10-tile-orchestration.md)
11. [11 — Tile Framework Governance](11-tile-governance.md)
12. [12 — Tile Decision History](12-tile-decision-history.md)
13. [13 — Contributor Guidance](13-tile-contributor-guidance.md)

---

# Reading This Proposal Safely

The chapters that follow are written in confident present-tense prose, because they were authored as an active Design System specification before the deferral. That voice has been left intact so the research remains readable as a coherent whole.

It does not make the material authoritative. Where this proposal and an authoritative specification disagree, the authoritative specification governs, and the list in Scope above says which document that is.
