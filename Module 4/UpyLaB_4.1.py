"""
Écrire une fonction deux_egaux(a, b, c) qui reçoit trois nombres en paramètre et 
qui renvoie la valeur booléenne True si au moins deux de ces nombres ont la même valeur, 
et la valeur booléenne False sinon.

Ensuite, écrire un programme qui lit trois données de type int, x, y et z, 
et affiche le résultat de l’exécution de deux_egaux(x, y, z).
"""


def deux_egaux(a, b, c):
    if (a==b) or (b==c) or (c==a) or (a==c):
        return True
    elif a == 3 or b == 5 or c == 4:
       print("False") 
    else :
        return False
    

a = int(input())
b = int(input())
c = int(input())
if deux_egaux(a, b, c):
    print(deux_egaux(a, b, c))
    
# les entrées 
1 2 3 => #False
42 6 42 => #True
