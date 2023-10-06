# syntax=docker/dockerfile:1

FROM ubuntu:20.04

RUN apt-get update
RUN apt-get install ca-certificates -y
RUN apt-get install -y software-properties-common
RUN apt-get install python3.9 -y
RUN apt-get -y install python3-pip
RUN apt-get install -y curl
RUN apt-get install -y git
RUN apt-get install ffmpeg -y
RUN apt-get clean
RUN apt-get update

WORKDIR /summaryclipper_api/

ADD ./requirements.txt .

RUN python3 -m pip install --upgrade pip
RUN python3 -m pip install --no-cache-dir -r requirements.txt

ADD . .

CMD [ "ddtrace-run" "python3", "main.py"]