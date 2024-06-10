.PHONY: build run show-ip

# Définir les noms des conteneurs
SERVER_CONTAINER := ftpserver
CLIENT_CONTAINER := ftpclient

# Utiliser la commande shell pour obtenir les adresses IP des conteneurs serveur et client
IP_SRC := $(shell docker inspect --format='{{range .NetworkSettings.Networks}}{{.IPAddress}}{{end}}' $(SERVER_CONTAINER))
IP_TARGET := $(shell docker inspect --format='{{range .NetworkSettings.Networks}}{{.IPAddress}}{{end}}' $(CLIENT_CONTAINER))

# Définir les adresses MAC pour les tests (à adapter selon votre réseau)
MAC_SRC := $(shell docker inspect --format='{{range .NetworkSettings.Networks}}{{.MacAddress}}{{end}}' $(SERVER_CONTAINER))
MAC_TARGET := $(shell docker inspect --format='{{range .NetworkSettings.Networks}}{{.MacAddress}}{{end}}' $(SERVCLIENT_CONTAINERER))

build:
	docker-compose build

run: build
	docker-compose up -d
	docker-compose run --rm inquisitor $(IP_SRC) $(MAC_SRC) $(IP_TARGET) $(MAC_TARGET)

