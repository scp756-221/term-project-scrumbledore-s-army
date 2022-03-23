FROM python:3.8-slim-buster

RUN mkdir /rcli-image

COPY ./rcli /rcli-image/
COPY requirements.txt /rcli-image/

WORKDIR /rcli-image

RUN pip install -r requirements.txt

ENTRYPOINT ["python", "rcli.py"]

CMD [ "0.0.0.0", "30001", "0.0.0.0", "30002", "0.0.0.0", "30003"]
