"""
Écrire un programme qui additionne des valeurs naturelles lues sur entrée et affiche le résultat.
La première donnée lue ne fait pas partie des valeurs à sommer. 
Elle détermine si la liste contient un nombre déterminé à l’avance de valeurs à lire ou non :

si cette valeur est un nombre positif ou nul, 
elle donne le nombre de valeurs à lire et à sommer ;

si elle est égale à -1, cela signifie qu’elle est suivie d’une 
liste de données à lire qui sera terminée par le caractère "F" signifiant 
que la liste est terminée.

Exemple 1
Avec les données lues suivantes :

4
1
3
5
7
qui indiquent qu’il y a 4 données à sommer : 1 + 3 + 5 + 7,
"""

somme = 0

while True:
    valeur = input("Entrez une valeur naturelle (ou 'F' pour terminer) : ")
    
    if valeur == 'F':
        break

    try:
        valeur = int(valeur)
        if valeur < 0:
            print("Veuillez entrer une valeur naturelle (nombre positif ou nul).")
            continue
    except ValueError:
        print("Veuillez entrer une valeur naturelle valide (nombre positif ou nul) ou 'F' pour terminer.")
        continue

    somme += valeur

print("La somme des valeurs naturelles est :", somme)


# L'appel à votre programme sur l'input "4↵1↵3↵5↵7↵" a renvoyé:
# 16
# ok	L'appel à votre programme sur l'input "-1↵1↵3↵5↵7↵21↵F↵" a renvoyé:
# 37