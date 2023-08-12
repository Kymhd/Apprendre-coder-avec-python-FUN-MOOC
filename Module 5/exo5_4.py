"""
Écrire une fonction distance_points() qui reçoit en paramètres deux tuples de deux composantes représentant
les coordonnées de deux points et qui retourne la distance euclidienne séparant ces deux points.
Pour rappel, la distance euclidienne entre les points (x_1, y_1) et (x_2, y_2) se calcule grâce à la formule :
"""
def distance_points(x, y):
    return ((y[0] - x[0]) ** 2 + (y[1] - x[1]) ** 2) ** (1 / 2)
  
distance_points((1.0, 1.0), (2.0, 1.0)) #1.0
