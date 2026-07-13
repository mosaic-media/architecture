<!--
File: engineering/meg/MEG-001 Go Engineering Standards/08-error-handling.md
Document: MEG-001
Status: Draft
Version: 0.1
-->

# Error Handling

> *Errors are not exceptional. They are an expected outcome of software interacting with the real world.*

---

# Purpose

Go treats errors as values.

Unlike languages that separate normal execution from exceptional execution, Go requires engineers to acknowledge failure explicitly.

Within Mosaic, error handling is considered part of the application's public behaviour.

An error should communicate:

- what failed
- why it failed
- whether recovery is possible
- enough context to diagnose the problem

Nothing more.

Nothing less.

---

# Philosophy

Within Mosaic:

> **Errors are part of the API.**

Returning an error is not admitting failure.

It is communicating reality.

Every function capable of failing should communicate that possibility honestly.

Ignoring failure is considered a defect.

---

# Errors Are Values

Errors should be treated like every other value in Go.

They should be:

- returned
- wrapped
- inspected
- propagated
- transformed

They should not be hidden.

They should not be ignored.

---

# Handle Errors Immediately

Errors SHOULD be handled at the point they are encountered.

Preferred:

```go
user, err := repo.Find(ctx, id)
if err != nil {
    return nil, fmt.Errorf("find user: %w", err)
}
```

Avoid:

```go
user, err := repo.Find(ctx, id)

// 50 lines later...

if err != nil {
    ...
}
```

The further an error travels before being acknowledged, the harder it becomes to understand.

---

# Never Ignore Errors

The following is prohibited.

```go
value, _ := parser.Parse(data)
```

Likewise:

```go
_ = file.Close()
```

Every ignored error must be an intentional engineering decision.

If an error is intentionally ignored, a comment SHOULD explain why.

Example:

```go
// Best effort cleanup.
_ = os.Remove(tempFile)
```

---

# Add Context

Errors should accumulate context as they move upwards.

Poor:

```go
return err
```

Better:

```go
return fmt.Errorf("load metadata: %w", err)
```

Even better:

```go
return fmt.Errorf("load metadata for %q: %w", mediaID, err)
```

Context should describe the operation that failed.

Not merely repeat the underlying error.

---

# Wrap Errors Deliberately

Wrapping an error exposes it to callers through `errors.Is` and `errors.As`.

Example:

```go
return fmt.Errorf("save media: %w", err)
```

Callers may now inspect the underlying error.

This is a deliberate API decision.

Do **not** wrap every error automatically.

If exposing the underlying implementation would leak internal details or constrain future changes, prefer adding context without wrapping. The Go team recommends using `%w` only when you intentionally want callers to inspect the underlying error.  [oai_citation:0‡Go](https://go.dev/blog/go1.13-errors?utm_source=chatgpt.com)

---

# Check Errors Using errors.Is

Sentinel errors MUST be checked using:

```go
errors.Is(err, ErrNotFound)
```

Never:

```go
err == ErrNotFound
```

Wrapped errors remain discoverable through `errors.Is`.

This keeps error handling resilient as additional context is added.

---

# Check Error Types Using errors.As

Custom error types SHOULD be inspected using:

```go
var validation *ValidationError

if errors.As(err, &validation) {
    ...
}
```

Never:

```go
validation := err.(*ValidationError)
```

or

```go
switch err.(type)
```

when wrapped errors are possible.

---

# Sentinel Errors

Sentinel errors represent known business conditions.

Example:

```go
var ErrNotFound = errors.New("not found")
```

Good uses include:

- not found
- already exists
- permission denied
- invalid credentials

Sentinel errors SHOULD represent stable concepts.

They SHOULD NOT represent implementation details.

---

# Custom Error Types

Custom error types SHOULD only exist when additional information is genuinely required.

Example:

```go
type ValidationError struct {
    Field string
    Reason string
}
```

Additional structured data is appropriate.

Merely changing the error message is not.

---

# Error Messages

Error messages SHOULD:

- begin with lowercase
- avoid punctuation
- describe what happened
- avoid repeating caller context

Good:

```
connection refused
```

```
media not found
```

Poor:

```
Error:
```

```
An unexpected error occurred.
```

```
MetadataService failed because...
```

The caller already knows which service produced the error.

Error messages should compose naturally when wrapped.

---

# Log Errors Once

Errors SHOULD be logged exactly once.

Typically this occurs at the application's boundary.

Examples include:

- HTTP middleware
- Worker entry point
- CLI command
- Scheduler
- Background processor

Lower layers SHOULD return errors.

They SHOULD NOT log them.

Otherwise identical failures become logged multiple times.

---

# Panic

`panic` is **not** an error handling mechanism.

Within Mosaic, panic is reserved for situations where the application cannot safely continue.

Examples include:

- impossible internal states
- programmer errors
- unrecoverable startup failures

Panics SHOULD NOT be used for:

- validation
- network failures
- database errors
- user input
- business logic

Most applications should execute for months without producing a panic.

---

# Recover

`recover` SHOULD only exist at application boundaries.

Examples:

- HTTP server middleware
- Worker runtime
- Scheduler

Recovering from panics deep within business logic hides defects.

Instead:

Crash the current operation.

Log sufficient diagnostic information.

Continue serving other requests where appropriate.

---

# Translate Errors

Different architectural layers speak different languages.

Example:

```
sql.ErrNoRows

↓

Repository

↓

ErrMediaNotFound

↓

Service

↓

HTTP 404
```

Business logic should never depend upon SQL errors.

Transport should never depend upon database drivers.

Each layer translates errors into concepts meaningful to the layer above.

---

# Error Boundaries

Every layer has clear responsibilities.

| Layer | Responsibility |
|--------|----------------|
| Infrastructure | Return implementation errors |
| Repository | Translate infrastructure into domain errors |
| Service | Add business context |
| Transport | Convert errors into HTTP, CLI or API responses |
| Middleware | Log and observe failures |

Each layer adds value.

None should duplicate responsibility.

---

# Avoid String Comparisons

The following is prohibited.

```go
if err.Error() == "record not found" {
    ...
}
```

Error messages are for humans.

Program logic should rely upon:

- `errors.Is`
- `errors.As`
- well-defined sentinel errors
- custom error types

Never textual comparison.

---

# Anti-Patterns

The following practices are prohibited.

## Ignoring Errors

```go
_, _ = writer.Write(data)
```

---

## Logging Then Returning

```go
log.Error(err)

return err
```

---

## Panic For Business Logic

```go
panic("user not found")
```

---

## Comparing Error Strings

```go
if err.Error() == ...
```

---

## Wrapping Everything

```go
fmt.Errorf("db: %w", sql.ErrNoRows)
```

when the caller should never know a SQL database exists.

Every wrapped error becomes part of your API surface.

---

# Mosaic Guidelines

Within Mosaic:

- Every returned error MUST be handled.
- Errors SHOULD gain context as they propagate.
- Errors MUST NOT be ignored silently.
- Lower layers MUST NOT log errors.
- Errors SHOULD be logged once.
- Business logic SHOULD define business errors.
- `errors.Is` MUST replace equality checks.
- `errors.As` MUST replace type assertions where wrapping is possible.
- Panic is reserved for unrecoverable programmer failures.

---

# Summary

Error handling is communication.

Every error should answer:

- What failed?
- Why did it fail?
- Can the caller recover?
- Is there enough context to diagnose the problem?

If those questions are answered clearly, the error has fulfilled its purpose.

---

# Review Status

**Status**

Draft

**Owner**

Lead Software Architect

**Previous File**

`07-composition-and-polymorphism.md`

**Next File**

`09-context-and-cancellation.md`
