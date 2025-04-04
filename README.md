# PCT - Plateforme d'État Civil (Django)

Ce projet est une application Django destinée à gérer les actes d’état civil. Elle permet aux administrateurs, agents d’état civil et citoyens de consulter ou enregistrer différents documents officiels (naissance, mariage, décès, etc.).

## Fonctionnalités principales

- Gestion des utilisateurs avec rôles (Admin, Agent, Utilisateur)
- Création d’actes d’état civil
- Gestion des localités, personnes morales, physiques
- Interface d’administration via Django admin
- Système d’authentification intégré (connexion / déconnexion)

## Technologies utilisées

- Python 3.10+
- Django 4.x
- SQLite (par défaut, peut être migré vers PostgreSQL)
- HTML / Bootstrap (templates)
- Django Admin

## Installation

1. **Cloner le projet :**
```bash
git clone https://github.com/ACHOYATTE2025/PCT.git
cd PCT
