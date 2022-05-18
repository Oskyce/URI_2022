# Configuration file for the Sphinx documentation builder.

# -- Project information

project = 'Linee guida per l\'utilizzo delle risorse informatiche'
copyright = '2022, DGSIA-CUS'
author = 'CUS'

release = '0.1'
version = '0.1.0'

# -- General configuration

extensions = [
    'sphinx.ext.duration',
    'sphinx.ext.doctest',
    'sphinx.ext.autodoc',
    'sphinx.ext.autosummary',
    'sphinx.ext.intersphinx',
]

intersphinx_mapping = {
    'python': ('https://docs.python.org/3/', None),
    'sphinx': ('https://www.sphinx-doc.org/en/master/', None),
}
intersphinx_disabled_domains = ['std']

templates_path = ['_templates']

html_theme_options = {
    'style_nav_header_background: #0369ab'
    # Toc options
    'collapse_navigation': False,
    'sticky_navigation': False,
    'navigation_depth': 4,
    'includehidden': True,
    'titles_only': False
}

html_logo = '_image/imginiz.jpg'

# The name for this set of Sphinx documents.  If None, it defaults to
# "<project> v<release> documentation".
html_title = "Linee guida per l\'utilizzo delle risorse informatiche"

# A shorter title for the navigation bar. Default is the same as html_title.
html_short_title = "Linee guida URI 2022"

# -- Options for HTML output

html_theme = 'sphinx_rtd_theme'

# -- Options for EPUB output
epub_show_urls = 'footnote'
