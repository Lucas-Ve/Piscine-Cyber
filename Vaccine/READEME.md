# Vaccine: SQL Injection Detection Tool

## Description
Vaccine est un outil en ligne de commande conçu pour tester les sites web pour les vulnérabilités d'injection SQL. Il permet de vérifier en toute sécurité les failles courantes d'injection SQL en fournissant une URL cible. Vaccine prend en charge diverses méthodes de test et peut identifier les configurations spécifiques de base de données susceptibles d'être vulnérables.

## Fonctionnalités
- **Test d'injection SQL** : Prend en charge plusieurs techniques d'injection, y compris Union, Error, Boolean, Time, et Blind.
- **Compatibilité des moteurs de base de données** : Compatible avec les principaux moteurs de base de données tels qu'Oracle, MySQL, SQLite, et Microsoft SQL Server.
- **Méthodes HTTP flexibles** : Permet des tests utilisant les méthodes HTTP GET et POST.

## Installation
Clonez le dépôt sur votre machine locale :

git clone [url-du-depot]

Accédez au répertoire cloné :

cd [nom-du-repertoire]

## Utilisation
Exécutez l'outil en utilisant :

./vaccine [-o <fichier_de_sortie>] [-X <methode_HTTP>] URL

### Paramètres
- `URL` : L'URL du site web cible à tester pour l'injection SQL.
- `-o` : Optionnel. Spécifie le fichier de sortie pour stocker les résultats. Par défaut, 'default_archive'.
- `-X` : Optionnel. Spécifie la méthode HTTP à utiliser (GET ou POST). Par défaut, GET.

## Exemple
Pour tester un site web en utilisant la méthode POST et enregistrer les résultats dans 'results.txt' :

./vaccine -o results.txt -X POST http://example.com


## Sortie
L'outil fournit :
- Les paramètres vulnérables détectés.
- Les payloads utilisés pour les tests.
- Les noms des bases de données, tables et colonnes potentiellement accessibles.
- Un dump complet de la base de données si les vulnérabilités le permettent.
