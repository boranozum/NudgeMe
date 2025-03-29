ARG PYTHON_VERSION=3.10.13
FROM python:${PYTHON_VERSION} as base

ENV PYTHONDONTWRITEBYTECODE=1

ENV PYTHONUNBUFFERED=1

RUN apt-get update && apt-get install -y vim && apt-get clean

WORKDIR /app

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY entrypoint/* /entrypoint/
RUN chmod -R +x "/entrypoint"