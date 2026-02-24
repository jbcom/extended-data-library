# Development Guidelines

## Core Philosophy

Write clean, tested, production-ready code. No shortcuts, no placeholders.

## Development Flow

1. **Read the requirements** from specs or issues
2. **Write tests first** (TDD approach)
3. **Implement the feature** completely
4. **Run linting**: `uvx ruff check packages/ tests/`
5. **Run tests**: `uv run pytest packages/<name>/tests/ -v`
6. **Commit** with conventional commits

## Testing Commands

```bash
# Install dependencies
uv sync --extra tests

# Run tests for a specific package
uv run pytest packages/<name>/tests/ -v

# Run with coverage for a specific package
uv run pytest packages/<name>/tests/ --cov=packages/<name>/src/ --cov-report=term-missing

# Linting
uvx ruff check packages/ tests/
uvx ruff format packages/

# Type checking for a specific package
uvx mypy packages/<name>/src/
```

## Commit Messages

Use conventional commits with package scopes matching release-please:
- `feat(scope): description` - minor bump
- `fix(scope): description` - patch bump
- `feat!: breaking change` - major bump

### Package Scopes

| Scope | Package |
|-------|---------|
| `edt` | extended-data-types |
| `logging` | lifecyclelogging |
| `inputs` | directed-inputs-class |
| `connectors` | vendor-connectors |
| `secretssync` | secretssync |

## Quality Standards

- All tests passing
- No linter errors
- Complete type annotations
- Proper error handling
- No TODOs or placeholders
- No shortcuts
