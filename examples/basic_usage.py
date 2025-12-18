#!/usr/bin/env python3
"""Basic usage examples for extended-data-types library.

This module demonstrates common operations with strings, lists, maps,
and state utilities provided by the library.
"""

from __future__ import annotations

from extended_data_types import (
    # State utilities
    all_non_empty,
    any_non_empty,
    # Map utilities
    deep_merge,
    # List utilities
    filter_list,
    filter_map,
    first_non_empty,
    flatten_list,
    flatten_map,
    is_nothing,
    # String utilities
    removeprefix,
    removesuffix,
    sanitize_key,
    truncate,
)


def demonstrate_state_utilities() -> None:
    """Demonstrate state checking utilities."""
    print("=== State Utilities ===\n")

    # Check if values are "nothing" (None, empty string, empty list, etc.)
    print(f"is_nothing(None): {is_nothing(None)}")
    print(f"is_nothing(''): {is_nothing('')}")
    print(f"is_nothing([]): {is_nothing([])}")
    print(f"is_nothing('hello'): {is_nothing('hello')}")

    # Check if all values are non-empty
    values = ["hello", "world", "!"]
    print(f"\nall_non_empty({values}): {all_non_empty(*values)}")

    values_with_empty = ["hello", "", "world"]
    print(f"all_non_empty({values_with_empty}): {all_non_empty(*values_with_empty)}")

    # Check if any value is non-empty
    mostly_empty = [None, "", "found"]
    print(f"\nany_non_empty({mostly_empty}): {any_non_empty(*mostly_empty)}")

    # Get first non-empty value
    print(f"first_non_empty(None, '', 'first', 'second'): {first_non_empty(None, '', 'first', 'second')}")


def demonstrate_list_utilities() -> None:
    """Demonstrate list manipulation utilities."""
    print("\n=== List Utilities ===\n")

    # Flatten nested lists
    nested = [[1, 2], [3, [4, 5]], 6]
    print(f"flatten_list({nested}): {flatten_list(nested)}")

    # Filter list items
    items = ["apple", "banana", "apricot", "cherry"]
    filtered = filter_list(items, lambda x: x.startswith("a"))
    print(f"\nfilter_list (starts with 'a'): {filtered}")


def demonstrate_map_utilities() -> None:
    """Demonstrate dictionary/map manipulation utilities."""
    print("\n=== Map Utilities ===\n")

    # Deep merge dictionaries
    dict1 = {"a": 1, "b": {"c": 2, "d": 3}}
    dict2 = {"b": {"d": 4, "e": 5}, "f": 6}
    merged = deep_merge(dict1, dict2)
    print(f"deep_merge({dict1}, {dict2}):")
    print(f"  Result: {merged}")

    # Flatten nested dictionary
    nested_dict = {"a": {"b": {"c": 1}}, "d": 2}
    flat = flatten_map(nested_dict)
    print(f"\nflatten_map({nested_dict}):")
    print(f"  Result: {flat}")

    # Filter dictionary
    data = {"name": "John", "age": 30, "city": "NYC", "active": True}
    filtered = filter_map(data, lambda _k, v: isinstance(v, str))
    print(f"\nfilter_map (string values only): {filtered}")


def demonstrate_string_utilities() -> None:
    """Demonstrate string manipulation utilities."""
    print("\n=== String Utilities ===\n")

    # Remove prefix/suffix (backport for older Python versions)
    text = "prefix_content_suffix"
    print(f"removeprefix('{text}', 'prefix_'): {removeprefix(text, 'prefix_')}")
    print(f"removesuffix('{text}', '_suffix'): {removesuffix(text, '_suffix')}")

    # Truncate strings
    long_text = "This is a very long string that needs to be truncated"
    print(f"\ntruncate('{long_text}', 20): '{truncate(long_text, 20)}'")

    # Sanitize keys for use in data structures
    messy_key = "User Name (Primary)"
    print(f"\nsanitize_key('{messy_key}'): '{sanitize_key(messy_key)}'")


if __name__ == "__main__":
    demonstrate_state_utilities()
    demonstrate_list_utilities()
    demonstrate_map_utilities()
    demonstrate_string_utilities()
