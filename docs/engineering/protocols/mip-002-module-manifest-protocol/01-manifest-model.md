<!--
File: docs/engineering/protocols/mip-002-module-manifest-protocol/01-manifest-model.md
Document: MIP-002
Status: Draft
Version: 0.4
-->

# 01 — Manifest Model

---

# Definition

A Module Manifest is a machine-readable declaration of what a module contributes to Mosaic.

It describes the module before the Build Pipeline includes executable code in a Platform package.

---

# Manifest Responsibilities

A manifest declares:

- identity
- metadata
- module version
- SDK compatibility
- dependencies
- permissions
- configuration expectations
- capability support
- provided contracts
- consumed contracts
- event publications
- event subscriptions
- lifecycle requirements

These declarations allow the Supervisor to decide whether the module can participate safely.

---

# Manifest Example

```yaml
id: anilist
version: 1.0.0
sdk: ">=2.0"
capabilities:
  metadata:
    supports:
      media:
        - Anime
      identifiers:
        - AniList
        - MAL
    priority: 100
permissions:
  network:
    - graphql.anilist.co
events:
  publishes:
    public:
      - anime.episode.released
    private:
      - anilist.sync.completed
  subscribes:
    - library.item.added
    - platform.started
```

---

# Manifest Rule

> **Discovery reads manifests. Build-time composition includes code. The two steps must remain separate.**
