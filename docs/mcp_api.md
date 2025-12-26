# MCP Server API Reference

The extended-data-types MCP server provides the following tools for AI agents to discover and use the library's functions.

## `resolve-function-id`

Resolves a function name or description to the exact extended-data-types function.

### Input

- `query` (string): The function name or a description of the function to search for.

### Output

A list of matching functions, each with the following information:

- `name` (string): The name of the function.
- `module` (string): The module where the function is located.
- `category` (string): The category of the function.
- `description` (string): A brief description of the function.
- `parameter_count` (integer): The number of parameters the function accepts.

## `get-function-docs`

Fetches comprehensive documentation for a specific function.

### Input

- `functionName` (string): The exact name of the function.
- `includeExamples` (boolean, optional): Whether to include usage examples from the test suite. Defaults to `false`.

### Output

- `name` (string): The name of the function.
- `signature` (string): The function's signature with full type annotations.
- `docstring` (string): The complete docstring of the function.
- `category` (string): The category of the function.
- `related_functions` (list of strings): A list of other functions in the same category.
- `examples` (list of strings): A list of usage examples extracted from the test suite.
