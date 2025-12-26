import ast
import inspect
import json
import logging
import os
import re
import sys
from pathlib import Path

from mcp.server.fastmcp import FastMCP
import extended_data_types
from extended_data_types import __all__ as edt_all

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

FUNCTION_CATEGORIES = {
    "Serialization": ["encode_yaml", "decode_yaml", "encode_json", "decode_json", "encode_toml", "decode_toml", "decode_hcl2", "base64_encode", "base64_decode"],
    "File Operations": ["read_file", "write_file", "decode_file", "delete_file", "resolve_local_path", "get_encoding_for_file_path", "match_file_extensions", "file_path_depth", "file_path_rel_to_root", "is_url"],
    "Git Integration": ["get_parent_repository", "get_repository_name", "get_tld", "clone_repository_to_temp"],
    "String Transformations": ["to_snake_case", "to_camel_case", "to_kebab_case", "to_pascal_case", "humanize", "pluralize", "singularize", "titleize", "ordinalize"],
    "String Utilities": ["bytestostr", "lower_first_char", "upper_first_char", "removeprefix", "removesuffix", "sanitize_key", "titleize_name", "truncate"],
    "Map Operations": ["deep_merge", "flatten_map", "filter_map", "deduplicate_map", "unhump_map", "zipmap", "all_values_from_map", "first_non_empty_value_from_map", "get_default_dict", "create_merger"],
    "List Operations": ["filter_list", "flatten_list", "split_list_by_type", "split_dict_by_type"],
    "State Utilities": ["is_nothing", "are_nothing", "any_non_empty", "all_non_empty", "all_non_empty_in_dict", "all_non_empty_in_list", "first_non_empty", "yield_non_empty"],
    "Type Utilities": ["typeof", "strtobool", "strtoint", "strtofloat", "strtodate", "strtodatetime", "strtotime", "strtopath", "convert_special_type", "convert_special_types", "reconstruct_special_type", "reconstruct_special_types", "make_hashable", "get_default_value_for_type", "get_primitive_type_for_instance_type"],
    "Matcher Utilities": ["is_non_empty_match", "is_partial_match"],
    "Stack Utilities": ["get_caller", "get_available_methods", "filter_methods", "get_inputs_from_docstring", "get_unique_signature", "update_docstring"],
    "Export/Import": ["make_raw_data_export_safe", "wrap_raw_data_for_export", "unwrap_raw_data_from_import"],
    "Data Types": ["FilePath", "SortedDefaultDict"],
}

class ExtendedDataTypesMCP:
    """MCP Server for Extended Data Types."""

    def __init__(self):
        self._functions = self._discover_functions()
        self._test_files_path = Path(__file__).parent.parent.parent.parent / "tests"
        self.mcp = FastMCP("extended-data-types", json_response=True)
        self._register_tools()

    def _register_tools(self):
        self.mcp.tool("resolve-function-id")(self._handle_resolve_function_id)
        self.mcp.tool("get-function-docs")(self._handle_get_function_docs)

    def _discover_functions(self):
        """Discover all functions exposed by the library."""
        functions = {}
        for func_name in edt_all:
            func = getattr(extended_data_types, func_name, None)
            if not func or not callable(func):
                continue

            doc = inspect.getdoc(func) or ""
            description = doc.split("\n\n")[0]

            try:
                signature = inspect.signature(func)
                param_count = len(signature.parameters)
            except (ValueError, TypeError):
                signature = "N/A"
                param_count = 0

            category = "Unknown"
            for cat, funcs in FUNCTION_CATEGORIES.items():
                if func_name in funcs:
                    category = cat
                    break

            functions[func_name] = {
                "name": func_name,
                "module": getattr(func, "__module__", ""),
                "doc": doc,
                "description": description,
                "signature": str(signature),
                "parameter_count": param_count,
                "category": category,
            }
        return functions

    def _extract_examples_from_tests(self, function_name):
        """Extract usage examples from test cases using AST."""
        examples = []
        test_file = self._find_test_file_for_function(function_name)
        if not test_file:
            return examples

        try:
            with open(test_file) as f:
                content = f.read()
                tree = ast.parse(content)
                for node in ast.walk(tree):
                    if isinstance(node, ast.FunctionDef) and node.name == f"test_{function_name}":
                        for sub_node in node.body:
                            if isinstance(sub_node, ast.Assert):
                                examples.append(ast.unparse(sub_node).strip())
        except (FileNotFoundError, SyntaxError) as e:
            logging.error(f"Error parsing {test_file}: {e}")
        return examples

    def _find_test_file_for_function(self, function_name):
        """Find the test file that contains tests for the given function."""
        module_name = self._functions.get(function_name, {}).get("module", "").split(".")[-1]
        if not module_name:
            return None

        test_file_name = f"test_{module_name}.py"
        test_file_path = self._test_files_path / test_file_name
        return test_file_path if test_file_path.exists() else None

    def _handle_resolve_function_id(self, query: str):
        """Resolve a function name or description."""
        query = query.lower()
        matches = []
        for func_name, func_data in self._functions.items():
            if query in func_name.lower() or query in func_data["description"].lower():
                matches.append({
                    "name": func_data["name"],
                    "module": func_data["module"],
                    "category": func_data["category"],
                    "description": func_data["description"],
                    "parameter_count": func_data["parameter_count"],
                })
        return matches

    def _handle_get_function_docs(self, functionName: str, includeExamples: bool = False):
        """Get comprehensive documentation for a function."""
        func_data = self._functions.get(functionName)
        if not func_data:
            return {"error": f"Function '{functionName}' not found."}

        related_functions = [
            f
            for f in self._functions.values()
            if f["category"] == func_data["category"] and f["name"] != functionName
        ]

        examples = []
        if includeExamples:
            examples = self._extract_examples_from_tests(functionName)

        return {
            "name": func_data["name"],
            "signature": func_data["signature"],
            "docstring": func_data["doc"],
            "category": func_data["category"],
            "related_functions": [f["name"] for f in related_functions],
            "examples": examples,
        }

    def run(self, transport="stdio", host="127.0.0.1", port=8080):
        """Run the MCP server."""
        self.mcp.settings.host = host
        self.mcp.settings.port = port
        transport_name = "streamable-http" if transport == "http" else "stdio"
        self.mcp.run(transport=transport_name)
