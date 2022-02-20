FROM python:3.7

RUN mkdir /rcli

COPY . /rcli/

WORKDIR /rcli

RUN pip install -r requirements.txt

CMD ["python", "rcli.py","3000", "2200", "1200", "1112"]
