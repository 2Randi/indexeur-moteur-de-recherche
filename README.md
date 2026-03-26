# Indexeur & Moteur de Recherche

Ce projet propose un mini moteur de recherche local, composé de deux scripts Python :

- indexation.py → parcourt le répertoire courant, lit tous les fichiers, extrait les mots et  génère un fichier index.json contenant les mots trouvés dans les fichiers
- recherche.py → permet de rechercher un mot dans cet index, avec filtrage optionnel par extension

#### Fichiers du projet
*indexation.py* 
Script qui parcourt les fichiers (selon ta logique interne) et génère un fichier index.json contenant une structure du type :
```
{
  "mot": [
    {
      "chemin": "chemin/vers/fichier.ext",
      "ligne": "contenu de la ligne où apparaît le mot"
    }
  ]
}
```
*recherche.py*  
Script qui :

- charge index.json
- demande à l’utilisateur une saisie du type :
```mot```
ou
```mot type:.py```
- affiche les résultats (dictionnaires) correspondant.

#### Utilisation
1. Générer l’index
Placezdans le répertoire où se trouvent vos fichiers, puis lance :
```
python indexation.py
```
Un fichier index.json est alors créé

2. Lancer la recherche

```
python recherche.py
```
Le script affiche :
```
Entrer le mot à rechercher et l'extension (ex: mot type:.py, ou simplement mot):
```
Tapez ensuite le mo ou mot avec extension 
Recherche simple (sans extension)

```
mot
```

```
mot type:.extension
```

Le script :

- découpe ta saisie avec `.split()`
- le premier élément est le mot recherché (`mot_rechercher`)
- le deuxième élément, s’il existe et commence par `type:`, est l’extension (`.py`, `.txt`, etc.)
- parcourt `new_dico` (chargé depuis `index.json`)
- pour chaque entrée :
  - vérifie que `mot_rechercher` est contenu dans la clé `mot`
  - récupère `chemin` et `ligne`
  - extrait l’extension réelle du fichier avec `os.path.splitext(chemin)[1].lower()`
  - si une extension a été donnée, vérifie qu’elle est bien contenue dans l’extension du fichier
  - vérifie aussi que `mot_rechercher` est présent dans `ligne`
- affiche chaque `resultat` qui correspond, par exemple :

```
{'chemin': 'main.py', 'ligne': 'print("bonjour")'}
```
#### Technologies
- Python 3.x
- Modules : os, json
