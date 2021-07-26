# FROM python:3.7.10-slim-buster
FROM debian:buster-slim

ADD ./requirements/ /code/requirements/
RUN apt update && apt upgrade -y && apt install python3-venv python3-pip -y
RUN pip3 install --upgrade pip && pip3 install -r /code/requirements/requirements.txt

COPY . /code/
WORKDIR /code/

ENV FLASK_APP=app.py

CMD ["run", "--host=0.0.0.0"]
ENTRYPOINT ["flask"]