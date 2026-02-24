# Contributing to Extended Data Library

Thank you for your interest in contributing! This monorepo contains multiple packages -- please read through these guidelines to get started.

## Prerequisites

- Python 3.10+
- [uv](https://docs.astral.sh/uv/) (fast Python package manager)
- [just](https://github.com/casey/just) (optional, for task running)
- Go 1.25+ (only if working on secretssync)

## Development Setup

```bash
# Clone the repository
git clone https://github.com/jbcom/extended-data-library.git
cd extended-data-library

# Install all dependencies (uv handles workspace resolution)
uv sync
```

## Running Tests

```bash
# All Python packages via tox
tox -e edt,logging,inputs,connectors

# Single package
tox -e edt            # extended-data-types
tox -e logging        # lifecyclelogging
tox -e inputs         # directed-inputs-class
tox -e connectors     # vendor-connectors

# Using just
just test

# Go (secretssync)
cd packages/secretssync && go test ./...
```

## Linting and Formatting

```bash
# Via tox
tox -e lint

# Directly
uvx ruff check packages/
uvx ruff format packages/

# Using just
just lint
```

## Type Checking

```bash
uvx mypy packages/extended-data-types/src/
uvx mypy packages/lifecyclelogging/src/
```

## Commit Conventions

All commits **must** follow [Conventional Commits](https://www.conventionalcommits.org/):

```
<type>(<scope>): <description>
```

### Types

| Type | Description | Release |
|------|-------------|---------|
| `feat` | New feature | Minor bump |
| `fix` | Bug fix | Patch bump |
| `docs` | Documentation only | No |
| `refactor` | Code restructuring | No |
| `test` | Adding/fixing tests | No |
| `chore` | Maintenance tasks | No |
| `feat!` | Breaking change | Major bump |

### Scopes

Use the package scope when the change is package-specific:

| Scope | Package |
|-------|---------|
| `edt` | extended-data-types |
| `logging` | lifecyclelogging |
| `inputs` | directed-inputs-class |
| `connectors` | vendor-connectors |
| `secretssync` | secretssync |

### Examples

```bash
feat(edt): add TOML round-trip support
fix(logging): handle empty context markers
docs: update installation instructions
test(inputs): add coverage for stdin JSON parsing
```

## Pull Request Process

1. Create a feature branch from `main` (`feat/`, `fix/`, `docs/`, etc.)
2. Make your changes with tests
3. Ensure CI passes locally (`tox -e lint` and `tox -e <package>`)
4. Submit a Pull Request with a clear title using conventional commit format
5. Address all review feedback

## Project Structure

```
packages/
  extended-data-types/   Foundation utilities (Python)
  lifecyclelogging/      Structured logging (Python)
  directed-inputs-class/ Input handling (Python)
  vendor-connectors/     Cloud connectors (Python)
  secretssync/           Secret sync pipeline (Go)
```

Each Python package lives in `packages/<name>/` with its own `pyproject.toml`, `src/`, and `tests/` directories. The root `pyproject.toml` defines the uv workspace.

## License

By contributing, you agree that your contributions will be licensed under the MIT License.
