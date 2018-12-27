#!/usr/bin/env python
# -*- coding: utf-8 -*- #

from __future__ import unicode_literals
import socket

AUTHOR = u'Lennart Jongeneel'
SITENAME = u'Coineva - Cryptocurrency Code Factory'

if socket.gethostname() == 'talisman':
    SITEURL = 'http://localhost:8000'
else:
    SITEURL = 'http://coineva.com'
SITETITLE = 'Coineva'
SITESUBTITLE = 'Cryptocurrency Code Factory'
SITEDESCRIPTION = 'bitcoin stuff'
SITELOGO = SITEURL + '/images/Peter-Behrens-Alphabet-1908-C.png'
# FAVICON = SITEURL + '/images/favicon.ico'
PYGMENTS_STYLE = 'monokai'

ROBOTS = 'index, follow'
PATH = 'content'

TIMEZONE = 'Europe/Amsterdam'

DEFAULT_LANG = u'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = 'feeds/all.atom.xml'
CATEGORY_FEED_ATOM = 'feeds/%s.atom.xml'
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

USE_FOLDER_AS_CATEGORY = True
MAIN_MENU = True
HOME_HIDE_TAGS = True
DISPLAY_PAGES_ON_MENU = False

# Blogroll
LINKS = (('BitcoinLib', '/python-bitcoin-library.html'),
         ('Bitcoinlib Docs', 'http://bitcoinlib.readthedocs.io/en/latest/'),
         ('Github BulkPaperWallets', 'https://github.com/1200wd/bulkpaperwallets'))

# MENUITEMS = (('Archives', '/archives.html'),
#              ('Categories', '/categories.html'),
#              ('Tags', '/tags.html'),)

# Social widget
SOCIAL = (('Github', 'https://github.com/1200wd'),
          ('Twitter', 'https://twitter.com/coineva1200'),
          ('RSS', 'feeds/all.atom.xml'))

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

THEME = "themes/pelican-sober"
PELICAN_SOBER_HOME_LISTS_ARTICLES = True
# PELICAN_SOBER_ABOUT = "My name is Henkie"

PLUGIN_PATHS = ['pelican-plugins']
PLUGINS = [u"disqus_static"]

DISQUS_SITENAME = u'coineva'
DISQUS_SECRET_KEY = u''
DISQUS_PUBLIC_KEY = u''
