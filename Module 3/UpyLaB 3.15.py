saut=int(input())
position_cible=int(input())
position_courante=0+saut
b=100

while position_courante in range (99+saut):
    print(position_courante)
    position_courante = position_courante + saut
    if position_courante>99:
        position_courante=position_courante%b
    if position_courante == position_cible:
            print("Cible atteinte")
            break
    if position_courante == 0:
            print(position_courante)
            print("Pas trouvée")
            break