FROM python:3.6-stretch

MAINTAINER tylercreardon@gmail.com

USER root

WORKDIR /app

ADD . /app

RUN pip install --trusted-host pypi.python.org -r requirements.txt

EXPOSE 80

ENV NAME searchTools

CMD ["python", "main.py"]