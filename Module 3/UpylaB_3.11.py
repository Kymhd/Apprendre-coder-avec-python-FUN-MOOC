"""
Écrire un programme qui lit sur input une valeur naturelle n et
 qui affiche à l’écran un carré de n caractères X (majuscule) de côté.
"""

n=int(input())
for i in range(0,n):
    print(n*'X')

"""
Exemple 1
Avec la donnée lue suivante :

6
le résultat à imprimer vaudra :

XXXXXX
XXXXXX
XXXXXX
XXXXXX
XXXXXX
XXXXXX
Exemple 2
Avec la donnée lue suivante :

2
le résultat à imprimer vaudra :

XX
XX
"""