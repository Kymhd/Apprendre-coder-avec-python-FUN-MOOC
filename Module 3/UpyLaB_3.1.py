"""
Écrire un programme qui lit 3 nombres entiers, et qui, si au moins deux d’entre eux ont la même valeur,
imprime cette valeur (le programme n’imprime rien dans le cas contraire).
"""

n = int(input())
m = int(input())
s = int(input())
if n == s or n == m:
    print(n)
elif n == m or m == s:
     print(m)
    
#les entrées   
#42 42 42 ====>  #42
#1 2 3 ====>  #le programme n'affiche rien
