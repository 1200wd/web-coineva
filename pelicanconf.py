#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Lennart Jongeneel'
SITENAME = u'Coineva'
SITEURL = ''
SITETITLE = 'Coineva'
SITESUBTITLE = 'Cryptocurrency Code Factory'
SITEDESCRIPTION = 'Foo Bar\'s Thoughts and Writings'
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

USE_FOLDER_AS_CATEGORY = False
MAIN_MENU = True
HOME_HIDE_TAGS = True

# Blogroll
LINKS = (('5 ways to explain bitcoin', 'five-ways-to-explain-bitcoin.html'),
         ('How to create a wallet', 'how-to-create-a-wallet.html'),
         ('BitcoinLib', 'python-bitcoin-library.html'),)

MENUITEMS = (('Archives', '/archives.html'),
             ('Categories', '/categories.html'),
             ('Tags', '/tags.html'),)

# Social widget
SOCIAL = (('linkedin', 'https://www.linkedin.com/company-beta/8098420/'),
          ('github', 'https://github.com/1200wd'),
          ('twitter', 'https://twitter.com/1200wd'),
          ('rss', 'feeds/all.atom.xml'))

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

THEME = "themes/Flex"
SITESUBTITLES = ('Coineva', 'cryptocurrency factory...')
