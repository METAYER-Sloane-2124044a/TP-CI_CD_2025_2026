# TP-Docker_Optimisation

## Informations Générales

L’objectif de ce TP est de vous familiariser avec les concepts fondamentaux de Docker, la création et la gestion de conteneurs, l’utilisation des images, ainsi que les commandes essentielles pour manipuler l’écosystème Docker.

## Prérequis

- Installer Docker sur le site officiel (adapté à votre système d'exploitation): [https://docs.docker.com/get-docker/](https://docs.docker.com/get-docker/)
- Télécharger Docker Desktop ou Docker Engine
- Vérifier l'installation via la commande `docker --version`

## Exercice

**Objectif**: L’objectif du TP est d’optimiser progressivement cette application et son image Docker étape par étape.

Vous devez :

- Analyser le code et le Dockerfile existants pour identifier les mauvaises pratiques.
- Proposer et appliquer des améliorations par itérations successives. (et les documenter dans le rendu)
- Mesurer et comparer les performances ainsi que la taille de l’image Docker après
  chaque étape.
- Documenter vos modifications et leurs impacts.

**Etape préalable**:

- Déplacez-vous dans TP-Docker_Optimisation : `cd TP-Docker_Optimisation`

**Etapes**:

A chaque étapes, supprimer le cache via la commande `docker build prune --all` pour ne pas fausser les résultats.

1. Construction de l'image sans modification

- Contruisez l'image node-app via le Docker file : `docker build -t node-app .`
- Lancer l'application `docker run -d -p 3000:3000 --name node-app-test node-app` et vérifier son fonctionnement

| Temps build | Taille image |
| ----------- | ------------ |
| 49.7s       | 1.77GB       |
