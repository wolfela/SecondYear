#!/bin/sh

echo "Starting ssh..."
/usr/sbin/sshd

echo "Starting Django..."
python /code/manage.py runserver 0.0.0.0:8000