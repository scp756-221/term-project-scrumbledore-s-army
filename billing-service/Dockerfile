FROM python:3.7

RUN mkdir /billing-image
RUN mkdir /billing-image/db

COPY ./billing-service /billing-image/
COPY ./db /billing-image/db
COPY requirements.txt /billing-image/

WORKDIR /billing-image

RUN pip install -r requirements.txt

EXPOSE 30001

CMD ["python", "app.py", "30001"]
