# Composing Helpers

The library is most useful when you treat its helpers as a small, typed utility
layer instead of one-off convenience functions. This guide shows the composition
patterns the public API is designed to support.

:::{card} Core Idea
:class-card: docs-card docs-card--primary

Use small primitives for one concern at a time: read content, infer a format,
decode it, normalize or merge it, and write it back through the matching export
path.
:::

## Why This Holds Up in Automation

- `read_file()` and `decode_file()` stay separate, so transport and parsing are explicit.
- format inference is centralized in the same public helpers that power file writes
- HCL support round-trips plain Terraform-style data instead of parser artifacts
- normalization helpers stay side-effect-free enough to compose inside larger agents,
  CLIs, and automation pipelines

## Pattern: Read, Decode, Merge, Write

```python
from extended_data_types import decode_file, deep_merge, read_file, write_file

base_text = read_file("config/base.yaml", tld=".")
env_text = read_file("config/dev.yaml", tld=".")

base_data = decode_file(base_text, file_path="config/base.yaml")
env_data = decode_file(env_text, file_path="config/dev.yaml")

merged = deep_merge(base_data, env_data)
write_file("build/config.yaml", merged, tld=".")
```

Why this works well:

- `read_file()` is responsible only for getting content.
- `decode_file()` is responsible only for suffix-aware decoding.
- `deep_merge()` combines structured data without forcing a specific format.
- `write_file()` re-encodes based on the output suffix.

## Pattern: Normalize for APIs and Config

```python
from extended_data_types import deduplicate_map, to_snake_case, write_file

payload = {
    "HTTPResponseCode": 200,
    "tags": ["api", "api", "docs"],
}

normalized = {
    to_snake_case(key): value
    for key, value in deduplicate_map(payload).items()
}

write_file("build/payload.json", normalized, tld=".")
```

This keeps transformation, map cleanup, and serialization separate while still
using the public root surface throughout.

## Pattern: Terraform-Style Data Pipelines

```python
from extended_data_types import base64_decode, base64_encode, decode_hcl2, encode_hcl2

terraform = {
    "locals": [{"region": "us-east-1"}],
    "resource": [
        {
            "aws_s3_bucket": {
                "logs": {
                    "bucket": "my-logs-bucket",
                    "acl": "private",
                }
            }
        }
    ],
}

hcl_text = encode_hcl2(terraform)
wrapped = base64_encode(hcl_text, wrap_raw_data=False)

decoded_text = base64_decode(wrapped, unwrap_raw_data=False)
round_tripped = decode_hcl2(decoded_text)

assert round_tripped == terraform
```

This composition works because the HCL helpers expose plain Python structures
and the Base64 helpers can operate either on wrapped structured content or raw
text payloads.

## Pattern: Move from Root Imports to Namespaced Modules

```python
from extended_data_types import humanize
from extended_data_types.transformations.numbers import to_fraction, to_words
from extended_data_types.transformations.strings import parameterize

label = humanize("deployment_target")
slug = parameterize(label)
display = f"{label}: {to_words(3.5)} replicas ({to_fraction(0.75)} threshold)"
```

Use the root package where compatibility matters most, then move into the
specialized transformation namespaces when you need the richer feature sets.

## When to Reach for Lower-Level Modules

Most callers should stay on `extended_data_types` or the documented
transformation namespaces. Reach for lower-level modules directly only when you
need a documented public surface like `extended_data_types.yaml_utils` for
tagged YAML wrappers and representers.

## Related Guides

- [Support and Compatibility](./support-and-compatibility.md)
- [Quickstart](../getting-started/quickstart.md)
- [Choosing the API Surface](./api-surface.md)
- [Workflow Recipes](./workflow-recipes.md)
- [Serialization Guide](./serialization.md)
- [File Utilities Guide](./file-utilities.md)
- [Transformations Guide](./transformations.md)
