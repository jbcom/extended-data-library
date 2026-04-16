# Contributing

Thanks for contributing to `extended-data-types`.

## Development Setup

```bash
git clone https://github.com/jbcom/extended-data-library.git
cd extended-data-library
uv sync --all-extras
```

## GitHub CLI

Use `gh` directly with your existing local authentication context.

```bash
gh auth status
gh pr list
gh issue list
```

## Required Local Checks

```bash
tox -e edt
tox -e edt-examples
tox -e lint
tox -e typecheck
tox -e docs
```

## Cross-Version Check

When a change touches compatibility-sensitive behavior, run the test suite
across the full supported Python range:

```bash
tox -e py310-edt,py311-edt,py312-edt,py313-edt,py314-edt
```

## Documentation Alignment

- Keep `README.md`, the docs site, examples, and the documented API surface in sync.
- Treat runnable examples as part of the public contract, not as optional extras.
- Do not commit generated `docs/_build/` output.

## Pull Requests

1. Start from `main`.
2. Keep changes focused and add or update tests for behavior changes.
3. Keep documentation and examples aligned with the implemented API.
4. Use conventional commit prefixes such as `feat:`, `fix:`, `docs:`,
   `refactor:`, `test:`, and `chore:`.
