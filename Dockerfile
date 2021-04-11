FROM python:3.8.2-slim-buster

RUN apt-get update && apt-get install -y git build-essential && apt-get clean
RUN pip install sqlalchemy pytest flake8 black

WORKDIR /app