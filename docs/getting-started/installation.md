# Installation

## Requirements

- Python 3.9+
- [uv](https://docs.astral.sh/uv/) (recommended) or pip

## Install from PyPI

```bash
# Using uv (recommended)
uv add extended-data-types

# Using pip
pip install extended-data-types
```

## Install from Source

```bash
git clone https://github.com/jbcom/extended-data-types.git
cd extended-data-types
uv sync
```

## Development Installation

```bash
# Clone and install with dev dependencies
git clone https://github.com/jbcom/extended-data-types.git
cd extended-data-types
uv sync --extra dev --extra docs
```
