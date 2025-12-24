# Active Context

## extended-data-types

Extended data type utilities for Python with transformations and helpers.

### Features
- Number transformations
- String utilities
- Data conversion helpers
- Type-safe operations

### Package Status
- **Registry**: PyPI
- **Python**: 3.9+
- **Dependencies**: None (pure Python)

### Development
```bash
uv sync --extra tests
uv run pytest tests/ -v
uvx ruff check src/ tests/
uvx ruff format src/ tests/
```

---
*Last updated: 2025-12-06*

## Session: 2025-12-24

### Completed
- [x] Fixed `PACKAGE_NAME` placeholders in all documentation files.
- [x] Improved `Deploy Documentation to Pages` workflow (`docs.yml`):
    - Added `pull_request` trigger for build verification.
    - Updated to Python 3.13.
    - Switched to `hynek/setup-cached-uv` for better performance.
    - Ensured correct permissions and deployment guards.
- [x] Added `docs/_build/` to `.gitignore`.
- [x] Verified core CI (tests and lint) passes locally.
- [x] Pushed changes to branch `fix/issue-6`.

### Issues
- [ ] PR creation via `gh pr create` failed due to permissions ("Resource not accessible by integration"). The branch is pushed and ready for manual PR creation or merge.
