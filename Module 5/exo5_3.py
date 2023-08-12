"""
Écrire une fonction duree qui reçoit deux paramètres debut et fin.
Ces derniers sont des couples (tuples de deux composantes) 
dont la première composante représente une heure et la seconde les minutes.
"""
def duree(debut, fin):
    D = debut[0]*60 + debut[1]
    F = fin[0]*60 + fin [1]
    if D < F:
        result = F - D
        H = result//60
        M = result % 60
        dur = (H,M)
    else:
        result = 1440 + (F-D)
        H = result//60
        M = result % 60
        dur = (H,M)
    return dur
 
duree ((14, 39), (18, 45)) #(4, 6)
