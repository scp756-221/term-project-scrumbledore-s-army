# Makefile for Menu service

VER=v1.0

PORT=3001

run-menu:
	docker image build -f Dockerfile -t menu-service:$(VER) .
	docker container run -p $(PORT):$(PORT) -it --rm --name menu-service menu-service:$(VER)
