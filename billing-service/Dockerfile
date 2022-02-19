FROM python:3.7

RUN mkdir /billing-image

COPY . /billing-image/

WORKDIR /billing-image

RUN pip install -r requirements.txt

EXPOSE 3000

CMD ["python", "app.py", "3000"]
