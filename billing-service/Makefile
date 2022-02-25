# Makefile for Billing service

VER=v1.0

PORT=3000

run-billing:
	docker image build -f Dockerfile -t billing-service:$(VER) .
	docker container run -p $(PORT):$(PORT) -it --rm --name billing-service billing-service:$(VER)
