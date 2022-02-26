FROM python:3.7

RUN mkdir /mcli-image

COPY . /mcli-image/

WORKDIR /mcli-image

RUN pip install -r requirements.txt

COPY rcli.py .

ENTRYPOINT ["python", "rcli.py"]

CMD [ "0.0.0.0", "3001", "0.0.0.0", "3000"]
