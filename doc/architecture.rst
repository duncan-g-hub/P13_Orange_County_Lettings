Architecture et technologies
============================

Technologies principales
------------------------

L'application repose sur les technologies suivantes :

* Python 3.13 : langage de programmation
* Django : framework web
* SQLite : base de données
* HTML/CSS/JavaScript : interface utilisateur
* Gunicorn : serveur WSGI utilisé pour exécuter Django en production
* WhiteNoise : gestion des fichiers statiques
* Docker : conteneurisation de l'application
* Docker Hub : stockage des images Docker
* GitHub Actions : automatisation de l'intégration continue et du
  déploiement
* Render : hébergement de l'application en production
* Sphinx : génération de la documentation technique
* Read the Docs : hébergement et génération automatique de la
  documentation

Tests et qualité du code
------------------------

Les tests automatisés sont réalisés avec ``pytest``.

La couverture de code est mesurée avec ``pytest-cov`` et doit être
supérieure ou égale à 80 % pour que le pipeline CI soit considéré
comme réussi.

Le linting du code Python est effectué avec ``flake8``.

Conteneurisation
----------------

L'application est construite sous la forme d'une image Docker.

L'image est identifiée par deux tags :

* le hash du commit GitHub, permettant d'identifier précisément la
  version de l'application ;
* ``latest``, permettant d'identifier la dernière version publiée.