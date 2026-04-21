# Contributing to Extended Data Library

Thanks for contributing. This repository is a small monorepo containing Python
packages, a Go package, and a docs site. Keep changes focused and validate the
surfaces you touch.

## Repository Shape

- `packages/extended-data-types`: typed serialization, file, map, string, and
  transformation helpers
- `packages/lifecyclelogging`: structured logging helpers
- `packages/directed-inputs-class`: input/config loading utilities
- `packages/vendor-connectors`: vendor API connectors and MCP surfaces
- `packages/secretssync`: Go-based secret synchronization pipeline
- `docs/`: Astro/Starlight site fed by generated Sphinx API content

## Development Setup

```bash
git clone https://github.com/jbcom/extended-data-library.git
cd extended-data-library
uv sync --all-extras
```

If you are working on the Astro docs site, install the Node dependencies too:

```bash
cd docs
npm install
cd ..
```

## GitHub CLI

Use `gh` directly with your existing local authentication context.

```bash
gh auth status
gh pr list
gh issue list
```

## Common Local Checks

Run the checks that match the areas you changed.

```bash
# Python quality gates
tox -e lint
tox -e typecheck

# Python package tests
tox -e edt
tox -e edt-examples
tox -e logging
tox -e inputs
tox -e connectors

# Cross-version compatibility for extended-data-types
tox -e py310-edt,py311-edt,py312-edt,py313-edt,py314-edt

# Docs pipeline
tox -e docs
bash tools/sphinx-to-astro.sh
cd docs && npm run build && cd ..

# Go package
cd packages/secretssync && go test ./... && cd ../..
```

## Documentation Alignment

- Keep `README.md`, package READMEs, the docs site, examples, and the
  documented API surface aligned.
- Treat runnable examples as part of the public contract.
- Do not commit generated `.tox/`, `docs/dist/`, or other local build output.
- Do not commit local agent/editor state such as `.gemini/`, `memory-bank/`,
  Aider history/state files like `.aider.chat.history.md` and
  `.aider.input.history`, or one-off assistant instruction files.

## Branch Hygiene

- Delete feature branches after their pull requests are merged or closed.
- Keep long-lived remote branches only when they have an active owner and a
  documented reason.
- Treat stale automation branches with no open pull request as cleanup
  candidates, not as active work.
- Before deleting an old branch, check whether it has an open pull request or
  unique commits that need to be migrated into a current branch.

## Current Roadmap

- The active repository cleanup and hardening roadmap lives in
  [docs/plans/2026-04-16-remaining-work-prd.md](docs/plans/2026-04-16-remaining-work-prd.md).

## Commit Conventions

Use conventional commits:

```text
feat(edt): add TOML round-trip support
fix(logging): handle empty context markers
docs(connectors): update MCP usage notes
test(inputs): cover stdin JSON parsing
```

Recommended scopes in this repo:

- `edt`
- `logging`
- `inputs`
- `connectors`
- `secretssync`
- `docs`

## Pull Requests

1. Start from `main`.
2. Keep the change set narrow and validate the affected surfaces locally.
3. Update tests or examples when behavior changes.
4. Update docs when package-facing behavior, setup, or support policy changes.
5. Address review feedback before merging.

## License

By contributing, you agree that your contributions will be licensed under the
MIT License.
