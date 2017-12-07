FROM circleci/python:3.6-jessie

COPY requirements.txt /opt/
COPY validator.py /opt/

RUN sudo pip install -r /opt/requirements.txt

