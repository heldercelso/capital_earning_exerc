# command to build:
# - docker build . -t capital_earning
# or use the docker-compose.yml with the build parameter
FROM python:3.7.6-alpine

# defining the working directory which will receive the web_project files
WORKDIR /code

# creating virtual environment and adding to path
ENV VIRTUAL_ENV=/venv
RUN python -m venv $VIRTUAL_ENV
ENV PATH="$VIRTUAL_ENV/bin:$PATH"

RUN pip install --upgrade pip

# some features needed to install requirements.txt on the alpine linux:
#RUN apk --update add postgresql-dev gcc musl-dev python3-dev libffi-dev openssl-dev cargo libxml2-dev libxslt-dev bash

# avoid pyc files
ENV PYTHONDONTWRITEBYTECODE 1

# python output is sent straight to terminal (container log) without being buffered
# so the output of the application (django logs) can be seen in real time.
ENV PYTHONUNBUFFERED 1

# copy the whole project into /code and installing the requirements
COPY . .
RUN pip install -r requirements.txt