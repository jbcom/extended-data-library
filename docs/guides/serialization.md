# Serialization Guide

`extended_data_types` ships convenience helpers for YAML, JSON, TOML, HCL, and
Base64 encoding and decoding.

::::{grid} 1 1 2 4
:gutter: 2

:::{grid-item-card} YAML
:class-card: docs-card docs-card--feature

Best when you need readable structured config, tagged values, or YAML-native
wrappers.
:::

:::{grid-item-card} JSON
:class-card: docs-card docs-card--feature

Best for machine-facing interchange, APIs, and deterministic serialization.
:::

:::{grid-item-card} TOML
:class-card: docs-card docs-card--feature

Best for application metadata and configuration documents with simple nesting.
:::

:::{grid-item-card} HCL
:class-card: docs-card docs-card--feature

Best for plain Terraform-style data composed of mappings, scalars, lists, and
block lists.
:::
::::

## YAML, JSON, and TOML

```python
from extended_data_types import decode_json, decode_toml, decode_yaml
from extended_data_types import encode_json, encode_toml, encode_yaml

payload = {"service": "api", "enabled": True, "ports": [80, 443]}

yaml_text = encode_yaml(payload)
json_text = encode_json(payload, indent_2=True)
toml_text = encode_toml({"app": payload})

assert decode_yaml(yaml_text) == payload
assert decode_json(json_text) == payload
assert decode_toml(toml_text)["app"] == payload
```

## HCL

HCL support targets plain Terraform-style data composed of scalars, mappings,
lists, and block lists.

```python
from extended_data_types import decode_hcl2, encode_hcl2

terraform = {
    "locals": [{"region": "us-east-1"}],
    "resource": [
        {
            "aws_s3_bucket": {
                "logs": {
                    "bucket": "my-logs-bucket",
                    "acl": "private",
                },
            },
        },
    ],
}

hcl_text = encode_hcl2(terraform)
round_tripped = decode_hcl2(hcl_text)

assert round_tripped == terraform
```

`decode_hcl2()` normalizes the raw parser output into plain Python structures by
removing parser-added quotes and block metadata. Terraform expressions remain
plain strings.

## Suffix-Aware File Writes

```python
from extended_data_types import write_file

write_file("config.yaml", {"service": "api"}, tld=".")
write_file("terraform.tf", {"locals": [{"region": "us-east-1"}]}, tld=".")
write_file("app.toml", {"tool": {"name": "extended-data-types"}}, tld=".")
```

## Base64

```python
from extended_data_types import base64_decode, base64_encode

encoded = base64_encode("hello", wrap_raw_data=False)
decoded = base64_decode(encoded, unwrap_raw_data=False)

assert decoded == "hello"
```

## Decoding File Content

Use `read_file()` and `decode_file()` together when you want to read and decode
content based on its suffix.

```python
from extended_data_types import decode_file, read_file

content = read_file("config.yaml", tld=".")
data = decode_file(content, file_path="config.yaml")
```

If you need to decide whether to use the root package or a lower-level module,
see [Choosing the API Surface](./api-surface.md).

If you need the public contract for supported Python versions and stability
rules, see [Support and Compatibility](./support-and-compatibility.md).

For end-to-end config and transport patterns that compose these helpers with
file and map utilities, see [Workflow Recipes](./workflow-recipes.md).
