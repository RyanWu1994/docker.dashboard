FROM python:3.8.7

WORKDIR /

COPY ./init.py /

RUN pip3 install mysql-connector-python

CMD ["python3", "init.py"]
