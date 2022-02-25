FROM python:3.7

RUN mkdir /menu-image 

COPY . /menu-image/

WORKDIR /menu-image

RUN pip install -r requirements.txt

EXPOSE 3001

CMD ["python","app.py","3001"] 


