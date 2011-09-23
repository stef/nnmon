#!/bin/sh
# launch this in the python virtualenv to regenerate the .pot :
pybabel extract -F babel.cfg -o locale/django.pot . 

# then this to push it to transifex (after cheching you didn't loose anything
# tx push -s 

# To pull the translated language do this : 
# tx pull

# To add a language link with transifex do : 
# tx set -r nnmon.messagespot -l nl locale/nl/LC_MESSAGES/django.po
