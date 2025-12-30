# Configuration file for the Sphinx documentation builder.

import os
import sys

# -- Path setup --------------------------------------------------------------

# Add any paths to sys.path if your modules are outside the root
# sys.path.insert(0, os.path.abspath('../src'))

# -- Project information -----------------------------------------------------

project = 'Syw Account Login'
copyright = '2026, SYW'
author = 'SYW Support Team'

# The full version, including alpha/beta/rc tags
release = '1.0.0'

# -- General configuration ---------------------------------------------------

# Sphinx extensions (leave blank or add as needed)
extensions = []

# Allow reStructuredText raw HTML
raw_enabled = True

# Templates and patterns to ignore
templates_path = ['_templates']  
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

# -- Options for HTML output -------------------------------------------------

# Theme (you can switch to 'sphinx_rtd_theme' or another as needed)
# html_theme = 'sphinx_rtd_theme'

# Basic page info
html_title = "Syw.accountonline.com Login – Step-by-Step Guide"
html_short_title = "SYW Login Guide"
html_favicon = 'favicon.ico'  # Place your favicon here

# Hide "View page source"
html_show_sourcelink = False

# Allow unsafe raw HTML in .rst files
html_allow_unsafe = True

# Theme customization
html_theme_options = {
    'show_powered_by': False,
}

# Static assets
# html_static_path = ['_static']

# -- Custom metadata for SEO -----------------------------------------------

html_context = {
    "meta_description": "Access your SYW account securely at syw.accountonline.com login. Learn how to register, log in, and manage your account safely.",
    "meta_keywords": "syw.accountonline.com login, SYW account, SYW login portal, SYW account registration, online account login",
    "meta_robots": "index, follow",
}
