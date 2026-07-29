Base de données et modèles
==========================

Présentation
------------

L'application utilise SQLite comme système de gestion de base de données.

Les données sont manipulées à travers l'ORM de Django.
Les modèles Python permettent ainsi de représenter les données sous forme d'objets
et Django se charge de leur correspondance avec les tables de la base de données.

Modèle Address
--------------

Le modèle ``Address`` représente l'adresse d'un bien immobilier.

Champs
~~~~~~

.. list-table::
   :header-rows: 1
   :widths: 20 20 60

   * - Champ
     - Type
     - Description
   * - ``number``
     - ``PositiveIntegerField``
     - Numéro de rue. La valeur maximale est 9999.
   * - ``street``
     - ``CharField``
     - Nom de la rue, limité à 64 caractères.
   * - ``city``
     - ``CharField``
     - Ville, limitée à 64 caractères.
   * - ``state``
     - ``CharField``
     - État américain représenté par un code de 2 caractères.
   * - ``zip_code``
     - ``PositiveIntegerField``
     - Code postal, limité à une valeur maximale de 99999.
   * - ``country_iso_code``
     - ``CharField``
     - Code pays ISO sur 3 caractères.

Le modèle utilise également des validateurs afin de contrôler certaines
valeurs saisies :

* ``MaxValueValidator`` limite les valeurs numériques ;
* ``MinLengthValidator`` impose une longueur minimale pour certains
  champs textuels.

La représentation textuelle d'une adresse correspond au numéro et au
nom de la rue.

Modèle Letting
--------------

Le modèle ``Letting`` représente un bien immobilier disponible sur
l'application.

Champs
~~~~~~

.. list-table::
   :header-rows: 1
   :widths: 20 20 60

   * - Champ
     - Type
     - Description
   * - ``title``
     - ``CharField``
     - Titre du bien, limité à 256 caractères.
   * - ``address``
     - ``OneToOneField``
     - Adresse associée au bien immobilier.

Relation avec Address
~~~~~~~~~~~~~~~~~~~~~

Chaque ``Letting`` est associé à une seule instance de ``Address`` par
l'intermédiaire d'une relation ``OneToOneField``.

La suppression d'une adresse entraîne la suppression du bien associé
grâce à l'option ``on_delete=models.CASCADE``.

La représentation textuelle d'un ``Letting`` correspond à son titre.

Modèle Profile
--------------

Le modèle ``Profile`` représente le profil associé à un utilisateur
de l'application.

Champs
~~~~~~

.. list-table::
   :header-rows: 1
   :widths: 20 20 60

   * - Champ
     - Type
     - Description
   * - ``user``
     - ``OneToOneField``
     - Utilisateur Django associé au profil.
   * - ``favorite_city``
     - ``CharField``
     - Ville favorite de l'utilisateur, limitée à 64 caractères.
       Ce champ est facultatif.

Relation avec User
~~~~~~~~~~~~~~~~~~

Chaque profil est associé à un seul utilisateur Django via une relation
``OneToOneField``.

La suppression de l'utilisateur entraîne la suppression du profil
associé grâce à l'option ``on_delete=models.CASCADE``.

Le modèle ``Profile`` utilise le modèle ``User`` fourni par le système
d'authentification de Django.

La représentation textuelle d'un profil correspond au nom d'utilisateur
Django associé.

