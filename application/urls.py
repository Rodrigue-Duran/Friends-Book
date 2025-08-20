from django.urls import path
from . import views  # Importation des vues

urlpatterns = [
    path('', views.accueil_connect, name='page_de_connection'),  # Page d'accueil (connexion)
    path('accueil_inscription', views.accueil_inscription, name='accueil_inscription'),  # Page d'inscription
    path('traitement_connection', views.traitement_connection, name='traitement_connection'),  # Traitement de la connexion
    path("traitement_inscription", views.traitement_inscription, name='traitement_inscription'),  # Traitement de l'inscription
    path('mon_profil', views.mon_profil, name='mon_profil'),  # Affichage du profil utilisateur
    path('mes_amis', views.mes_amis, name='mes_amis'),  # Liste des amis
    path('retour_mon_profil_to_menu', views.retour_mon_profil_to_menu, name='retour_mon_profil_to_menu'),  # Retour au menu principal
    path('modifier_mon_profil', views.modifier_mon_profil, name='modifier_mon_profil'),  # Page de modification du profil
    path('valider_les_modifications_de_mon_profil', views.valider_les_modifications_de_mon_profil, name='valider_les_modifications_de_mon_profil'),  # Validation des modifications du profil
    path('profil_ami', views.profil_ami, name='profil_ami'),  # Affichage du profil d’un ami
    path('retour_listes_amis', views.retour_listes_amis, name='retour_listes_amis'),  # Retour à la liste des amis
    path('modifier_profil_ami', views.modifier_profil_ami, name='modifier_profil_ami'),  # Page de modification du profil d’un ami
    path('valider_les_modifications_de_profil_ami', views.valider_les_modifications_de_profil_ami, name='valider_les_modifications_de_profil_ami'),  # Validation des modifications du profil d’un ami
    path('supprimer_ami', views.supprimer_ami, name='supprimer_ami'),  # Suppression d’un ami
    path('ajouter_ami', views.ajouter_ami, name='ajouter_ami'),  # Ajout d’un nouvel ami
]
