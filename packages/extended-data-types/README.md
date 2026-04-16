# Extended Data Types

Typed utilities for serialization, repository-aware file workflows, YAML and
HCL interoperability, and automation-friendly transformation pipelines.

[![CI Status](https://github.com/jbcom/extended-data-library/actions/workflows/ci.yml/badge.svg)](https://github.com/jbcom/extended-data-library/actions/workflows/ci.yml)
[![PyPI Package latest release](https://img.shields.io/pypi/v/extended-data-types.svg)](https://pypi.org/project/extended-data-types/)
[![Supported versions](https://img.shields.io/pypi/pyversions/extended-data-types.svg)](https://pypi.org/project/extended-data-types/)

## Supported Python Versions

`extended-data-types` supports Python `3.10`, `3.11`, `3.12`, `3.13`, and
`3.14`.

## Public API Model

- `extended_data_types` is the backward-compatible root convenience surface.
- `extended_data_types.transformations.numbers` and
  `extended_data_types.transformations.strings` expose the richer namespaced
  transformation APIs.
- `extended_data_types.yaml_utils` is the documented advanced surface for
  tagged YAML values and lower-level YAML helpers.

## Key Features

- Serialization helpers for YAML, JSON, TOML, HCL, and Base64.
- Repository-aware file helpers for reading, writing, decoding, and path resolution.
- Map, list, and type utilities for normalization and deep composition.
- String and number transformations for case conversion, words, ordinals, and fractions.
- Predictable read/decode/write boundaries for larger automation and agentic systems.

## Quick Start

```python
from extended_data_types import decode_file, encode_hcl2, encode_yaml, read_file, write_file

config = {"service": "api", "enabled": True}
write_file("config.yaml", config, tld=".")

yaml_text = read_file("config.yaml", tld=".")
decoded = decode_file(yaml_text, file_path="config.yaml")

terraform = {"locals": [{"region": "us-east-1"}]}
hcl_text = encode_hcl2(terraform)

print(encode_yaml(decoded))
print(hcl_text)
```

## Documentation

- Package docs: [extended-data.dev/core/data-types](https://extended-data.dev/core/data-types/)
- Monorepo docs: [extended-data.dev](https://extended-data.dev)
- Examples: [packages/extended-data-types/examples](https://github.com/jbcom/extended-data-library/tree/main/packages/extended-data-types/examples)

## Contributing

Contributions are welcome. See the shared
[Contributing Guidelines](https://github.com/jbcom/extended-data-library/blob/main/CONTRIBUTING.md).

## Project Links

- [PyPI](https://pypi.org/project/extended-data-types/)
- [GitHub](https://github.com/jbcom/extended-data-library/tree/main/packages/extended-data-types)
- [Documentation](https://extended-data.dev/core/data-types/)
- [Changelog](https://github.com/jbcom/extended-data-library/blob/main/packages/extended-data-types/CHANGELOG.md)
