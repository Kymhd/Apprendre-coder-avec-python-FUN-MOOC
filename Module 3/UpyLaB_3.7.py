"""
Écrire un programme qui aide le croupier à déterminer la somme que le casino
doit donner au joueur.

Le programme lira, dans l’ordre, deux nombres entiers en entrée : 
le pari du joueur (représenté par un nombre entre 0 et 16, voir description plus bas),
et le numéro issu du tirage (nombre entre 0 et 12).
Le programme affichera alors le montant gagné par le joueur.
"""

paire = 13
paire2 = 16
pari = int(input()) # le pari du joueur
tirage = int(input()) #le tirage de la roulette
if pari >= 0 and pari <= 12:  # Si le résultat du tirage est compris entre 0 et 12, le joueur parie sur le chiffre qui sort.
    if pari == tirage:  # On compare le résultat du pari au tirage
        print("120" ) # Le joueur remporte 12 fois la mise de 10€
    elif pari == 14 or pari == 16 :
        print("20" )
    else:
        print("0" )
elif pari == 14 and tirage % 2 == 0:
    print("0") 
elif pari == paire and tirage % 2 != 0:
    print("0" ) 
elif pari == paire2 and tirage % 2 == 0:
    print("0" )
elif pari == paire2 and tirage == 1:
    print("0" )
else :
    print("20" )