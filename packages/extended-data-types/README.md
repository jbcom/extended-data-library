# Extended Data Types

*Typed utilities for Python data formats and structures.*

[![CI Status](https://github.com/jbcom/extended-data-library/actions/workflows/ci.yml/badge.svg)](https://github.com/jbcom/extended-data-library/actions/workflows/ci.yml)
[![PyPI Package latest release](https://img.shields.io/pypi/v/extended-data-types.svg)](https://pypi.org/project/extended-data-types/)
[![Supported versions](https://img.shields.io/pypi/pyversions/extended-data-types.svg)](https://pypi.org/project/extended-data-types/)

Extended Data Types provides safe, typed helpers for working with common serialization formats (YAML, JSON, TOML, HCL, Base64), file system operations, data structure manipulation, string transformations, and type utilities.

## Key Features

- **Serialization** - Encode and decode YAML, JSON, TOML, HCL, and Base64 with consistent APIs
- **File System** - Platform-aware path handling, Git repository discovery, encoding detection
- **Data Structures** - Enhanced list and dictionary operations (flatten, filter, deep merge)
- **String Utilities** - Case conversion, humanization, pluralization, URL validation
- **Type Safety** - Safe type conversion, validation, and full type annotations

---

## Installation

```bash
pip install extended-data-types
```

## Quick Start

### YAML

```python
from extended_data_types import encode_yaml, decode_yaml

data = {"name": "Alice", "age": 30}
yaml_str = encode_yaml(data)
print(yaml_str)
# name: Alice
# age: 30

decoded = decode_yaml(yaml_str)
print(decoded)  # {'name': 'Alice', 'age': 30}
```

### Base64

```python
from extended_data_types import base64_encode

encoded = base64_encode("Hello, world!")
print(encoded)  # SGVsbG8sIHdvcmxkIQ==
```

### File Path Utilities

```python
from extended_data_types import match_file_extensions

is_text = match_file_extensions("example.txt", [".txt", ".log"])
print(is_text)  # True
```

### String Transformations

```python
from extended_data_types import to_snake_case, to_camel_case

print(to_snake_case("MyClassName"))   # my_class_name
print(to_camel_case("my_function"))   # myFunction
```

---

## Contributing

Contributions are welcome! Please see the [Contributing Guidelines](https://github.com/jbcom/extended-data-library/blob/main/CONTRIBUTING.md) for more information.

## Project Links

- [**PyPI**](https://pypi.org/project/extended-data-types/)
- [**GitHub**](https://github.com/jbcom/extended-data-library/tree/main/packages/extended-data-types)
- [**Documentation**](https://extendeddata.dev)
- [**Changelog**](https://github.com/jbcom/extended-data-library/blob/main/packages/extended-data-types/CHANGELOG.md)
