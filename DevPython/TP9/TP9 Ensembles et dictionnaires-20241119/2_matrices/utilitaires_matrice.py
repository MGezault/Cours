""" Fonctions utilitaires pour manipuler les matrices """


import API_matrice1 as matrice_util

def get_ligne(matrice,ligne):
    
    ligneres = []
    for ind in range(matrice_util.get_nb_colonnes(matrice)):
        ligneres.append(matrice_util.get_val(matrice,ligne,ind))
    return ligneres


def get_colonne(matrice,colonne):
    
    col = []
    for ind in range(matrice_util.get_nb_lignes(matrice)):
        col.append(matrice_util.get_val(matrice,ind,colonne))
    return col


def get_diagonale_principale(matrice):
    
    diagonale = []
    for ind in range(matrice_util.get_nb_colonnes(matrice)):
        diagonale.append(matrice_util.get_val(matrice,ind,ind))
    return diagonale

def get_diagonale_secondaire(matrice):
    diagonale = []
    for ind in range(matrice_util.get_nb_colonnes(matrice)):
        diagonale.append(matrice_util.get_val(matrice, matrice_util.get_nb_colonnes(matrice)-ind-1,ind))
    return diagonale

def transpose