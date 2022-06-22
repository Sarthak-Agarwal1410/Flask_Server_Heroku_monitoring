FROM python:3.7.2
RUN pip3 install flask

RUN mkdir assign
WORKDIR /assign

COPY app.py .

RUN export FLASK_RUN_PORT=8000
RUN python3 app.py &
