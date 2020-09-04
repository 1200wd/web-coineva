#!/usr/bin/env bash

WEBSITEDIR='/var/www/web-coineva'

source /var/www/web-coineva/venv/bin/activate

cd $WEBSITEDIR
git pull
rm -r output/*
pelican content
chown -R root:www-data $WEBSITEDIR
