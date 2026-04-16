# Support and Compatibility

This guide defines the documented public contract for `extended-data-types`.
Use it when you need to know what the project considers stable, which Python
versions it actively supports, and where the compatibility boundaries are.

::::{grid} 1 1 2 3
:gutter: 2

:::{grid-item-card} Supported runtimes
:class-card: docs-card docs-card--feature

The package targets Python `3.10`, `3.11`, `3.12`, `3.13`, and `3.14`.
:::

:::{grid-item-card} Stable entry points
:class-card: docs-card docs-card--feature

The root package, the documented transformation namespaces, and `yaml_utils`
form the supported public surface.
:::

:::{grid-item-card} Verified quality bar
:class-card: docs-card docs-card--feature

Tests, lint, typing, docs, runnable examples, packaging, and coverage are part
of the release bar for the documented package contract.
:::
::::

## Supported Python Versions

`extended-data-types` is documented and tested as a Python 3.10+ library, with
the currently tagged support window covering:

- Python 3.10
- Python 3.11
- Python 3.12
- Python 3.13
- Python 3.14

The project does not treat those versions as “best effort” tiers. The same
documented behavior is expected to hold across the full supported range.

## Public API Contract

The supported import surfaces are:

- `extended_data_types`
- `extended_data_types.transformations.numbers`
- `extended_data_types.transformations.strings`
- `extended_data_types.yaml_utils`

Those are the surfaces the guides, examples, and API reference intentionally
document. They are the right starting point for most callers.

Lower-level implementation modules may still be importable, but they should be
treated as internal unless the documentation points to them directly.

## Compatibility Rules

- The root package is the backward-compatible convenience layer.
- Namespaced transformation modules are the preferred surface for richer,
  growing domains like number and string transformations.
- `yaml_utils` is a documented advanced surface for tagged YAML values,
  representers, constructors, and YAML-native wrappers.
- `decode_file()` decodes already-read content. It is not a path reader.
- The root-exported `is_url()` is intentionally strict and accepts only
  `http` and `https` URLs.
- HCL support targets plain Terraform-style data made of scalars, mappings,
  lists, and block lists. Parser metadata is normalized away on decode.

## Stability Bar

The project treats documentation and examples as part of the public contract,
not just supporting material.

That means a stable release expects:

- typed public helpers
- passing tests across the supported Python range
- runnable example scripts
- a clean Sphinx build with warnings treated as errors
- aligned README, docs pages, and API reference
- packaging and distribution checks

## Automation and Agentic Workflows

The library is intentionally structured to behave predictably inside larger
automation systems:

- `read_file()` and `decode_file()` are separate, so I/O and parsing stay explicit
- suffix-aware export helpers keep write behavior deterministic
- HCL is normalized to plain data instead of parser-specific structures
- map and string helpers can be composed into normalization pipelines without
  introducing hidden global state

If you are building agentic or automation-heavy workflows, the guides in this
docs site use those same boundaries rather than inventing wrapper APIs.

## Verifying the Contract Locally

The contributing guide includes the full release-bar commands. When you need a
cross-version spot-check, run the test suite across the supported Python range:

```bash
export UV_LINK_MODE=copy
for py in 3.10 3.11 3.12 3.13 3.14; do
  uv run --python "$py" --extra tests pytest tests -q
done
```

## Related Guides

- [Quickstart](../getting-started/quickstart.md)
- [Choosing the API Surface](./api-surface.md)
- [Composing Helpers](./composing-helpers.md)
- [Workflow Recipes](./workflow-recipes.md)
- [Contributing](../development/contributing.md)
