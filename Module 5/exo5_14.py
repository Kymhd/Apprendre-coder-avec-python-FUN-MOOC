"""
Écrire une fonction distance_mots(mot_1, mot_2) qui retourne la distance entre deux mots.
Vous pouvez supposer que les deux mots sont de même longueur, et sont écrits sans accents.

Par exemple, les mots « lire » et « bise » sont à une distance de 2, 
puisqu’il faut changer le “l” et le “r” du mot « lire » pour obtenir « bise ».
"""
def distance_mots(a, b):
    c = 0
    for y,z in zip(a,b):
        if y != z:
            c += 1
    return c
  
  distance_mots("lire", "bise") #2
  distance_mots("Python", "Python") #0
