# Makefile for Booking service

VER=v1.0

PORT=30003

run-booking:
	cd .. && docker image build -f booking-service/Dockerfile -t booking-service:$(VER) .
	docker container run -p $(PORT):$(PORT) -it --rm --name booking-service booking-service:$(VER)
