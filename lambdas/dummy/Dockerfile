FROM python:3.8-slim

WORKDIR /app
RUN mkdir coverage

COPY requirements*.txt .

RUN pip install -r requirements-dev.txt
RUN pip install -r requirements-dev.txt -t /libs/

COPY . .
