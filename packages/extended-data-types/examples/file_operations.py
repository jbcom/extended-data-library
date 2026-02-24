#!/usr/bin/env python3
"""File operation examples for extended-data-types library.

This module demonstrates file path utilities, encoding detection,
and file read/write operations provided by the library.
"""

from __future__ import annotations

import tempfile

from pathlib import Path

from extended_data_types import (
    decode_file,
    file_path_depth,
    is_url,
    read_file,
    resolve_local_path,
    write_file,
)


def demonstrate_filepath_type() -> None:
    """Demonstrate the FilePath type and related utilities."""
    # FilePath accepts both str and Path
    Path("/home/user/documents/file.txt")

    # Calculate path depth
    paths = [
        "/home/user/file.txt",
        "/home/user/docs/project/readme.md",
        "relative/path/to/file.py",
    ]

    print("=== File Path Depth ===\n")
    for p in paths:
        depth = file_path_depth(p)
        print(f"  file_path_depth({p!r}) -> {depth}")
    print()


def demonstrate_url_detection() -> None:
    """Demonstrate URL detection."""
    test_strings = [
        "https://example.com/path/to/file",
        "http://localhost:8080",
        "/home/user/file.txt",
        "relative/path.txt",
        "ftp://files.example.com/data",
    ]

    print("=== URL Detection ===\n")
    for s in test_strings:
        result = is_url(s)
        print(f"  is_url({s!r}) -> {result}")
    print()


def demonstrate_file_operations() -> None:
    """Demonstrate file read/write operations."""
    print("=== File Read/Write Operations ===\n")

    # Create a temporary directory for demo
    with tempfile.TemporaryDirectory() as tmpdir:
        # Write a file
        test_file = Path(tmpdir) / "test.txt"
        content = "Hello, Extended Data Types!\nThis is a test file."

        write_file(test_file, content)
        print(f"  Wrote text file: {test_file}")

        # Read the file back
        result = read_file(test_file)
        print(f"  Read back content: {result!r}")

        # Write and read YAML
        yaml_file = Path(tmpdir) / "config.yaml"
        yaml_content = """
name: example
version: 1.0.0
settings:
  debug: true
  port: 8080
"""
        write_file(yaml_file, yaml_content)
        print(f"\n  Wrote YAML file: {yaml_file}")

        # decode_file automatically detects format
        yaml_data = decode_file(yaml_file)
        print(f"  Decoded YAML data: {yaml_data}")

        # Write and read JSON
        json_file = Path(tmpdir) / "data.json"
        json_content = '{"users": [{"id": 1, "name": "Alice"}]}'
        write_file(json_file, json_content)
        print(f"\n  Wrote JSON file: {json_file}")

        json_data = decode_file(json_file)
        print(f"  Decoded JSON data: {json_data}")

    print()


def demonstrate_path_resolution() -> None:
    """Demonstrate path resolution utilities."""
    print("=== Path Resolution ===\n")

    # Resolve paths relative to a base
    base_path = Path.cwd()
    relative_paths = ["src/main.py", "../parent/file.txt", "./current/file.txt"]

    print(f"  Base path: {base_path}")
    for rel in relative_paths:
        resolved = resolve_local_path(rel, tld=base_path)
        print(f"  resolve_local_path({rel!r}) -> {resolved}")

    print()


if __name__ == "__main__":
    demonstrate_filepath_type()
    demonstrate_url_detection()
    demonstrate_file_operations()
    demonstrate_path_resolution()
