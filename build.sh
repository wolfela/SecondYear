#!/bin/bash

function setup {
  echo "Creating Docker Machine..."
  docker-machine create --driver virtualbox coolbeans-host
  eval "$(docker-machine env coolbeans-host)"
  if [[ "$OSTYPE" == "darwin"* ]]; then
    echo "$(docker-machine ip coolbeans-host) coolbeans.dev" | sudo tee -a /etc/hosts > /dev/null
  else
    echo "$(docker-machine ip coolbeans-host) coolbeans.dev" | sudo tee --append /etc/hosts > /dev/null
  fi
}

function run {
  echo "Starting up docker..."
  docker-compose up -d
}

function setup-db {
  docker-compose run web python ./manage.py migrate
}

function shutdown {
  docker-compose down
}

if [ "$1" == "setup" ]; then
  setup
  run
  setup-db
  shutdown
elif [ "$1" == "run" ]; then
  run
elif [ "$1" == "rebuild" ]; then
  docker-compose build
elif [ "$1" == "shutdown" ]; then
  shutdown
else
  echo './build.sh [setup|run|rebuild|shutdown]'
fi