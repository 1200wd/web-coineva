#!/usr/bin/env bash

# Create virtual environment
python3 -m venv venv

# Install required python modules
venv/bin/pip3 install pelican markdown disqus-python

cp update.sh update.local.sh

git clone --recursive https://github.com/getpelican/pelican-plugins

mkdir themes
cd themes

git clone https://github.com/1200wd/pelican-sober.git
