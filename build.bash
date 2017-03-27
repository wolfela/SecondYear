#!/bin/bash

if [ "$(id -u)" != "0" ]; then
	echo "Sorry, you are not root."
	exit 1
fi

find . -name "*.pyc" -exec rm -f {} \;  
sudo npm install
sudo npm install --global gulp
sudo npm rebuild
sudo gulp
sudo pip3 install -r requirements.txt
sudo python3 manage.py makemigrations
sudo python3 manage.py migrate
