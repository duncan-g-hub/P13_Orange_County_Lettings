Démarrage rapide
================

Démarrage avec Python
---------------------

Après avoir installé les dépendances et configuré les variables
d'environnement, lancer le serveur Django :

.. code-block:: bash

   python manage.py runserver

L'application est alors accessible à l'adresse :

.. code-block:: text

   http://127.0.0.1:8000/


Démarrage avec Docker
---------------------
Prérequis
~~~~~~~~~

Pour exécuter l'application localement avec Docker, les éléments
suivants sont nécessaires :

* Windows, macOS ou Linux
* Docker Desktop
* Git

Docker Desktop fournit Docker Engine ainsi que Docker Compose et
permet de construire et d'exécuter les conteneurs Docker localement.

Installation de Docker Desktop
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Docker Desktop peut être téléchargé depuis le site officiel de Docker.

Après son installation, vérifier que Docker fonctionne correctement
avec :

.. code-block:: bash

   docker --version

Puis vérifier que Docker Compose est disponible :

.. code-block:: bash

   docker compose version

Les commandes doivent retourner les versions installées de Docker et
Docker Compose.

Démarrage
~~~~~~~~~

L'application peut être exécutée directement à partir de l'image
Docker publiée sur Docker Hub.

Le fichier ``docker-compose.yml`` permet de récupérer automatiquement l'image
et de démarrer l'application.

Depuis le répertoire contenant le fichier ``docker-compose.yml``, exécuter :

.. code-block:: bash

   docker compose up

Docker récupère automatiquement l'image indiquée dans ``docker-compose.yml``
si celle-ci n'est pas déjà présente localement.

L'application est alors accessible à l'adresse :

.. code-block:: text

   http://localhost:8000/

Arrêt de l'application Docker
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Pour arrêter l'application :

.. code-block:: bash

   docker compose down