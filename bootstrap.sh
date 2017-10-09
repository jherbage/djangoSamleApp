#!/usr/bin/env bash

sudo apt-get update
sudo apt-get install -y git
sudo apt-get install -y python
git clone https://github.com/jherbage/djangoSamleApp.git
sudo apt-get install -y python-pip
sudo pip install django
# This is horrible but without the sleep the runserver just does not happen
nohup ./djangoSamleApp/djangoSampleApp/manage.py runserver 0.0.0.0:8080 & sleep 1
