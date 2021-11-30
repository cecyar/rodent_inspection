FROM python:3.9.7-alpine

RUN apk update && apk add python3-dev \
                        gcc \
                        libc-dev \
                        g++ \
                        postgresql-dev \
                        musl-dev

WORKDIR /app

COPY requirements.txt .

RUN pip install -r requirements.txt

EXPOSE 5000

COPY . .

