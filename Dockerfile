FROM ubuntu:bionic-20191029
MAINTAINER szecsenyi

# install python
RUN apt-get update && apt-get install -y python3.6 python3-venv python3-pip
RUN python3.6 -m venv /python
ENV PATH /python/bin:$PATH
ENV PYTHONPATH /app
ENV PYTHONUNBUFFERED 1

# pip install
RUN pip3 install --no-cache-dir  Django==2.1.3
RUN pip3 install --no-cache-dir  djangorestframework==3.9.0
RUN pip3 install --no-cache-dir  psycopg2-binary==2.8.4
# django-admin miatt kell ez:
ENV DJANGO_SETTINGS_MODULE app.settings

COPY ./app /app
WORKDIR /app
RUN groupadd -r django --gid=8000 && useradd -r -m -g django --uid=8000 django
USER django
