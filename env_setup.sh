#!/bin/bash

### TO DO
# https://unix.stackexchange.com/questions/6345/how-can-i-get-distribution-name-and-version-number-in-a-simple-shell-script
# Install and use 'uv' package manager in place of 'pip'

# https://stackoverflow.com/questions/70422866/how-to-create-a-venv-with-a-different-python-version

# install Homebrew if it isn't already present
command -v brew >/dev/null 2>/dev/null
if [ $? == 0 ]
then
    echo -n "✅︎ "
    brew --version 2>/dev/null
else
    echo "❌ Homebrew not installed"
    /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
fi

# install Python3.9 if it isn't already present
command -v python3.9 >/dev/null 2>/dev/null
if [ $? == 0 ]
then
    echo -n "✅︎ "
    python3.9 --version 2>/dev/null
else
    echo "❌ Python not installed"
    sudo apt install python3.9-venv
fi

# it is useful to organize virtual envs
mkdir -p ~/.venvs

# create new venv && activate
python3.9 -m venv ~/.venvs/q-env
source ~/.venvs/quantum/bin/activate

# useful package to prevent package install errors, particulary:
# AttributeError: module 'platform' has no attribute 'linux_distribution'
# https://stackoverflow.com/questions/53204916/what-is-the-meaning-of-failed-building-wheel-for-x-in-pip-install
# pip install wheel

# Install modules
python install -r requirements.txt
# to update modules using current venv, use: python -m pip freeze > requirements.txt
