# Configuration file for the Sphinx documentation builder.
# This config generates markdown output that feeds into Astro Starlight.

import os
import sys

# Add each package's source to the path for autodoc
packages_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", "packages"))
for pkg in ["extended-data-types", "lifecyclelogging", "directed-inputs-class", "vendor-connectors"]:
    src_path = os.path.join(packages_dir, pkg, "src")
    if os.path.isdir(src_path):
        sys.path.insert(0, src_path)

# -- Project information -----------------------------------------------------
project = "Extended Data Library"
copyright = "2025-2026, Jon Bogaty"
author = "Jon Bogaty"

# -- General configuration ---------------------------------------------------
extensions = [
    "myst_parser",
    "sphinx.ext.autodoc",
    "sphinx.ext.autosummary",
    "sphinx.ext.napoleon",
    "sphinx_autodoc_typehints",
    "sphinx.ext.viewcode",
    "sphinx.ext.intersphinx",
]

templates_path = []
exclude_patterns = ["_build", "Thumbs.db", ".DS_Store"]

# Source file suffixes
source_suffix = {
    ".md": "markdown",
    ".rst": "restructuredtext",
}

# -- Extension configuration -------------------------------------------------

# autodoc settings
autodoc_default_options = {
    "members": True,
    "member-order": "bysource",
    "special-members": "__init__",
    "undoc-members": True,
    "exclude-members": "__weakref__",
    "show-inheritance": True,
}
autodoc_typehints = "description"
autodoc_class_signature = "separated"

# autosummary settings
autosummary_generate = True

# napoleon settings (Google/NumPy style docstrings)
napoleon_google_docstring = True
napoleon_numpy_docstring = True
napoleon_include_init_with_doc = True
napoleon_use_param = True
napoleon_use_rtype = True

# intersphinx settings
intersphinx_mapping = {
    "python": ("https://docs.python.org/3", None),
}

# myst_parser settings
myst_enable_extensions = [
    "colon_fence",
    "deflist",
    "fieldlist",
    "tasklist",
]
myst_heading_anchors = 3
