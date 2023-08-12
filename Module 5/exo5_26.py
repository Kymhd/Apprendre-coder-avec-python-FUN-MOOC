"""
Une matrice M = \{m_{ij}\} de taille {n}\times{n} est dite antisymétrique lorsque, 
pour toute paire d’indices i, j, on a m_{ij} = - m_{ji}.
Écrire une fonction booléenne antisymetrique(M) qui teste si la matrice M reçue est antisymétrique.
"""

def antisymetrique(M):
    reponse = True
    for i in range(len(M)):
        for j in range(len(M[i])):
            if M[i][j] != -M[j][i]:
                return False
    return reponse
  
  
  antisymetrique([[0, 1], [1, 0]]) #False
  antisymetrique([[0, 1, 1], [-1, 0, 1], [-1, -1, 0]]) #True
