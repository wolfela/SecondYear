#!/bin/bash

function setup {
  echo "Creating Docker Machine..."
  cp .env.example .env
  echo "Please change the value of SECRET_KEY in .env to a random string, then press Enter to continue."
  read _DUMMY_
}

function run {
  echo "Starting up docker... this may take a while."
  docker-compose up -d
}

function make-shell {
  docker-compose exec web /bin/bash
}

function migrate-db {
  echo "Migrating database..."
  docker-compose exec web python ./manage.py migrate
}

function reinstall-deps {
  echo "Reinstalling dependencies..."
}

function shutdown {
  docker-compose stop
}

function install-node-modules {
  echo "Installing node modules..."
  npm install
}

function install-python-deps {
  echo "Installing Python dependencies..."
  docker-compose exec web pip install -r requirements.txt
}

if [ "$1" == "setup" ]; then
  setup
  run
  migrate-db
  shutdown
  install-node-modules

  echo 'Setup is now complete.'
  echo 'To compile scss and javascript files, run `gulp watch`.'
elif [ "$1" == "run" ]; then
  run
elif [ "$1" == "rebuild" ]; then
  docker-compose build
elif [ "$1" == "reinstall-deps" ]; then
  install-python-deps
  install-node-modules
elif [ "$1" == "migrate" ]; then
  migrate-db
elif [ "$1" == "make-shell" ]; then
  make-shell
elif [ "$1" == "shutdown" ]; then
  shutdown
else
  echo './build.sh [setup|run|rebuild|shutdown]'
fi