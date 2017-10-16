FROM circleci/python:3.6-jessie

RUN sudo pip install openapi-spec-validator ansicolors

COPY validator.py /opt/
