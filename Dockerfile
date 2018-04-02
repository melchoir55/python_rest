FROM python:3.6

ADD . /app

RUN apt-get update
RUN apt-get install -y postgresql postgresql-contrib libpq-dev python3-dev
RUN pip3 install -r /app/requirements.txt
EXPOSE  8080