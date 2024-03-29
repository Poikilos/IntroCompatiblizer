#!/bin/sh
#sudo dnf install python-virtualenv
KIVY_VENV="$HOME/venv/kivy"

python -m pip install --upgrade --user pip setuptools virtualenv
python -m virtualenv $KIVY_VENV
source $KIVY_VENV/bin/activate
echo "* using \"`which python`\""
python -m pip install cython
python -m pip install kivy
#python -m pip install kivy_examples
##"Gstreamer is not included, so if you would like to use media playback
##with kivy, you should install ffpyplayer like so"
#python -m pip install ffpyplayer
#-<https://kivy.org/doc/stable/installation/installation-linux.html>
echo "Now you can use `which python` to run kivy apps."
deactivate
