# Choosing the API Surface

Use this guide when you know what task you need to solve but you are not sure
whether to reach for the root package, a namespaced transformation module, or a
lower-level utility module.

::::{grid} 1 1 2 2
:gutter: 2

:::{grid-item-card} Use Root Imports
:class-card: docs-card

Choose the root package when you want the compatibility-friendly convenience
surface that existing callers already rely on.

- `read_file`, `write_file`, `decode_file`
- `encode_yaml`, `encode_json`, `encode_hcl2`
- `humanize`, `pluralize`, `to_snake_case`
- `all_non_empty`, `first_non_empty`, `filter_map`
:::

:::{grid-item-card} Use Namespaced Modules
:class-card: docs-card

Choose namespaced modules when you want the richer, more explicit APIs that have
grown beyond the original root surface.

- `extended_data_types.transformations.numbers`
- `extended_data_types.transformations.strings`
- `extended_data_types.yaml_utils`
:::
::::

## Recommended Defaults

:::{card} Start Here
:class-card: docs-card docs-card--primary

If the library already exposes the helper you need from `extended_data_types`,
prefer that import first. Move to a namespaced module when you need a richer
specialized surface, or when the guide and API reference point there directly.
:::

## Common Decisions

::::{tab-set}

:::{tab-item} Serialization

Use the root package.

```python
from extended_data_types import decode_hcl2, encode_json, encode_yaml
```

These helpers are stable, central to the library, and the guides document them
as the default public entry points.
:::

:::{tab-item} File Workflows

Use the root package.

```python
from extended_data_types import decode_file, read_file, resolve_local_path, write_file
```

These helpers are intentionally designed to compose: read content, infer format,
decode it, and write structured output back with matching suffix-aware encoding.
:::

:::{tab-item} Number Conversions

Prefer the namespaced module.

```python
from extended_data_types.transformations.numbers import (
    from_fraction,
    to_fraction,
    to_roman,
    to_words,
)
```

The namespaced module is where the richer number APIs live, including notation,
fractions, Roman numerals, and word-based conversions.
:::

:::{tab-item} String Transformations

Prefer the namespaced module when you need inflection helpers directly.

```python
from extended_data_types.transformations.strings import (
    camelize,
    humanize,
    parameterize,
    underscore,
)
```

Use root imports when you only need the compatibility layer such as
`humanize()` or `to_snake_case()`.
:::

:::{tab-item} YAML Internals

Use `yaml_utils` directly.

```python
from extended_data_types.yaml_utils import YamlTagged, decode_yaml, encode_yaml
```

This is the right surface when you care about tagged YAML values, custom
constructors, representers, or preserving YAML-native wrappers during export.
:::

::::

## Public Surface Rules

- The root package is the backward-compatible convenience layer.
- Namespaced transformation modules are the preferred surface for richer,
  growing domains like number and string transformations.
- Lower-level implementation modules should only be imported directly when the
  API reference documents them as intentional public surfaces.

## Related Guides

- [Support and Compatibility](./support-and-compatibility.md)
- [Quickstart](../getting-started/quickstart.md)
- [Serialization Guide](./serialization.md)
- [Transformations Guide](./transformations.md)
- [API Reference](../api/index.rst)
