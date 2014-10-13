#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals
import os

AUTHOR = u'Steven Pav'
SITENAME = u'minimum-viable-parenting'
SITEURL = u'http://www.minimum-viable-parenting.com'
AUTHOR_EMAIL = u'steven@minimum-viable-parenting.com'

PATH = 'content'

TIMEZONE = 'America/Los_Angeles'

DEFAULT_LANG = u'en'

# Feed generation is usually not desired when developing
#FEED_ALL_ATOM = None
#CATEGORY_FEED_ATOM = None
#TRANSLATION_FEED_ATOM = None

FEED_ALL_ATOM = u'feeds/all.atom.xml'
CATEGORY_FEED_ATOM = u'feeds/%s.atom.xml'
TRANSLATION_FEED_ATOM = None
FEED_MAX_ITEMS = 10

FEED_RSS = u'feeds/all.rss'

USE_FOLDER_AS_CATEGORY = True
DEFAULT_CATEGORY = u'misc'

HOME = os.environ['HOME']
#THEME = HOME + '/github/pelican-themes/nmnlist'
#THEME = 'theme/pure'
THEME = 'theme/pelican-chunk'

# Blogroll
#LINKS = (('Pelican', 'http://getpelican.com/'),)

# Social widget
SOCIAL = (('github', 'https://github.com/shabbychef/minimum-viable-parenting'),)

# for pelican-chunk:
LINKS = (('PWD', 'http://www.parenting-without-dignity.com'),
		('github', 'https://github.com/shabbychef/minimum-viable-parenting'),
	('RSS', 'feeds/all.rss'),
	('atom', 'feeds/all.atom.xml'),)
MINT = False
SITESUBTITLE = 'why daddy drinks'
FOOTER_TEXT = u'<!-- pelican-chunk -->'

DEFAULT_PAGINATION = 10

# see http://docs.getpelican.com/en/latest/tips.html
STATIC_PATHS = ['images', 'extra/CNAME', 'extra/geetignore']
EXTRA_PATH_METADATA = {'extra/CNAME': {'path': 'CNAME'},
        'extra/geetignore': {'path': '.gitignore'},}

SUMMARY_MAX_LENGTH = 100

DISQUS_SITENAME = u'minimum-viable-parenting'

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

