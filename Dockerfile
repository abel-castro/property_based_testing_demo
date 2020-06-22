FROM python:3.7-slim

COPY ./requirements.txt /requirements.txt

RUN pip install --upgrade pip && pip install --no-cache-dir  -r requirements.txt

COPY ./app/ /app/

WORKDIR /app
