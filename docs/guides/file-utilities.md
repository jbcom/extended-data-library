# File Utilities Guide

The filesystem helpers are designed for repository-aware workflows and explicit
content decoding.

:::{card} Design Rule
:class-card: docs-card docs-card--primary

`read_file()` reads bytes or text. `decode_file()` decodes already-read content.
Keeping those responsibilities separate makes it easier to compose local files,
remote URLs, and explicit format inference cleanly.
:::

## Reading and Writing Files

```python
from extended_data_types import decode_file, read_file, write_file

write_file("settings.json", {"debug": True}, tld=".")
content = read_file("settings.json", tld=".")
settings = decode_file(content, file_path="settings.json")
```

`decode_file()` decodes a string payload. It does not open paths directly.

## Supported Suffix Inference

:::{table}
:widths: 30 70

| Suffix | Decoding / writing behavior |
| --- | --- |
| `.yaml`, `.yml` | YAML |
| `.json` | JSON |
| `.toml`, `.tml` | TOML |
| `.hcl`, `.tf`, `.tfvars` | HCL / Terraform-style data |
| anything else | Raw text |
:::

## Path Resolution

```python
from pathlib import Path

from extended_data_types import resolve_local_path

project_root = Path.cwd()
print(resolve_local_path("src/extended_data_types/__init__.py", tld=project_root))
```

If you omit `tld`, the helper tries to discover the current Git repository root.

## Repository Helpers

```python
from extended_data_types import get_parent_repository, get_repository_name, get_tld

repo = get_parent_repository()
print(get_repository_name(repo) if repo else None)
print(get_tld())
```

## URL Validation

The root-exported `is_url()` helper is intentionally strict and only accepts
safe `http` and `https` URLs.

If you need the lower-level parser-style URL check, import
`extended_data_types.string_data_type.is_url` directly.

## Related Guides

- [Support and Compatibility](./support-and-compatibility.md)
- [Quickstart](../getting-started/quickstart.md)
- [Serialization Guide](./serialization.md)
- [Workflow Recipes](./workflow-recipes.md)
- [Choosing the API Surface](./api-surface.md)
