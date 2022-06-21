FROM python:3.9

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ARG WM_VERSION=v2021.03.01.00

RUN apt-get update

WORKDIR /helpcenter

COPY Pipfile Pipfile.lock /helpcenter/
RUN pip install --upgrade pip
RUN pip install pipenv && pipenv install --system

COPY . /helpcenter/