#!/usr/bin/env bash

# Create virtual environment
virtualenv ~/.virtualenvs/web1200

# Install required python modules
~/.virtualenvs/web1200/bin/pip install pelican markdown

mkdir themes
cd themes

git clone https://github.com/1200wd/pelican-themes-tuxlite-tbs.git
