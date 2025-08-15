# Configuration file for the Sphinx documentation builder.  # noqa: D100, INP001
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

import sys
from pathlib import Path

sys.path.insert(0, str(Path("..", "src").resolve()))

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = "micropython-units"
copyright = "2025, Matthew Woolley"
author = "Matthew Woolley"
release = "0.1"

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    "sphinx.ext.duration",
    "sphinx.ext.doctest",
    "sphinx.ext.autodoc",
    "sphinx.ext.viewcode",
    "sphinx.ext.napoleon",
]

# Autodoc settings
autodoc_default_options = {
    "members": True,
    "undoc-members": True,
    "special-members": True,
    "autodoc-member-order": "groupwise",
    "exclude-members": "__dict__, __weakref__, __annotations__, __new__, __module__, __str__, __repr__",  # noqa: E501
}

templates_path = ["_templates"]
exclude_patterns = ["_build", "Thumbs.db", ".DS_Store"]

# Build directory
html_output_dir = "_build"

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = "alabaster"
