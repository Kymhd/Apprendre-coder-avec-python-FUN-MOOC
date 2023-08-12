"""
Écrire une fonction prime_numbers qui reçoit comme paramètre un nombre entier nb 
et qui renvoie la liste des nb premiers nombres premiers.
Si le paramètre n’est pas du type attendu, 
ou ne correspond pas à un nombre entier positif ou nul, la fonction renvoie None.
"""
def premier(n):
    res = True
    if n < 2:
        res = False
    else:
        for i in range(2, n):
            if n % i == 0:
                res = False
    return res

def prime_numbers(nb):
    if type(nb) != int or nb < 0:
        return None
    primes = []
    i = 2
    while (len(primes) != nb):
        if(premier(i)):
            primes.append(i)
        i+=1
    return primes 
prime_numbers(4)   #[2, 3, 5, 7]
