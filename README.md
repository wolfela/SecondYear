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

# Using build.sh

The following commands are exposed in `build.sh`:

    * `setup` - sets up Docker, install npm dependencies and migrate the database.
    * `run` - Runs Docker.
    * `rebuild` - Rebuild the Docker containers - this will wipe your database as well!
    * `reinstall-deps` - Reinstalls Python and npm dependencies.
    * `shutdown` - Shuts down the Docker instances.

# Using gulp

Gulp is an automated build system which can help you with compiling SCSS and JavaScript into a single file ready for production.

    * `gulp` will compile the SCSS and JavaScript and put them in the right directory.
    * `gulp --production` does the above, but with production settings (i.e. all files minified)
    * `gulp watch` will watch for changes in the source files, and recompiles them if necessary.