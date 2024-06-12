# Utiliser une image de base pour Python
FROM python:3.9-slim

# Installer les dépendances
RUN pip install flask sqlalchemy pymysql

# Copier les fichiers de l'application dans le conteneur
COPY . /app

# Définir le répertoire de travail
WORKDIR /app

# Exposer le port 5000
EXPOSE 5000

# Définir la commande pour démarrer l'application
CMD ["python", "app.py"]
