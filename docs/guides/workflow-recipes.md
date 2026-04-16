# Workflow Recipes

Use this guide when you want to combine the library's primitives into complete
config, payload, and serialization workflows, especially inside larger
automation and agentic systems where explicit boundaries matter.

::::{grid} 1 1 2 2
:gutter: 2

:::{grid-item-card} Layered Config
:class-card: docs-card docs-card--feature

Read structured files, decode them explicitly, merge them, and write the result
back through the matching suffix-aware export path.
:::

:::{grid-item-card} Terraform Hand-offs
:class-card: docs-card docs-card--feature

Move plain Terraform-style data through HCL text, Base64 transport, and decode
it back without parser metadata leaking into callers.
:::

:::{grid-item-card} API Payloads
:class-card: docs-card docs-card--feature

Normalize mixed-case keys, filter lists, deduplicate list values, and serialize
the result for downstream systems.
:::

:::{grid-item-card} YAML-Native Data
:class-card: docs-card docs-card--feature

Preserve YAML tags and multiline strings while still using the higher-level file
helpers instead of dropping into custom serialization code.
:::
::::

## Recipe: Layered Config Files

```python
from extended_data_types import decode_file, deep_merge, read_file, write_file

write_file("config/base.yaml", {"service": {"debug": False}}, tld=".")
write_file("config/dev.yaml", {"service": {"debug": True}}, tld=".")

base = decode_file(read_file("config/base.yaml", tld="."), file_path="config/base.yaml")
dev = decode_file(read_file("config/dev.yaml", tld="."), file_path="config/dev.yaml")

merged = deep_merge(base, dev)
write_file("build/config.yaml", merged, tld=".")
```

This keeps file I/O, format decoding, merging, and re-encoding as separate
steps, which makes the behavior easier to reason about in larger systems.

## Recipe: Terraform Payload Hand-offs

```python
from extended_data_types import base64_decode, base64_encode, decode_hcl2, encode_hcl2

terraform = {"locals": [{"region": "us-east-1"}]}
hcl_text = encode_hcl2(terraform)

transport = base64_encode(hcl_text, wrap_raw_data=False)
decoded_hcl = base64_decode(transport, unwrap_raw_data=False)

assert decode_hcl2(decoded_hcl) == terraform
```

This is useful when a higher-level workflow needs raw text transport while the
library still owns the structured HCL contract on both ends.

## Recipe: Normalize API Payloads

```python
from extended_data_types import deduplicate_map, filter_list, to_snake_case, write_file

payload = {
    "HTTPResponseCode": 200,
    "SelectedServices": filter_list(["api", "worker", "db"], denylist=["db"]),
    "Tags": ["api", "api", "docs"],
}

normalized = {
    to_snake_case(key): value
    for key, value in deduplicate_map(payload).items()
}

write_file("build/payload.json", normalized, tld=".")
```

The primitives stay small, but together they give you a predictable
normalization pipeline without a separate wrapper layer.

## Recipe: YAML-Native Tagged Data

```python
from extended_data_types import decode_file, read_file, write_file
from extended_data_types.yaml_utils import YamlTagged

template = {
    "bucket_name": YamlTagged("!Ref", "BucketName"),
    "script": "echo one\necho two",
}

write_file("template.yaml", template, tld=".")
decoded = decode_file(read_file("template.yaml", tld="."), file_path="template.yaml")

assert decoded["bucket_name"].tag == "!Ref"
assert decoded["bucket_name"].__wrapped__ == "BucketName"
```

This is the intended path when you need YAML-native wrappers but still want the
root file helpers to handle disk I/O and format selection.

## Why These Patterns Work Well in Automation

- file I/O and decoding are separate steps, which keeps side effects explicit
- the same suffix-aware helpers are used in both examples and the public API
- HCL payloads round-trip as plain Python data
- normalization helpers can be chained without introducing wrapper state
- repository-aware path resolution makes it easier to run the same code from
  scripts, tests, and longer-lived automation processes

## Related Example Scripts

- [`packages/extended-data-types/examples/composed_workflows.py`](https://github.com/jbcom/extended-data-library/blob/main/packages/extended-data-types/examples/composed_workflows.py)
- [`packages/extended-data-types/examples/serialization.py`](https://github.com/jbcom/extended-data-library/blob/main/packages/extended-data-types/examples/serialization.py)
- [`packages/extended-data-types/examples/file_operations.py`](https://github.com/jbcom/extended-data-library/blob/main/packages/extended-data-types/examples/file_operations.py)

## Related Guides

- [Quickstart](../getting-started/quickstart.md)
- [Support and Compatibility](./support-and-compatibility.md)
- [Choosing the API Surface](./api-surface.md)
- [Composing Helpers](./composing-helpers.md)
- [Serialization Guide](./serialization.md)
