<!--
File: docs/engineering/architecture/mdp-001-adaptive-composition-runtime/14-adaptive-tile-model.md
Document: MDP-001
Status: Draft
-->

# Adaptive Tile Model

> **Proposal status:** Deferred and non-authoritative. This chapter preserves post-v1 research; it is not a Mosaic v1 requirement.

---

# Purpose

This chapter preserves the deferred Tile model that previously sat between Expressions and Components.

Mosaic v1 does not require this abstraction. Its semantic SDUI resolves directly into the governed components defined by [MDS-008 — Component Library](../../../design/system/mds-008-component-library/index.md).

---

# Stable Identity

A future Adaptive Composition Runtime may use a Tile as the presentation identity of one solved Expression.

Tile identity would remain stable while the Tile is repositioned, resized, reparented or moved between logical depth planes. Component instances would remain disposable renderer details.

---

# Capacity-Sensitive Viewport

A Tile shell may change width, height and aspect ratio while preserving:

- artwork aspect ratio
- content orientation
- item ordering
- row dimensions
- semantic priority

For vertically repeating content, the proposed visible item count is:

\[
N_{\mathrm{visible}}
=
\operatorname{clamp}\left(
\left\lfloor
\frac{H_{\mathrm{content}}+g}{H_{\mathrm{row}}+g}
\right\rfloor,
1,
N_{\mathrm{available}}
\right)
\]

Additional capacity reveals additional semantically ordered content. Reduced capacity suppresses the lowest-priority content that no longer fits.

Visibility thresholds use hysteresis:

\[
H\ge H_{\mathrm{show}}
\quad\Longrightarrow\quad
\text{show the next item}
\]

\[
H<H_{\mathrm{hide}}
\quad\Longrightarrow\quad
\text{hide that item}
\]

with:

\[
H_{\mathrm{show}}>H_{\mathrm{hide}}
\]

This prevents content from oscillating near one capacity boundary.

---

# Nested Scroll Model

The proposed main Canvas owns vertical scrolling while individual Tiles may own horizontal content scrolling:

\[
\mathbf{s}_{\mathrm{canvas}}=(0,\Delta y,0)
\]

\[
\mathbf{s}_{\mathrm{tile}}=(\Delta x,0,0)
\]

For gesture displacement \((\Delta x,\Delta y)\):

\[
\operatorname{owner}
=
\begin{cases}
\text{Tile},
& |\Delta x|>|\Delta y|+\delta
\text{ and horizontal scrolling is available}\\
\text{Canvas},
& \text{otherwise}
\end{cases}
\]

When directional navigation is enabled, two horizontal scrollers should not occupy the same projected vertical band:

\[
Y(H_i)\cap Y(H_j)=\varnothing
\]

---

# Relationship To v1 Components

Mosaic v1 may implement equivalent qualitative behaviour through curated responsive variants, ordinary CSS layout and component-owned interaction.

The formulas in this chapter become relevant only if the proposal returns to Active review.
