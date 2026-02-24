# Monorepo Migration Design

## Overview

Migrate all extended-data-library Python packages and the Go secretssync binary into a single monorepo, orchestrated by Nx with uv workspaces for Python, and an Astro Starlight docs site fed by Sphinx-generated markdown.

## Target Structure

```
extended-data-types/                    # repo root
├── nx.json                             # Nx workspace config
├── package.json                        # Nx + plugins (root)
├── pyproject.toml                      # uv workspace root
├── uv.lock                             # single Python lockfile
├── tox.ini                             # root tox-uv (envs per package)
├── justfile                            # human-facing task runner
├── .npmrc                              # npm config
├── tsconfig.base.json                  # shared TS config (for docs)
│
├── packages/
│   ├── extended-data-types/            # Python: foundation library
│   │   ├── pyproject.toml
│   │   ├── src/extended_data_types/
│   │   └── tests/
│   │
│   ├── lifecyclelogging/               # Python: logging library
│   │   ├── pyproject.toml
│   │   ├── src/lifecyclelogging/
│   │   └── tests/
│   │
│   ├── directed-inputs-class/          # Python: input management
│   │   ├── pyproject.toml
│   │   ├── src/directed_inputs_class/
│   │   └── tests/
│   │
│   ├── vendor-connectors/              # Python: API connectors
│   │   ├── pyproject.toml
│   │   ├── src/vendor_connectors/
│   │   └── tests/
│   │
│   └── secretssync/                    # Go: vault-to-AWS sync
│       ├── go.mod
│       ├── go.sum
│       ├── cmd/
│       ├── pkg/
│       └── api/
│
├── docs/                               # Astro Starlight docs site
│   ├── package.json
│   ├── astro.config.mjs
│   ├── sphinx/                         # Sphinx configuration
│   │   └── conf.py
│   └── src/
│       ├── content/
│       │   └── docs/                   # Hand-written + generated
│       │       ├── index.mdx
│       │       ├── extended-data-types/
│       │       ├── lifecyclelogging/
│       │       ├── directed-inputs-class/
│       │       ├── vendor-connectors/
│       │       ├── secretssync/
│       │       └── api/                # Sphinx-generated markdown
│       └── assets/
│
└── tools/                              # Build scripts
    └── sphinx-to-astro.sh              # Bridge script
```

## Dependency Graph

```
extended-data-types (foundation, no internal deps)
├── lifecyclelogging (depends on extended-data-types)
├── directed-inputs-class (depends on extended-data-types)
└── vendor-connectors (depends on all three above)

secretssync (standalone Go, no Python deps)
docs (builds from all packages)
```

## Key Configuration Files

### Root pyproject.toml (uv workspace)

```toml
[project]
name = "extended-data-library"
version = "0.0.0"
requires-python = ">=3.9"

[tool.uv]
workspace = { members = [
    "packages/extended-data-types",
    "packages/lifecyclelogging",
    "packages/directed-inputs-class",
    "packages/vendor-connectors",
] }
```

### Per-package pyproject.toml (workspace deps)

Internal dependencies use `{ workspace = true }`:

```toml
# packages/lifecyclelogging/pyproject.toml
dependencies = [
    "extended-data-types",  # resolved from workspace
    "rich>=13.7.1",
]

[tool.uv.sources]
extended-data-types = { workspace = true }
```

### nx.json

```json
{
  "$schema": "./node_modules/nx/schemas/nx-schema.json",
  "namedInputs": {
    "default": ["{projectRoot}/**/*"],
    "production": ["default", "!{projectRoot}/tests/**/*"]
  },
  "plugins": [
    "@nxlv/python",
    "@naxodev/nx-go"
  ],
  "targetDefaults": {
    "test": { "cache": true },
    "lint": { "cache": true },
    "build": { "cache": true, "dependsOn": ["^build"] }
  }
}
```

### tox.ini (root, tox-uv)

```ini
[tox]
envlist = edt, logging, inputs, connectors
requires = tox-uv

[testenv:edt]
changedir = packages/extended-data-types
commands = pytest tests/ {posargs}

[testenv:logging]
changedir = packages/lifecyclelogging
commands = pytest tests/ {posargs}

[testenv:inputs]
changedir = packages/directed-inputs-class
commands = pytest tests/ {posargs}

[testenv:connectors]
changedir = packages/vendor-connectors
commands = pytest tests/ {posargs}

[testenv:docs]
changedir = docs
commands = sphinx-build -b markdown sphinx/ src/content/docs/api/
```

### Justfile

```just
default:
    @just --list

# Python
test *args:
    tox {{args}}

lint:
    uvx ruff check packages/

format:
    uvx ruff format packages/

typecheck:
    uvx mypy packages/*/src/

# Go
test-go:
    cd packages/secretssync && go test ./...

build-go:
    cd packages/secretssync && go build -o bin/secretsync ./cmd/secretsync

# Docs
docs-api:
    tox -e docs

docs-build: docs-api
    cd docs && npm run build

docs-dev:
    cd docs && npm run dev

# Nx
affected *args:
    npx nx affected {{args}}

graph:
    npx nx graph

# CI
ci: lint typecheck test test-go
```

## Docs Pipeline

```
Python packages (src/)
       │
       ▼
Sphinx + myst-parser + autodoc
  (sphinx-build -b markdown)
       │
       ▼
docs/src/content/docs/api/    (generated markdown)
  +
docs/src/content/docs/*.mdx   (hand-written guides)
       │
       ▼
Astro Starlight (npm run build)
       │
       ▼
Static site (dist/)
```

## Implementation Phases

### Phase 1: Scaffold monorepo structure (parallel)
- Create directory structure under packages/
- Set up root pyproject.toml, nx.json, package.json, tox.ini, justfile
- Initialize Nx workspace with plugins

### Phase 2: Migrate Python packages (parallel, 4 agents)
- Copy src/ and tests/ from each cloned repo
- Adapt pyproject.toml for workspace membership
- Convert inter-package deps to `{ workspace = true }`
- Preserve all tool config (ruff, mypy, pytest, semantic-release)

### Phase 3: Migrate Go package
- Copy secretssync source into packages/secretssync/
- Preserve go.mod, Makefile, Dockerfile
- Verify module path still works

### Phase 4: Set up docs site
- Merge Astro Starlight from extended-data-library.github.io
- Configure Sphinx with myst-parser for all Python packages
- Create sphinx-to-astro bridge script
- Set up per-package doc sections

### Phase 5: Verify & clean up
- Run all Python tests via tox
- Run Go tests
- Run linting
- Build docs
- Remove migrated files from old locations if present
