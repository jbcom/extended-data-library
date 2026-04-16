# Extended Data Library Copilot Instructions

This repository intentionally keeps agent guidance lightweight.

## Repository Shape

- `packages/extended-data-types`
- `packages/lifecyclelogging`
- `packages/directed-inputs-class`
- `packages/vendor-connectors`
- `packages/secretssync`
- `docs/`

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

## GitHub CLI

Use `gh` directly with the existing local authentication context. Do not wrap
local commands with `GH_TOKEN=...`.

```bash
gh auth status
gh pr list
```

## Working Style

- Keep docs, examples, and implementation aligned.
- Prefer the repo's `tox` environments over ad hoc one-off commands.
- Do not introduce extra agent-specific files or automation unless the repo
  actually depends on them.
