"""
Écrire une fonction signature qui reçoit un paramètre identite . 
Ce paramètre est un couple (tuple de deux composantes)
dont la première composante représente un nom et la seconde un prénom.
Cette fonction doit retourner la chaîne de caractères formée du prénom suivi du nom, séparés par une espace.
"""
def signature(identite):
    return identite[1] + " " + identite[0]
 
signature(('Seurel', 'François')) #"François Seurel"
signature(('de Saint-Exupéry', 'Antoine')) #'Antoine de Saint-Exupéry'
