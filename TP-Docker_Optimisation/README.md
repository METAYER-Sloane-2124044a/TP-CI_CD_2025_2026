# TP-Docker_Optimisation

## Informations Générales

L’objectif de ce TP est de vous familiariser avec les concepts fondamentaux de Docker, la création et la gestion de conteneurs, l’utilisation des images, ainsi que les commandes essentielles pour manipuler l’écosystème Docker.

## Prérequis

- Installer Docker sur le site officiel (adapté à votre système d'exploitation): [https://docs.docker.com/get-docker/](https://docs.docker.com/get-docker/)
- Télécharger Docker Desktop ou Docker Engine
- Vérifier l'installation via la commande `docker --version`

## Objectif

L’objectif du TP est d’optimiser progressivement cette application et son image Docker étape par étape.

Vous devez :

- Analyser le code et le Dockerfile existants pour identifier les mauvaises pratiques.
- Proposer et appliquer des améliorations par itérations successives. (et les documenter dans le rendu)
- Mesurer et comparer les performances ainsi que la taille de l’image Docker après
  chaque étape.
- Documenter vos modifications et leurs impacts.

## Etape préalable

- Déplacez-vous dans TP-Docker_Optimisation&nbsp;:

```bash
      cd TP-Docker_Optimisation
```

## Etapes

A chaque étape, pour ne pas fausser les résultats, lancer la commande&nbsp;:

```bash
      docker system prune --all
```

Cela va supprimer les conteneurs arrêtés, les images, le cache.

Une fois l'image l'étape effectuée, contruiser l'image node-app via le Dockerfile:

```bash
      docker build -t node-app .
```

Par la suite, vous pouvez lancer l'application pour vérifier son fonctionnement:

```bash
      docker run -d -p 3000:3000 --name node-app-test node-app
```

### Etape 1 : Construction de l'image sans modification

Lancer l'application tel quel pour avoir un aperçu.

| Temps build | Taille image |
| ----------- | ------------ |
| 71.1s       | 1.73GB       |

### Etape 2 : Suppression des packages inutiles

Le dockerfile inclu l'installation de packages inutiles via la commande :

```
RUN apt-get update && apt-get install -y build-essential ca-certificates locales && echo "en_US.UTF-8 UTF-8" > /etc/locale.gen && locale-gen
```

Par ailleurs, cela alourdi notre image, nous pouvons donc supprimer cette commande.

| Temps build | Taille image |
| ----------- | ------------ |
| 47.8s       | 1.66GB       |

### Etape 3 : Utilisation d'une meilleure image de base

L'image `node:latest` représente la dernière image node. Cela implique d'installer de nombreux packages. Or, notre application ne nécessite pas une telle version. Nous pouvons donc la modifier. En effet, `node_modules/tr46` et `node_modules/whatwg-url` demandent une version de node `>=18`. Nous utilisons alors une version alpine (plus légère) : `node:18-alpine`.

| Temps build | Taille image |
| ----------- | ------------ |
| 12.9s       | 201MB        |

### Etape 4 : Copie et installation des dépendances

La commande `COPY node_modules ./node_modules` n'est pas recommandée. En effet, il est préférable de copier les fichiers `package*.json` (package-lock.json et package.json) définissant les dépendances du projet. En effet, les dépendances changent généralement moins souvent que le code du projet.

| Temps build | Taille image |
| ----------- | ------------ |
| 7.8s        | 201MB        |

### Etape 5 : Suppression de la commande build

Mon application ne nécessite pas d'être compilée avant d'être exécutée. Nous pouvons donc supprimer cette étape dans notre dockerfile.

| Temps build | Taille image |
| ----------- | ------------ |
| 6.9s        | 201MB        |

### Etape 6 : Utilisation d'un seul port

Il n'est pas nécessaire d'exposer plusieurs ports pour notre application. En effet, seul le 3000 suffit. Par ailleurs, dans le fichier `server.js`, le port par défaut est 3000.

| Temps build | Taille image |
| ----------- | ------------ |
| 7.3s        | 201MB        |

### Etape 7 : Utilisation de .dockerignore

Nous ne souhaitons pas copier des dépendances inutiles telles que `node_modules` et alléger notre image. Pour cela, nous utilisons un fichier `.dockerignore`.

| Temps build | Taille image |
| ----------- | ------------ |
| 7.1s        | 208MB        |

### Etape 8 : Modification des droits

Pour plus de sécurité, nous utilisons `USER node` afin de ne pas attribuer les droits administrateurs.

| Temps build | Taille image |
| ----------- | ------------ |
| 14.9s       | 208MB        |
