import sys, os, re,json
os.system("clear")

dico={}

def parcours (repertoire, prof) :
   #Affiche le répertoire actuel avec une indentation proportionnelle au niveau de profondeur. 
    print(" "*prof, repertoire)
   #liste de repertoire 
    liste = os.listdir(repertoire)
    for fichier in liste :
        print(fichier)
        if re.search("^[\.]", fichier) :
            #print(repertoire+"/"+fichier, "testé")
            continue
        if os.path.isdir(repertoire+"/"+fichier) :
            try:
                if os.access(repertoire+"/"+fichier, os.X_OK) and os.access(repertoire+"/"+fichier, os.R_OK) :
                    parcours(repertoire+"/"+fichier, prof + 1)
                else:
                    continue
            except UnicodeDecodeError:
                print("Erreur 1")
                continue
            except OSError as error:
                print("Erreur 2")
                continue
            except Exception as error:
                print("Erreur 3")
                continue
            except :
                print("Erreur")
                continue
       
        else :
            if fichier != "index.json" :
                #vérifier si c'est un fichier text
                fd = os.popen("file "+repertoire+"/"+fichier+" |grep -i 'text'")
                # si fichier text
                if fd.read()!='':
                    print("Ouverture du fichier ", repertoire+"/"+fichier)
                    #creation chemin 
                    chemin = os.path.join(repertoire+"/"+fichier)
                    try:
                        #ouvre le fichier et parcourt chaque ligne. 
                        with open(repertoire+"/"+fichier, 'r') as file:
                    
                            lines = file.readlines()
                            for line_number, line in enumerate(lines):
                                words = line.split()

                                for word in words:
                                    #re: expression réguliere
                                    #recherche de motifs dans un mot (word
                                    match = re.match(r'^[a-zA-Z0-9_]+$', word)
                                    
                                    if match:
                                        
                                        matched_word = match.group()
                                        for i in range(4, min(9, len(matched_word) + 1)):
                                            #itère sur des longueurs de sous-chaînes allant de 4 à la longueur maximale
                                            #min(9, len(matched_word) + 1: garantit que la longueur maximale de la sous-chaîne ne dépasse pas 9 caractères
                                            for j in range(len(matched_word) - i + 1):
                                                #À chaque itération des deux boucles, cette ligne extrait la sous-chaîne du mot, 
                                                #en commençant par la position j et en se prolongeant sur i caractères.
                                                substring = matched_word[j:j+i]
                                                if substring not in dico.keys():
                                                    dico[substring] = [{'chemin':chemin, 'ligne':line.strip()}]
                                                else:
                                                    dico[substring].append({'chemin':chemin, 'ligne':line.strip()})

    #                                matched_word = match.group()

    #                               if 4 <= len(matched_word)<= 8:
    #                                    for i in range(4, 9):
    #                                        if matched_word[:i] not in dico.keys():
    #                                            dico[matched_word[:i]] = [{'chemin':chemin, 'ligne':line.strip()}]
    #                                        else:
    #                                            if i <= len(matched_word[:i]) :
    #                                                if fichier == "indexation.py" : print('>>'+matched_word[:i]+'|')
    #                                                dico[matched_word[:i]].append({'chemin':chemin, 'ligne':line.strip()})

                    except UnicodeDecodeError:
                        pass
                    except OSError as error:
                        pass
                    except Exception as error:
                        pass

#dikan le 0 de indentation ref le manao test       
parcours(sys.argv[1], 0)
#print(dico)

#creation dico.json s'il n'existe pas, écraser s'il existe
with open('index.json', 'w') as json_file:
    #ecrire dico dans le fichier json, indentation 4 espaces 
    json.dump(dico, json_file, indent=4)

print("Résultats stockés dans 'index.json'")