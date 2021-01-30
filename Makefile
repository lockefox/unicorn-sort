
VERSION = $(shell cat unicorn_sort/VERSION)
DOCKER_IMAGE = prosper/unicorn_sort:${VERSION}
HOMEDIR = /home/prosper/unicorn

build: Dockerfile setup.py unicorn_sort/VERSION
	@docker build \
		--build-arg PROJECT_HOMEDIR=${HOMEDIR} \
		-f Dockerfile \
		-t ${DOCKER_IMAGE} \
		--no-cache \
		.
	@touch $@

.PHONY: run
run: build
	@docker run -it --rm \
		--volume `pwd`:${HOMEDIR} \
		${DOCKER_IMAGE} \
		/bin/bash

.PHONY: black
black: build
	@docker run --rm \
		--volume `pwd`:${HOMEDIR} \
		${DOCKER_IMAGE} \
		black -l 100 .
