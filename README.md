# (insert name here) - An interactive language learning system

# Setting up the development environment

1. [Get Docker.](https://docs.docker.com/engine/installation/). If you're on Windows, use Cygwin for the rest of the steps, and pray.
2. Run `./build.sh setup` and wait for the Docker instance to be set up. You'll need to enter your password during the process. You may have to `chmod +x ./build.sh` as well.
3. Run `./build.sh run` to run the Docker container. The website will be available from `coolbeans.dev`.
3. If you have PyCharm, you can set up a Remote Interpreter - [instructions are here](https://www.jetbrains.com/help/pycharm/2016.3/configuring-remote-interpreters-via-docker-compose.html?search=docker-compose). If the default IP doesn't work, find the IP by running `docker-machine ip coolbeans-host`.

TODO: Grunt and other things