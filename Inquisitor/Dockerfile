FROM python:3

RUN apt-get -y update \
	&& pip install scapy \
	&& apt -y install libpcap0.8

WORKDIR /usr/src/app

COPY Inquisitor.py /usr/src/app

CMD ["tail", "-f", "/dev/null"]