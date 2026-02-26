"""MCP Server for Extended Data Types.

Provides natural language API documentation and usage guidance for all
extended-data-types utilities via the Model Context Protocol.
"""

from __future__ import annotations

import inspect

from typing import Any

from mcp.server.fastmcp import FastMCP


mcp = FastMCP(
    "extended-data-types",
    instructions=(
        "This server provides documentation and discovery for the extended-data-types "
        "Python utility library. Use resolve-function-id to search for functions by name "
        "or description, get-function-docs for detailed documentation, and "
        "list-all-functions to browse all 90+ functions by category."
    ),
)

# ---------------------------------------------------------------------------
# Function categories
# ---------------------------------------------------------------------------

CATEGORIES: dict[str, list[str]] = {
    "Serialization": [
        "encode_yaml",
        "decode_yaml",
        "is_yaml_data",
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
    "Matcher Utilities": [
        "is_non_empty_match",
        "is_partial_match",
    ],
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
    "Data Types": [
        "FilePath",
        "SortedDefaultDict",
    ],
    "Ecosystem": [
        "DevelopmentIntegration",
        "EcosystemPackageDiscovery",
        "EcosystemStatusMonitor",
        "ReleaseCoordinator",
    ],
}


def _get_category(name: str) -> str:
    """Return the category a function belongs to."""
    for category, funcs in CATEGORIES.items():
        if name in funcs:
            return category
    return "Other"


def _get_library_functions() -> dict[str, Any]:
    """Load all public symbols from extended_data_types."""
    import extended_data_types  # deferred to avoid circular import

    functions: dict[str, Any] = {}
    for name in extended_data_types.__all__:
        attr = getattr(extended_data_types, name, None)
        if attr is None or inspect.ismodule(attr):
            continue
        functions[name] = attr
    return functions


def _get_signature(obj: Any) -> str:
    """Safely extract a signature string."""
    try:
        return str(inspect.signature(obj))
    except (ValueError, TypeError):
        return "(…)"


def _format_function_entry(name: str, obj: Any) -> str:
    """Format a single function for display."""
    sig = _get_signature(obj)
    doc_line = (getattr(obj, "__doc__", "") or "").split("\n")[0].strip()
    category = _get_category(name)
    kind = "class" if inspect.isclass(obj) else "function"
    return f"- **{name}**{sig}  [{kind} · {category}]\n  {doc_line}"


# ---------------------------------------------------------------------------
# MCP Tools
# ---------------------------------------------------------------------------


@mcp.tool()
def resolve_function_id(query: str) -> str:
    """Search for extended-data-types functions by name or description.

    Returns matching functions with their signature, category, and a brief
    description.  Use this when you know part of a function name or want to
    find functions that handle a particular task (e.g. "yaml", "merge", "snake").
    """
    query_lower = query.lower()
    functions = _get_library_functions()
    matches: list[str] = []

    for name, obj in functions.items():
        doc = (getattr(obj, "__doc__", "") or "").lower()
        if query_lower in name.lower() or query_lower in doc:
            matches.append(_format_function_entry(name, obj))

    if not matches:
        return f"No functions matching '{query}'."
    return f"## Functions matching '{query}' ({len(matches)} results)\n\n" + "\n".join(
        matches
    )


@mcp.tool()
def get_function_docs(function_name: str) -> str:
    """Get full documentation for an extended-data-types function.

    Returns the complete signature, docstring, category, and list of
    related functions in the same category.
    """
    functions = _get_library_functions()

    if function_name not in functions:
        available = ", ".join(sorted(functions.keys()))
        return f"Function '{function_name}' not found.\n\nAvailable: {available}"

    obj = functions[function_name]
    sig = _get_signature(obj)
    doc = getattr(obj, "__doc__", "") or "No documentation available."
    category = _get_category(function_name)
    module = getattr(obj, "__module__", "unknown")

    # Related functions in the same category
    related = [
        n
        for n in CATEGORIES.get(category, [])
        if n != function_name and n in functions
    ]

    lines = [
        f"# {function_name}{sig}",
        "",
        f"**Module:** `{module}`  ",
        f"**Category:** {category}",
        "",
        doc.strip(),
    ]

    if related:
        lines += ["", "## Related functions", ""]
        lines += [f"- {r}" for r in related]

    return "\n".join(lines)


@mcp.tool()
def list_all_functions(category: str | None = None) -> str:
    """List all functions in the extended-data-types library by category.

    Optionally filter by category name.  Categories include: Serialization,
    File Operations, Git Integration, String Transformations, String Utilities,
    Map Operations, List Operations, State Utilities, Type Utilities,
    Matcher Utilities, Stack Utilities, Export/Import, Data Types, Ecosystem.
    """
    functions = _get_library_functions()
    lines: list[str] = []

    for cat, func_names in CATEGORIES.items():
        if category and category.lower() != cat.lower():
            continue
        present = [f for f in func_names if f in functions]
        if not present:
            continue
        lines.append(f"## {cat} ({len(present)})")
        lines.append("")
        for name in present:
            obj = functions[name]
            sig = _get_signature(obj)
            doc_line = (getattr(obj, "__doc__", "") or "").split("\n")[0].strip()
            lines.append(f"- **{name}**{sig} — {doc_line}")
        lines.append("")

    total = sum(
        1 for cat_funcs in CATEGORIES.values() for f in cat_funcs if f in functions
    )
    header = f"# extended-data-types API ({total} functions)\n\n"
    if category:
        header = f"# extended-data-types — {category}\n\n"

    return header + "\n".join(lines)


# ---------------------------------------------------------------------------
# Entry point
# ---------------------------------------------------------------------------


def main() -> None:
    """Run the MCP server over stdio."""
    mcp.run()
