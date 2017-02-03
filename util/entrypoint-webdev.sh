#!/bin/sh


if [ ! -f "/etc/ssh/ssh_host_rsa_key" ]; then
    # generate fresh rsa key
    ssh-keygen -f /etc/ssh/ssh_host_rsa_key -N '' -t rsa
fi
if [ ! -f "/etc/ssh/ssh_host_dsa_key" ]; then
    # generate fresh dsa key
    ssh-keygen -f /etc/ssh/ssh_host_dsa_key -N '' -t dsa
fi

#prepare run dir
if [ ! -d "/var/run/sshd" ]; then
  mkdir -p /var/run/sshd
fi

adduser -D docker -s /bin/bash && echo "docker:password" | chpasswd
chown -R docker:docker /code
chown -R docker:docker /static
chown -R docker:docker /home/docker
echo 'cd /code && export $(cat .env | xargs)' > /home/docker/.profile

echo "Starting ssh..."
/usr/sbin/sshd -D
python /code/manage.py runserver 0.0.0.0:8000