# Extended Data Library - Monorepo Task Runner

default:
    @just --list

# ── Python ────────────────────────────────────────────

# Run all Python tests via tox
test *args:
    tox {{ args }}

# Run tests for a specific package (edt, logging, inputs, connectors)
test-pkg pkg *args:
    tox -e {{ pkg }} -- {{ args }}

# Lint all Python packages
lint:
    uvx ruff check packages/extended-data-types/src/ packages/lifecyclelogging/src/ packages/directed-inputs-class/src/ packages/vendor-connectors/src/

# Format all Python packages
format:
    uvx ruff format packages/extended-data-types/src/ packages/lifecyclelogging/src/ packages/directed-inputs-class/src/ packages/vendor-connectors/src/

# Type-check all Python packages
typecheck:
    uvx mypy packages/extended-data-types/src/ packages/lifecyclelogging/src/ packages/directed-inputs-class/src/ packages/vendor-connectors/src/

# Sync all Python dependencies
sync:
    uv sync --all-extras

# ── Go ────────────────────────────────────────────────

# Run Go tests
test-go *args:
    cd packages/secretssync && go test ./... {{ args }}

# Build Go binary
build-go:
    cd packages/secretssync && go build -o bin/secretsync ./cmd/secretsync

# Lint Go code
lint-go:
    cd packages/secretssync && golangci-lint run

# ── Docs ──────────────────────────────────────────────

# Generate API docs from Python source via Sphinx
docs-api:
    tox -e docs

# Build the full docs site (Sphinx API + Astro Starlight)
docs-build: docs-api
    cd docs && npm run build

# Start docs dev server
docs-dev:
    cd docs && npm run dev

# ── Nx ────────────────────────────────────────────────

# Show Nx dependency graph
graph:
    npx nx graph

# Run Nx affected command
affected *args:
    npx nx affected {{ args }}

# ── CI ────────────────────────────────────────────────

# Run full CI pipeline
ci: lint typecheck test test-go

# Run full CI pipeline including docs
ci-full: ci docs-build
