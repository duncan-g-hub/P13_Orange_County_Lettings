Orange County Lettings
===========

Présentation
------------

Orange County Lettings est une application web développée avec Django permettant
de consulter des annonces immobilières et des profils d'utilisateurs.

L'application permet notamment :

* de consulter la liste des biens disponibles
* d'afficher les détails d'un bien immobilier
* de consulter les profils des utilisateurs
* d'afficher les informations détaillées d'un profil

L'application dispose également d'une interface d'administration Django
permettant aux utilisateurs autorisés de gérer les données de
l'application.

Objectifs du projet
-------------------

Le projet a pour objectif de fournir une application web fonctionnelle,
maintenable et déployable dans différents environnements.

L'application est conteneurisée avec Docker et son intégration automatisée avec GitHub Actions.
Et son déploiement est géré avec Render.

Documentation
-------------

Cette documentation présente l'architecture technique de l'application,
son installation, son utilisation, sa base de données, ses interfaces
ainsi que ses procédures de déploiement.

.. toctree::
   :maxdepth: 2
   :caption: Documentation technique

   installation
   quickstart
   architecture
   database
   api
   usage
   deployment