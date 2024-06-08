# Utiliser une image de base avec nginx et tor
FROM debian:latest

# Définir les variables d'environnement pour les mots de passe
ARG ROOT_PASSWORD
ARG USER_PASSWORD

# Installer les paquets nécessaires
RUN apt-get update && apt-get install -y \
    nginx \
    tor \
    openssh-server \
    && rm -rf /var/lib/apt/lists/*

# Créer les répertoires nécessaires
RUN mkdir -p /var/lib/tor/hidden_service /var/log/tor

# Copier les fichiers de configuration
COPY nginx.conf /etc/nginx/nginx.conf
COPY index.html /var/www/html/index.html
COPY torrc /etc/tor/torrc

# Ajouter l'utilisateur et définir son mot de passe
RUN useradd -rm -d /home/lveloso -s /bin/bash lveloso && \
    echo "lveloso:${USER_PASSWORD}" | chpasswd

COPY sshd_config /etc/ssh/sshd_config

# Configurer SSH pour l'utilisateur non-root
RUN mkdir /home/lveloso/.ssh && \
    chmod 700 /home/lveloso/.ssh

COPY id_rsa.pub /home/lveloso/.ssh/authorized_keys

RUN chown lveloso:lveloso -R /home/lveloso/.ssh && \
    chmod 600 /home/lveloso/.ssh/authorized_keys

# Changer les permissions des répertoires Tor
RUN chown -R debian-tor:debian-tor /var/lib/tor /var/log/tor
RUN chmod 700 /var/lib/tor/hidden_service

# Redémarrer le service SSH pour prendre en compte les modifications
RUN service ssh restart

# Exposer les ports nécessaires
EXPOSE 8080
EXPOSE 4343

# Démarrer les services lors de l'exécution du conteneur
CMD service tor start && service ssh start && nginx -g 'daemon off;'
