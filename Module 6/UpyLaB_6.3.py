"""
Un jury doit attribuer le prix du « Codeur de l’année ».

Afin de récompenser les trois candidats ayant obtenu la meilleure moyenne, 
nous vous demandons d’écrire une fonction top_3_candidats(moyennes) 
qui reçoit un dictionnaire contenant comme clés les noms des candidats et comme valeurs la moyenne que chacun a obtenue.

Cette fonction doit retourner un tuple contenant les noms des trois meilleurs candidats, par ordre décroissant de leurs moyennes.
"""

def top_3_candidats(moyennes):
    list = []
    for i in sorted(moyennes.items(), key=lambda x: -x[1]):
        list.append(i[0])

    return tuple(list[:3])
  
  
top_3_candidats({'Candidat 7': 2, 'Candidat 2': 38, 'Candidat 6': 85,
                 'Candidat 1': 8, 'Candidat 3': 17, 'Candidat 5': 83,
                 'Candidat 4': 33}) #('Candidat 6', 'Candidat 5', 'Candidat 2')
