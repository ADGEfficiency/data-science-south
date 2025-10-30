---
id: python-function-signatures
title: "Function Signatures as Contracts: Python's Hidden Type Safety"
tags: []
competencies:
- Python
- Software Engineering
date_created: 2025-10-13
date_updated: 2025-10-13
---

Stop Writing Buggy Python Functions: 4 Signature Tricks That Actually Work

Python's Secret Weapon for Type Safety (It's Not Type Hints)

Why Your Python Functions Are Breaking in Production (And How to Fix Them)

I Stopped Writing Python Functions the Wrong Way After Learning This

---

Type as a contract???  Contracts as an idea?

This blog post covers four ways to strengthen Python function signatures:

1. Positional & Keyword Function Parameters
2. Generic Functions with TypeVar
3. Function Overloading with `@overload`


---

https://claude.ai/chat/e532199e-0173-4370-9835-188f2eef69b9

Python developers obsess over type hints for return values and parameters, but they ignore the most powerful contract mechanism available: the function signature itself.

Most Python functions accept arguments in ways that guarantee bugs. Consider this common pattern:

```python
def process_data(data, encoding="utf-8", strict=False) -> None:
    pass
```

This signature permits all of the below as valid uses of the `process_data` function:

```python
process_data(my_data)
process_data(my_data, "latin-1")
process_data(my_data, strict=True)
process_data(my_data, "latin-1", True)
process_data(encoding="utf-8", data=my_data)
```

The variety of different calling conventions have the following impacts:

- **Refactoring**: You won't know how users are using your code, which makes changing it safely hard
- **Debugging**: Parameter order mistakes

## Constraining Parameter Passing: `/` and `*` Syntax

Most Python functions accept arguments in ways that guarantee bugs. The solution: constrain how callers can pass parameters using `/` and `*` in your function signature.

```python
def process_data(data, /, mode="strict", *, encoding="utf-8", errors="ignore"):
    pass
```

This signature divides parameters into three zones:

- Before `/`: positional-only (`data`)
- Between `/` and `*`: flexible (`mode`)
- After `*`: keyword-only (`encoding`, `errors`)

### Positional-Only Parameters `/`

```python
def process_data(data, /, encoding="utf-8", strict=False) -> None:
    # implementation
```

Parameters before `/` must be positional. This forbids `process_data(data=my_data)`, which seems restrictive until you realize what it enables: you can rename the parameter without breaking any code.

```python
def process_data(content, /, encoding="utf-8", strict=False):
    # implementation
```

Every call site still works. This is why `len(obj)` works but `len(obj=my_list)` doesn't. The standard library uses positional-only parameters everywhere to maintain backward compatibility while evolving parameter names.

### Keyword-Only Parameters `*`

```python
def process_data(data, /, *, encoding="utf-8", strict=False):
    # implementation
```

Parameters after `*` must be keywords. This prevents `process_data(my_data, "latin-1", True)`, which is unreadable at the call site. It forces `process_data(my_data, encoding="latin-1", strict=True)`.

This matters most when booleans are involved:

```python
# What does True mean here?
result = fetch_user(user_id, True)


# vs forcing clarity
def fetch_user(user_id, /, *, include_deleted=False):
    pass


result = fetch_user(user_id, include_deleted=True)
```

Keyword-only parameters make code self-documenting. They prevent reordering bugs when adding parameters. They make refactoring safer because you can't accidentally swap arguments of the same type.

The standard library adopted this pattern heavily in Python 3. Functions like `sorted()` now enforce `sorted(iterable, *, key=None, reverse=False)` to prevent the mistake of passing `reverse` positionally.

### When to Use Each

- **Positional-only**: Parameter name adds no clarity, might be renamed later, or is obvious from context
- **Keyword-only**: Configuration options, boolean flags, or any parameter that benefits from explicit naming
- **Flexible**: Parameters where both calling styles are equally clear

## Using `Typevar` for Polymorphic Contracts

Typing is a intermediate level Python topic.  Adding types to your Python program allows you to:

Type hints help, but they can lose information when functions return the same type they receive:

```python
def first(items: list) -> object:
    return items[0]


numbers = [1, 2, 3]
result = first(numbers)  # Type: object
print(result + 1)  # Type error: can't add object + int
```

The function works, but the type checker only sees `object` as the return type. You know it's an `int`, but that information is lost.

`TypeVar` preserves type information through functions:

```python
from typing import TypeVar

T = TypeVar("T")


def first(items: list[T]) -> T:
    return items[0]


numbers = [1, 2, 3]
result = first(numbers)  # Type: int
print(result + 1)  # Works!

words = ["a", "b", "c"]
result = first(words)  # Type: str
print(result.upper())  # Works!
```

The contract now says: "Give me a list of T, I'll return a T." The type checker preserves the specific type through the function.

When to use TypeVar:

**Input type determines output type:**

```python
T = TypeVar("T")


def identity(value: T) -> T:
    return value
```

**Multiple related type parameters:**

```python
K = TypeVar("K")
V = TypeVar("V")


def invert_dict(d: dict[K, V]) -> dict[V, K]:
    return {v: k for k, v in d.items()}
```

**Constrained TypeVars** limit what types are allowed:

```python
Numeric = TypeVar("Numeric", int, float)


def double(x: Numeric) -> Numeric:
    return x * 2


double(5)  # Type: int
double(5.0)  # Type: float
double("hi")  # Type error!
```

**Bounded TypeVars** require a subtype:

```python
class Animal:
    def make_sound(self) -> str: ...


T = TypeVar("T", bound=Animal)


def get_sound(animal: T) -> T:
    animal.make_sound()  # Type checker knows T has this method
    return animal
```

TypeVar is for "same type in, same type out" - one polymorphic contract that preserves type information through your function.

## Overload: Multiple Contracts for One Function

Sometimes one function needs to behave differently based on input types, and the return type changes accordingly. Type checkers can't infer this from a single signature:

```python
def transform(data: str, mode: str) -> str | list[str]:
    if mode == "split":
        return data.split()
    return data.upper()
```

A type checker sees `str | list[str]` as the return type for all calls, even though you know `mode="split"` always returns `list[str]`. This forces defensive checks:

```python
result = transform(text, "split")
# Type checker thinks result could be str or list[str]
for item in result:  # Type error: str is not iterable
    print(item)
```

Use `@overload` to declare multiple contracts:

```python
from typing import Literal, overload


@overload
def transform(data: str, mode: Literal["split"]) -> list[str]: ...


@overload
def transform(data: str, mode: Literal["upper"]) -> str: ...


def transform(data: str, mode: Literal["split", "upper"]) -> str | list[str]:
    if mode == "split":
        return data.split()
    return data.upper()
```

Now the type checker understands:

```python
result = transform(text, "split")  # Type: list[str]
for item in result:  # No type error
    print(item)

result = transform(text, "upper")  # Type: str
print(result.lower())  # No type error
```

The `@overload` signatures are type-checker-only declarations. The final signature is the actual implementation. This pattern appears throughout typed libraries to provide precise return types based on input values.

Common use cases:
- Functions that return different types based on a mode parameter
- Functions with optional parameters that change the return type
- APIs that return more specific types when given more specific inputs

```python
@overload
def fetch_user(user_id: int, *, include_profile: Literal[True]) -> UserWithProfile: ...

@overload
def fetch_user(user_id: int, *, include_profile: Literal[False] = False) -> User: ...

def fetch_user(user_id: int, *, include_profile: bool = False) -> User | UserWithProfile:
    # implementation
```

Type checkers now know that `fetch_user(123, include_profile=True)` returns `UserWithProfile`, not just `User`.

## Why This Matters

Function signatures are contracts between you and every caller. Loose contracts mean:
- Refactoring breaks code in unexpected places
- Call sites are ambiguous
- Type checkers can't help you

Tight contracts mean:
- Refactoring is safer
- Code is self-documenting
- Type checkers catch bugs before runtime

The Python standard library evolved to use these features heavily. Your code should too.

Start with keyword-only for any boolean or configuration parameter. Add positional-only when parameter names are unstable or meaningless. Use `TypeVar` when you need to preserve type information through a function. Use `@overload` when return types vary with input values.

Your future self, debugging production at 2am, will thank you for the clarity.
