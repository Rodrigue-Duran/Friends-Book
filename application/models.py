from django.db import models

# Modèle représentant une personne inscrite sur FriendBook
class Personne(models.Model):
    id = models.CharField(max_length=9, primary_key=True)  # Identifiant unique (personnalisé)
    nom = models.CharField(max_length=100)  # Nom de famille
    prenom = models.CharField(max_length=100)  # Prénom
    age = models.IntegerField(blank=True)  # Âge (optionnel)
    domaine_dactiviter = models.CharField(max_length=100, blank=True)  # Domaine professionnel (optionnel)
    niveau_detude = models.CharField(max_length=100, blank=True)  # Niveau d'études (optionnel)
    telephone = models.CharField(max_length=20, blank=True)  # Numéro de téléphone (optionnel)
    universite_actuel = models.CharField(max_length=100, blank=True)  # Université actuelle (optionnel)
    ville = models.CharField(max_length=100, blank=True)  # Ville de résidence (optionnel)
    pays = models.CharField(max_length=100, blank=True)  # Pays de résidence (optionnel)
    mot_de_passe = models.CharField()  # Mot de passe (⚠️ à sécuriser avec un champ adapté)

    def __str__(self):
        # Représentation textuelle de l'objet : "Prénom Nom (ID)"
        return f"{self.prenom} {self.nom} ({self.id})"


# Modèle représentant une compétence associée à une personne
class Competence(models.Model):
    id = models.CharField(max_length=9, primary_key=True)  # Identifiant unique de la compétence
    nom = models.CharField(max_length=100)  # Nom de la compétence (ex: Python, Communication)
    level = models.CharField(max_length=100, blank=True)  # Niveau de maîtrise (optionnel)
    personne = models.ForeignKey(
        Personne, 
        on_delete=models.CASCADE,  # Supprime les compétences si la personne est supprimée
        related_name='competences'  # Permet d'accéder aux compétences via personne.competences
    )

    def __str__(self):
        # Représentation textuelle : "Compétence : nom (Niveau : level)"
        return f"Compétence : {self.nom} (Niveau : {self.level})"
