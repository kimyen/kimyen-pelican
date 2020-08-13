#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'kimyen'
SITENAME = 'kimyen'
SITEURL = 'https://kimyen.github.io'

PATH = 'content'

TIMEZONE = 'America/Los_Angeles'

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('Home', '/index.html'),
         ('About', '/about.html'),
         ('Projects', '/projects.html'),
         ('Hobbies', '/hobbies.html'),)

# Social widget
SOCIAL = (('Email', 'mailto:kimyen@github.com'),
          ('GitHub', 'http://github.com/github'),
          ('Linkedin', 'https://www.linkedin.com/in/kimyen-ladia-a3b50884'))

DEFAULT_PAGINATION = 5

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

# Publish
DELETE_OUTPUT_DIRECTORY = False

# theme
THEME = '/Users/kimyen/GitHub/pelican-themes/voce'

