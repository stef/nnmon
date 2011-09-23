#!/bin/sh

echo "Compiling django/gettext language files ..."
echo -n "   "
for i in `find -mindepth 1 -maxdepth 1  -type d` 
do
    echo -n "$i "
    cd $i/LC_MESSAGES
    msgfmt -o django.mo django.po 
    cd ../..
done
echo " Finished"
