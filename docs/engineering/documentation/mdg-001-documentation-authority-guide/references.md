<!--
File: docs/engineering/documentation/mdg-001-documentation-authority-guide/references.md
Document: MDG-001
Status: Active
-->

# References

---

# Purpose

This chapter identifies documents that support, complement or govern the material presented within MDG-001.

References exist to improve traceability throughout the Mosaic documentation library while avoiding unnecessary duplication.

As the documentation ecosystem evolves, this chapter should be expanded to include additional authoritative specifications.

---

# Governing Documents

The following documents govern or are governed by this specification.

| Document | Relationship |
|----------|--------------|
| MDG-001 | Governing documentation standard. |
| [MAC-001](../../architecture/mac-001-platform-architecture/index.md) | Applies the standards defined by this guide. |
| MEG Series | Should conform to this guide. |
| MIP Series | Should conform to this guide. |
| MOP Series | Should conform to this guide. |
| MDL Series | Should conform to this guide. |
| MDS Series | Should conform to this guide. |
| MAD Series | Should conform to this guide. |
| MDP Series | Should conform to this guide. |
| MRM Series | Should conform to this guide. |

---

# Related Mosaic Specifications

As the documentation library expands, additional references should be maintained here.

Examples include:

- [MAC-001 — Platform Architecture](../../architecture/mac-001-platform-architecture/index.md)
- [MAC-001 — Platform Architecture](../../architecture/mac-001-platform-architecture/03-capability-model.md), Capability Model
- [MEG-001 — Go Engineering Standards](../../guides/meg-001-go-engineering-standards/index.md)
- [MDL-001 — Mosaic Design Language Vision](../../../design/language/mdl-001-vision/index.md)
- [MDS-001 — Design Token Architecture](../../../design/system/mds-001-design-token-architecture/index.md)

References should always identify the authoritative document rather than duplicate its contents.

---

# External Standards

Each Mosaic document type is a branded profile of an established open standard. The profiles themselves are recorded within [10 — Standards Mapping](10-standards-mapping.md). The sources are listed here.

## Architecture Decision Records (ADR)

Architecture Decision Records provide a well-established approach to preserving architectural reasoning and historical decision making.

Mosaic Architecture Decisions profile the ADR pattern, and specifically the Markdown Architectural Decision Record (MADR) template, under the Mosaic name.

- Michael Nygard, *Documenting Architecture Decisions*, 2011.
- *MADR — Markdown Architectural Decision Records*, <https://adr.github.io/madr/>
- *Architecture Decision Record organisation*, <https://adr.github.io/>

---

## RFC And PEP Process Documents

The Internet Engineering Task Force Request for Comments series and the Python Enhancement Proposal process both demonstrate the long-term value of a written proposal process that records rejected and withdrawn ideas alongside accepted ones.

Mosaic Design Proposals profile that process.

- *PEP 1 — PEP Purpose and Guidelines*, <https://peps.python.org/pep-0001/>
- *IETF RFC Series*, <https://www.rfc-editor.org/>

---

## RFC 2119 And RFC 8174 (BCP 14)

RFC 2119, as clarified by RFC 8174, defines the normative keywords used to indicate requirement levels within technical specifications. Together they form BCP 14.

Mosaic normative language carries RFC 2119 semantics using ordinary capitalisation, as recorded within [10 — Standards Mapping](10-standards-mapping.md).

- *RFC 2119 — Key words for use in RFCs to Indicate Requirement Levels*, <https://www.rfc-editor.org/rfc/rfc2119>
- *RFC 8174 — Ambiguity of Uppercase vs Lowercase in RFC 2119 Key Words*, <https://www.rfc-editor.org/rfc/rfc8174>

---

## Diátaxis Documentation Framework

The Diátaxis framework identifies four fundamental forms of documentation:

- Tutorials
- How-to Guides
- Explanation
- Reference

Mosaic Architecture Canon, Engineering Guides and Operations Playbooks profile the Diátaxis modes, which is why this guide forbids mixing explanation with instruction within a single document type.

- *Diátaxis*, <https://diataxis.fr/>

---

## Semantic Versioning

Semantic Versioning defines `MAJOR.MINOR.PATCH` numbering for released software artefacts.

Mosaic adopts only the major component, and applies it only to the contracts defined by Integration Protocols. Mosaic prose documents carry no version.

- *Semantic Versioning 2.0.0*, <https://semver.org/>

---

## Keep A Changelog

Keep a Changelog defines a human-readable convention for recording meaningful change.

Mosaic revision histories profile this convention, grouped by effective date rather than by release.

- *Keep a Changelog*, <https://keepachangelog.com/>

---

## Material for MkDocs

Material for MkDocs provides the current publishing platform for the Mosaic Architecture library.

Documentation should remain independent of any particular documentation engine while taking advantage of modern navigation, search and presentation capabilities where appropriate.

---

# Future References

As Mosaic evolves, this chapter should expand to include additional:

- architectural standards
- engineering references
- protocol specifications
- academic publications
- industry guidance

References should remain selective.

Only authoritative or genuinely influential sources should be included.

---

# Reference Maintenance

References should be reviewed periodically to ensure:

- linked documents remain available;
- referenced Mosaic specifications still exist;
- superseded documents are updated;
- obsolete references are removed where appropriate.

Maintaining accurate references improves the integrity and long-term usefulness of the documentation library.
