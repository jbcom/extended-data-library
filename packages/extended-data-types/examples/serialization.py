#!/usr/bin/env python3
"""Serialization examples for extended-data-types library.

This module demonstrates YAML, JSON, TOML, and Base64 encoding/decoding
utilities provided by the library.
"""

from __future__ import annotations

from extended_data_types import (
    base64_decode,
    base64_encode,
    decode_json,
    decode_toml,
    decode_yaml,
    encode_json,
    encode_toml,
    encode_yaml,
)


def demonstrate_yaml() -> None:
    """Demonstrate YAML encoding and decoding."""
    data = {
        "name": "example",
        "version": "1.0.0",
        "features": ["yaml", "json", "toml"],
        "config": {"debug": True, "port": 8080},
    }

    # Encode to YAML
    yaml_str = encode_yaml(data)

    # Decode from YAML
    decode_yaml(yaml_str)


def demonstrate_json() -> None:
    """Demonstrate JSON encoding and decoding."""
    data = {
        "users": [
            {"id": 1, "name": "Alice", "active": True},
            {"id": 2, "name": "Bob", "active": False},
        ],
        "metadata": {"total": 2, "page": 1},
    }

    # Encode to JSON (uses orjson for speed)
    json_str = encode_json(data)

    # Decode from JSON
    decode_json(json_str)


def demonstrate_toml() -> None:
    """Demonstrate TOML encoding and decoding."""
    data = {
        "package": {"name": "my-app", "version": "0.1.0"},
        "dependencies": {"requests": ">=2.28.0", "pyyaml": ">=6.0"},
    }

    # Encode to TOML
    toml_str = encode_toml(data)

    # Decode from TOML
    decode_toml(toml_str)


def demonstrate_base64() -> None:
    """Demonstrate Base64 encoding and decoding."""
    # Simple string encoding
    text = "Hello, World!"
    encoded = base64_encode(text, wrap_raw_data=False)

    # Decoding
    base64_decode(encoded, unwrap_raw_data=False)

    # With data wrapping (useful for structured data)
    wrapped_encoded = base64_encode(text, wrap_raw_data=True)
    base64_decode(wrapped_encoded, unwrap_raw_data=True)


if __name__ == "__main__":
    demonstrate_yaml()
    demonstrate_json()
    demonstrate_toml()
    demonstrate_base64()
