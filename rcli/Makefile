# Makefile for Restaurant-Command-Line-Interface

VER=v1.0

BILLING_IP=host.docker.internal
BILLING_PORT=30002
MENU_IP=host.docker.internal
MENU_PORT=30001

run-rcli:
	cd .. && docker image build -f rcli/Dockerfile -t rcli-service:$(VER) .
	docker container run -it --rm --name rcli-service rcli-service:$(VER) $(MENU_IP) $(MENU_PORT) $(BILLING_IP) $(BILLING_PORT)
