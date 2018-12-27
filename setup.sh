#!/usr/bin/env bash

# Create virtual environment
virtualenv ~/.virtualenvs/web1200

# Install required python modules
~/.virtualenvs/web1200/bin/pip install pelican markdown disqus-python

cp update.sh update.local.sh

git clone --recursive https://github.com/getpelican/pelican-plugins

mkdir themes
cd themes

https://github.com/fle/pelican-sober.git
