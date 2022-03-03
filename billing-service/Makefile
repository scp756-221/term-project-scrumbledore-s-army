# Makefile for Billing service

VER=v1.0

PORT=30001

run-billing:
	cd  .. && docker image build -f billing-service/Dockerfile -t billing-service:$(VER) .
	docker container run -p $(PORT):$(PORT) -it --rm --name billing-service billing-service:$(VER)
