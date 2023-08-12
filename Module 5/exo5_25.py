"""
Écrire une fonction trace(M) qui reçoit en paramètre une matrice M de taille {n}\times{n} contenant des valeurs numériques
(de type int ou float), et qui renvoie sa trace, c’est-à-dire la somme de tous les éléments de la première diagonale.

Exemple 1
L’appel suivant de la fonction :

trace([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
doit retourner :

15
En effet, 1 + 5 + 9 est égal à 15.
"""
def trace(M):
     return sum([M[i][i] for i in range(len(M))])
    #c = 0
    #for i in range(len(M)):
        #c += M[i][i]
    #return c
trace([]) #0
trace([[1,0,0],[2,4,5],[1,87,15]]) #20
