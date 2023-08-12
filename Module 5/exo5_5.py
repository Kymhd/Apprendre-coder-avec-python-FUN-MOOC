"""
Écrire une fonction longueur(*points) qui reçoit en paramètres un nombre arbitraire de points (tuples de deux composantes), 
et retourne la longueur de la ligne brisée correspondante.
Cette longueur se calcule en additionnant les longueurs des segments formés par deux points consécutifs.
"""
def distance_points(x, y):
    return ((y[0] - x[0]) ** 2 + (y[1] - x[1]) ** 2) ** (1 / 2)
def longueur(*points):
    long=0
    for i in range(len(points)-1):
        long+=distance_points(points[i], points[i+1])      
    return long
  
longueur((1.0, 1.0), (2.0, 1.0), (3.0, 1.0)) #2.0
