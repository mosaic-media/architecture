<!--
File: engineering/meg/MEG-001 Go Engineering Standards/02-thinking-in-go.md
Document: MEG-001
Status: Draft
Version: 0.1
-->

# Thinking in Go

> *Go is not a simpler Java. It is a language built upon a fundamentally different philosophy.*

---

# Purpose

Many engineers arriving at Go have backgrounds in object-oriented languages such as Java, C# or C++.

While experience from those languages remains valuable, directly translating object-oriented design patterns into Go often produces software that feels unnecessarily complex, difficult to maintain and distinctly non-idiomatic.

This document establishes the mental model required to engineer software that embraces Go's strengths rather than fighting against them.

---

# Why This Matters

Most poorly designed Go software is not written by inexperienced programmers.

It is written by experienced programmers attempting to solve Go problems using the tools and philosophies of another language.

Go intentionally omits many language features common elsewhere.

This is not because they are impossible.

It is because the language encourages solving problems differently.

Learning Go therefore requires more than learning syntax.

It requires changing how software is designed.

The Go team explicitly cautions against translating Java or C++ designs directly, encouraging developers to think in Go's own idioms instead.  [oai_citation:0‡Go](https://go.dev/doc/effective_go?v=1&utm_source=chatgpt.com)

---

# The Fundamental Shift

Most object-oriented languages begin with types.

Go begins with behaviour.

Traditional OO thinking often follows:

```
Object

↓

Inheritance

↓

Framework

↓

Application
```

Go thinking instead follows:

```
Problem

↓

Behaviour

↓

Composition

↓

Application
```

The focus shifts from building class hierarchies to composing small behaviours into larger systems.

---

# Java Thinking vs Go Thinking

| Object-Oriented Thinking | Go Thinking |
|--------------------------|-------------|
| Everything is an object | Everything is a value |
| Build inheritance trees | Compose small components |
| Start with abstractions | Start with concrete implementations |
| Design interfaces first | Discover interfaces when needed |
| Frameworks organise applications | Packages organise applications |
| Configuration drives behaviour | Code drives behaviour |
| Exceptions | Explicit error values |
| Dependency Injection Containers | Constructor injection |
| Large service hierarchies | Small cohesive packages |

Neither philosophy is universally better.

They optimise for different goals.

Mosaic adopts the Go approach because it produces software that is easier to understand, easier to refactor and easier to operate.

---

# Concrete Before Abstract

One of the most common mistakes made by developers new to Go is introducing abstraction before it has demonstrated value.

For example:

```
UserService

↓

UserServiceImpl

↓

DefaultUserService

↓

BaseUserService

↓

AbstractUserService
```

This hierarchy communicates very little.

Instead, Go encourages:

```
UserService
```

If only one implementation exists, one type is sufficient.

Additional abstractions should only appear when multiple implementations genuinely require them.

---

# Behaviour Over Hierarchy

Go does not organise software through inheritance.

Instead, software is built by combining behaviours.

Rather than asking:

> "What does this type inherit?"

Ask:

> "What behaviour does this type provide?"

This small change dramatically influences software architecture.

Systems become collections of collaborating components rather than deeply nested inheritance trees.

---

# Interfaces Are Discovered

In many object-oriented languages, interfaces are designed before implementations.

Within Mosaic, the opposite approach is preferred.

Implement the concrete type first.

Allow the interface to emerge naturally from actual usage.

Interfaces should exist because multiple consumers require a common behaviour.

Not because every service "might one day" need another implementation.

This aligns with common Go guidance that interfaces generally belong near the consumer and should not be created speculatively.  [oai_citation:1‡GitHub](https://github.com/pthethanh/effective-go?utm_source=chatgpt.com)

---

# Fewer Layers

Enterprise software often accumulates unnecessary architectural layers.

```
Controller

↓

Service

↓

Manager

↓

Provider

↓

Repository

↓

DAO

↓

Database
```

Each layer introduces:

- indirection
- coupling
- maintenance cost
- cognitive overhead

Go generally favours fewer, more meaningful boundaries.

Every layer should exist because it owns a distinct responsibility.

Not because another project used the same architecture.

---

# Packages Replace Frameworks

Large object-oriented applications frequently rely on frameworks to define application structure.

Go instead relies upon packages.

Packages define:

- ownership
- responsibility
- visibility
- dependency direction

A well-designed package communicates more architectural intent than dozens of annotations or configuration files.

Later chapters establish Mosaic's package organisation standards.

---

# Explicit Dependencies

Dependencies should always be visible.

Poor:

```
Global state

↓

Hidden singleton

↓

Reflection

↓

Runtime discovery
```

Preferred:

```
main()

↓

Construct dependencies

↓

Inject explicitly

↓

Application starts
```

Reading `main.go` should explain how the application is assembled.

Nothing important should happen "behind the scenes."

---

# Errors Are Expected

Many languages treat errors as exceptional.

Go treats them as ordinary outcomes.

This changes software design considerably.

Instead of assuming success and catching failures later, Go encourages engineers to acknowledge failure immediately.

Error handling therefore becomes part of the normal control flow rather than a separate mechanism.

Future chapters establish Mosaic's error handling philosophy.

---

# Small Things Build Large Systems

Large systems should emerge from combining many small pieces.

Examples include:

- small packages
- small interfaces
- small structs
- small functions
- focused responsibilities

Large components should be considered a design smell until proven necessary.

---

# Engineering Through Constraints

Some developers initially perceive Go as "missing features."

In reality, Go intentionally limits certain language capabilities.

Examples include:

- no inheritance
- no implicit constructors
- no exceptions
- limited metaprogramming
- minimal reflection
- no annotation system

These constraints encourage simpler software.

Rather than asking:

> "Why doesn't Go allow this?"

Ask:

> "What design is Go encouraging instead?"

Very often, the simpler solution proves easier to maintain.

---

# Mosaic Philosophy

Within Mosaic, engineers SHOULD continuously ask:

- Can this become simpler?
- Is this abstraction necessary?
- Would another engineer immediately understand this?
- Does this follow established Go conventions?
- Am I solving today's problem or an imaginary future problem?

If uncertainty exists, the simpler solution should generally be preferred.

Complexity should justify itself.

Simplicity does not.

---

# Key Takeaways

Thinking in Go means accepting several fundamental ideas.

- Concrete types come before abstractions.
- Behaviour is more important than hierarchy.
- Composition replaces inheritance.
- Packages replace frameworks.
- Explicit dependencies replace runtime magic.
- Simplicity is a competitive advantage.
- Readability is an engineering feature.
- Good architecture removes unnecessary decisions.

These ideas form the foundation upon which every subsequent engineering standard within the MEG is built.

---

# Review Status

**Status**

Draft

**Owner**

Lead Software Architect

**Previous File**

`01-engineering-philosophy.md`

**Next File**

`03-project-structure.md`
