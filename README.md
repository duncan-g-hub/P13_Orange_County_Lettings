# P13 : Orange County Lettings - Site web de gestion de locations de biens immobiliers
 
## Objectif
 
Site web réorganisé en une architecture modulaire afin d'améliorer la maintenabilité, la flexibilité et l'évolutivité du code. 
Le projet inclut :
 
- Une séparation en 3 applications : `oc_lettings_site` (cœur du projet), `lettings` et `profiles`.
- Une surveillance des erreurs en production via Sentry, couplée à des logs applicatifs.
- Une suite de tests (unitaires et d'intégration) avec une couverture de code supérieure à 80 %.
- Un pipeline CI/CD complet : lint, tests, build/push de l'image Docker, déploiement automatique avec Render.

---

## Fonctionnalités
 
- Page d'accueil :
  - Présentation du site et liens de navigation vers les sections "Lettings" et "Profiles"
  

- Gestion des locations (lettings) :
  - Visualisation de la liste de toutes les locations
  - Visualisation du détail d'une location (titre, adresse complète)
  

- Gestion des profils (profiles) :
  - Visualisation de la liste de tous les profils utilisateurs
  - Visualisation du détail d'un profil (nom, prénom, email, ville favorite)

    
- Administration :
  - Interface d'administration Django pour créer, modifier et supprimer des adresses, locations et profils


- Gestion des erreurs :
  - Pages d'erreur personnalisées 404 (page non trouvée) et 500 (erreur serveur), cohérentes avec le design du site


- Supervision :
  - Suivi des erreurs et des performances via Sentry
  - Journalisation (logs) des événements clés dans les vues (accès aux pages, requêtes non trouvées, etc.)

---

## Architecture
 
Le projet suit une architecture MVT (Model-View-Template) et est divisé en 3 applications :
- `oc_lettings_site` : cœur du projet (configuration globale, page d'accueil, gestion des erreurs 404/500)
- `lettings` : application métier pour les locations (`Address`, `Letting`)
- `profiles` : application métier pour les profils utilisateurs (`Profile`)


- Model : Défini dans `models.py` de chaque application, chaque classe correspond à une table de la base de données, Django ORM traduit le python en SQL.
- View : Défini dans `views.py` de chaque application, reçoit une requête HTTP, interroge les modèles, prépare les données et retourne une réponse.
- Template : Défini par les fichiers `.html` dans les dossiers `templates/`, reçoit le contexte de la vue et génère le html final.

---

## Structure du projet
 
```
P13_Orange_County_Lettings/
 
    README.md                               # Documentation
    .gitignore                              # Liste des dossiers et fichiers à ignorer pour le repository
    requirements.txt                        # Liste des dépendances
    .env                                    # Gestion des variables d'environnement sensibles (non-inclu dans le repository)
    Dockerfile                              # Image Docker de production (gunicorn + collectstatic)
    docker-compose.yml                      # Lancement du site via l'image Docker publiée
    .github/
        workflows/
            ci.yml                          # Pipeline CI/CD (lint, tests, build/push image, déploiement)
 
    oc_lettings_site/                       # Configuration globale du projet Django
        settings.py                         # Configuration (base de données, apps, Sentry, logging, statiques)
        urls.py                             # Routage principal (inclut lettings.urls et profiles.urls)
        wsgi.py / asgi.py                   # Points d'entrée serveur
        views.py                            # Vue de la page d'accueil
        apps.py                             # Configuration de l'application
        tests/                              # Tests unitaires (views, urls)
        templates/                          # Gabarits HTML communs
            base.html                       # Gabarit de base (navbar, footer)
            index.html                      # Page d'accueil
            404.html / 500.html             # Pages d'erreur personnalisées
 
    lettings/                               # Application métier - locations (MVT)
        models.py                           # Modèles Address et Letting
        views.py                            # Vues liste et détail des locations
        urls.py                             # Routes de l'application
        apps.py                             # Configuration de l'application
        migrations/                         # Migrations de la base de données
        tests/                              # Tests unitaires et d'intégration (models, views, urls)
        templates/                          # Gabarits HTML lettings

    profiles/                               # Application métier - profils utilisateurs (MVT)
        models.py                           # Modèle Profile (lié à User)
        views.py                            # Vues liste et détail des profils
        urls.py                             # Routes de l'application
        apps.py                             # Configuration de l'application
        migrations/                         # Migrations de la base de données
        tests/                              # Tests unitaires et d'intégration (models, views, urls)
        templates/                          # Gabarits HTML profiles
 
    static/                                 # Fichiers statiques communs (CSS, JS, assets)
    oc-lettings-site.sqlite3                # Base de données
    manage.py                               # Fichier de gestion de commandes Django
 
```
 
---

## Dépendances
 
- Python 3.13
- Django 6.0.6
- gunicorn (serveur WSGI de production)
- whitenoise (fichiers statiques)
- sentry-sdk (monitoring et logs)
- python-dotenv (variables d'environnement)
- pytest / pytest-django / pytest-cov (tests et couverture)
- flake8 (linting)

La liste complète et versionnée se trouve dans `requirements.txt`.

---

## Installation
 
1. Cloner le dépôt :
    ```bash
       git clone https://github.com/duncan-g-hub/P13_Orange_County_Lettings.git
       cd P13_Orange_County_Lettings
    ```
 
2. Créer et activer un environnement virtuel :
    ```bash
       python -m venv venv
       source venv/bin/activate  # Linux/macOS
       venv\Scripts\activate     # Windows
    ```
 
3. Installer les dépendances :
    ```bash
       pip install -r requirements.txt
    ```
 
4. Créer un fichier `.env` à la racine du projet avec les variables suivantes :
    ```
       SECRET_KEY=<votre-cle-secrete-django>
       DEBUG=True
       ALLOWED_HOSTS=localhost
       SENTRY_DSN=<votre-dsn-sentry>
    ```
 
---

## Lancement local
 
1. Appliquer les migrations :
    ```bash
       python manage.py migrate
    ```
 
2. (Optionnel) Créer un superutilisateur pour accéder à l'admin :
    ```bash
       python manage.py createsuperuser
    ```
 
3. Lancer le serveur de développement :
    ```bash
       python manage.py runserver
    ```
    Le site est accessible sur [http://localhost:8000](http://localhost:8000).
 
4. Lancer les outils qualité :
    ```bash
       flake8 .
       pytest --cov=. --cov-fail-under=80
    ```

---

## Lancement Docker (avec WSL Ubuntu)
 
Prérequis : Docker Desktop installé avec l'intégration WSL2 activée pour votre distribution Ubuntu.
 
1. Ouvrir un terminal WSL Ubuntu, se placer dans le dossier du projet.
2. S'assurer que le fichier `.env` est présent à la racine (mêmes variables que ci-dessus).
3. Construire et lancer le conteneur avec Docker Compose :
    ```bash
       cd P13_Orange_County_Lettings/
       docker compose up
    ```
   Cette commande récupère l'image `duncangdev/oc-lettings:latest` sur Docker Hub et démarre le site.
 
4. Le site est accessible sur [http://localhost:8000](http://localhost:8000).

---

## Pipeline CI/CD
 
Le pipeline CI/CD (GitHub Actions) se déclenche différemment selon la branche :
 
- Toute branche / pull request vers `master` → exécute uniquement le job test :
  1. Installation des dépendances
  2. Linting du code avec `flake8`
  3. Exécution de la suite de tests avec `pytest`, avec vérification que la couverture est ≥ 80 %
  

- Push sur `master` uniquement (en plus du job test) :
  1. Job docker (ne se lance que si le job test réussit) :
     - Connexion à Docker Hub
     - Construction de l'image Docker
     - Tag de l'image avec le hash du commit (`github.sha`) et avec `latest`
     - Push des deux tags sur Docker Hub
  2. Job deploy (ne se lance que si le job docker réussit) :
     - Déclenchement du déploiement sur Render via un webhook (`RENDER_DEPLOY_HOOK`)
     - Render récupère automatiquement la nouvelle image `latest` et redémarre le service
  

Résumé du flux : `push` → test/lint → build & push image Docker (master uniquement) → déploiement Render (master uniquement, après succès du build).

---

## Aperçu 

![Aperçu.png](Aper%C3%A7u.png)

---

## Contact

Pour toute question :  
Duncan GAURAT - duncan.dev@outlook.fr