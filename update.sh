#!/usr/bin/env bash

WEBSITEDIR='/var/www/web-coineva'

source ~/.virtualenvs/web1200/bin/activate

cd $WEBSITEDIR
git pull
rm -r output
pelican content
