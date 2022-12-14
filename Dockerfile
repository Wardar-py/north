FROM python:3.9

WORKDIR /app

COPY ./src /app
COPY requirements.txt /app/requirements.txt


RUN pip3 install -r /app/requirements.txt
