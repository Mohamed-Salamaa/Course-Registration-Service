#!/bin/bash
set -e

sudo apt install -y postgresql-client
sudo apt-get install -y python3.9 python3.9-dev python3.9-venv python3-pip
sudo pip3 install --upgrade virtualenv 


# get parent dir
home="$( cd "$( dirname "${BASH_SOURCE[0]}" )"/../ && pwd )/proj_course"


# installs project dependencies
# delete Python virtual environment and recreate it
rm -rf $home/env
# Do something under GNU/Linux platform
virtualenv --python=python3.9 $home/env
echo "export PYTHONPATH='$home'" >> $home/env/bin/activate
# enter the venv and install dependencies
source $home/env/bin/activate

pip install -r $home/requirements.txt

