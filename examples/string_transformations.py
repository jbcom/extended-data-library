#!/usr/bin/env python3
"""String transformation examples for extended-data-types library.

This module demonstrates case conversion, humanization, pluralization,
and other string manipulation utilities provided by the library.
"""

from __future__ import annotations

from extended_data_types import (
    humanize,
    ordinalize,
    pluralize,
    singularize,
    titleize,
    to_camel_case,
    to_kebab_case,
    to_pascal_case,
    to_snake_case,
)


def demonstrate_case_conversion() -> None:
    """Demonstrate case conversion utilities."""
    print("=== Case Conversion ===\n")

    original = "user_account_settings"

    print(f"Original: '{original}'")
    print(f"  to_camel_case: '{to_camel_case(original)}'")
    print(f"  to_pascal_case: '{to_pascal_case(original)}'")
    print(f"  to_kebab_case: '{to_kebab_case(original)}'")

    # From camelCase
    camel = "userAccountSettings"
    print(f"\nOriginal: '{camel}'")
    print(f"  to_snake_case: '{to_snake_case(camel)}'")
    print(f"  to_kebab_case: '{to_kebab_case(camel)}'")


def demonstrate_humanization() -> None:
    """Demonstrate string humanization."""
    print("\n=== Humanization ===\n")

    examples = [
        "user_id",
        "createdAt",
        "HTTPResponse",
        "employee_salary_amount",
    ]

    for example in examples:
        print(f"humanize('{example}'): '{humanize(example)}'")

    print("\n")
    for example in examples:
        print(f"titleize('{example}'): '{titleize(example)}'")


def demonstrate_pluralization() -> None:
    """Demonstrate pluralization and singularization."""
    print("\n=== Pluralization ===\n")

    words = ["cat", "child", "person", "mouse", "analysis", "octopus"]

    print("Pluralize:")
    for word in words:
        print(f"  '{word}' -> '{pluralize(word)}'")

    print("\nSingularize:")
    plural_words = ["cats", "children", "people", "mice", "analyses", "octopi"]
    for word in plural_words:
        print(f"  '{word}' -> '{singularize(word)}'")


def demonstrate_ordinalization() -> None:
    """Demonstrate number ordinalization."""
    print("\n=== Ordinalization ===\n")

    numbers = [1, 2, 3, 4, 11, 12, 13, 21, 22, 23, 100, 101, 102, 103]

    for num in numbers:
        print(f"ordinalize({num}): '{ordinalize(num)}'")


if __name__ == "__main__":
    demonstrate_case_conversion()
    demonstrate_humanization()
    demonstrate_pluralization()
    demonstrate_ordinalization()
