#!/usr/bin/env bash

#Script to run To-do app using the bash script

#Step1: Download package from the repository  
sudo apt-get update -y

#Step2: Install PyEnv Requisites using apt get
sudo apt-get install -y git

#Step3: Installs pip Python3 Version 
sudo apt-get install python3-pip

#Step4: Copy poetry installation file to local 
curl -sSL https://raw.githubusercontent.com/python-poetry/ \
poetry/master/get-poetry.py | python

#Step5: Clone repository of To-Do App code from GIT
git clone https://github.com/sunnygunjesh/DevOps-Course-Starter.git

#Step6:Install poetry
poetry install 

#Step7: Copy required environment key/token for the app to run
cp .env.template .env
