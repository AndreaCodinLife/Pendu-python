from operator import contains
from random import *
import time 
import math

#code Couleur sous forme de classe pour l'intégrer au print
class couleur:
    vert = '\033[92m' #Vert
    jaune = '\033[93m' #Jaune
    rouge = '\033[91m' #Rouge
    bleu = '\033[34m' #Bleu
    RESET = '\033[0m' #Reset couleur
# Image de pendu sous forme de sous-liste
pendu1=[["","       ","        ","      ","      ","          ","==========="],["","||/       ","||        ","||      ","||      ","||    ","||\          ","==========="],["========Y=","||/       ","||        ","||      ","||      ","||    ","||\          ","==========="],["========Y=","||/     |  ","||        ","||      ","||      ","||    ","||\          ","==========="],["========Y=","||/     |  ","||      0  ","||      ","||      ","||    ","||\          ","==========="],["========Y=","||/     |  ","||      0  ","||      | ","||      | ","||    ","||\          ","==========="],["========Y=","||/     |  ","||      0  ","||     /| ","||      | ","||    ","||\          ","==========="],["========Y=","||/     |  ","||      0  ","||     /|\ ","||      | ","||    ","||\         ","==========="],["========Y=","||/     |  ","||      0  ","||     /|\ ","||      | ","||     / ","||\          ","==========="],["========Y=","||/     |  ","||      0  ","||     /|\ ","||      | ","||     / \ ","||\          ","==========="]]

def debut():
#Début du temps:
    tps1 = time.time()
# Variables de départ:
    gagne= 0
    tentatives = 0
    pendu = 0
    scorependu = 0
    lettres = []
# On ouvre le fichier en mode 'read' :
    fichier = open("dico.txt", 'r')
# On lis le fichier :
    contenu_du_fichier = fichier.readlines()
    r=randint(1,835)
    mot = contenu_du_fichier[r]
    t= []
    for i in range(len(mot)-1): #On créé le visuel du mot à trouver
        t.append("-")
    f = str(t).strip('[]').replace(',', '').replace("'","") # on retire ce qui sert a rien pour l'utilisateur (esthétique)
    print(f)
    print(mot)
    while gagne!= 1:
        lettre=input("Écrivez une lettre: ")
        speverif = 1
        while speverif != 0:
            if len(lettre)>1:
                print(f"{couleur.rouge}Veuillez rentrer UNE SEULE LETTRE{couleur.RESET}")
                lettre=input(f"{couleur.rouge}Écrivez UNE LETTRE: {couleur.RESET}")
            else:
                if not lettre.isalnum():        # Vérifie si ce qui est rentré est une lettre ou non
                    lettre=input(f"{couleur.rouge}Écrivez UNE LETTRE: {couleur.RESET}")
                else:
                    speverif =0
                if lettre.isdigit():
                    lettre=input(f"{couleur.rouge}Écrivez UNE LETTRE: {couleur.RESET}")
                    speverif = 1
        lettre = lettre.upper() # convertie la lettre minuscule en lettre majuscule
        verif=0
        for i in range(len(mot)-1): # cherche si dans le mot il y a la lettre entrée
            if lettre in lettres and i == 0:            #On regarde si la lettre à déjà été utilisée
                print(f"{couleur.jaune}Lettre déjà utilisée{couleur.RESET}")
            if lettre == mot[i]:
                if lettre not in lettres:
                    lettres.append(lettre)
                t[i] = mot[i]
                f = str(t).strip('[]').replace(',', '').replace("'","")
                scorependu +=100
                verif=1 #On controle pour les mots dans lesquels il y a plusieurs fois la meme lettre
        lliste = str(lettres).strip('[]').replace(',', '').replace("'","")
        print(f"Lettres utilisées",lliste)   
        print(f)
        if verif !=1:
            if lettre not in lettres:
                lettres.append(lettre)
            print("La lettre n'est pas dans le mot")
            scorependu += -10
            pendu += 1
            print(*pendu1[pendu-1], sep="\n") #affiche le pendu correspondant
            lliste = str(lettres).strip('[]').replace(',', '').replace("'","")
            print(f"Lettres utilisées",lliste)
            print(f)
        tentatives +=1 # Nombre de tentatives du joueur
        if pendu==10:
            print(f"{couleur.rouge}Perdu !{couleur.RESET}")
            gagne = 1
            print(f"Le mot était {mot}")
            print("Pour rejouer tapez 1 ou une autre touche pour arrêter")
            rejouer = input("Voulez-vous rejouer ? ")
            if int(rejouer) == 1:
                menu()
            else:
                fin = "Merci d'avoir joué"
                return fin

        if t.count('-') == 0 : #On regarde si le mot a été complètement trouvé
                tps2=time.time() #le temps a la fin du jeu
                print("")
                print(f"{couleur.vert}Vous avez réussi en", tentatives,"coups !") # On affiche les résultats 
                print(f"{couleur.jaune}Vous avez terminé de pendu en",math.trunc(tps2-tps1),"secondes.")
                scorependu = scorependu-((math.trunc(tps2-tps1))*2) # Calcul du score en fonciton du temps
                print(f"{couleur.rouge}Vous avez",scorependu,"points.")
                file = open('highscores.txt', 'r') #On ouvre le fichier des meilleure score

                highest_score = 1 # On créé les valeurs défaut
                highest_score_name = ''

                for line in file:
                    line = line.strip()
                    # Vérifiez si la ligne est vide
                    if line == '':
                        continue

                    name, score = line.split()              
                    if int(score) > highest_score:              # On trie le fichier pour avoir les valeurs du meilleur score
                        highest_score = int(score)  
                        highest_score_name = name

                if scorependu > highest_score:      # on compare le meilleure score avec le score du joueur
                    nom = input('Votre nom: ')      # si oui on lui demande son nom pour lui créer le sien
                    nouveauscore= f"{nom} {scorependu}"
                    with open("highscores.txt", "a") as a_file:     # On l'ajoute au fichier des meilleurs score
                        a_file.write("\n")
                        a_file.write(nouveauscore)
                file = open('highscores.txt', 'r')

                highest_score = 1
                highest_score_name = ''

                for line in file:
                    line = line.strip()
                    # Vérifiez si la ligne est vide
                    if line == '':
                        continue

                    name, score = line.split()
                    if int(score) > highest_score:
                        highest_score = int(score)
                        highest_score_name = name


                print(f'{couleur.bleu}Le nom et le score du joueur avec le score le plus élevé:')
                print('Nom:', highest_score_name)   # On affiche le meilleur score
                print('Score:', highest_score)


                file.close()
                gagne=1 # On ferme la boucle while
                print(f"{couleur.RESET}Pour rejouer tapez 1 ou une autre touche pour arrêter !")
                rejouer = input("Voulez-vous rejouer ? ")
                if int(rejouer) == 1:
                    menu()
                    print("rejouer")
                else:
                    fin = "Merci d'avoir joué"
                    return fin
 

#Menu principal du jeu
def menu():
    print(f"{couleur.bleu}Bienvenue dans le pendu fait par {couleur.vert}Andrea{couleur.RESET}")
    print(f"{couleur.jaune}Tapez 1 pour commencer une nouvelle partie{couleur.RESET}")
    print(f"{couleur.jaune}Tapez 2 pour quitter{couleur.RESET}")

    choix=input("choix = ")
    try:
        val = int(choix)
    except ValueError:
        print("Ce n'est pas un nombre")
        menu()
    
    if int(choix) == 1:
        debut()
    if int(choix) == 2:
        fin = "Fin"
        return fin
    else:
        print("Veuillez rentrer 1 pour jouer")
        menu()

menu()