FROM python:3.10-alpine

COPY requirements.txt /opt/openapi-validator/
COPY validator.py lookup.py main.py  /opt/openapi-validator/

RUN pip install -r /opt/openapi-validator/requirements.txt

ENTRYPOINT ["python", "/opt/openapi-validator/main.py"]

