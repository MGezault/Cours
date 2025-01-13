#Question 1) Pour que l'appel de la fonction soit correct, il faut que nb_lignes et colonnes
#soient tous deux positifs et inférieurs ou égaux à la taille maximale de la matrice.
#Il faut aussi que position_haut et position_gauche soient des coordonnées présentes dans la matrice.

import API_matrice2 as API

def sous_matrice(matrice, nb_lignes, nb_colonnes, position_haut, position_gauche):
    nv_matrice = []
    for ligne in range(nb_lignes): 
        nvligne = []
        for col in range(nb_colonnes):
            nvligne.append(matrice[position_gauche+ligne][position_gauche+col])
        nv_matrice.append(nvligne)
    return nv_matrice


def colle_sous_matrice(matrice, sousma,position_haut, position_gauche):
    for lig in range (API.get_nb_lignes(sousma)):
        for col in range (API.get_nb_colonnes(sousma)):
            API.set_val(matrice,lig,col,API.get_val(sousma,lig,col))
    return matrice
