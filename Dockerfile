FROM python:3.6-alpine
ENV PYTHONUNBUFFERED 1
RUN apk update && apk add build-base gcc abuild binutils zsh mariadb-dev
RUN mkdir /code
ADD requirements.txt /code/
WORKDIR /code
RUN pip install -r requirements.txt
ADD . /code/
