Déploiement et gestion de l'application
========================================

Présentation
------------

L'application est déployée automatiquement en production à l'aide
d'une chaîne CI/CD reposant sur les outils suivants :

* GitHub et GitHub Actions pour la gestion du code et l'automatisation
* pytest pour l'exécution des tests
* flake8 pour le linting
* Docker pour la conteneurisation
* Docker Hub pour le stockage et la distribution des images Docker
* Render pour l'hébergement de l'application en production

Le déploiement est effectué à partir de la branche ``master``.

Architecture du pipeline
------------------------

Le pipeline est organisé en trois étapes principales :

.. code-block:: text

   GitHub
      |
      v
   Tests et qualité
      |
      | succès
      v
   Construction de l'image Docker
      |
      | succès
      v
   Docker Hub
      |
      | Deploy Hook
      v
   Render
      |
      v
   Application en production

Intégration continue
--------------------

Le workflow GitHub Actions exécute automatiquement les tests et les
contrôles de qualité du code.

Le job de test comprend :

* l'installation des dépendances Python
* l'exécution de ``flake8``
* l'exécution des tests avec ``pytest``
* la vérification de la couverture du code

La couverture minimale exigée est de 80 %.

La commande utilisée est :

.. code-block:: bash

   python -m pytest --cov=. --cov-fail-under=80

Si le linting, les tests ou la couverture échouent, le pipeline est
arrêté et l'image Docker n'est pas construite.

Gestion des branches
--------------------

Les modifications apportées aux branches autres que ``master``
déclenchent uniquement le job de test.

La construction et la publication de l'image Docker sont réservées
à la branche ``master``.

Le déploiement en production dépend de la réussite de la construction
et de la publication de l'image Docker.

Le pipeline suit donc les dépendances suivantes :

.. code-block:: text

   Tests
     |
     | succès
     v
   Docker
     |
     | succès
     v
   Déploiement Render

Conteneurisation
----------------

L'application est conteneurisée avec Docker à partir du fichier
``Dockerfile`` situé à la racine du projet.

Avant le déploiement, le fonctionnement de l'image est vérifié
localement.

Construction de l'image
~~~~~~~~~~~~~~~~~~~~~~~

L'image peut être construite localement avec :

.. code-block:: bash

   docker build -t oc-lettings .

L'image peut ensuite être lancée avec Docker afin de vérifier le
fonctionnement de l'application.

Publication sur Docker Hub
~~~~~~~~~~~~~~~~~~~~~~~~~~

L'image est publiée sur Docker Hub par GitHub Actions.

Deux tags sont utilisés :

* ``latest`` : correspond à la dernière version publiée
* le hash du commit Git : identifie précisément la version du code
  correspondant à l'image

Par exemple :

.. code-block:: text

   duncangdev/oc-lettings:latest

et :

.. code-block:: text

   duncangdev/oc-lettings:<commit-sha>

Le tag basé sur le hash du commit permet de retrouver précisément
la version de l'application utilisée pour un déploiement donné.

Exécution locale depuis Docker Hub
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

L'image publiée sur Docker Hub peut être récupérée et exécutée
localement.

Le fichier ``compose.yml`` contient notamment :

.. code-block:: yaml

   services:
     web:
       image: duncangdev/oc-lettings:latest
       env_file:
         - .env
       ports:
         - "8000:8000"

Une seule commande permet de récupérer l'image et de démarrer
l'application :

.. code-block:: bash

   docker compose up

L'application est ensuite accessible à l'adresse :

.. code-block:: text

   http://localhost:8000/

Pour arrêter l'application :

.. code-block:: bash

   docker compose down

Cette procédure permet de vérifier qu'une image publiée sur Docker Hub
peut être exécutée localement avant son utilisation en production.

Configuration de l'application
------------------------------

L'application Django utilise des variables d'environnement afin de
séparer la configuration du code source.

Les informations sensibles ne sont pas stockées dans le dépôt Git.

Les principales variables utilisées sont :

``SECRET_KEY``
   Clé secrète utilisée par Django.

``DEBUG``
   Active ou désactive le mode debug de Django.

``ALLOWED_HOSTS``
   Liste des domaines autorisés par Django.

Exemple de configuration locale :

.. code-block:: text

   SECRET_KEY=<clé-secrète>
   DEBUG=True
   ALLOWED_HOSTS=localhost,127.0.0.1

En production, les valeurs doivent être adaptées à l'environnement
de production.

La clé secrète ne doit jamais être ajoutée au dépôt GitHub ou à
l'image Docker.

Fichiers statiques
------------------

Les fichiers statiques de l'application sont collectés lors de la
construction de l'image Docker avec la commande :

.. code-block:: bash

   python manage.py collectstatic --noinput

Les fichiers collectés sont placés dans le répertoire configuré par
``STATIC_ROOT``.

L'application utilise WhiteNoise pour servir les fichiers statiques
en production.

La configuration Django utilise notamment :

.. code-block:: python

   STATIC_URL = '/static/'
   STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

   STATICFILES_DIRS = [BASE_DIR / "static"]

Le middleware WhiteNoise est également activé afin de permettre le
chargement des fichiers statiques en production.

Une vérification visuelle des fichiers CSS et JavaScript doit être
effectuée après chaque déploiement.

Déploiement sur Render
----------------------

L'application est hébergée en production sur Render.

Render utilise l'image Docker publiée sur Docker Hub pour exécuter
l'application.

La configuration de production doit notamment contenir les variables
d'environnement nécessaires au fonctionnement de Django :

.. code-block:: text

   SECRET_KEY=<clé-secrète-de-production>
   DEBUG=False
   ALLOWED_HOSTS=<domaine-de-production>

Les valeurs sensibles sont configurées directement dans
l'environnement de production et ne sont pas stockées dans le
repository GitHub.


Déploiement automatique Render
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Le déploiement automatique de Render depuis le dépôt GitHub est
désactivé.

Le déploiement est exclusivement déclenché par GitHub Actions après
la réussite des étapes de tests et de conteneurisation.

Déclenchement du déploiement
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Le déploiement est déclenché depuis GitHub Actions à l'aide d'un
Deploy Hook Render.

Le workflow utilise une variable secrète GitHub contenant l'URL du
Deploy Hook :

.. code-block:: text

   RENDER_DEPLOY_HOOK

Cette valeur ne doit pas être écrite directement dans le fichier
du workflow.

GitHub Actions déclenche le Deploy Hook uniquement après la réussite
du travail de conteneurisation.

Le workflow garantit ainsi l'ordre suivant :

.. code-block:: text

   Tests réussis
        |
        v
   Image Docker construite
        |
        v
   Image publiée sur Docker Hub
        |
        v
   Deploy Hook Render
        |
        v
   Nouvelle version en production

Configuration des secrets GitHub
--------------------------------

Les secrets utilisés par GitHub Actions doivent être configurés dans
les paramètres du repository GitHub.

Les principaux secrets nécessaires sont :

``SECRET_KEY``
   Clé secrète utilisée pour exécuter les tests Django dans GitHub
   Actions.

``DOCKERHUB_USERNAME``
   Nom d'utilisateur Docker Hub.

``DOCKERHUB_TOKEN``
   Token d'accès permettant à GitHub Actions de publier les images
   sur Docker Hub.

``RENDER_DEPLOY_HOOK``
   URL du Deploy Hook permettant de déclencher le déploiement Render.

Ces valeurs ne doivent jamais être écrites directement dans le
fichier ``ci.yml``.

Procédure de déploiement
------------------------

Pour effectuer un nouveau déploiement :

#. Développer la modification sur une branche dédiée.
#. Vérifier localement que l'application fonctionne.
#. Vérifier les tests et le linting.
#. Créer une Pull Request vers ``master``.
#. Vérifier que le travail de CI est réussi.
#. Fusionner la Pull Request dans ``master``.
#. GitHub Actions exécute à nouveau les tests.
#. Si les tests réussissent, l'image Docker est construite.
#. L'image est publiée sur Docker Hub avec son hash de commit et le
   tag ``latest``.
#. Le travail de déploiement déclenche le Deploy Hook Render.
#. Render déploie la nouvelle version de l'application.

Vérifications après déploiement
-------------------------------

Après chaque déploiement, les éléments suivants doivent être vérifiés :

* l'application est accessible depuis son URL publique
* la page d'accueil fonctionne
* les pages de biens immobiliers fonctionnent
* les pages de profils fonctionnent
* les fichiers CSS sont correctement chargés
* les fichiers JavaScript sont correctement chargés
* les images et autres ressources statiques sont correctement chargées
* l'interface d'administration Django est accessible pour un
  utilisateur autorisé
* les fichiers statiques de l'interface d'administration sont
  correctement chargés

Gestion des versions Docker
---------------------------

Le tag correspondant au hash du commit permet de conserver une
référence précise vers chaque version publiée.

Le tag ``latest`` permet quant à lui d'identifier l'image correspondant
à la dernière version publiée.

Pour reproduire une version précise, il est recommandé d'utiliser le
tag correspondant au hash du commit plutôt que ``latest``.

Sécurité
--------

Les informations sensibles doivent être stockées uniquement dans les
variables d'environnement et les secrets des différents services.

Il ne faut jamais versionner :

* la clé secrète Django
* les tokens Docker Hub
* le Deploy Hook Render
* les fichiers ``.env`` contenant des informations sensibles

Le mode debug doit être désactivé en production :

.. code-block:: text

   DEBUG=False