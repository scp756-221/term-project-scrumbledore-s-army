FROM python:3.8-slim-buster

RUN mkdir /billing-image
RUN mkdir /billing-image/db

COPY ./billing-service /billing-image/
COPY ./db /billing-image/db
COPY requirements.txt /billing-image/

WORKDIR /billing-image

RUN pip install -r requirements.txt

EXPOSE 30002

CMD ["python", "app.py", "30002"]
