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
HOME_HIDE_TAGS = False
DISPLAY_PAGES_ON_MENU = True

# Blogroll
LINKS = (('What to do with my paper wallet?', '/what-to-do-with-my-paper-wallet.html'),
         # ('5 ways to explain bitcoin', '/five-ways-to-explain-bitcoin.html'),
         # ('why bitcoin?', '/why-bitcoin.html'),
         ('bitcoinlib', '/python-bitcoin-library.html'),
         ('bulkpaperwallets', 'https://github.com/1200wd/bulkpaperwallets'))

# MENUITEMS = (('Archives', '/archives.html'),
#              ('Categories', '/categories.html'),
#              ('Tags', '/tags.html'),)

# Social widget
SOCIAL = (('github', 'https://github.com/1200wd'),
          ('bitcoinlib', 'http://bitcoinlib.readthedocs.io/en/latest/'),
          ('rss', 'feeds/all.atom.xml'))

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

THEME = "themes/pelican-themes-tuxlite-tbs"
SITESUBTITLES = ('Coineva- Cryptocurrency Code Factory')

PLUGIN_PATHS = ['pelican-plugins']
PLUGINS = [u"disqus_static"]

DISQUS_SITENAME = u'coineva'
DISQUS_SECRET_KEY = u'4DRbwCCduyXpJIlOKQTClklccjXHoMYpvPPzwKSZ1bPUMpqJaXvzAVbUCtFioicd'
DISQUS_PUBLIC_KEY = u'MCDSIEr3LjY65MXIM5baRUGiSo3C4y2glCAR0GK0wwvs23yZaDcB3Ytpk82fTutY'
