FROM python:3.8-slim

# Install necessary packages
RUN apt-get update && apt-get install -y \
    iproute2 \
    tcpdump \
    gcc \
    libpcap-dev \
    python3-dev \
    && rm -rf /var/lib/apt/lists/*

# Install scapy
RUN pip install scapy

# Copy the inquisitor script
COPY inquisitor /usr/src/inquisitor

# Set the working directory
WORKDIR /usr/src

# Entry point to run the inquisitor script
ENTRYPOINT ["python3", "inquisitor"]
