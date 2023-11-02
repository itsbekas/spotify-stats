FROM python:3.11-alpine

WORKDIR /app

COPY . /app

COPY ./.env /app/.env

RUN pip install -r requirements.txt

RUN pip install .