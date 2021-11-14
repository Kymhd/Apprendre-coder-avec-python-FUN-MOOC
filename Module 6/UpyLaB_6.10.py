"""
Écrire une fonction valeurs(dico) qui doit fournir,
à partir du dictionnaire donné en paramètre, une liste des valeurs du dictionnaire triées selon leur clé.
"""
def valeurs(dico):
    return [dico[i] for i in sorted(dico.keys())]
    #d = []
    #for i in sorted(dico.keys()):
        #d.append(dico[i])
    #return d
    
valeurs({'three': 'trois', 'two': 'deux', 'one': 'un'}) #['un', 'trois', 'deux']
