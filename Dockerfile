FROM python:3.7
WORKDIR /app
COPY . /app
ENTRYPOINT chmod +x ./init.sh; ./init.sh; /bin/bash
