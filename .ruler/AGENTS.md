# Extended Data Library - AI Agent Instructions

This is the central source of truth for AI agent instructions in this repository.
Rules defined here are distributed to all supported AI coding assistants via Ruler.

## Project Overview

This is a **uv workspace monorepo** (extended-data-library) containing multiple packages for data processing, logging, configuration, and vendor integrations.

### Packages

| Path | Package | Description |
|------|---------|-------------|
| `packages/extended-data-types` | extended-data-types | Python utility library (core) -- serialization, file system, data structures, strings, types |
| `packages/lifecyclelogging` | lifecyclelogging | Structured logging |
| `packages/directed-inputs-class` | directed-inputs-class | Input processing |
| `packages/vendor-connectors` | vendor-connectors | Vendor API connectors (AWS, Google, GitHub, Slack, etc.) |
| `packages/secretssync` | secretssync | Go CLI for secret syncing |
| `docs/` | -- | Astro/Starlight documentation site |

### Key Design Principles

- **Type safety**: Full type annotations and mypy compliance
- **Reliability**: Comprehensive test coverage with automated CI/CD
- **Ergonomics**: Clean, intuitive APIs
- **Platform awareness**: Handles cross-platform differences gracefully
- **Production ready**: No shortcuts, placeholders, or experimental features

## Technology Stack

- **Package manager**: `uv` (workspace mode, fast, Rust-based)
- **Build backend**: `hatchling`
- **Configuration**: `pyproject.toml` (root + per-package)
- **Python versions**: 3.10+
- **Go**: 1.25+ (secretssync only)
- **Docs**: Astro + Starlight
- **Linting & formatting**: `ruff`
- **Type checking**: `mypy` (strict mode)
- **Testing**: `pytest` (Python), `go test` (Go), `vitest` + `playwright` (docs)
- **CI/CD**: GitHub Actions
- **Releases**: `release-please` (NOT semantic-release)
- **PyPI publishing**: OIDC trusted publishers
