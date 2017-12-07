FROM circleci/python:3.6-jessie

RUN sudo pip install -r requirements.txt

COPY validator.py /opt/
