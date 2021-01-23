FROM python:3.7

WORKDIR /
COPY ./requirements.txt ./
COPY ./api.py ./
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

CMD [ "python", "./api.py" ]