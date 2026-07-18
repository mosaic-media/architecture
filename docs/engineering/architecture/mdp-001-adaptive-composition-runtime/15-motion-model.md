<!--
File: docs/engineering/architecture/mdp-001-adaptive-composition-runtime/15-motion-model.md
Document: MDP-001
Status: Draft
-->

# Adaptive Motion Model

> **Proposal status:** Deferred and non-authoritative. This chapter preserves post-v1 research; it is not a Mosaic v1 requirement.

---

# Purpose

This chapter preserves the deferred mathematical motion model for identity-preserving Adaptive Composition.

It does not replace v1 Motion Tokens or the Refraction Motion required to render Acrylic.

---

# Behavioural Cost

The proposed Runtime Motion Resolver derives a normalised transition significance:

\[
C_b
=
\operatorname{clamp}
\left(
w_fF+w_dD+w_tT-w_aA,
0,
1
\right)
\]

| Term | Meaning |
|------|---------|
| \(F\) | Significance of the Focus change. |
| \(D\) | Domain Boundary Cost. |
| \(T\) | Hierarchy, grouping and depth-topology change. |
| \(A\) | Continuity credit from shared identities and Anchors. |
| \(w_f,w_d,w_t,w_a\) | Private calibration weights. |

Higher Behavioural Cost may broaden participating choreography and make settlement more deliberate. It must not delay acknowledgement of user intent.

---

# Identity Classification

Before motion begins, the proposed resolver compares previous and next semantic states and classifies each Continuity Key as:

- persistent
- repositioned
- resized
- reparented
- moved between logical depth planes
- entering
- exiting

Persistent identities evolve rather than being destroyed and recreated.

---

# Critically Damped Spatial Motion

For resolved position or extent \(x\) and target \(x_t\):

\[
\ddot{x}
+2\zeta\omega\dot{x}
+\omega^2(x-x_t)
=0,
\qquad
\zeta=1
\]

For constant target and displacement \(y=x-x_t\), the exact response is:

\[
y(t)
=
\left[
y_0+\left(\dot{y}_0+\omega y_0\right)t
\right]
e^{-\omega t}
\]

Behavioural Cost may govern natural frequency within calibrated bounds:

\[
\omega(C_b)
=
\operatorname{clamp}
\left(
\omega_0-k_cC_b,
\omega_{\min},
\omega_{\max}
\right)
\]

Exact frequencies, coefficients and interruption behaviour require future prototype calibration.

---

# v1 Boundary

Mosaic v1 uses governed component transitions and Motion Tokens. This chapter does not defer or weaken the renderer mathematics owned by [MEG-014 — Refraction Engine](../../guides/meg-014-refraction-engine/index.md).
