# TP-CI_CD_2025_2026

## Informations Générales

Ce repository contient l'ensemble des Travaux Pratiques (TP) effectués. Vous trouverez, ci-dessous, le détail des tâches.

## TP-Docker

### Prérequis

- Installer Docker sur le site officiel (adapté à votre système d'exploitation): [https://docs.docker.com/get-docker/](https://docs.docker.com/get-docker/)
- Télécharger Docker Desktop ou Docker Engine
- Vérifier l'installation via la commande `docker --version`

### Exercice 1 : Manipulation de base de conteneurs

Vous trouverez, ci-dessous, les étapes de manipulation de base de conteneurs.

![TP Docker Capture Base 1](img\TP_Docker-base_1.png?raw=true "TP Docker Capture Base 1")

![TP Docker Capture Base 2](img\TP_Docker-base_2.png?raw=true "TP Docker Capture Base 2")

### Exercice 2 : Création d'un serveur web avec Docker

Vous trouverez, ci-dessous, les étapes de création d'un serveur web.

![TP Docker Capture Serveur Web](img\TP_Docker-serveur_web.png?raw=true "TP Docker Capture Serveur Web")

### Exercice 3 : Déploiement d'une application Python Flask

**Objectif** : Créer et lancer une application web simple avec Flask à l’aide de Docker.

**Etapes**:

1. Déplacer-vous dans TP-Docker : `cd TP-Docker`
2. Créer le fichier `app.py` contenant l'application Flask suivante:

```python
from flask import Flask

# Création de l'application
app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

if __name__ == "__main__":
    # Lancement de l'application
    app.run(host="0.0.0.0")
```

3. Créer le Dockerfile suivant:

```Dockerfile
FROM python:3.12
WORKDIR /app

RUN pip install flask

COPY . .

EXPOSE 5000

CMD ["python", "app.py"]
```

4. Contruisez l'image flask-app via le Docker file : `docker build -t flask-app .`
5. Vérifier que l'image existe : `docker images`
6. Lancer le conteneur : `docker run -d -p 5000:5000 --name flask-test-app flask-app`
7. L'application est lancer à l'adresse [http://localhost:5000/](http://localhost:5000/)

### Exercice 4 : Déployer une application complexe avec Docker

**Objectif** : Déployer une application complexe avec Docker.

**Etapes préalables** : Créer une BDD MongoDB "MyDatabase" et une collection "MyCollection".

**Etapes** :

1. Ajouter une connexion à mongoDB dans `app.py`. Le contenu du fichier est le suivant:

```python
from flask import Flask
from pymongo import MongoClient

# Création de l'application
app = Flask(__name__)
# Connexion à la Base De Données (BDD) mongoDB
client = MongoClient("mongodb://mongo:27017/")

# Récupération de la BDD
db = client["myDatabase"]
# Récupération de la collection dans la BDD
collection = db["myCollection"]

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route('/users')
def get_users():
  # Insertion de données
  collection.insert_one({"name": "Durant"})
  # Test la connexion à la BDD
  user = collection.find_one({"name": "Durant"})
  return 'Connected to MongoDB, found {} user.'.format(user)

if __name__ == "__main__":
    # Lancement de l'application
    app.run(host="0.0.0.0")
```

2. Modifier le Dockerfile pour y ajouter la dépendance à `flask_pymongo` :

```Dockerfile
FROM python:3.12
WORKDIR /app

RUN pip install flask flask_pymongo

COPY . .

EXPOSE 5000

CMD ["python", "app.py"]
```

3. Rédaction du fichier `compose.yml`

```yml
services:
  web:
    build: .
    ports:
      - 5000:5000
    depends_on:
      - mongo

  mongo:
    image: mongo:6
    container_name: mongo
    ports:
      - "27017:27017"
    volumes:
      - mongo_data:/data/db

volumes:
  mongo_data:
```

4. Lancer le docker compose : `docker compose up -d`
5. L'application est lancer à l'adresse [http://localhost:5000/](http://localhost:5000/). Vous pouvez vérifier la connexion à la BDD à l'adresse [http://localhost:5000/users](http://localhost:5000/users).
6. Arrêter l'application : `docker compose stop`.
