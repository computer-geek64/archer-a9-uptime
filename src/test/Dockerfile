# Dockerfile

FROM archer-a9-uptime:latest

RUN apt-get update --fix-missing
RUN apt-get install -y iproute2

RUN pip install --upgrade pytest

ENTRYPOINT ["pytest"]
CMD ["test"]
