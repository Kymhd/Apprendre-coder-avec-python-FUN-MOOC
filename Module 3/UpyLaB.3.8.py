"""
Écrire un programme qui lit :

la première lettre en majuscule du nom du polyèdre ("T", "C", "O", "D" ou "I"),

la longueur de l’arête du polyèdre,

et qui imprime le volume du polyèdre correspondant.

Si la lettre lue ne fait pas partie des cinq initiales, le programme imprime le message "Polyèdre non connu".
"""

from math import *
b = input()
a = float(input())
T = (sqrt(2)/12)*a**3
C = (a**3)
O = (sqrt(2)/3) * (a**3)
D = (15+7*sqrt(5))/(4) * a**3
I = (5*((3+sqrt(5))/(12))) * a**3
if b == "T":
    print(T)
elif b == "C" :
    print(C)
elif b == "O" :
    print(O)
elif b == "D" :
    print(D)
elif b == "I" :
    print(I)
else : 
    print("Polyèdre non connu")