.PHONY: all build run fclean clean server client inquisitor show-ip info

all: build

# Définir les noms des conteneurs
TARGET := inquisitor
SERVER_CONTAINER := ftpserver
CLIENT_CONTAINER := ftpclient
NAME := Inquisitor.py

build:
	docker-compose up --build
	@echo "Waiting for containers to start..."
	@sleep 5

clean:
	docker-compose down

fclean: clean
	-docker stop $(shell docker ps -qa) 2>/dev/null
	-docker rm $(shell docker ps -qa) 2>/dev/null
	-docker rmi -f $(shell docker images -qa) 2>/dev/null
	-docker volume rm $(shell docker volume ls -q) 2>/dev/null
	-docker network rm $(shell docker network ls -q) 2>/dev/null

# Utiliser la commande shell pour obtenir les adresses IP et MAC des conteneurs serveur et client
IP_SRC := $(shell docker inspect --format='{{range .NetworkSettings.Networks}}{{.IPAddress}}{{end}}' $(SERVER_CONTAINER))
IP_TARGET := $(shell docker inspect --format='{{range .NetworkSettings.Networks}}{{.IPAddress}}{{end}}' $(CLIENT_CONTAINER))
MAC_SRC := $(shell docker inspect --format='{{range .NetworkSettings.Networks}}{{.MacAddress}}{{end}}' $(SERVER_CONTAINER))
MAC_TARGET := $(shell docker inspect --format='{{range .NetworkSettings.Networks}}{{.MacAddress}}{{end}}' $(CLIENT_CONTAINER))

run:
	@echo "Running Inquisitor:"
	@echo ./$(NAME) $(IP_SRC) $(MAC_SRC) $(IP_TARGET) $(MAC_TARGET)

show-ip:
	@echo "L'adresse IP du serveur FTP est : $(IP_SRC)"
	@echo "L'adresse IP du client FTP est : $(IP_TARGET)"
	@echo "L'adresse MAC du serveur FTP est : $(MAC_SRC)"
	@echo "L'adresse MAC du client FTP est : $(MAC_TARGET)"

server:
	docker exec -it ftpserver /bin/sh

client:
	docker exec -it ftpclient /bin/sh

inquisitor:
	docker exec -it inquisitor /bin/bash

info	:
	@printf "[docker informations]\n"

	@echo $(CYAN)$(SERVER_CONTAINER)$(RESET)
	@printf " - IPAddress	: "
	@docker inspect --format='{{range .NetworkSettings.Networks}}{{.IPAddress}}{{end}}' $(SERVER_CONTAINER)
	@printf " - MacAddress	: "
	@docker inspect --format='{{range .NetworkSettings.Networks}}{{.MacAddress}}{{end}}' $(SERVER_CONTAINER)

	@echo $(CYAN)$(CLIENT_CONTAINER)$(RESET)
	@printf " - IPAddress	: "
	@docker inspect --format='{{range .NetworkSettings.Networks}}{{.IPAddress}}{{end}}' $(CLIENT_CONTAINER)
	@printf " - MacAddress	: "
	@docker inspect --format='{{range .NetworkSettings.Networks}}{{.MacAddress}}{{end}}' $(CLIENT_CONTAINER)

	@echo $(CYAN)$(TARGET)$(RESET)
	@printf " - IPAddress	: "
	@docker inspect --format='{{range .NetworkSettings.Networks}}{{.IPAddress}}{{end}}' $(TARGET)
	@printf " - MacAddress	: "
	@docker inspect --format='{{range .NetworkSettings.Networks}}{{.MacAddress}}{{end}}' $(TARGET)

cp	:
	docker cp Inquisitor.py $(TARGET):/usr/src/app