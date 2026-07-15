<!--
File: docs/design/system/mds-006-composition-engine/10-multi-device-composition.md
Document: MDS-006
Chapter: 10
Title: Multi-Device Composition
Status: Draft
Version: 0.4
-->

# Multi-Device Composition

---

# Purpose

The Composition Engine solves one Runtime World.

Users, however, may experience that World across many different devices.

Examples include:

- phone
- tablet
- desktop
- television
- foldable devices
- future spatial interfaces
- voice interfaces

This chapter defines how one solved Composition becomes many presentations without fragmenting behavioural understanding.

There should never be:

- Mobile Composition
- TV Composition
- Desktop Composition

There should only ever be:

> **One Composition.**

---

# Definition

Within MDS, **Multi-Device Composition** is defined as:

> **The deterministic projection of one solved Runtime Composition across multiple presentation environments while preserving behavioural understanding.**

Presentation adapts.

Understanding does not.

---

# Philosophy

Traditional applications frequently solve interfaces separately.

Examples.

```mermaid
flowchart TD

N1["Mobile UI"]
N2["Desktop UI"]
N3["TV UI"]

N1 --> N2
N2 --> N3
```

These experiences often diverge over time.

Mosaic intentionally solves once.

```mermaid
flowchart TD

N1["Runtime World"]
N2["Composition"]
N3["Expressions"]
N4["Device Projection"]
N5["Presentation"]

N1 --> N2
N2 --> N3
N3 --> N4
N4 --> N5
```

The World remains identical.

Only its physical expression changes.

---

# One Runtime

Every client consumes the same Runtime World.

Desktop.

↓

Runtime World.

Phone.

↓

Same Runtime World.

Television.

↓

Same Runtime World.

No client owns independent behavioural state.

The Runtime World remains the single source of truth.

---

# One Composition

Likewise.

Every client consumes the same solved Composition.

Examples.

```

Hero

Timeline

Relationships

Progress

Actions
```

These Expressions remain identical regardless of device.

The Adaptive Layout system determines presentation.

---

# Device Projection

The client-side Adaptive Layout implementation projects solved Expressions into layouts for the current Presentation constraints.

Conceptually.

```mermaid
flowchart TD

N1["Composition"]
N2["Expression Tree"]
N3["Adaptive Layout"]
N4["Phone"]

N1 --> N2
N2 --> N3
N3 --> N4
```

```mermaid
flowchart TD

N1["Composition"]
N2["Expression Tree"]
N3["Adaptive Layout"]
N4["Desktop"]

N1 --> N2
N2 --> N3
N3 --> N4
```

Behaviour remains identical.

---

# Capability Profiles

Implementations may describe current Presentation constraints through a capability profile.

The profile may include:

- available extent and orientation
- viewing distance
- input methods
- typography and accessibility settings
- renderer features
- measured runtime budget

It must not reduce these inputs to a permanent phone, tablet, desktop or television layout class.

No capability profile receives a different Composition.

---

# Viewing Distance

Projection should account for viewing distance.

Television.

↓

Greater spacing.

↓

Larger typography.

↓

Expanded Hero.

Phone.

↓

Closer reading.

↓

Compact hierarchy.

The behavioural language remains unchanged.

---

# Input Independence

Different devices expose different interaction methods.

Examples.

- touch
- mouse
- keyboard
- remote
- voice
- gesture

These affect interaction.

They do not affect Composition.

Behaviour remains independent from input technology.

---

# Expression Stability

Expressions should remain recognisable across every platform.

Timeline.

↓

Timeline.

Hero.

↓

Hero.

Relationships.

↓

Relationships.

Only visual expression changes.

Conceptual identity remains constant.

---

# Progressive Projection

Smaller devices should progressively disclose information.

Not remove it.

Incorrect.

```mermaid
flowchart TD

N1["Desktop"]
N2["Cast"]
N3["Phone"]
N4["Removed"]

N1 --> N2
N2 --> N3
N3 --> N4
```

Preferred.

```mermaid
flowchart TD

N1["Desktop"]
N2["Cast"]
N3["Phone"]
N4["Collapsed"]
N5["Expandable"]

N1 --> N2
N2 --> N3
N3 --> N4
N4 --> N5
```

Understanding remains available.

Presentation adapts.

---

# Simultaneous Devices

Future Mosaic experiences may span multiple devices simultaneously.

Examples.

Television.

↓

Playback.

Phone.

↓

Companion controls.

Tablet.

↓

Metadata.

Each device receives a different Presentation Model.

All consume the same Runtime World.

Behaviour remains synchronised.

---

# Runtime Synchronisation

Every device should observe identical behavioural evolution.

Example.

Playback pauses.

↓

Television updates.

↓

Phone updates.

↓

Tablet updates.

↓

Runtime World remains authoritative.

Presentation latency should never alter behavioural ordering.

---

# Material Consistency

Different devices may implement Materials differently.

Desktop.

↓

Premium Acrylic.

Phone.

↓

Simplified Acrylic.

Television.

↓

Greater perceived depth.

The Material language remains recognisably Mosaic.

Only rendering fidelity changes.

---

# Typography Consistency

Editorial hierarchy remains identical.

Examples.

Hero.

↓

Heading.

Supporting.

↓

Body.

Caption.

↓

Caption.

Different devices may alter:

- spacing
- measure
- scale

Editorial meaning remains unchanged.

---

# Motion Consistency

Motion sequencing should remain identical.

Examples.

Hero moves.

↓

Supporting responds.

↓

Environment settles.

Different platforms may adjust:

- duration
- interpolation
- rendering fidelity

Behavioural ordering must remain identical.

---

# Accessibility

Accessibility should remain device independent.

Large text.

↓

All devices.

Reduced motion.

↓

All devices.

High contrast.

↓

All devices.

Accessibility profiles belong to the Runtime World.

Not individual platforms.

---

# Runtime Identity

Users should always feel they are interacting with:

> The same Companion.

Changing device should never require relearning:

- hierarchy
- navigation
- behaviour
- editorial language

Only presentation changes.

---

# Device Handover

Future implementations may support seamless device handover.

Example.

Watching.

↓

Television.

↓

Continue on Phone.

↓

Same Runtime World.

↓

Same Hero.

↓

Same Progress.

↓

Same Composition.

The transition should feel like continuing the same experience rather than opening a different application.

---

# Modules

Modules contribute:

- behaviour
- information
- relationships

Modules never target specific devices.

The Composition Engine determines how module content appears everywhere.

Every module therefore automatically supports future devices.

---

# Good Examples

## Television

Hero.

↓

Large presentation.

↓

Minimal controls.

↓

Immersive experience.

---

## Phone

Hero.

↓

Compact presentation.

↓

Progressive disclosure.

↓

Comfortable touch interaction.

The behavioural language remains identical.

---

## Foldable

One Runtime World.

↓

Adaptive projection.

↓

Expanded editorial layout.

↓

Same Expressions.

The experience evolves naturally with the device.

---

# Anti-patterns

## Mobile Features

Mobile receives different behaviour.

---

## Platform Hierarchy

Television invents different conceptual priorities.

---

## Device Modules

Modules creating independent device interfaces.

---

## Separate Runtime

Every client maintaining its own behavioural state.

---

# Multi-Device Composition Model

```mermaid
flowchart TD

RuntimeWorld
RuntimeWorld --> Composition
Composition --> ExpressionTree
ExpressionTree --> AdaptiveLayout
AdaptiveLayout --> Desktop
AdaptiveLayout --> Phone
AdaptiveLayout --> Tablet
AdaptiveLayout --> Television
AdaptiveLayout --> Voice
Desktop --> Presentation
Phone --> Presentation
Tablet --> Presentation
Television --> Presentation
Voice --> Presentation
```

One Runtime World.

One Composition.

Many Presentations.

---

# Relationship To Future Chapters

The next chapter defines **Composition Engine Governance**.

Multi-Device Composition explains:

> **How one solved World becomes many device experiences.**

Governance explains:

> **How the Composition Engine evolves while preserving one consistent behavioural architecture across every future client.**

Together they complete the architectural foundation of the Mosaic runtime.

---

# Summary

Multi-Device Composition ensures that Mosaic remains one platform rather than a collection of applications.

Users should experience:

- one World,
- one Companion,
- one behavioural language,

regardless of:

- screen size,
- input method,
- rendering technology,
- future devices.

Presentation may change.

Understanding never should.
