Interfaces de programmation
===========================

Présentation
------------

L'application utilise le système d'URL de Django pour associer
les requêtes HTTP aux vues correspondantes.

Les URLs sont organisées au niveau du projet puis incluses depuis
les applications ``lettings`` et ``profiles``.

Les principales interfaces accessibles sont présentées ci-dessous.

URLs principales
------------------

Page d'accueil
~~~~~~~~~~~~~~

**URL :**

.. code-block:: text

   /

**Méthode HTTP :** ``GET``

**Vue :** ``oc_lettings_site.views.index``

Cette URL affiche la page d'accueil de l'application.


Lettings
--------

Liste des biens
~~~~~~~~~~~~~~~

**URL :**

.. code-block:: text

   /lettings/

**Méthode HTTP :** ``GET``

**Vue :** ``lettings.views.index``

Cette URL récupère l'ensemble des biens immobiliers enregistrés dans
la base de données et les transmet au template
``lettings/index.html``.

Détail d'un bien
~~~~~~~~~~~~~~~~

**URL :**

.. code-block:: text

   /lettings/<letting_id>/

**Méthode HTTP :** ``GET``

**Paramètre :** ``letting_id``

Le paramètre ``letting_id`` correspond à l'identifiant numérique du
bien immobilier.

La vue recherche le bien correspondant dans la base de données.

Si le bien existe, ses informations sont transmises au template
``lettings/letting.html``.

Si aucun bien ne correspond à l'identifiant fourni, Django renvoie
une réponse HTTP 404.

Profiles
--------

Liste des profils
~~~~~~~~~~~~~~~~~

**URL :**

.. code-block:: text

   /profiles/

**Méthode HTTP :** ``GET``

**Vue :** ``profiles.views.index``

Cette URL récupère l'ensemble des profils enregistrés dans la base
de données et les transmet au template ``profiles/index.html``.

Détail d'un profil
~~~~~~~~~~~~~~~~~~

**URL :**

.. code-block:: text

   /profiles/<username>/

**Méthode HTTP :** ``GET``

**Paramètre :** ``username``

Le paramètre ``username`` correspond au nom d'utilisateur Django.

La vue recherche le profil associé à l'utilisateur correspondant.

Si le profil existe, ses informations sont transmises au template
``profiles/profile.html``.

Si aucun profil ne correspond au nom d'utilisateur fourni, Django
renvoie une réponse HTTP 404.

Administration
--------------

L'interface d'administration Django est accessible via :

.. code-block:: text

   /admin/

Elle permet aux utilisateurs autorisés de gérer les données de
l'application à travers l'interface d'administration Django.

Gestion des erreurs
-------------------

Les vues de détail des biens et des profils utilisent
``get_object_or_404``.

Lorsqu'un bien ou un profil demandé n'existe pas, l'application renvoie
donc une réponse HTTP 404 au lieu de provoquer une erreur serveur.