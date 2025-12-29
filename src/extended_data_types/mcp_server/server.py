"""MCP Server for Extended Data Types."""

from __future__ import annotations

import asyncio
import inspect

from typing import Any

from mcp.server import NotificationOptions, Server
from mcp.server.models import InitializationOptions
from mcp.server.stdio import stdio_server

import extended_data_types


# Initialize MCP server
server = Server("extended-data-types")


def get_library_functions() -> dict[str, Any]:
    """Helper to get all functions from the library."""
    functions = {}
    for name in extended_data_types.__all__:
        attr = getattr(extended_data_types, name)
        # Include if it's a function, class, or TypeAlias (captured as Any for docs)
        if (
            inspect.isfunction(attr)
            or inspect.isclass(attr)
            or hasattr(attr, "__origin__")
            or hasattr(attr, "__metadata__")
        ):
            functions[name] = attr
        elif not inspect.ismodule(attr):
            # Include other types too, as long as they aren't modules
            functions[name] = attr
    return functions


# Categories from Issue #3
CATEGORIES = {
    "Serialization": [
        "encode_yaml",
        "decode_yaml",
        "encode_json",
        "decode_json",
        "encode_toml",
        "decode_toml",
        "decode_hcl2",
        "base64_encode",
        "base64_decode",
    ],
    "File Operations": [
        "read_file",
        "write_file",
        "decode_file",
        "delete_file",
        "resolve_local_path",
        "get_encoding_for_file_path",
        "match_file_extensions",
        "file_path_depth",
        "file_path_rel_to_root",
        "is_url",
    ],
    "Git Integration": [
        "get_parent_repository",
        "get_repository_name",
        "get_tld",
        "clone_repository_to_temp",
    ],
    "String Transformations": [
        "to_snake_case",
        "to_camel_case",
        "to_kebab_case",
        "to_pascal_case",
        "humanize",
        "pluralize",
        "singularize",
        "titleize",
        "ordinalize",
    ],
    "String Utilities": [
        "bytestostr",
        "lower_first_char",
        "upper_first_char",
        "removeprefix",
        "removesuffix",
        "sanitize_key",
        "titleize_name",
        "truncate",
    ],
    "Map Operations": [
        "deep_merge",
        "flatten_map",
        "filter_map",
        "deduplicate_map",
        "unhump_map",
        "zipmap",
        "all_values_from_map",
        "first_non_empty_value_from_map",
        "get_default_dict",
        "create_merger",
    ],
    "List Operations": [
        "filter_list",
        "flatten_list",
        "split_list_by_type",
        "split_dict_by_type",
    ],
    "State Utilities": [
        "is_nothing",
        "are_nothing",
        "any_non_empty",
        "all_non_empty",
        "all_non_empty_in_dict",
        "all_non_empty_in_list",
        "first_non_empty",
        "yield_non_empty",
    ],
    "Type Utilities": [
        "typeof",
        "strtobool",
        "strtoint",
        "strtofloat",
        "strtodate",
        "strtodatetime",
        "strtotime",
        "strtopath",
        "convert_special_type",
        "convert_special_types",
        "reconstruct_special_type",
        "reconstruct_special_types",
        "make_hashable",
        "get_default_value_for_type",
        "get_primitive_type_for_instance_type",
    ],
    "Matcher Utilities": ["is_non_empty_match", "is_partial_match"],
    "Stack Utilities": [
        "get_caller",
        "get_available_methods",
        "filter_methods",
        "get_inputs_from_docstring",
        "get_unique_signature",
        "update_docstring",
    ],
    "Export/Import": [
        "make_raw_data_export_safe",
        "wrap_raw_data_for_export",
        "unwrap_raw_data_from_import",
    ],
    "Data Types": ["FilePath", "SortedDefaultDict"],
}


def get_category(function_name: str) -> str:
    """Organize functions into categories for discovery."""
    for category, funcs in CATEGORIES.items():
        if function_name in funcs:
            return category
    return "Other"


@server.list_tools()
async def handle_list_tools() -> list[dict[str, Any]]:
    """List available tools."""
    return [
        {
            "name": "resolve-function-id",
            "description": "Resolves a function name or description to the exact extended-data-types function.",
            "inputSchema": {
                "type": "object",
                "properties": {
                    "query": {
                        "type": "string",
                        "description": "Function name or description to search for",
                    }
                },
                "required": ["query"],
            },
        },
        {
            "name": "get-function-docs",
            "description": "Fetches comprehensive documentation for a specific function.",
            "inputSchema": {
                "type": "object",
                "properties": {
                    "functionName": {
                        "type": "string",
                        "description": "Exact function name from __all__ exports",
                    },
                    "includeExamples": {
                        "type": "boolean",
                        "description": "Include usage examples from tests",
                    },
                },
                "required": ["functionName"],
            },
        },
        {
            "name": "list-all-functions",
            "description": "Lists all 90+ functions available in the library by category.",
            "inputSchema": {
                "type": "object",
                "properties": {
                    "category": {
                        "type": "string",
                        "description": "Filter by category (optional)",
                    }
                },
            },
        },
    ]


@server.call_tool()
async def handle_call_tool(name: str, arguments: dict[str, Any]) -> list[dict[str, Any]]:
    """Handle tool calls."""
    functions = get_library_functions()

    if name == "resolve-function-id":
        query = arguments.get("query", "").lower()
        results = []
        for func_name, func in functions.items():
            doc = (func.__doc__ or "").lower()
            if query in func_name.lower() or query in doc:
                results.append(
                    {
                        "name": func_name,
                        "module": getattr(func, "__module__", "unknown"),
                        "category": get_category(func_name),
                        "description": (func.__doc__ or "").split("\n")[0],
                        "parameters": len(inspect.signature(func).parameters)
                        if hasattr(func, "__signature__") or inspect.isfunction(func)
                        else 0,
                    }
                )
        return [{"type": "text", "text": str(results)}]

    elif name == "get-function-docs":
        func_name = arguments.get("functionName")
        if func_name not in functions:
            return [{"type": "text", "text": f"Error: Function '{func_name}' not found."}]

        func = functions[func_name]
        sig = str(inspect.signature(func))
        doc = func.__doc__ or "No documentation available."
        category = get_category(func_name)

        return [
            {
                "type": "text",
                "text": f"Function: {func_name}{sig}\nCategory: {category}\n\n{doc}",
            }
        ]

    elif name == "list-all-functions":
        filter_cat = arguments.get("category")
        output = []
        for cat, funcs in CATEGORIES.items():
            if filter_cat and filter_cat.lower() != cat.lower():
                continue
            output.append(f"## {cat}")
            output.extend(f"- {f}" for f in funcs if f in functions)
            output.append("")
        return [{"type": "text", "text": "\n".join(output)}]

    else:
        raise ValueError(f"Unknown tool: {name}")


async def main():
    """Main entry point."""
    async with stdio_server() as (read_stream, write_server):
        await server.run(
            read_stream,
            write_server,
            InitializationOptions(
                server_name="extended-data-types",
                server_version="1.0.0",
                capabilities=server.get_capabilities(
                    notification_options=NotificationOptions(),
                    experimental_capabilities={},
                ),
            ),
        )


if __name__ == "__main__":
    asyncio.run(main())
