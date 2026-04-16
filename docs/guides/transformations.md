# Transformations Guide

The root package keeps the convenience aliases that existing callers rely on.
The namespaced transformation modules expose the richer number and string APIs.

::::{grid} 1 1 2 2
:gutter: 2

:::{grid-item-card} Root Convenience Imports
:class-card: docs-card

Best when you only need the established helpers already exported from the root
package.
:::

:::{grid-item-card} Namespaced Modules
:class-card: docs-card docs-card--secondary

Best when you want the richer, more explicit transformation APIs directly.
:::
::::

## Root Convenience Imports

```python
from extended_data_types import humanize, ordinalize, pluralize, to_snake_case

print(humanize("api_key"))
print(ordinalize(42))
print(pluralize("person"))
print(to_snake_case("HTTPResponse"))
```

## Number Transformations

```python
from extended_data_types.transformations.numbers import (
    from_fraction,
    to_fraction,
    to_roman,
    to_words,
)

print(to_roman(42))
print(to_words(3.14))
print(to_fraction(0.75))
print(from_fraction("1 1/2"))
```

## String Transformations

```python
from extended_data_types.transformations.strings import (
    camelize,
    humanize,
    parameterize,
    underscore,
)

print(camelize("api_response", uppercase_first_letter=False))
print(underscore("HTTPResponse"))
print(humanize("author_id"))
print(parameterize("Hello, World!"))
```

The root string helpers intentionally preserve the existing compatibility
surface. Use the namespaced modules when you want the newer transformation API
directly.

## Choosing Between Them

- Use root imports when compatibility and brevity matter most.
- Use namespaced modules when you want a fuller feature set in a specific domain.
- Use [Support and Compatibility](./support-and-compatibility.md) when you need
  the documented boundary between supported public surfaces and lower-level
  implementation modules.
- Use [Choosing the API Surface](./api-surface.md) when you need a broader rule
  for the whole library, not just transformations.
