FROM python:3.7-alpine
MAINTAINER szecsenyi

ENV PYTHONUNBUFFERED 1

COPY  ./requirements.txt /requirements.txt
RUN pip install -r /requirements.txt

COPY ./app /app
WORKDIR /app

RUN adduser --uid 1000 -D django
USER django
