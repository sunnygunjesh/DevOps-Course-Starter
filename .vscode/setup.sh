#! /usr/bin/env bash

#Activate Python
python -i

#Install PIP
python -m pip --version
curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py

#Install Poetry
echo 'poetry --version' poetry --version

curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | python -

poetry install

echo 'poetry --version' poetry --version

#Clone the repository
git clone https://github.com/sunnygunjesh/DevOps-Course-Starter.git

#Setup environment parameters
cp .env.template .env 

#Run the app
poetry run flask run

#Exit python 
exit()