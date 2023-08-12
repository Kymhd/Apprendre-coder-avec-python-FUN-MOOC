"""
Écrire une fonction anagrammes(v, w) qui renvoie la valeur booléenne True si les mots v et w sont des anagrammes.
La fonction retourne la valeur booléenne False dans le cas contraire.
"""

def anagrammes(s1, s2):
    a1 = list(s1)
    a2 = list(s2)
    for i in range(len(s1)):
        if a1.count(a1[i]) != a2.count(a1[i]) or len(s1) != len(s2):
            return False
    return True

print(anagrammes('aimer', 'xarie')) #False
anagrammes('marion', 'romina') #True
anagrammes('bonjour', 'jour') #False
