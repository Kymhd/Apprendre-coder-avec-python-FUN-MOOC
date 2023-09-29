"""
Dans cet exercice, nous revenons sur le petit jeu de devinette.

Écrire un programme qui génère de manière (pseudo) aléatoire un entier (nombre secret)
 compris entre 0 et 100. Ensuite, le joueur doit deviner ce nombre en utilisant le moins
   d’essais possible.

À chaque tour, le joueur est invité à proposer un nombre et le programme 
doit donner une réponse parmi les suivantes :

« Trop grand » : si le nombre secret est plus petit que la proposition 
et qu’on n’est pas au maximum d’essais

« Trop petit » : si le nombre secret est plus grand que la proposition 
et qu’on n’est pas au maximum d’essais

« Gagné en n essai(s) ! » : si le nombre secret est trouvé

« Perdu ! Le secret était nombre » : si le joueur a utilisé six essais sans trouver le nombre secret.

Exemple 1
Une partie gagnée (après la génération du nombre à deviner) :

NB : Les nombres sont les valeurs saisies par l’utilisateur,
 et les textes sont imprimés par le programme.

50
Trop grand
8
Trop petit
20
Trop petit
27
Gagné en 4 essai(s) !
"""

import random

# Génération du nombre secret
secret = random.randint(0, 100)
NB_ESSAIS_MAX = 6

for essai in range(1, NB_ESSAIS_MAX + 1):
    proposition = int(input())

    if proposition == secret:
        print(f"Gagné en {essai} essai(s) !")
        break
    elif essai == NB_ESSAIS_MAX:
        print(f"Perdu ! Le secret était {secret}")
    elif proposition < secret:
        print("Trop petit")
    else:
        print("Trop grand")


# L'appel à votre programme sur l'input "50↵75↵88↵94↵97↵95↵" avec les arguments "26" a renvoyé:
# Trop petit
# Trop petit
# Trop petit
# Trop petit
# Trop grand
# Gagné en 6 essai(s) !
# ok	L'appel à votre programme sur l'input "50↵24↵37↵43↵46↵48↵" avec les arguments "25" a renvoyé:
# Trop grand
# Trop petit
# Trop petit
# Trop petit
# Trop petit
# Gagné en 6 essai(s) !
# ok	L'appel à votre programme sur l'input "50↵24↵37↵43↵46↵44↵" avec les arguments "98" a renvoyé:
# Trop grand
# Trop petit
# Trop petit
# Trop petit
# Trop grand
# Perdu ! Le secret était 45
# ok	L'appel à votre programme sur l'input "50↵24↵37↵30↵33↵35↵" avec les arguments "73" a renvoyé:
# Trop grand
# Trop petit
# Trop grand
# Trop petit
# Trop petit
# Gagné en 6 essai(s) !