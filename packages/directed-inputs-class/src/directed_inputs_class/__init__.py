"""Directed Inputs Class.

This package provides tools for managing and processing directed inputs from
various sources like environment variables, stdin, and predefined dictionaries.
"""

from __future__ import annotations

from directed_inputs_class.__main__ import DirectedInputsClass
from directed_inputs_class.decorators import directed_inputs, input_config


__version__ = "2.1.0"

__all__ = ["DirectedInputsClass", "directed_inputs", "input_config"]
