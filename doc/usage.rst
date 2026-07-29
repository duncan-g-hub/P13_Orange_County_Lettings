Guide d'utilisation
===================

Présentation
------------

OC Lettings permet aux visiteurs de consulter les biens immobiliers
et les profils disponibles sur le site.

L'application est principalement consultative : les utilisateurs
peuvent parcourir les différentes pages et consulter les informations
associées aux biens et aux profils.

Les principales fonctionnalités sont :

* consulter la page d'accueil
* consulter la liste des biens immobiliers
* consulter le détail d'un bien immobilier
* consulter la liste des profils
* consulter le détail d'un profil
* accéder à l'interface d'administration pour les utilisateurs autorisés

Navigation sur le site
----------------------

Page d'accueil
~~~~~~~~~~~~~~

La page d'accueil constitue le point d'entrée de l'application.

Elle permet d'accéder aux principales fonctionnalités du site,
notamment aux listes de biens immobiliers et de profils.

Consulter les biens immobiliers
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Depuis la section dédiée aux biens immobiliers, l'utilisateur peut
consulter la liste des biens disponibles.

Chaque bien est présenté avec son titre.

L'utilisateur peut sélectionner un bien afin d'accéder à sa page de
détail.

Consulter le détail d'un bien
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

La page de détail d'un bien présente les informations disponibles
pour celui-ci, notamment :

* son titre ;
* son adresse ;
* les informations associées à cette adresse.

Si le bien demandé n'existe pas, l'application affiche une page
d'erreur ``404``.

Consulter les profils
~~~~~~~~~~~~~~~~~~~~~

L'utilisateur peut consulter la liste des profils disponibles.

Chaque profil est associé à un utilisateur de l'application.

Consulter le détail d'un profil
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

La sélection d'un profil permet de consulter les informations
associées à l'utilisateur.

Le profil peut notamment contenir sa ville favorite.

Si le profil demandé n'existe pas, l'application affiche une page
d'erreur ``404``.

Interface d'administration
--------------------------

Les utilisateurs disposant des droits nécessaires peuvent accéder à
l'interface d'administration Django :

.. code-block:: text

   /admin/

Cette interface permet aux administrateurs de gérer les données de
l'application.

Elle est notamment destinée à la gestion des utilisateurs, des profils,
des biens immobiliers et des adresses.

L'accès à cette interface est réservé aux utilisateurs autorisés par
le système d'authentification de Django.

Cas d'utilisation
-----------------

Consulter la liste des biens
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

**Acteur :** Visiteur

**Objectif :** Consulter les biens immobiliers disponibles.

**Précondition :** Le site est accessible.

**Scénario nominal :**

#. Le visiteur accède à la page des biens immobiliers.
#. L'application récupère les biens enregistrés dans la base de données.
#. L'application affiche la liste des biens.
#. Le visiteur peut sélectionner un bien pour consulter son détail.

**Résultat :** La liste des biens disponibles est affichée.

Consulter un bien immobilier
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

**Acteur :** Visiteur

**Objectif :** Consulter les informations détaillées d'un bien.

**Précondition :** Le bien existe dans la base de données.

**Scénario nominal :**

#. Le visiteur accède à la liste des biens.
#. Le visiteur sélectionne un bien.
#. L'application récupère le bien correspondant à son identifiant.
#. L'application affiche les informations du bien et son adresse.

**Résultat :** Les informations détaillées du bien sont affichées.

**Cas alternatif :**

Si l'identifiant demandé ne correspond à aucun bien, l'application
renvoie une erreur HTTP ``404``.

Consulter un profil
~~~~~~~~~~~~~~~~~~~

**Acteur :** Visiteur

**Objectif :** Consulter les informations d'un profil.

**Précondition :** Le profil existe dans la base de données.

**Scénario nominal :**

#. Le visiteur accède à la liste des profils.
#. Le visiteur sélectionne un profil.
#. L'application recherche le profil correspondant au nom d'utilisateur.
#. L'application affiche les informations du profil.

**Résultat :** Les informations du profil sont affichées.

**Cas alternatif :**

Si aucun profil ne correspond au nom d'utilisateur demandé,
l'application renvoie une erreur HTTP ``404``.

Gérer les données depuis l'administration
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

**Acteur :** Administrateur

**Objectif :** Administrer les données de l'application.

**Précondition :** L'utilisateur dispose des droits d'administration
nécessaires.

**Scénario nominal :**

#. L'administrateur accède à ``/admin/``.
#. Django demande une authentification.
#. L'administrateur s'authentifie avec ses identifiants.
#. L'interface d'administration est affichée.
#. L'administrateur peut gérer les données auxquelles il a accès.

**Résultat :** Les données de l'application peuvent être administrées
depuis l'interface Django.