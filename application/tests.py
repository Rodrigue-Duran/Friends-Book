from django.test import TestCase
from models import Personne


# Create your tests here.

p1 = Personne(
    id="P000001",
    nom="Dupont",
    prenom="Alice",
    age=28,
    domaine_dactiviter="Informatique",
    niveau_detude="Master",
    telephone="0601020304",
    universite_actuel="Université de Rennes",
    ville="Rennes",
    pays="France"
)

p2 = Personne(
    id="P000002",
    nom="Martin",
    prenom="Jean",
    age=35,
    domaine_dactiviter="Biologie",
    niveau_detude="Doctorat",
    telephone="0605060708",
    universite_actuel="Université de Lyon",
    ville="Lyon",
    pays="France"
)

p3 = Personne(
    id="P000003",
    nom="Nguyen",
    prenom="Linh",
    age=22,
    domaine_dactiviter="Design",
    niveau_detude="Licence",
    telephone="0611121314",
    universite_actuel="Université de Paris",
    ville="Paris",
    pays="France"
)

p4 = Personne(
    id="P000004",
    nom="Kouadio",
    prenom="Serge",
    age=30,
    domaine_dactiviter="Finance",
    niveau_detude="MBA",
    telephone="0620212223",
    universite_actuel="Université de Bordeaux",
    ville="Bordeaux",
    pays="France"
)
lp1 = [p1, p2, p3, p4]
for p in lp1:
    print(p)

#lp2 = list(Personne.objects.all())
