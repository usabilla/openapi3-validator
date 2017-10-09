FROM circleci/python:3.6-jessie

RUN sudo pip install openapi-spec-validator

COPY validator.py /opt/
