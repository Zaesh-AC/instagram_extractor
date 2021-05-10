FROM python:3.7.10-slim-buster

ADD ./requirements/ /code/requirements/
RUN pip install --upgrade pip && pip install -r /code/requirements/requirements.txt

COPY . /code/
WORKDIR /code/

CMD ["instagram_data_extractor.py"]
ENTRYPOINT ["python"]