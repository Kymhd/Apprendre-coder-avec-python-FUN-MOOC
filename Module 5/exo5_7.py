"""
Écrire une fonction plus_grand_bord(w) qui reçoit un mot w et retourne le plus grand bord de ce mot.
On dit qu’un mot u est un bord du mot w si u est à la fois un préfixe strict et un suffixe strict de w, 
c’est-à-dire qu’on retrouve le mot u au début et à la fin du mot w, sans que u soit égal à w lui-même.
"""
def plus_grand_bord(w):
    n = len(w)
    bord = ""
    i = 0
    for i in range(n):
        if w[0:i] == w[-i:]:
            bord = w[0:i]
    return bord
  
plus_grand_bord('abdabda') #'abda'
