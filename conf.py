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
html_css_files = ['custom.css', 's5roles.css']

# allows for the use of inline notation, via s5defs.txt and _static/s5roles.css
# alternative to having this line at the top of every content page where it is needed
rst_prolog = """
.. include:: /s5defs.txt

"""

suppress_warnings = ['autosectionlabel.*']

###############
# get the environment variable build_all_docs and pages_root
build_all_docs = os.environ.get("build_all_docs")
pages_root = os.environ.get("pages_root", "")

# if not there, we dont call this
if build_all_docs is not None:
    # we get the current language and version
    current_version = os.environ.get("current_version")
    # we set the html_context wit current version and empty languages and versions for now
    html_context = {'current_version' : current_version, 'versions' : []}
    # and we append all versions accordingly, we treat the main branch as latest 
    #if (current_version == 'latest'):
    html_context['versions'].append(['latest', pages_root])
    # and loop over all other versions from our yaml file to set versions 
    with open("versions.yaml", "r") as yaml_file:
        docs = yaml.safe_load(yaml_file)
    for version, details in docs.items():
        html_context['versions'].append([version, pages_root+'/'+version+'/'])
