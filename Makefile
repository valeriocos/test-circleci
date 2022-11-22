.PHONY: synth colima-start build build-dummy build-rummy test-dummy test-rummy test-stack install-deps

A_STACK_NAME = AStack
synth:
	A_STACK_NAME=$(A_STACK_NAME) cdk synth --no-staging

colima-start:
	colima start --runtime docker --mount $(HOME):w --mount /tmp/colima:w

build-dummy:
	docker-compose build dummy

build-rummy:
	docker-compose build rummy

build: build-dummy build-rummy

test-dummy:
	docker-compose run --rm dummy pytest

test-rummy:
	docker-compose run --rm rummy pytest

test-stack:
	pytest -vs tests

install-deps: build
	docker-compose up
	rm -rf libs
	mkdir libs
	docker-compose down