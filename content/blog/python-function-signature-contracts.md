---
id: python-function-signature-contracts
title: "Python Function Signatures as Contracts"
competencies:
- Python
- Software Engineering
date_created: 2025-10-13
date_updated: 2025-10-13
description: Three tips to write better function signatures with positional & keyword parameters, generic functions and function overloads.
---

This blog post covers three ways to strengthen Python function signatures:

1. Positional & Keyword Function Parameters
2. Generic Functions with `TypeVar`
3. Function Overloading with `@overload`

## Preamble

Typing is an intermediate level Python topic.  Adding types to your Python program allows you to:

- **Improve code readability and maintainability**
- **Catch potential bugs early through static analysis**
- **Provide better documentation for your functions and methods**
- **Enable advanced tooling, such as autocompletion and refactoring support**

Good Python developers put time, care and effort into type hints for return values and parameters of functions, but they ignore the most powerful contract mechanism available: the function signature itself.

A contract is an agreement between two parties. In programming, a function signature defines the contract between the function and its callers - the stronger the contract, the happier the world.

Too much freedom in how a function is called also increases the number of mistakes a function caller can make when using a function.

## Solution One: Constraining Parameter Passing: `/` and `*` Syntax

The first solution to tightening the function signature contract is to constrain how callers can pass parameters using `/` and `*` in your function signature.

Many Python functions accept arguments in ways that invite bugs. Consider the function signature below:

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

All of these different valid function calling patterns makes refactoring the function difficult.  If we change the order of function arguments, or change parameter names, we will break code that relied on that order or those names.

The solution is to use `/` and `*` in the function signature to constrain how parameters can be passed. The function below divides parameters into three zones:

- **Positional only**: Use `/` to force parameters to be passed positionally
- **Keyword only**: Use `*` to force parameters to be passed as keywords
- **Flexible**: Parameters between `/` and `*` can be passed either way

```python
def process_data(
    data: pd.DataFrame, /, mode: str = "strict", *, encoding: str = "utf-8"
) -> None:
    pass
```

In the function above:

- We can only pass the dataframe `data` positionally
- We can pass `mode` as either positional or keyword
- We can only pass ` encoding` as a keyword

## Solution Two: Using `Typevar` for Multiple Return Types

`Typevar` allows polymorphic contracts - generic functions that can work with different return types.

Type hints lose information when functions return the same type they receive:

```python
def first(items: list) -> object:
    return items[0]


numbers = [1, 2, 3]
result = first(numbers)  # Type: object
print(result + 1)  # Type error: can't add object + int
```

The function works, but the type checker only sees `object` as the return type. You know it's an `int`, but that information is lost.

The solution to this problem is to use `TypeVar` from the `typing` module, which preserves type information through functions:

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

## Solution Three: Overloading For Multiple Function Signatures

Above we saw that `TypeVar` preserves type information through a function. But what if the return type changes based on input values?

Sometimes one function needs to behave differently based on input types, and the return type changes accordingly. Type checkers can't infer this from a single signature.  The `transform` function below illustrates the problem, as it returns different types based on the `mode` parameter:

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

The solution to this problem is to use `@overload` to declare multiple contracts:

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

## Summary

**Problems we solve:**

- **Fragile refactoring**: Changing parameter order or names breaks code in unexpected places
- **Lost type information**: Generic functions return `object` instead of preserving specific types
- **Ambiguous return types**: Type checkers can't infer return types based on input values

**Solutions:**

- **Positional/keyword constraints (`/` and `*`)**: Restrict how parameters can be passed to prevent fragile calling patterns
- **TypeVar for generics**: Preserve type information through functions with "same type in, same type out" contracts
- **@overload for multiple signatures**: Declare different return types based on input values

**When to use each:**

- **`/` and `*` syntax**: Start with keyword-only for boolean or configuration parameters, add positional-only when parameter names are unstable or meaningless
- **TypeVar**: Use when you need to preserve type information through a function (lists, dictionaries, generic containers)
- **@overload**: Use when return types vary based on input values (mode parameters, optional flags)
