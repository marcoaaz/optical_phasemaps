
project = 'Optical Phase Maps: Documentation'
copyright = '2026, Marco Acevedo'
author = 'Marco A. Acevedo Z.'

extensions = [
    'sphinx_design',
    'sphinx_rtd_theme',
    'sphinx.ext.githubpages'
]

html_theme = 'sphinx_rtd_theme'
html_static_path = ['_static']

html_theme_options = {
    'collapse_navigation': True,
    'sticky_navigation': True,
    'navigation_depth': 4,
    'includehidden': True,
    'titles_only': False
}
