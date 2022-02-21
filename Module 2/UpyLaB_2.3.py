"""
Écrire un programme qui lit des valeurs de type float pour a, b et c et qui affiche la valeur de d vérifiant l'égalité \frac{a}{b} = \frac{c}{d}.
"""

a = float(input())
b = float(input())
c = float(input())
d = (b * c)/ a
print(d)

# L'appel à votre programme sur l'input "4.5↵3.5↵0.5↵" a renvoyé:
# 0.3888888888888889
