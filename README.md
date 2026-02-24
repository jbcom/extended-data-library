# Extended Data Library

A collection of high-performance Python libraries and tools for data processing, configuration management, logging, and cloud integrations.

[![CI Status](https://github.com/jbcom/extended-data-library/actions/workflows/ci.yml/badge.svg)](https://github.com/jbcom/extended-data-library/actions/workflows/ci.yml)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

## Packages

| Package | Version | Description |
|---------|---------|-------------|
| [extended-data-types](packages/extended-data-types/) | [![PyPI](https://img.shields.io/pypi/v/extended-data-types.svg)](https://pypi.org/project/extended-data-types/) | Typed utilities for YAML, JSON, TOML, HCL, Base64, file paths, strings, lists, and maps |
| [lifecyclelogging](packages/lifecyclelogging/) | [![PyPI](https://img.shields.io/pypi/v/lifecyclelogging.svg)](https://pypi.org/project/lifecyclelogging/) | Lifecycle-aware logging with rich output, verbosity control, and message storage |
| [directed-inputs-class](packages/directed-inputs-class/) | [![PyPI](https://img.shields.io/pypi/v/directed-inputs-class.svg)](https://pypi.org/project/directed-inputs-class/) | Transparent input handling from environment variables, stdin, and config files |
| [vendor-connectors](packages/vendor-connectors/) | [![PyPI](https://img.shields.io/pypi/v/vendor-connectors.svg)](https://pypi.org/project/vendor-connectors/) | Universal cloud and service connectors (AWS, GitHub, Slack, Vault, Anthropic, Cursor, Meshy) |
| [secretssync](packages/secretssync/) | [![GitHub Release](https://img.shields.io/github/v/release/jbcom/extended-data-library.svg)](https://github.com/jbcom/extended-data-library/releases) | Enterprise-grade secret synchronization pipeline (Go) |

## Quick Start

```bash
# Install any package directly
pip install extended-data-types
pip install lifecyclelogging
pip install directed-inputs-class
pip install vendor-connectors
```

## Monorepo Structure

```
extended-data-library/
  packages/
    extended-data-types/   Python foundation utilities
    lifecyclelogging/      Structured logging library
    directed-inputs-class/ Configuration and input handling
    vendor-connectors/     Cloud and service connectors
    secretssync/           Secret sync pipeline (Go)
  docs/                    Documentation site (Astro + Sphinx)
  tox.ini                  Test orchestration
  justfile                 Developer task runner
```

## Development

### Prerequisites

- Python 3.10+
- [uv](https://docs.astral.sh/uv/) (package manager)
- Go 1.25+ (only for secretssync)

### Setup

```bash
git clone https://github.com/jbcom/extended-data-library.git
cd extended-data-library
uv sync
```

### Running Tests

```bash
# All Python packages
tox -e edt,logging,inputs,connectors

# Single package
tox -e edt

# Using just
just test
```

### Linting and Formatting

```bash
tox -e lint

# Or directly
uvx ruff check packages/
uvx ruff format packages/
```

### Commit Conventions

This project uses [Conventional Commits](https://www.conventionalcommits.org/) with scoped types:

```
feat(edt): add new TOML parser        # minor bump for extended-data-types
fix(logging): handle empty messages    # patch bump for lifecyclelogging
feat!: breaking API change             # major bump
```

## Documentation

Full documentation is available at [extendeddata.dev](https://extendeddata.dev).

## License

[MIT](LICENSE) -- Copyright (c) 2025 Extended Data Library
