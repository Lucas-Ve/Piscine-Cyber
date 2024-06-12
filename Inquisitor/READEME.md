# Inquisitor

## Overview

Inquisitor is an ARP poisoning tool designed to intercept and manipulate network traffic between two nodes in a local area network.

## Prerequisites

- Docker
- Docker Compose
- Python 3

## Installation

Clone the repository and navigate to the project directory:
- `git clone <REPOSITORY_URL>`
- `cd Inquisitor`

## Makefile Commands

### Build and Management Commands

- `make build` - Build and start the Docker containers.
- `make run` - Execute the Inquisitor program.
- `make clean` - Stop and remove the Docker containers.
- `make fclean` - Remove all Docker containers, images, volumes, and networks.
- `make server` - Access the FTP server container.
- `make client` - Access the FTP client container.
- `make inquisitor` - Access the Inquisitor container.
- `make show-ip` - Display the IP and MAC addresses of the containers.
- `make info` - Display Docker container information.
- `make prune` - Clean up the Docker environment forcefully.
- `make cp` - Copy the `Inquisitor.py` file into the Inquisitor container.

## Project Structure

- `Inquisitor.py`: The main script that performs ARP poisoning.
- `docker-compose.yaml`: Docker Compose configuration for setting up the necessary containers.
- `Makefile`: Commands to manage the Docker containers and the Inquisitor script.
