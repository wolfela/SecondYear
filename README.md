LQ - An Interactive Language Learning System

Dependencies:

Please make sure you have all of these installed before running the application: (We recommend using this on Ubuntu 14.04+ however any Linux should work as long as you can install these)

-   python3
-   mysql-server and mariadb
-   libmysqlclient-dev
-   python3-setuptools 
-   python3-dev 
-   pip3 and easy_install
-   Your Distributions Version of build-essential
-   npm

If using ubuntu, please make a symbolic link between nodejs and node:

ln -s /usr/bin/nodejs /usr/bin/node

Deployment:

First you need to install MySql and save the root password. Then you need to create a new database named "coolbeans" (use this tutorial if unsure how https://www.digitalocean.com/community/tutorials/a-basic-mysql-tutorial). Set the root password in coolbeans/settings.py under the line 'PASSWORD' in the DATABASES section. We recommend using root / root for the purposes of this project.

Once this is set, you need to run build.bash using sudo or root. If it completes with no problems, you can then run:

python3 manage.py runserver

This will turn the server on under localhost:8000. If you wish to set a different URL, run it with python3 manage.py runserver 0.0.0.0:8000 and configure your webserver to redirect to port 8000 under the URL you wish.

