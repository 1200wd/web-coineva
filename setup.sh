#!/usr/bin/env bash

# Create virtual environment
virtualenv ~/.virtualenvs/web1200

# Install required python modules
~/.virtualenvs/web1200/bin/pip install pelican markdown disqus-python

cp update.sh update.local.sh

git clone --recursive https://github.com/getpelican/pelican-plugins

mkdir themes
cd themes

git clone https://github.com/1200wd/pelican-sober.git
