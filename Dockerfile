# Dockerfile

FROM python:3.10

RUN apt-get update
RUN apt-get install -y firefox-esr iputils-ping

WORKDIR /code
RUN wget -q https://github.com/mozilla/geckodriver/releases/download/v0.30.0/geckodriver-v0.30.0-linux64.tar.gz
RUN tar -xzf geckodriver-v0.30.0-linux64.tar.gz -C /usr/local/bin
RUN rm geckodriver-v0.30.0-linux64.tar.gz

RUN pip install --upgrade pip
COPY requirements.txt .
RUN pip install -r requirements.txt

COPY src .

ARG router_password
ENV ROUTER_PASSWORD="${router_password}"

ENTRYPOINT ["./monitor.py"]
