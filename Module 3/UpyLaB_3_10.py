"""
Écrire un programme qui calcule la taille moyenne (en nombre de salariés)
des Petites et Moyennes Entreprises de la région.
Les tailles seront données en entrée, chacune sur sa propre ligne, 
et la fin des données sera signalée par la valeur sentinelle -1.
Cette valeur n’est pas à comptabiliser pour le calcul de la moyenne,
mais indique que l’ensemble des valeurs a été donné.

Après l’entrée de cette valeur sentinelle -1,
le programme affiche la valeur de la moyenne arithmétique calculée.

On suppose que la suite des tailles contient toujours au moins un élément avant la valeur sentinelle -1,
et que toutes ces valeurs sont positives ou nulles.
"""

"""
entreprises = 0
sommes = 0
taille = 0
while taille != -1:
      entreprises = entreprises + 1
      taille = int(input())
      sommes = sommes + taille
entreprises -= 1
sommes += 1
moyenne = sommes  / entreprises 
print(moyenne)

"""
liste = []

valeur = 0
while valeur != -1:
    valeur = int(input())
    if valeur < 0 :
        break
    else:
        liste.append(valeur)
moyenne = sum(liste)
reponse = moyenne / len(liste)

print(reponse)


"""
12
6
7
-1

le résultat à imprimer vaudra approximativement :

8.333333333333334
"""
