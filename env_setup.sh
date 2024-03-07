#!/bin/bash

# https://stackoverflow.com/questions/70422866/how-to-create-a-venv-with-a-different-python-version

# grab python3.9
sudo apt install python3.9-venv

# a useful directory to organize virtual envs
mkdir ~/.venvs

# create new venv && activate
python3.9 -m venv ~/.venvs/quantum
source ~/.venvs/quantum/bin/activate

# useful package to prevent package install errors, particulary:
# AttributeError: module 'platform' has no attribute 'linux_distribution'
# https://stackoverflow.com/questions/53204916/what-is-the-meaning-of-failed-building-wheel-for-x-in-pip-install
pip install wheel

# install all necessary packages
pip install qiskit qiskit[visualization] qiskit-aer qiskit-ibm-provider matplotlib --no-cache-dir

