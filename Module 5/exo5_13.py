"""
L’exercice est le même que le précédent, mais ici, si les paramètres ont le type attendu, 
la fonction modifie la liste en place et ne retourne rien.
Si les paramètres ne sont pas valides, une erreur se produit à l’exécution.

exemple 1
l = [1, 3, 5]
my_insert(l, 4)
print(l)

doit afficher:
[1, 3, 4, 5]
"""
def my_insert(x, w):
    assert type(w) != str and type(w) != float
    if type(w) == int:
        x.append(w)
        x.sort()
 
l = [1, 3, 5]
my_insert(l, 'a')
print(l) #doit lever un AssertionError
AssertionError

exemple 1
l = [1, 3, 5]
my_insert(l, 4)
print(l) #[1, 3, 4, 5]
