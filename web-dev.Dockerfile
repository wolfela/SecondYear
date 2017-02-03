FROM python:3.6-alpine
ENV PYTHONUNBUFFERED 1
RUN apk update && apk upgrade && \
    apk add build-base gcc abuild binutils bash mariadb-dev openssh && \
    rm -rf /var/cache/apk/*
RUN touch /var/log/lastlog
RUN rm -rf /etc/ssh/ssh_host_rsa_key /etc/ssh/ssh_host_dsa_key
RUN mkdir /code
ADD requirements.txt /code/
WORKDIR /code
RUN pip install -r requirements.txt
ADD . /code/
RUN mkdir -p /home/docker && echo 'cd /code && export $(cat .env | xargs)' > /home/docker/.profile

ENTRYPOINT ["util/entrypoint-webdev.sh"]