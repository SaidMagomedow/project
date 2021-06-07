FROM python:3.9

ENV PYTHONUNBUFFERED=1


RUN pip install --upgrade pip\
    asgiref==3.3.4\
    Django==3.2.4\
    pytz==2021.1\
    sqlparse==0.4.1\
    psycopg2-binary

WORKDIR code
COPY . /code