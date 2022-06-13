FROM python:3.9-slim

WORKDIR /app

COPY ./req.txt /app/req.txt

RUN apt-get update \
    && apt-get install gcc -y \
    && apt-get install libpq-dev -y \
    && apt-get clean

RUN pip install -r /app/req.txt \
    && rm -rf /root/.cache/pip

COPY . /app/