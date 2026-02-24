#!/usr/bin/env python3
"""Basic usage examples for extended-data-types library.

This module demonstrates common operations with strings, lists, maps,
and state utilities provided by the library.
"""

from __future__ import annotations

from extended_data_types import (
    # State utilities
    deep_merge,
    # List utilities
    filter_list,
    filter_map,
    flatten_map,
)


def demonstrate_state_utilities() -> None:
    """Demonstrate state checking utilities."""
    # Check if values are "nothing" (None, empty string, empty list, etc.)

    # Check if all values are non-empty

    # Check if any value is non-empty

    # Get first non-empty value


def demonstrate_list_utilities() -> None:
    """Demonstrate list manipulation utilities."""
    # Flatten nested lists

    # Filter list items
    items = ["apple", "banana", "apricot", "cherry"]
    filter_list(items, lambda x: x.startswith("a"))


def demonstrate_map_utilities() -> None:
    """Demonstrate dictionary/map manipulation utilities."""
    # Deep merge dictionaries
    dict1 = {"a": 1, "b": {"c": 2, "d": 3}}
    dict2 = {"b": {"d": 4, "e": 5}, "f": 6}
    deep_merge(dict1, dict2)

    # Flatten nested dictionary
    nested_dict = {"a": {"b": {"c": 1}}, "d": 2}
    flatten_map(nested_dict)

    # Filter dictionary
    data = {"name": "John", "age": 30, "city": "NYC", "active": True}
    filter_map(data, lambda _k, v: isinstance(v, str))


def demonstrate_string_utilities() -> None:
    """Demonstrate string manipulation utilities."""
    # Remove prefix/suffix (backport for older Python versions)

    # Truncate strings

    # Sanitize keys for use in data structures


if __name__ == "__main__":
    demonstrate_state_utilities()
    demonstrate_list_utilities()
    demonstrate_map_utilities()
    demonstrate_string_utilities()
