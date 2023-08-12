
""" 
Afin de l’aider, nous vous demandons d’écrire une fonction correcteur(mot, liste_mots)
où mot est le mot que Joao écrit et liste_mots est une liste qui contient les mots
(ayant la bonne orthographe) que Joao est susceptible d’utiliser.
Cette fonction doit retourner le mot dont l’orthographe a été corrigée.
"""
def distance_mots(a, b):
    c = 0
    for y,z in zip(a,b):
        if y != z:
            c += 1
    return c

def correcteur(mot, liste_mots):
    for i in liste_mots:
        if len(mot) == len(i) and distance_mots(mot, i) == 1:
            return i
    return mot

print(correcteur("chat", ["chien", "chat", "train", "voiture", "bonjour", "merci"])) #chat
correcteur("bonvour", ["chien", "chat", "train", "voiture", "bonjour", "merci"]) #bonjour
