"""
Écrire une fonction est_adn qui reçoit une chaîne de caractères en paramètre et qui retourne True
si cette chaîne de caractères n'est pas vide et peut représenter un brin d’ADN, False sinon.
"""
def est_adn(val):              
    adn="ACGT"
    if val == "":
        return False
    for test in val:
        if test not in adn:
            return False
    return True
  
est_adn("ATGGT") #True
