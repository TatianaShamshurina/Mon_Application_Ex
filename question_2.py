"""
Exercice 02 (Python) :
Remettre en ordre alphabétique les prénoms présents dans la chaîne de caractères suivante :
chaine = "Pierre, Julien, Anne, Marie, Lucien"
Vous devez donc afficher à la fin de l'exercice, la chaîne de caractères suivante :
Anne, Julien, Lucien, Marie, Pierre
"""

chaine = "Pierre, Julien, Anne, Marie, Lucien"

chaine_liste = chaine.split(", ")
chaine_liste.sort()
chaine_en_ordre = ", ".join(chaine_liste)
print(chaine_en_ordre)