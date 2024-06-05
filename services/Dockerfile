FROM python:3.11-slim

COPY ./app ./apart_cost_app
WORKDIR /apart_cost_app
COPY requirements.txt .

COPY ./models /models

RUN pip3 install -r requirements.txt

EXPOSE 8081

VOLUME /models

CMD uvicorn apart_cost_app:app --reload --port 8081 --host 0.0.0.0
