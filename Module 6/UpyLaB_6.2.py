"""
Écrire une fonction calcul_prix(produits, catalogue) où :

produits est un dictionnaire contenant, comme clés, 
les produits souhaités par Monsieur Germain et comme valeurs associées, la quantité désirée de chacun d’entre eux,

catalogue est un dictionnaire contenant tous les produits du magasin avec leur prix associé.

La fonction retourne le montant total des achats de Monsieur Germain.
"""

def calcul_prix(produits, catalogue):
    somme = 0.0
    for i in catalogue:
        if i in produits:
            somme += catalogue[i] * produits[i]
    return somme
  
calcul_prix({"brocoli":2, "mouchoirs":5, "bouteilles d'eau":6},
            {"brocoli":1.50, "bouteilles d'eau":1, "bière":2,
             "savon":2.50, "mouchoirs":0.80}) #13.0
