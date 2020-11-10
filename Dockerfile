FROM 644152709166.dkr.ecr.eu-west-1.amazonaws.com/usabilla/dev/dockerhub-mirror/python:3.6-alpine

COPY requirements.txt /opt/openapi-validator/
COPY validator.py /opt/openapi-validator/

RUN pip install -r /opt/openapi-validator/requirements.txt

ENTRYPOINT ["python", "/opt/openapi-validator/validator.py"]

