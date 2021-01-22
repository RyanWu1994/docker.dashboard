FROM python:3.7

WORKDIR /
COPY ./requirements.txt ./
COPY ./crawler.py ./
RUN pip install --no-cache-dir -r requirements.txt

CMD [ "python", "./crawler.py" ]
