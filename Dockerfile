FROM python:3-alpine

WORKDIR /geizhals

COPY ./ /geizhals

RUN pip3 install -r requirements.txt

ENTRYPOINT ["python3", "geizhals.py"]
