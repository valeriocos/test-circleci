.PHONY: synth colima-start build build-dummy build-list-user-instruments test-dummy test-list-user-instruments test-stack install-deps refresh-codeartifact-token

A_STACK_NAME = AStack
synth:
	A_STACK_NAME=$(A_STACK_NAME) cdk synth --no-staging

colima-start:
	colima start --runtime docker --mount $(HOME):w --mount /tmp/colima:w


build-dummy:
	docker-compose build dummy

build: build-dummy

test-dummy:
	docker-compose run --rm dummy pytest

test-stack:
	pytest -vs tests

install-deps: build
	docker-compose up
	rm -rf libs
	mkdir libs
	docker-compose down