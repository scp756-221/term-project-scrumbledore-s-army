# Makefile for Menu service

VER=v1.0

PORT=30001

run-menu:
	cd .. && docker image build -f menu-service/Dockerfile -t menu-service:$(VER) .
	docker container run -p $(PORT):$(PORT) -it --rm --name menu-service menu-service:$(VER)

publish-image:
	cd .. && docker image build -f menu-service/Dockerfile -t menu-service:$(VER) .
	docker tag menu-service:$(VER) ghcr.io/subclassy/menu-service:$(VER)
	docker push ghcr.io/subclassy/menu-service:$(VER)
