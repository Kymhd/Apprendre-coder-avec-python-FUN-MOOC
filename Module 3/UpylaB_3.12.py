"""
Cet exercice propose une variante de l’exercice précédent sur le carré de X.

Écrire un programme qui lit en entrée une valeur naturelle n 
et qui affiche à l’écran un triangle supérieur droit formé de X (voir exemples plus bas).

Exemple 1
Avec la donnée lue suivante :

6
le résultat à imprimer vaudra :

XXXXXX
 XXXXX
  XXXX
   XXX
    XX
     X
"""
n=int(input())
for i in range(0,n):
    print(i*' '+(n-i)*'X')

"""
L'appel à votre programme sur l'input "15" a renvoyé:
XXXXXXXXXXXXXXX
 XXXXXXXXXXXXXX
  XXXXXXXXXXXXX
   XXXXXXXXXXXX
    XXXXXXXXXXX
     XXXXXXXXXX
      XXXXXXXXX
       XXXXXXXX
        XXXXXXX
         XXXXXX
          XXXXX
           XXXX
            XXX
             XX
              X
"""