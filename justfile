# Extended Data Library - Monorepo Task Runner

default:
    @just --list

# ── Python ────────────────────────────────────────────

# Run all Python tests via tox
test *args:
    tox -e edt,logging,inputs,connectors {{ args }}

# Run tests for a specific package (edt, logging, inputs, connectors)
test-pkg pkg *args:
    tox -e {{ pkg }} -- {{ args }}

# Lint all Python packages (check + format check)
lint:
    uvx ruff check packages/
    uvx ruff format --check packages/

# Format all Python packages
format:
    uvx ruff format packages/

# Type-check Python packages
typecheck:
    tox -e typecheck

# Run all Python tests with coverage XML output (for SonarCloud)
coverage:
    tox -e edt,logging,inputs,connectors

# Sync all Python dependencies
sync:
    uv sync --all-extras

# ── Go ────────────────────────────────────────────────

# Run Go tests for secretssync
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

# Run tests with coverage for local SonarCloud prep
sonar: coverage test-go

# ── Housekeeping ─────────────────────────────────────

# Remove build artifacts, caches, and coverage files
clean:
    rm -rf .tox
    rm -rf build/ dist/
    rm -f coverage.xml
    find . -type d -name __pycache__ -exec rm -rf {} + 2>/dev/null || true
    find . -type d -name '*.egg-info' -exec rm -rf {} + 2>/dev/null || true
    find . -name coverage.xml -exec rm -f {} + 2>/dev/null || true
    find . -name '.coverage' -exec rm -f {} + 2>/dev/null || true
