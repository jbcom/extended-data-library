# Repository Instructions

This repository is a small `uv` workspace monorepo for Python libraries plus a
Go package and a docs site. Keep the repo guidance minimal and factual.

## Scope

- `packages/extended-data-types`: core typed serialization, file, map, list,
  string, and type utilities
- `packages/lifecyclelogging`: structured logging
- `packages/directed-inputs-class`: input/config loading
- `packages/vendor-connectors`: vendor API connectors
- `packages/secretssync`: Go-based secret sync pipeline
- `docs/`: Astro/Starlight docs site fed by Sphinx-generated API content

## Preferred Commands

```bash
uv sync
tox -e lint
tox -e typecheck
tox -e edt
tox -e logging
tox -e inputs
tox -e connectors
tox -e edt-examples
tox -e docs
bash tools/sphinx-to-astro.sh
cd docs && npm run build
cd packages/secretssync && go test ./...
```

For cross-version checks on `extended-data-types`:

```bash
tox -e py310-edt,py311-edt,py312-edt,py313-edt,py314-edt
```

## GitHub CLI

Use `gh` directly with the existing local authentication context.

```bash
gh auth status
gh pr list
gh issue list
```

## Expectations

- Keep `README.md`, docs pages, examples, and implementation aligned.
- Treat runnable examples as part of the public contract.
- Prefer focused package-scoped changes over repo-wide churn.
- Do not add agent-specific scaffolding unless a live workflow actually uses it.
- Releases are managed by `release-please`; do not edit version numbers or tags
  by hand.
