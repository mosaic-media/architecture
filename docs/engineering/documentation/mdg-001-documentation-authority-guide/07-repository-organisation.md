<!--
File: docs/engineering/documentation/mdg-001-documentation-authority-guide/07-repository-organisation.md
Document: MDG-001
Status: Draft
Version: 0.1
-->

# 07 — Repository Organisation

---

# Purpose

A consistent repository structure improves discoverability, maintainability and long-term scalability.

Readers should be able to locate documentation intuitively without understanding the historical evolution of the repository.

Repository organisation should therefore reflect the logical structure of Mosaic rather than the order in which documents were created.

---

# Guiding Principles

The repository should be organised according to the following principles.

## Discipline Before Document Type

Top-level directories should represent disciplines rather than document identifiers.

For example:

```text
engineering/

design/

product/

community/
```

This allows readers to locate documentation according to subject matter rather than documentation taxonomy.

---

## Document Type Within Discipline

Within each discipline, documents should be grouped according to their document type.

For example:

```text
engineering/

    architecture/

    guides/

    protocols/

    operations/
```

Likewise:

```text
design/

    language/

    system/
```

This structure mirrors the documentation hierarchy established by this guide.

---

## One Specification Per Directory

Each specification should exist within its own directory.

For example:

```text
MAC-001 Platform Architecture/

    README.md

    00-document-control.md

    01-purpose.md

    ...

    references.md

    glossary.md
```

A specification should be treated as a self-contained publication rather than a collection of unrelated Markdown files.

---

# Chapter Structure

Specifications should follow a consistent chapter structure.

Typical organisation is:

```text
README.md

00-document-control.md

01-...

02-...

...

10-references.md

11-glossary.md
```

Additional chapters may be introduced where appropriate.

However:

- Document Control should remain first.
- References should remain near the end.
- Glossary should remain the final chapter.

This consistency improves navigation across the documentation library.

---

# Naming Conventions

Directories should use descriptive names.

Preferred:

```text
MAC-001 Platform Architecture
```

Avoid:

```text
MAC001

Architecture

Platform
```

Document identifiers should always remain visible within the directory name.

---

# File Naming

Chapter filenames should use a numbered prefix.

For example:

```text
00-document-control.md

01-purpose.md

02-capability-model.md

03-runtime-lifecycle.md
```

Benefits include:

- predictable ordering
- improved readability
- stable navigation
- consistent chapter references

Numbering should remain sequential.

---

# Metadata

Every Markdown document should begin with a metadata block.

Example:

```html

```

Metadata provides:

- document identity
- file location
- publication status
- version information

Metadata should remain synchronised with the document.

---

# Repository Hierarchy

The documentation repository should remain organised by discipline.

Example:

```text
engineering/

    architecture/

        MAC-001/

        MAD-001/

        MDP-001/

    guides/

        MEG-001/

    protocols/

        MIP-001/

    operations/

        MOP-001/

documentation/

    MDG-001/

design/

    language/

        MDL-001/

    system/

        MDS-001/
```

Future disciplines may be introduced without affecting existing documentation.

---

# Supporting Assets

Shared assets should be stored separately from specifications.

For example:

```text
docs/

    assets/

        images/

        diagrams/

        logos/

        icons/

    stylesheets/

    javascripts/
```

Specifications should reference shared assets rather than duplicating them.

---

# Generated Content

Generated documentation should remain clearly separated from authored documentation.

Examples include:

- navigation indexes
- search indexes
- generated tables
- static site artefacts

Generated files should never become the authoritative source of documentation.

The Markdown specifications remain the canonical source.

---

# Documentation Tooling

Repository organisation should remain independent of any specific documentation platform.

The repository should remain readable:

- directly on GitHub
- as plain Markdown
- through static documentation generators
- through future documentation tooling

Documentation structure should therefore prioritise portability over tool-specific optimisation.

---

# Scalability

Repository organisation should support long-term growth.

The documentation library is expected to expand significantly over the lifetime of the Mosaic project.

Organisation should therefore optimise for:

- discoverability
- consistency
- maintainability
- automation

A contributor should be able to determine where a new document belongs by following the hierarchy defined within this guide rather than relying upon historical convention.
