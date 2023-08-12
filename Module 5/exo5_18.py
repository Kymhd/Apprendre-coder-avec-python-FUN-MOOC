"""
Écrire une fonction my_filter qui reçoit une liste lst et une fonction booléenne f
en paramètres et renvoie une nouvelle liste constituée des éléments de lst pour lesquels la fonction f renvoie True.
Exemples
Pour tester dans votre IDE (Thonny ou PyCharm par exemple) la fonction my_filter, vous allez devoir définir 
une fonction booléenne f et la passer en argument à la fonction my_filter.

Vous pourrez donc d’abord définir la fonction f à l’aide du mot-clé def, 
mais sachez que l’on peut aussi définir directement la fonction f lors de l’appel à la
fonction my_filter en utilisant ce qu’on appelle une fonction lambda.

Il s’agit de fonctions anonymes que l’on peut utiliser au moment même.
"""


def my_filter(lis, f):
    return [i for i in lis if f(i)]


print(my_filter(['hello', 666, 42.2, 'Thierry', 1.5], lambda x: isinstance(x, str))) # ['hello', 'Thierry']
print(my_filter([-2, 0, 4, -5, -6], lambda x : x < 0)) # [-2, -5, -6]
