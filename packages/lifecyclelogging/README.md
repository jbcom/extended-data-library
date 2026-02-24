# LifecycleLogging

*Lifecycle-aware logging with rich output and message storage.*

[![CI Status](https://github.com/jbcom/extended-data-library/actions/workflows/ci.yml/badge.svg)](https://github.com/jbcom/extended-data-library/actions/workflows/ci.yml)
[![PyPI version](https://img.shields.io/pypi/v/lifecyclelogging.svg)](https://pypi.org/project/lifecyclelogging/)
[![Python versions](https://img.shields.io/pypi/pyversions/lifecyclelogging.svg)](https://pypi.org/project/lifecyclelogging/)

LifecycleLogging is a comprehensive logging utility that combines Python's `logging` with rich output formatting. It provides configurable console and file outputs, message storage with context markers, verbosity controls, and seamless Gunicorn integration.

## Key Features

- **Rich Formatting** - Enhanced readability with configurable console and file outputs
- **Message Storage** - Store and retrieve messages by context and storage markers
- **Verbosity Control** - Fine-grained verbosity thresholds with bypass markers
- **Level Filtering** - Case-insensitive allowed/denied storage rules
- **JSON Attachment** - Attach structured data to log entries
- **Gunicorn Integration** - Automatic logger inheritance when running under Gunicorn
- **Type-Safe** - Full type annotations throughout

---

## Installation

```bash
pip install lifecyclelogging
```

## Quick Start

```python
from lifecyclelogging import Logging

# Initialize logger
logger = Logging(
    enable_console=True,
    enable_file=True,
    logger_name="my_app"
)

# Basic logging
logger.logged_statement("Basic message", log_level="info")

# With context marker
logger.logged_statement(
    "Application started",
    context_marker="STARTUP",
    log_level="info"
)

# With JSON data
logger.logged_statement(
    "Request received",
    json_data={"method": "GET", "path": "/api/users"},
    log_level="debug"
)
```

## Advanced Features

### Verbosity Control

```python
logger = Logging(
    enable_verbose_output=True,
    verbosity_threshold=2
)

# Only logged if verbosity threshold allows
logger.logged_statement(
    "Detailed debug info",
    verbose=True,
    verbosity=2,
    log_level="debug"
)
```

### Verbosity Bypass

```python
logger.register_verbosity_bypass_marker("IMPORTANT")

# Logged regardless of verbosity settings
logger.logged_statement(
    "Critical info",
    context_marker="IMPORTANT",
    verbose=True,
    verbosity=5,
    log_level="debug"
)
```

### Message Storage

```python
# Store message under a marker
logger.logged_statement(
    "Important event",
    storage_marker="EVENTS",
    log_level="info"
)

# Access stored messages
events = logger.stored_messages["EVENTS"]
```

---

## Contributing

Contributions are welcome! Please see the [Contributing Guidelines](https://github.com/jbcom/extended-data-library/blob/main/CONTRIBUTING.md) for more information.

## Project Links

- [**PyPI**](https://pypi.org/project/lifecyclelogging/)
- [**GitHub**](https://github.com/jbcom/extended-data-library/tree/main/packages/lifecyclelogging)
- [**Documentation**](https://extendeddata.dev)
- [**Changelog**](https://github.com/jbcom/extended-data-library/blob/main/packages/lifecyclelogging/CHANGELOG.md)
