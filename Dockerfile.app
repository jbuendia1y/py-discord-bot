FROM python:3.8-alpine

WORKDIR /app

COPY ./app /app

RUN apk update

RUN pip3 install pipenv

RUN pipenv shell
RUN pipenv install
RUN pipenv run start