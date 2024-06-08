 FROM ubuntu:latest

RUN apt-get update && apt-get install -y zsh

WORKDIR /app
COPY requirements.txt /tmp/requirements.txt

RUN apt-get install -y $(cat /tmp/requirements.txt)

SHELL ["/usr/bin/zsh"]

CMD ["/bin/zsh"]