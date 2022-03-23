FROM python:3.8-slim-buster

RUN mkdir /booking-image
RUN mkdir /booking-image/db

COPY ./booking-service /booking-image/
COPY ./db /booking-image/db
COPY requirements.txt /booking-image/

WORKDIR /booking-image

RUN pip install -r requirements.txt

EXPOSE 30003

CMD ["python", "app.py", "30003"]
