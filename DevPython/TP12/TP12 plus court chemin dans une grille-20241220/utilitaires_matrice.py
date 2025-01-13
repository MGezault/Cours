""" Fonctions utilitaires pour manipuler les matrices """


import API_matrice2 as matrice_util

def get_ligne(matrice,ligne):
    """renvoie sous la forme d'une liste la ligne de la matrice dont le numéro est spécifié.

    Args:
        matrice (matrice): La matrice concernée
        ligne (int): La ligne que l'on veut obtenir 

    Returns:
        list: La liste des valeurs contenue sur la ligne indiquée 
    """
    ligneres = []
    for ind in range(matrice_util.get_nb_colonnes(matrice)):
        ligneres.append(matrice_util.get_val(matrice,ligne,ind))
    return ligneres


def get_colonne(matrice,colonne):
    """renvoie sous la forme d'une liste la colonne de la matrice dont le numéro est spécifié.

    Args:
        matrice (matrice): La matrice concernée
        colonne (int): La colonne que l'on veut obtenir 

    Returns:
        list: La liste des valeurs contenue sur la colonne indiquée
        """
    col = []
    for ind in range(matrice_util.get_nb_lignes(matrice)):
        col.append(matrice_util.get_val(matrice,ind,colonne))
    return col


def get_diagonale_principale(matrice):
    """Renvoie sous la forme d'une liste la diagonale principale d'une matrice carrée

    Args:
        matrice (matrice): La matrice (carrée) concernée

    Returns:
        list: la liste des valeurs contenue sur la diagonale principale
    """
    diagonale = []
    for ind in range(matrice_util.get_nb_colonnes(matrice)):
        diagonale.append(matrice_util.get_val(matrice,ind,ind))
    return diagonale

def get_diagonale_secondaire(matrice):
    """Renvoie sous la forme d'une liste la diagonale secondaire d'une matrice carrée

    Args:
        matrice (matrice): La matrice (carrée) concernée

    Returns:
        list: la liste des valeurs contenue sur la diagonale secondaire
    """
    diagonale = []
    for ind in range(matrice_util.get_nb_colonnes(matrice)):
        diagonale.append(matrice_util.get_val(matrice, matrice_util.get_nb_colonnes(matrice)-ind-1,ind))
    return diagonale

def transpose(matrice):
    """Renvoie la transposée liste la diagonale secondaire d'une matrice donnée

    Args:
        matrice (matrice): La matrice  concernée

    Returns:
        list: la transposée de la matrice concernée sous forme de matrice plate
    """
    transpose =[]
    for col in range (matrice_util.get_nb_colonnes(matrice)):
        for ligne in range(matrice_util.get_nb_lignes(matrice)):
            transpose.append(matrice_util.get_val(matrice,ligne,col))
    return transpose


def is_triangle_inferieur(matrice):
    """indique si une matrice est triangulaire inférieure.

    Args:
        matrice (matrice): La matrice (carrée) concernée

    Returns:
        bool: True si la matrice est un carrée inférieur, False sinon
    """
    coordonnes = [(ind,ind) for ind in range(matrice_util.get_nb_colonnes(matrice))]
    for ligne in range(matrice_util.get_nb_lignes(matrice)):
        for col in range (matrice_util.get_nb_colonnes(matrice)):
            if (col >coordonnes[ligne][1]): 
                if (matrice_util.get_val(matrice,ligne,col) == 0):
                    pass
                else:
                    return False
    return True
        

def bloc(matrice , ligne , colonne , hauteur , largeur ):
    """renvoie la sous-matrice de la matrice commençant à la ligne et colonne indiquées et 
    dont les dimensions sont hauteur et largeur.


    Args:
        matrice (matrice): La matrice concernée
        ligne (int): La ligne de début de la nouvelle matrice
        colonne (int): La colonne  de début de la nouvelle matrice
        hauteur (int): la hauteur de la nouvelle matrice
        largeur (int): la largeur de la nouvelle matrice

    Returns:
        list: La nouvelle matrice avec les conditions imposées
    """
    nvmatrice= []
    for taille in range (hauteur):
        for large in range(largeur):
            nvmatrice.append(matrice_util.get_val(matrice,ligne+taille,colonne+large))
    return nvmatrice


    
