from datetime import datetime

# pylint: disable=W0622

project = 'Ansible Semi - Documentation'
copyright = f'{datetime.now().year}, Community'
author = 'Community'
extensions = ['sphinx_rtd_theme']
templates_path = ['_templates']
exclude_patterns = []
html_theme = 'sphinx_rtd_theme'
html_theme_options = {}
html_static_path = ['_static']
html_css_files = ['css/wiki.css']
master_doc = 'index'
display_version = True
sticky_navigation = True
html_logo = '_static/img/logo.png'
html_favicon = '_static/img/logo.png'
