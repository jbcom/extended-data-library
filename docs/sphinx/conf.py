# Configuration file for the Sphinx documentation builder.
# This config generates markdown output that feeds into Astro Starlight.
#
# Uses sphinx-autodoc2 for source-based documentation extraction.
# autodoc2 parses Python source with astroid (no imports needed),
# making it reliable in CI where dependencies may not be installed.

# -- Project information -----------------------------------------------------
project = "Extended Data Library"
copyright = "2025-2026, Jon Bogaty"
author = "Jon Bogaty"

# -- General configuration ---------------------------------------------------
extensions = [
    "myst_parser",
    "autodoc2",
    "sphinx.ext.napoleon",
    "sphinx.ext.intersphinx",
]

templates_path = []
exclude_patterns = ["_build", "Thumbs.db", ".DS_Store"]

# Source file suffixes
source_suffix = {
    ".md": "markdown",
    ".rst": "restructuredtext",
}

# -- autodoc2 configuration -------------------------------------------------
# Point autodoc2 at each package's source directory.
# Paths must be relative to this conf.py file's directory.
# To add a new package, append a (package-dir, module-name) tuple below.

_packages_to_document = [
    ("extended-data-types", "extended_data_types"),
    ("lifecyclelogging", "lifecyclelogging"),
    ("directed-inputs-class", "directed_inputs_class"),
    ("vendor-connectors", "vendor_connectors"),
]

autodoc2_packages = [
    {
        "path": f"../../packages/{pkg_dir}/src/{module_name}",
        "module": module_name,
        "exclude_dirs": ["__pycache__"],
    }
    for pkg_dir, module_name in _packages_to_document
]

# Render as MyST Markdown (compatible with Starlight via sphinx-markdown-builder)
autodoc2_render_plugin = "myst"

# Hide inherited members and undocumented dunder methods by default
autodoc2_hidden_objects = ["inherited", "dunder"]

# Merge class and __init__ docstrings
autodoc2_class_docstring = "merge"

# Include per-module summary tables
autodoc2_module_summary = True

# -- Napoleon configuration (Google-style docstrings) ----------------------
napoleon_google_docstring = True
napoleon_numpy_docstring = False
napoleon_include_init_with_doc = True
napoleon_use_param = True
napoleon_use_rtype = True

# -- intersphinx configuration ---------------------------------------------
intersphinx_mapping = {
    "python": ("https://docs.python.org/3", None),
}

# -- myst_parser configuration ---------------------------------------------
myst_enable_extensions = [
    "colon_fence",
    "deflist",
    "fieldlist",
    "tasklist",
]
myst_heading_anchors = 3
