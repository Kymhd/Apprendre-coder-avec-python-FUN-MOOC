""" 
Écrire une fonction init_mat(m, n) qui construit et renvoie une matrice
d’entiers initialisée à la matrice nulle et de dimension m x n.
"""

def init_mat(valeur_1, valeur_2,):
    return [[0] * valeur_2 for i in range(valeur_1)]
  
  
init_mat(2, 3) #[[0, 0, 0], [0, 0, 0]]
init_mat(0, 0) #[]
