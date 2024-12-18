#Question 1) Pour que l'appel de la fonction soit correct, il faut que nb_lignes et colonnes
#soient tous deux positifs et inférieurs ou égaux à la taille maximale de la matrice.
#Il faut aussi que position_haut et position_gauche soient des coordonnées présentes dans la matrice.

def sous_matrice(matrice, nb_lignes, nb_colonnes, position_haut, position_gauche):
    nv_matrice = []
    for ligne in range(nb_lignes)