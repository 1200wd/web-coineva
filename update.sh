#!/usr/bin/env bash

WEBSITEDIR='/home/lennart/code/web-coineva'

source ~/.virtualenvs/web1200/bin/activate

cd $WEBSITEDIR

pelican content
