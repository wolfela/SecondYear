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

function setup-db {
  echo "Migrating database..."
  docker-compose exec web python ./manage.py migrate
}

function shutdown {
  docker-compose stop
}

function install-node-modules {
  echo "Installing node modules..."
  npm install
}

if [ "$1" == "setup" ]; then
  setup
  run
  setup-db
  shutdown
  install-node-modules

  echo 'Setup is now complete.'
  echo 'To compile scss and javascript files, run `gulp watch`.'
elif [ "$1" == "run" ]; then
  run
elif [ "$1" == "rebuild" ]; then
  docker-compose build
elif [ "$1" == "shutdown" ]; then
  shutdown
else
  echo './build.sh [setup|run|rebuild|shutdown]'
fi