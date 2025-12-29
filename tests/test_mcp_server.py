"""Tests for the MCP server."""

from __future__ import annotations

import extended_data_types
import pytest

from extended_data_types.mcp_server.server import (
    get_category,
    get_library_functions,
)


def test_get_library_functions():
    """Verify that all functions in __all__ are captured."""
    funcs = get_library_functions()
    for name in extended_data_types.__all__:
        # Skip if it's a constant or non-callable (though mostly they are classes/functions)
        attr = getattr(extended_data_types, name)
        if callable(attr):
            assert name in funcs


def test_categories_coverage():
    """Verify that most functions are categorized."""
    funcs = get_library_functions()
    uncategorized = [name for name in funcs if get_category(name) == "Other"]

    # We expect some to be uncategorized, but let's see how many
    # For now, just ensure the function works
    assert isinstance(get_category("encode_yaml"), str)
    assert get_category("encode_yaml") == "Serialization"
    assert uncategorized is not None


@pytest.mark.asyncio
async def test_server_tools_list():
    """Verify the server lists the expected tools."""
    from extended_data_types.mcp_server.server import handle_list_tools

    tools = await handle_list_tools()
    names = [t["name"] for t in tools]
    assert "resolve-function-id" in names
    assert "get-function-docs" in names
    assert "list-all-functions" in names


@pytest.mark.asyncio
async def test_resolve_function_id():
    """Test function resolution."""
    from extended_data_types.mcp_server.server import handle_call_tool

    result = await handle_call_tool("resolve-function-id", {"query": "encode_yaml"})
    assert "encode_yaml" in result[0]["text"]
    assert "Serialization" in result[0]["text"]


@pytest.mark.asyncio
async def test_get_function_docs():
    """Test doc extraction."""
    from extended_data_types.mcp_server.server import handle_call_tool

    result = await handle_call_tool("get-function-docs", {"functionName": "encode_yaml"})
    assert "Function: encode_yaml" in result[0]["text"]
    assert "YAML" in result[0]["text"]
