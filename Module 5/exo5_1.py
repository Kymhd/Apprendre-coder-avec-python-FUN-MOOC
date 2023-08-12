"""
Écrire une fonction signature qui reçoit un paramètre identite . 
Ce paramètre est un couple (tuple de deux composantes) dont la première composante représente un nom et la seconde un prénom.
"""

def signature(identite):
    return identite[1] + " " + identite[0]
    
signature(('de Saint-Exupéry', 'Antoine')) #'Antoine de Saint-Exupéry'
