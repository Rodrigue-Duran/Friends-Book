# FriendBook

![Django](https://img.shields.io/badge/Django-5.2.5-green)
![Python](https://img.shields.io/badge/Python-3.13.5-blue)
![Statut](https://img.shields.io/badge/Version-v1.0-yellow)

FriendBook est une plateforme sociale conçue pour faciliter la mise en relation entre individus du monde entier en fonction de leurs compétences. Elle permet à chacun de créer un profil détaillé, d’ajouter des amis, et de consulter les informations professionnelles et académiques des autres utilisateurs.

---

## 📚 Sommaire

- [🎯 Objectif](#-objectif)
- [📌 Version actuelle](#-version-actuelle)
- [⚙️ Fonctionnalités](#-fonctionnalités)
- [🛠️ Technologies utilisées](#-technologies-utilisées)
- [🚀 Installation et lancement du projet](#-installation-et-lancement-du-projet)
- [📁 Structure du projet](#-structure-du-projet)
- [🔮 Roadmap](#-roadmap)
- [🤝 Contribuer](#-contribuer)
- [👤 Auteur](#-auteur)

---

## 🎯 Objectif

L’objectif de FriendBook est de devenir un annuaire mondial des talents. Que vous soyez une entreprise à la recherche d’un profil compétent ou un particulier souhaitant élargir son réseau, FriendBook vous aide à trouver les bonnes personnes, au bon moment.

---

## 📌 Version actuelle

Cette version est une **première ébauche** du projet. Certaines fonctionnalités sont encore en cours de développement ou d’amélioration. Le projet évoluera progressivement pour intégrer davantage d’outils, de sécurité et d’interactions.

---

## ⚙️ Fonctionnalités

- 🔐 Inscription et connexion sécurisée  
- 📝 Création et modification de profil utilisateur  
- 👥 Ajout et suppression d’amis  
- 🔍 Consultation du profil d’un ami  
- 🧠 Gestion des compétences associées à chaque utilisateur  
- 🌐 Interface web avec pages HTML et styles CSS  
- 🔔 Sons de notification pour les actions réussies  

---

## 🛠️ Technologies utilisées

- Python 3  
- Django  
- SQLite  
- HTML5 / CSS3  
- Django Templates  

---

## 🚀 Installation et lancement du projet


# 1. Cloner le dépôt
git clone https://github.com/Rodrigue-Duran/Friends-Book.git
cd friend_book

# 2. Créer un environnement virtuel (optionnel mais recommandé)
python -m venv venv
source venv/bin/activate  # Sur Linux/macOS
venv\Scripts\activate     # Sur Windows

# 3. Installer Django
pip install django

# 4. Appliquer les migrations
python manage.py makemigrations
python manage.py migrate

# 5. Lancer le serveur
python manage.py runserver


👉 Ouvrez votre navigateur à l’adresse suivante :  
[http://127.0.0.1:8000](http://127.0.0.1:8000)

---

## 📁 Structure du projet

```
friend_book/
│
├── .gitignore
├── db.sqlite3
├── manage.py
├── README.md
├── run_tests.py
│
├── application/
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── tests.py
│   ├── urls.py
│   ├── views.py
│   ├── migrations/
│   │   └── 0001_initial.py
│   ├── static/
│   │   ├── css/
│   │   │   ├── accueil_connect.css
│   │   │   ├── accueil_inscription.css
│   │   │   ├── menu_principal.css
│   │   │   ├── mes_amis.css
│   │   │   ├── modifier_mon_profil.css
│   │   │   └── mon_profil.css
│   │   └── sounds/
│   │       └── success.wav
│   ├── templates/
│   │   ├── accueil_connect.html
│   │   ├── accueil_inscription.html
│   │   ├── menu_principal.html
│   │   ├── mes_amis.html
│   │   ├── modifier_mon_profil.html
│   │   ├── modifier_profil_ami.html
│   │   ├── mon_profil.html
│   │   └── profil_ami.html
│   └── __init__.py
│
└── friend_book/
    ├── asgi.py
    ├── settings.py
    ├── urls.py
    ├── wsgi.py
    └── __init__.py
```

---

## 🔮 Roadmap

Fonctionnalités prévues pour les prochaines versions :

- 🔐 Authentification via réseaux sociaux (Google, LinkedIn)
- 📩 Système de messagerie entre amis
- 🧠 Recommandation intelligente de profils selon les compétences
- 📊 Statistiques de réseau et visualisation des connexions
- 🌍 Déploiement sur un serveur distant (Heroku, Render, etc.)

---

## 🤝 Contribuer

Les contributions sont les bienvenues ! Pour participer :

1. Fork le dépôt  
2. Crée une branche (`git checkout -b feature/ma-fonctionnalite`)  
3. Commits tes modifications (`git commit -m 'Ajout d'une nouvelle fonctionnalité'`)  
4. Push ta branche (`git push origin feature/ma-fonctionnalite`)  
5. Ouvre une Pull Request  

N’hésite pas à ouvrir une issue pour discuter d’une idée ou d’un bug.

---

## 👤 Auteur

Développé avec passion par **Rodrigue Nguetsa**  
💡 *“Le code est une langue universelle, et FriendBook veut en faire un pont entre les talents du monde entier.”*


