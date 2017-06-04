#!/usr/bin/env bash

#WEBSITEDIR='/home/lennart/code/web-coineva'
WEBSITEDIR='/var/www/web-coineva'

source ~/.virtualenvs/web1200/bin/activate

cd $WEBSITEDIR
rm -r output
pelican content
