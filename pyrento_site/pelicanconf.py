#!/usr/bin/env python
# -*- coding: utf-8 -*- #

AUTHOR = 'Dan Williams'
SITENAME = 'DW.site'
SITEURL = ''

PATH = 'content'

TIMEZONE = 'America/Chicago'

DEFAULT_LANG = 'en'

THEME = '../pyrento_theme'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

MENUITEMS = (
    ("Dan's Acidemic Page", 'http://www.cs.virginia.edu/~dww4s/index_old.html'),
    ("NVidia", 'http://nvidia.com'),
    )

# Blogroll
# Social widget
DEFAULT_PAGINATION = False

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

STATIC_PATHS = [
    'static'
]
