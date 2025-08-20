from django.shortcuts import get_object_or_404, render, redirect
from django.http import HttpRequest, HttpResponse
from django.db.models import Max
from .models import Personne
from application import models

# ============================
# VUES DE CONNEXION / INSCRIPTION
# ============================

# Affiche la page de connexion
def accueil_connect(request: HttpRequest):
    return render(request, 'accueil_connect.html')

# Traite les données de connexion envoyées par formulaire
def traitement_connection(request: HttpRequest):
    if request.method == 'POST':
        id = request.POST.get('id')
        password = request.POST.get('mot_de_passe')
        me = Personne.objects.filter(id=id, mot_de_passe=password).count()
        if me == 1:
            personne = Personne.objects.get(id=id)
            context = {'personne': personne}
            return render(request, 'menu_principal.html', context)
    
    # Si l'identifiant ou le mot de passe est incorrect
    message_derreur = f"L'identifiant {id} n'existe pas ou le mot de passe saisi est incorrect"
    context = {'erreur': message_derreur}
    return render(request, 'accueil_connect.html', context)

# Affiche la page d'inscription
def accueil_inscription(request: HttpRequest):
    return render(request, 'accueil_inscription.html')

# Traite les données d'inscription envoyées par formulaire
def traitement_inscription(request: HttpRequest):
    if request.method == 'POST':
        id = len(Personne.objects.all()) + 1  # Génère un nouvel ID simple
        nom = request.POST.get('nom')
        prenom = request.POST.get('prenom')
        age = request.POST.get('age')
        mot_de_passe = request.POST.get('mot_de_passe')
        
        # Crée une nouvelle personne
        p = Personne.objects.create(id=id, nom=nom, prenom=prenom, age=age, mot_de_passe=mot_de_passe)
        message_de_reussite_dinscription = f"Inscription réussie, votre id est {p.id}"
        context = {'message_de_reussite_dinscription': message_de_reussite_dinscription}
        return render(request, 'accueil_connect.html', context)
    
    # Si la méthode n'est pas POST
    context = {'erreur': 'Activité illicite détectée'}
    return render(request, 'accueil_inscription', context)

# ============================
# VUES DU PROFIL UTILISATEUR
# ============================

# Affiche le profil de l'utilisateur
def mon_profil(request: HttpRequest):
    id = request.GET.get('id')
    personne = get_object_or_404(Personne, pk=id)
    return render(request, 'mon_profil.html', {'personne': personne})

# Affiche le formulaire de modification du profil
def modifier_mon_profil(request: HttpRequest):
    id = request.GET.get('id')
    personne = get_object_or_404(Personne, pk=id)
    return render(request, 'modifier_mon_profil.html', {'personne': personne})

# Valide et enregistre les modifications du profil
def valider_les_modifications_de_mon_profil(request):
    if request.method == 'POST':
        personne_id = request.POST.get('id')
        personne = get_object_or_404(Personne, pk=personne_id)

        # Mise à jour des champs
        personne.nom = request.POST.get('nom')
        personne.prenom = request.POST.get('prenom')
        personne.age = request.POST.get('age')
        personne.domaine_dactiviter = request.POST.get('domaine_dactiviter')
        personne.niveau_detude = request.POST.get('niveau_detude')
        personne.telephone = request.POST.get('telephone')
        personne.universite_actuel = request.POST.get('universite_actuel')
        personne.ville = request.POST.get('ville')
        personne.pays = request.POST.get('pays')
        personne.mot_de_passe = request.POST.get('mot_de_passe')

        personne.save()
        return render(request, 'mon_profil.html', {'personne': personne})
    
    return HttpResponse("Erreur : méthode POST attendue")

# ============================
# VUES DE GESTION DES AMIS
# ============================

# Affiche la liste des amis (tous les autres utilisateurs)
def mes_amis(request: HttpRequest):
    id = request.GET.get('id')
    personne = get_object_or_404(Personne, pk=id)
    amis = Personne.objects.exclude(id=id)
    return render(request, 'mes_amis.html', {'amis': amis, 'personne': personne})

# Affiche le profil d’un ami
def profil_ami(request: HttpRequest):
    id = request.GET.get('id')
    id_ami = request.GET.get('id_ami')
    ami = get_object_or_404(Personne, pk=id_ami)
    return render(request, 'profil_ami.html', {'id': id, 'ami': ami})

# Retourne à la liste des amis avec un message optionnel
def retour_listes_amis(request: HttpRequest):
    id = request.GET.get('id')
    personne = get_object_or_404(Personne, pk=id)
    amis = Personne.objects.exclude(id=id)
    message = request.GET.get('message')
    return render(request, 'mes_amis.html', {
        'amis': amis,
        'personne': personne,
        'message': message
    })

# Affiche le formulaire de modification du profil d’un ami
def modifier_profil_ami(request: HttpRequest):
    id = request.GET.get('id')
    id_ami = request.GET.get('id_ami')
    ami = get_object_or_404(Personne, pk=id_ami)
    return render(request, 'modifier_profil_ami.html', {'ami': ami, 'id': id})

# Valide et enregistre les modifications du profil d’un ami
def valider_les_modifications_de_profil_ami(request: HttpRequest):
    if request.method == 'POST':
        id = request.POST.get('id')
        ami_id = request.POST.get('id_ami')
        ami = get_object_or_404(Personne, pk=ami_id)

        # Mise à jour des champs
        ami.nom = request.POST.get('nom')
        ami.prenom = request.POST.get('prenom')
        ami.age = request.POST.get('age')
        ami.domaine_dactiviter = request.POST.get('domaine_dactiviter')
        ami.niveau_detude = request.POST.get('niveau_detude')
        ami.telephone = request.POST.get('telephone')
        ami.universite_actuel = request.POST.get('universite_actuel')
        ami.ville = request.POST.get('ville')
        ami.pays = request.POST.get('pays')
        ami.mot_de_passe = request.POST.get('mot_de_passe')

        ami.save()
        return render(request, 'profil_ami.html', {'ami': ami, 'id': id})
    
    return HttpResponse("Erreur : méthode POST attendue")

# Retour au menu principal depuis le profil
def retour_mon_profil_to_menu(request: HttpRequest):
    id = request.GET.get('id')
    personne = get_object_or_404(Personne, pk=id)
    return render(request, 'menu_principal.html', {'personne': personne})

# Supprime un ami de la base de données
def supprimer_ami(request: HttpRequest):
    if request.method == 'POST':
        id = request.POST.get('id')
        id_ami = request.POST.get('id_ami')
        ami = get_object_or_404(Personne, pk=id_ami)
        ami.delete()
        return redirect(f'/retour_listes_amis?id={id}&message=Ami supprimé avec succès')
    return HttpResponse("Méthode non autorisée")

# Ajoute un nouvel ami à la base
def ajouter_ami(request):
    if request.method == 'POST':
        nom = request.POST['nom']
        prenom = request.POST['prenom']
        age = request.POST['age']
        id_ami = get_next_available_id()
        Personne.objects.create(id=id_ami, nom=nom, prenom=prenom, age=age)
        return redirect('/retour_listes_amis?id=12&message=Ami ajouté avec succès')

# Génère le prochain ID disponible pour une nouvelle personne
def get_next_available_id():
    dernier_id = Personne.objects.aggregate(max_id=Max('id'))['max_id']
    return str(int(dernier_id or 0) + 1)
