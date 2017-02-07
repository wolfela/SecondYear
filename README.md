# (insert name here) - An interactive language learning system

# Setting up the development environment

1. [Get Docker](https://docs.docker.com/engine/installation/). You'll also need docker-compose and npm.
2. Run `./build.sh setup` and wait for the Docker instance to be set up. You'll need to enter your password during the process. You may have to `chmod +x ./build.sh` as well.
3. Run `./build.sh run` to run the Docker container. The website will be available from `localhost:8000`.
4. If you have PyCharm, you can set up a Remote Interpreter - [instructions are here](https://www.jetbrains.com/help/pycharm/2016.3/configuring-remote-interpreters-via-ssh.html).
Host: localhost:2222
Username: docker
Password: Password
python interpreter path: /usr/local/bin/python
Path mappings: \<your local project folder\> -> /code
