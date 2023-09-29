"""
Écrire un programme qui lit un nombre entier strictement positif n et imprime une pyramide de chiffres de hauteur n (sur n lignes complètes, c'est-à-dire toutes terminées par une fin de ligne).

La première ligne imprime un “1” (au milieu de la pyramide).

La ligne i commence par le chiffre i % 10 et tant que l’on n’est pas au milieu, le chiffre suivant a la valeur suivante ((i+1) % 10).

Après le milieu de la ligne, les chiffres vont en décroissant modulo 10 (symétriquement au début de la ligne).

Notons qu’à la dernière ligne, aucune espace n’est imprimée avant d’écrire les chiffres 0123....

Exemple 1
Avec la donnée lue suivante :

1
le résultat à imprimer vaudra :

1
Exemple 2
Avec la donnée lue suivante :

2
le résultat à imprimer vaudra :

 1
232
Exemple 3
Avec la donnée lue suivante :

10
le résultat à imprimer vaudra :

         1
        232
       34543
      4567654
     567898765
    67890109876
   7890123210987
  890123454321098
 90123456765432109
0123456789876543210
Consignes
Attention, nous rappelons que votre code sera évalué en fonction de ce qu’il affiche, donc veillez à n’imprimer que le résultat attendu.

En particulier, il ne faut rien écrire à l’intérieur des appels à input (int(input()) et non int(input("Entrer un nombre : ")) par exemple), ni ajouter du texte dans ce qui est imprimé.
"""

# L'utilisateur entre la hauteur de la pyramide
n = int(input())

# Boucle pour générer chaque ligne de la pyramide
for i in range(1, n + 1):
    # Imprime des espaces pour aligner les chiffres au centre de la ligne
    print(" " * (n - i), end="")

    # Boucle pour générer les chiffres croissants de la pyramide
    for j in range(i, 2 * i):
        # Utilisation de j % 10 pour limiter les chiffres à la plage de 0 à 9
        print(j % 10, end="")

    # Boucle pour générer les chiffres décroissants de la pyramide
    for j in range(2 * i - 2, i - 1, -1):
        # Utilisation de j % 10 pour limiter les chiffres à la plage de 0 à 9
        print(j % 10, end="")

    # Ajoute une nouvelle ligne à la fin de chaque ligne de la pyramide
    print()

# L'appel à votre programme sur l'input "2" a renvoyé:
#  1
# 232
# ok	L'appel à votre programme sur l'input "3" a renvoyé:
#   1
#  232
# 34543
# ok	L'appel à votre programme sur l'input "12" a renvoyé:
#            1
#           232
#          34543
#         4567654
#        567898765
#       67890109876
#      7890123210987
#     890123454321098
#    90123456765432109
#   0123456789876543210
#  123456789010987654321
# 23456789012321098765432
# ok	L'appel à votre programme sur l'input "6" a renvoyé:
#      1
#     232
#    34543
#   4567654
#  567898765
# 67890109876