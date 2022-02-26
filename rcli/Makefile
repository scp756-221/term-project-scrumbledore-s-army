# Makefile for Restaurant-Command-Line-Interface

VER=v1.0

BILLING_IP=0.0.0.0
BILLING_PORT=3001
MENU_IP=0.0.0.0
MENU_PORT=3000

run-rcli:
	docker image build -f Dockerfile -t rcli-service:$(VER) .
	docker container run -it --rm --name rcli-service rcli-service:$(VER) $(BILLING_IP) $(BILLING_PORT) $(MENU_IP) $(MENU_PORT)
