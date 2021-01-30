
VERSION = $(shell cat unicorn_sort/VERSION)
DOCKER_IMAGE = prosper/unicorn_sort:${VERSION}

build: Dockerfile setup.py unicorn_sort/VERSION
	@docker build \
		-f Dockerfile \
		-t ${DOCKER_IMAGE} \
		--no-cache \
		.
	@touch $@

run: build
	@docker run -it --rm \
		--volume `pwd`:/opt/unicorn \
		${DOCKER_IMAGE} \
		/bin/bash

black: build
	@docker run --rm \
		--volume `pwd`:/opt/unicorn \
		${DOCKER_IMAGE} \
		black -l 100 .
