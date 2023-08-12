"""On considère une liste qui décrit une séquence t. Chaque élément
de cette liste est un tuple de deux composantes : le nombre de répétitions
successives de l’élément x dans la séquence t, et l’élément x lui-même.
Par exemple, la liste [(1, 'He'), (2, 'l'), (1,'o')] décrit la séquence "Hello".
Écrire une fonction decompresse qui reçoit une telle liste en paramètre et
 renvoie la séquence t sous forme d’une nouvelle liste.
"""

def decompress(x):
    # l = []
    # for i in x:
    #     for d in range(i[0]):
    #         l.append(i[1])
    # return l
    return [i[1] for i in x for d in range(i[0])]

print(decompress([(4, 1), (0, 2), (2, 'test'), (3, 3), (1, 'bonjour')]))
