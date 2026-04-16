# Installation

:::{card} Supported Runtime
:class-card: docs-card docs-card--primary

`extended-data-types` supports Python 3.10 and newer, with the documented
contract currently verified across Python 3.10 through 3.14.
:::

## Requirements

- Python 3.10 or newer
- [uv](https://docs.astral.sh/uv/) or `pip`

## Install from PyPI

::::{tab-set}

:::{tab-item} uv

```bash
uv add extended-data-types
```
:::

:::{tab-item} pip

```bash
pip install extended-data-types
```
:::

::::

## Install from Source

```bash
git clone https://github.com/jbcom/extended-data-library.git
cd extended-data-library
uv sync
```

## Development Installation

```bash
git clone https://github.com/jbcom/extended-data-library.git
cd extended-data-library
uv sync --all-extras
```

## After Installation

::::{grid} 1 1 2 2
:gutter: 2

:::{grid-item-card} Quickstart
:link: quickstart
:link-type: doc
:class-card: docs-card

Write a structured config file, read it back, and decode it with the root file
helpers.
:::

:::{grid-item-card} Serialization Guide
:link: ../guides/serialization
:link-type: doc
:class-card: docs-card

See format-specific examples for YAML, JSON, TOML, HCL, and Base64 helpers.
:::

:::{grid-item-card} Support & Compatibility
:link: ../guides/support-and-compatibility
:link-type: doc
:class-card: docs-card

See the supported Python range, public API contract, and release-bar
expectations before you wire the package into larger systems.
:::
::::
