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

  cp .env.example .env
  echo "Please change the value of SECRET_KEY in .env, then press any key to continue."
  read _DUMMY_
}

function run {
  echo "Starting up docker..."
  docker-machine start coolbeans-host
  eval "$(docker-machine env coolbeans-host)"
  docker-compose up -d
}

function setup-db {
  eval "$(docker-machine env coolbeans-host)"
  docker-compose run web python ./manage.py migrate
}

function shutdown {
  eval "$(docker-machine env coolbeans-host)"
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

  echo 'Gulp setup is now complete. To compile scss and javascript files, run `gulp watch`.'
  echo 'Docker setup complete. IMPORTANT: If you ever want to run docker commands, run `eval "$(docker-machine env coolbeans-host)"` before you do so!'
  echo 'This will put you in the correct context.'
elif [ "$1" == "run" ]; then
  run
elif [ "$1" == "rebuild" ]; then
  docker-compose build
elif [ "$1" == "shutdown" ]; then
  shutdown
else
  echo './build.sh [setup|run|rebuild|shutdown]'
fi