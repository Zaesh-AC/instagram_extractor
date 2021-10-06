FROM python:3.7.10-slim-buster

EXPOSE 5000

ADD ./requirements/ /code/requirements/
RUN pip install --upgrade pip && pip install -r /code/requirements/requirements.txt

COPY . /code/
WORKDIR /code/

CMD ["run", "--host=0.0.0.0"]
ENTRYPOINT ["flask"]