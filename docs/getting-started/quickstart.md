# Quickstart

The top-level package exposes a backward-compatible convenience API for the
most common helpers, and the documented behavior is aligned across the
project's supported Python versions.

:::{card} What You’ll Do
:class-card: docs-card

Create structured data, write it to disk with suffix-aware encoding, read it
back, and decode it without dropping down into lower-level modules.
:::

## Serialization and File Helpers

```python
from extended_data_types import decode_file, encode_yaml, read_file, write_file

config = {"service": "api", "enabled": True}
write_file("config.yaml", config, encoding="yaml", tld=".")

yaml_text = read_file("config.yaml", tld=".")
decoded = decode_file(yaml_text, file_path="config.yaml")

print(encode_yaml(decoded))
```

`decode_file()` decodes already-read content. It does not read from the
filesystem on its own.

## HCL in One Step

```python
from extended_data_types import decode_hcl2, encode_hcl2

terraform = {"locals": [{"region": "us-east-1"}]}
hcl_text = encode_hcl2(terraform)

assert decode_hcl2(hcl_text) == terraform
```

## Transformation Namespaces

```python
from extended_data_types import humanize, to_snake_case
from extended_data_types.transformations.numbers import to_fraction, to_words

print(to_snake_case("HTTPResponse"))
print(humanize("api_key"))
print(to_words(42))
print(to_fraction(0.75))
```

## Next Steps

- See [Support and Compatibility](../guides/support-and-compatibility.md) for
  the supported Python range, public API boundaries, and release-bar rules.
- See [Choosing the API Surface](../guides/api-surface.md) for when to stay on
  root imports and when to move into namespaced modules.
- See [Composing Helpers](../guides/composing-helpers.md) for end-to-end
  patterns that combine file, serialization, map, and transformation helpers.
- See [Workflow Recipes](../guides/workflow-recipes.md) for complete patterns
  you can lift into real config and payload pipelines.
- See [Serialization Guide](../guides/serialization.md) for format-specific examples.
- See [File Utilities Guide](../guides/file-utilities.md) for filesystem and decoding helpers.
- See [Transformations Guide](../guides/transformations.md) for the namespaced helper modules.
