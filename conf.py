# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#

import os
import yaml
#import sys
#if os.path.isdir('../improve'):
#    sys.path.insert(0, os.path.abspath('../improve/framework.py'))
#else:
#    print("Can't find path.")
#    sys.exit(404)


# -- Project information -----------------------------------------------------

project = 'IMPROVE'
copyright = '2023, IMPROVE Team'
author = 'IMPROVE Team'

# The full version, including alpha/beta/rc tags
release = '0.1'


# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    'sphinx_copybutton',
    'sphinx.ext.autosectionlabel',
]

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']


# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
#html_theme = 'alabaster'
#import sphinx_rtd_theme
html_theme = "sphinx_rtd_theme"
html_theme_options = {
    'collapse_navigation': False,
    'display_version': False
}
#html_theme_path = [sphinx_rtd_theme.get_html_theme_path()]

#pages_root = "https://jdacs4c-improve.github.io/docs"
#html_context = {'current_version' : "v0.1.0", 'versions' : [["v0.0.3-beta", pages_root+"/v0.0.3-beta/index.html"], ["v0.1.0", pages_root+"/v0.1.0-alpha/index.html"]]}

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']
html_css_files = ['custom.css',]


