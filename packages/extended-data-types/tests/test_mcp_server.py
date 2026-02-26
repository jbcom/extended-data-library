"""Tests for the MCP server."""

from __future__ import annotations

import pytest

import extended_data_types

from extended_data_types.mcp_server.server import (
    CATEGORIES,
    _get_category,
    _get_library_functions,
    _get_signature,
    get_function_docs,
    list_all_functions,
    mcp,
    resolve_function_id,
)


# ---------------------------------------------------------------------------
# Unit tests for helper functions
# ---------------------------------------------------------------------------


class TestGetLibraryFunctions:
    """Tests for _get_library_functions."""

    def test_loads_all_callable_exports(self) -> None:
        funcs = _get_library_functions()
        for name in extended_data_types.__all__:
            attr = getattr(extended_data_types, name)
            if callable(attr):
                assert name in funcs, f"{name} missing from loaded functions"

    def test_excludes_none_and_modules(self) -> None:
        funcs = _get_library_functions()
        assert all(v is not None for v in funcs.values())

    def test_returns_dict(self) -> None:
        assert isinstance(_get_library_functions(), dict)


class TestGetCategory:
    """Tests for _get_category."""

    @pytest.mark.parametrize(
        "name,expected",
        [
            ("encode_yaml", "Serialization"),
            ("read_file", "File Operations"),
            ("to_snake_case", "String Transformations"),
            ("deep_merge", "Map Operations"),
            ("is_nothing", "State Utilities"),
            ("FilePath", "Data Types"),
            ("DevelopmentIntegration", "Ecosystem"),
        ],
    )
    def test_known_categories(self, name: str, expected: str) -> None:
        assert _get_category(name) == expected

    def test_unknown_returns_other(self) -> None:
        assert _get_category("nonexistent_function") == "Other"


class TestGetSignature:
    """Tests for _get_signature."""

    def test_function_signature(self) -> None:
        sig = _get_signature(extended_data_types.encode_yaml)
        assert "raw_data" in sig

    def test_class_without_signature(self) -> None:
        sig = _get_signature(extended_data_types.FilePath)
        assert isinstance(sig, str)


class TestCategoriesCoverage:
    """Tests for category completeness."""

    def test_all_categorized_names_exist_in_library(self) -> None:
        funcs = _get_library_functions()
        for cat, names in CATEGORIES.items():
            for name in names:
                assert name in funcs, f"{name} in category '{cat}' not in library"

    def test_no_uncategorized_functions(self) -> None:
        funcs = _get_library_functions()
        all_categorized = {n for names in CATEGORIES.values() for n in names}
        # mcp_server_main is intentionally excluded from categories
        skip = {"mcp_server_main"}
        uncategorized = {n for n in funcs if n not in all_categorized} - skip
        assert not uncategorized, f"Uncategorized functions: {uncategorized}"


# ---------------------------------------------------------------------------
# Integration tests for MCP tools (call functions directly)
# ---------------------------------------------------------------------------


class TestResolveFunctionId:
    """Tests for the resolve_function_id tool."""

    def test_finds_yaml_functions(self) -> None:
        text = resolve_function_id("yaml")
        assert "encode_yaml" in text
        assert "decode_yaml" in text

    def test_finds_by_description(self) -> None:
        text = resolve_function_id("merge")
        assert "deep_merge" in text

    def test_no_matches(self) -> None:
        text = resolve_function_id("zzz_nonexistent_zzz")
        assert "No functions matching" in text

    def test_result_contains_category(self) -> None:
        text = resolve_function_id("encode_yaml")
        assert "Serialization" in text

    def test_result_count(self) -> None:
        text = resolve_function_id("yaml")
        assert "results" in text


class TestGetFunctionDocs:
    """Tests for the get_function_docs tool."""

    def test_returns_full_docs(self) -> None:
        text = get_function_docs("encode_yaml")
        assert "encode_yaml" in text
        assert "Category:" in text
        assert "Module:" in text

    def test_includes_related_functions(self) -> None:
        text = get_function_docs("encode_yaml")
        assert "Related functions" in text
        assert "decode_yaml" in text

    def test_unknown_function(self) -> None:
        text = get_function_docs("nonexistent")
        assert "not found" in text

    def test_includes_docstring(self) -> None:
        text = get_function_docs("deep_merge")
        assert "deep_merge" in text


class TestListAllFunctions:
    """Tests for the list_all_functions tool."""

    def test_lists_all_categories(self) -> None:
        text = list_all_functions()
        assert "Serialization" in text
        assert "File Operations" in text
        assert "Map Operations" in text

    def test_filter_by_category(self) -> None:
        text = list_all_functions(category="Serialization")
        assert "Serialization" in text
        assert "Map Operations" not in text

    def test_shows_function_count(self) -> None:
        text = list_all_functions()
        assert "functions" in text.lower()

    def test_all_functions_present(self) -> None:
        text = list_all_functions()
        assert "encode_yaml" in text
        assert "deep_merge" in text
        assert "FilePath" in text


class TestMCPServerRegistration:
    """Tests for MCP server tool registration."""

    def test_server_name(self) -> None:
        assert mcp.name == "extended-data-types"

    def test_has_instructions(self) -> None:
        assert mcp.instructions is not None
        assert "extended-data-types" in mcp.instructions
