import os,json

os.system("clear")

with open('index.json', 'r') as json_file:
    new_dico = json.load(json_file)

# Demande à l'utilisateur de spécifier l'extension et le mot
user = input("Entrer le mot à rechercher et l'extension (ex: mot type:.py, ou simplement mot): ").split()

#initialise la variable ext à None si aucun extension spécifié par défaut
ext = None
#extraire le premier élément de la liste user et le stocke dans la variable mot_rechercher
mot_rechercher = user[0]

# Si l'utilisateur a spécifié une extension, la récupérer
if len(user) == 2 and user[1].startswith("type:"):
    #extraire la partie de la saisie utilisateur après la chaîne "type:"
    ext = user[1][len("type:"):]

# Recherche dans le dictionnaire en fonction du mot recherché et de l'extension
for mot, resultats in new_dico.items():
    if mot_rechercher in mot:
        for resultat in resultats:
            chemin = resultat['chemin']
            ligne = resultat['ligne']

           #divise le chemin complet en deux parties : le nom de fichier et l'extension
          #lower(): pour conversion en minuscle  
            extension=os.path.splitext(chemin)[1].lower()
            
            # Vérifier à la fois le mot clé et l'extension si spécifiée
            if (ext is None or ext.lower() in extension) and mot_rechercher in ligne:
                print(resultat)