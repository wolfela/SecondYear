FROM python:3.6-alpine
ENV PYTHONUNBUFFERED 1

RUN apk update \
      && apk upgrade \
      && apk add build-base gcc abuild binutils bash mariadb-dev openssh sudo \
      && rm -rf /var/cache/apk/*

RUN adduser -s /bin/bash -D docker -h /home/docker \
      && echo "docker:password" | chpasswd \
      && echo "docker ALL=(ALL) NOPASSWD:ALL" >> /etc/sudoers \
      && mkdir /code /static \
      && chown -R docker:docker /code /static /home/docker \
      && echo 'cd /code && export $(cat .env | xargs)' >> /home/docker/.profile

RUN rm -rf /etc/ssh/ssh_host_rsa_key /etc/ssh/ssh_host_dsa_key \
      && ssh-keygen -f /etc/ssh/ssh_host_rsa_key -N '' -t rsa \
      && ssh-keygen -f /etc/ssh/ssh_host_dsa_key -N '' -t dsa \
      && ssh-keygen -f /etc/ssh/ssh_host_ecdsa_key -N '' -t ecdsa \
      && ssh-keygen -f /etc/ssh/ssh_host_ed25519_key -N '' -t ed25519

ADD requirements.txt /code/
WORKDIR /code
RUN pip install -r requirements.txt
ADD . /code/

ENTRYPOINT ["util/entrypoint-webdev.sh"]
