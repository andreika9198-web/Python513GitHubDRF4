FROM python:3

WORKDIR /code
COPY ./requirements_docker.txt /code/
RUN pip install -r requirements_docker.txt

COPY . .