# Base python package
FROM python:3.9.6-slim-buster

RUN apt-get -y update
RUN apt-get -y install git

# Copy the dependencies
COPY requirements.txt /app/requirements.txt

# Working directory
WORKDIR /app

# Install the dependencies
RUN pip install -r requirements.txt

COPY . /app

# Executable commands
CMD git clone https://github.com/juanrafael/fullstack-interview-test.git repo && flask run --host=0.0.0.0 --port=4040