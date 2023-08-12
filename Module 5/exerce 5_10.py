"""
Écrire une fonction dupliques qui reçoit une séquence en paramètre.
La fonction doit renvoyer la valeur booléenne True si
la séquence passée en paramètre contient des éléments dupliqués, et la valeur booléenne False sinon.
"""

def dupliques(s):
    if len(set(s)) != len(s):
        return True
    return False

dupliques([1, 2, 3, 4]) #False
