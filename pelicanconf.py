#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals
from datetime import datetime 
from pathlib import Path

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
         ('About', '/pages/about.html'),
         ('Projects', '/projects.html'),
         ('Hobbies', '/hobbies.html'),)

# Social widget
SOCIAL = (('Email', 'mailto:kimyen@github.com'),
          ('GitHub', 'http://github.com/kimyen'),
          ('Linkedin', 'https://www.linkedin.com/in/kimyen-ladia-a3b50884'))

DEFAULT_PAGINATION = 5

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

# Publish
DELETE_OUTPUT_DIRECTORY = False

# theme
CURRENT_DIR_PATH = Path(__file__).resolve().parent
THEME = '{}/voce-theme'.format(CURRENT_DIR_PATH)

# Custom Vars
USER_LOGO_URL = 'https://avatars1.githubusercontent.com/u/4404426?s=460&u=005f2c61c8afb6778c2d00b4a9746a67cd1c39f1&v=4'
FUZZY_DATES = True
CURRENT_YEAR = datetime.now().year
DEFAULT_DATE_FORMAT = "%b %d, %Y" 

