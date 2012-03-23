SETUP
=====

This describes how to setup the nnmon dev environment

Install the base dependencies
-----------------------------

Install the following packages:

    sudo aptitude install python-sqlite python-ooolib

Install the base python virtualenv tools:

    sudo apt-get install python-setuptools
    sudo pip install virtualenv
    sudo pip install virtualenvwrapper


You don't use the virtualenv/virtualenvwrapper tools yet
--------------------------------------------------------

Create a directory to hold the virtual environments:

    mkdir ~/.virtualenvs

Add to your .bashrc (or equivalent) the following lines:

    export WORKON_HOME=$HOME'/.virtualenvs'
    source /usr/local/bin/virtualenvwrapper.sh

Then run the following command:

    source ~/.bashrc

This will end up creating (relatively large) folders in ~/.virtualenvs
where all the projet dependencies will be installed.


Setup your virtual environment
-----------------------------

Create the virtualenv for nnmon and workon it:

    mkvirtualenv --system-site-packages --distribute nnmon

Install nnmon's depdendencies:

    pip install -r pip-requirements.txt


Run the server
--------------

    cd ../nnmon
    python manage.py syncdb # run the database migrations
    python manage.py runserver 8080

Your application is available on http://localhost:8080/

