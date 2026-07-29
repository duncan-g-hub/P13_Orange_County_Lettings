Installation
============

Prérequis
---------

Pour installer le projet localement, les éléments suivants sont
nécessaires :

* Git
* Python 3.13
* pip
* Docker, si l'application doit être exécutée avec son image Docker

Récupération du projet
----------------------

Cloner le dépôt GitHub :

.. code-block:: bash

    git clone https://github.com/duncan-g-hub/P13_Orange_County_Lettings.git
    cd P13_Orange_County_Lettings



Installation avec Python
------------------------

Créer un environnement virtuel :

.. code-block:: bash

    python -m venv venv

Activer l'environnement virtuel /

.. code-block:: bash

    source venv/bin/activate

Installer les dépendances :

.. code-block:: bash

    pip install -r requirements.txt

Variables d'environnement
-------------------------

L'application utilise des variables d'environnement pour sa
configuration.

Créer un fichier ``.env`` à la racine du projet :

.. code-block:: text

    SECRET_KEY=<clé-secrète>
    DEBUG=True
    ALLOWED_HOSTS=localhost

La valeur de ``SECRET_KEY`` doit rester confidentielle.

Le fichier ``.env`` ne doit pas être ajouté au dépôt Git.

Base de données
--------------

La base de données SQLite utilisée par le projet est fournie avec
l'application pour permettre de retrouver les données nécessaires
au fonctionnement du site.

L'application peut être démarrée après l'installation des dépendances
et la configuration des variables d'environnement.