FROM python:3.7

RUN mkdir /menu-image 
RUN mkdir /menu-image/db

COPY ./menu-service /menu-image/
COPY ./db /menu-image/db
COPY requirements.txt /menu-image/

WORKDIR /menu-image

RUN pip install -r requirements.txt

EXPOSE 30001

CMD ["python", "app.py", "30001"]


