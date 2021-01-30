FROM ubuntu:focal

RUN apt-get update && apt-get install -y \
	exiftool \
	exempi \
	libnfs-dev \
	python3 \
	python3-pip

COPY . /opt/unicorn
WORKDIR /opt/unicorn

RUN pip3 install .[dev]

WORKDIR /home/docker
