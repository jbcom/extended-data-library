# CHANGELOG

> **Note:** Historical links reference pre-monorepo repositories.

<!-- version list -->

## [1.1.0](https://github.com/jbcom/extended-data-library/compare/connectors-v1.0.0...connectors-v1.1.0) (2026-02-26)


### Features

* **docs:** switch to sphinx-autodoc2 for source-based API docs ([#74](https://github.com/jbcom/extended-data-library/issues/74)) ([6edc542](https://github.com/jbcom/extended-data-library/commit/6edc5426fd91ae39459d43ae26da8db4774287ed))

## [1.0.0](https://github.com/jbcom/extended-data-library/compare/connectors-v0.2.0...connectors-v1.0.0) (2026-02-24)


### ⚠ BREAKING CHANGES

* Repository restructured as monorepo. Import paths unchanged but package installation from source requires uv workspace.

### Features

* consolidate extended-data-library org into monorepo ([a6a0f63](https://github.com/jbcom/extended-data-library/commit/a6a0f63fe5a2cc4658b6ae59205890658ca66e16))


### Bug Fixes

* **ci:** remove semantic-release, add docs testing, fix CD ([#49](https://github.com/jbcom/extended-data-library/issues/49)) ([055eded](https://github.com/jbcom/extended-data-library/commit/055eded0026932058b522cd3f82a9524bb61204e))

## v0.2.0 (2025-12-07)

### Features

- **connectors**: Add Cursor and Anthropic connectors
  ([#16](https://github.com/jbcom/vendor-connectors/pull/16),
  [`2edc23f`](https://github.com/jbcom/vendor-connectors/commit/2edc23f3e706919dff4196c489773442cdf8cb31))


## v0.1.1 (2025-12-07)

### Bug Fixes

- Restore working Dockerfile with Go 1.25.3 and correct process-compose install
  ([`aa10854`](https://github.com/jbcom/vendor-connectors/commit/aa10854a11ed0e87e1450743f7925acf8b5bcf4c))


## v0.1.0 (2025-12-06)

- Initial Release
