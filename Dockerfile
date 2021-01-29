FROM ubuntu:focal

RUN apt-get update && apt-get install -y exiftool

WORKDIR /opt/unicorn
RUN pip3 install .
