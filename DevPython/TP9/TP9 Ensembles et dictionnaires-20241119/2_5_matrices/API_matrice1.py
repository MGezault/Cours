""" Matrices : API n 1 """


def matrice(nb_lignes, nb_colonnes, valeur_par_defaut):
    """crée une nouvelle matrice en mettant la valeur par défaut dans chacune de ses cases.

    Args:
        nb_lignes (int): le nombre de lignes de la matrice
        nb_colonnes (int): le nombre de colonnes de la matrice
        valeur_par_defaut : La valeur que prendra chacun des éléments de la matrice

    Returns:
        une nouvelle matrice qui contient la valeur par défaut dans chacune de ses cases
    """
    nv_matrice=[nb_lignes,nb_colonnes]
    liste=[]
    #A chaque tour de boucle, il y a un nouvel élement dans la matrice, il y a nb_elem élements dans liste
    for nb_elem in range(nb_lignes*nb_colonnes):
        liste.append(valeur_par_defaut)
    nv_matrice.append(liste)
    return nv_matrice




def set_val(la_matrice, ligne, colonne, nouvelle_valeur):
    """permet de modifier la valeur de l'élément qui se trouve à la ligne et à la colonne
    spécifiées. Cet élément prend alors la valeur nouvelle_valeur

    Args:
        la_matrice : une matrice
        ligne (int) : le numéro d'une ligne (la numérotation commence à zéro)
        colonne (int) : le numéro d'une colonne (la numérotation commence à zéro)
        nouvelle_valeur : la nouvelle valeur que l'on veut mettre dans la case

    Returns:
        None
    """
    la_matrice[2][ligne * la_matrice[1] + colonne]=nouvelle_valeur



def get_nb_lignes(la_matrice):
    """permet de connaître le nombre de lignes d'une matrice

    Args:
        la_matrice : une matrice

    Returns:
        int : le nombre de lignes de la matrice
    """
    return (la_matrice[0])


def get_nb_colonnes(la_matrice):
    """permet de connaître le nombre de colonnes d'une matrice

    Args:
        la_matrice : une matrice

    Returns:
        int : le nombre de colonnes de la matrice
    """
    return (la_matrice[1])


def get_val(la_matrice, ligne, colonne):
    """permet de connaître la valeur de l'élément de la matrice dont on connaît
    le numéro de ligne et le numéro de colonne.

    Args:
        la_matrice : une matrice
        ligne (int) : le numéro d'une ligne (la numérotation commence à zéro)
        colonne (int) : le numéro d'une colonne (la numérotation commence à zéro)

    Returns:
        la valeur qui est dans la case située à la ligne et la colonne spécifiées
    """
    return (la_matrice[2][ligne*la_matrice[1]+colonne])

# Fonctions pour l'affichage

def affiche_ligne_separatrice(la_matrice, taille_cellule=4):
    """fonction auxilliaire qui permet d'afficher (dans le terminal)
    une ligne séparatrice

    Args:
        la_matrice : une matrice
        taille_cellule (int, optional): la taille d'une cellule. Defaults to 4.
    """
    print()
    for _ in range(get_nb_colonnes(la_matrice) + 1):
        print('-'*taille_cellule+'+', end='')
    print()


def affiche(la_matrice, taille_cellule=4):
    """permet d'afficher une matrice dans le terminal

    Args:
        la_matrice : une matrice
        taille_cellule (int, optional): la taille d'une cellule. Defaults to 4.
    """
    nb_colonnes = get_nb_colonnes(la_matrice)
    nb_lignes = get_nb_lignes(la_matrice)
    print(' '*taille_cellule+'|', end='')
    for i in range(nb_colonnes):
        print(str(i).center(taille_cellule) + '|', end='')
    affiche_ligne_separatrice(la_matrice, taille_cellule)
    for i in range(nb_lignes):
        print(str(i).rjust(taille_cellule) + '|', end='')
        for j in range(nb_colonnes):
            print(str(get_val(la_matrice, i, j)).rjust(taille_cellule) + '|', end='')
        affiche_ligne_separatrice(la_matrice, taille_cellule)
    print()


# Ajouter ici les fonctions supplémentaires, sans oublier de compléter le fichier
# tests_API_matrice.py avec des fonctions de tests

def nb_lignes_nb_colonnes(nom_fic):
    with open(nom_fic, 'r') as fic:
        nb_lignes = 0
        for ligne in fic:
            nb_lignes += 1
            ligne = ligne.strip()
            ligne_split = ligne.split(',')
            nb_colonnes = 0
            for i in range(len(ligne_split)):
                nb_colonnes += 1
        return nb_lignes, nb_colonnes

def charge_matrice_str(nom_fichier):
    """permet crÃ©er une matrice de str Ã  partir d'un fichier CSV.

    Args:
        nom_fichier (str): le nom d'un fichier CSV (sÃ©parateur  ',')

    Returns:
        une matrice de str

    ComplexitÃ©s:
        O(NÂ²)
    """
    (nb_lignes, nb_colonnes) = nb_lignes_nb_colonnes(nom_fichier)
    matrice_res = matrice(nb_lignes, nb_colonnes, None)
    with open(nom_fichier, "r") as fic:
        ind_ligne = 0
        for ligne in fic:
            ligne = ligne.strip()
            ligne_split = ligne.split(",")
            ind_colonne = 0
            for valeur in ligne_split:
                if valeur.isdigit():
                    valeur = int(valeur)
                set_val(matrice_res, ind_ligne, ind_colonne, valeur)
                ind_colonne += 1
            ind_ligne += 1
        return matrice_res
    
def sauve_matrice(la_matrice, nom_fichier):
    """permet sauvegarder une matrice dans un fichier CSV.
    Attention, avec cette fonction, on perd l'information sur le type des Ã©lÃ©ments

    Args:
        matrice : une matrice
        nom_fichier (str): le nom du fichier CSV que l'on veut crÃ©er (Ã©craser)

    Returns:
        None

    ComplexitÃ©:
        O(NÂ²)
    """
    with open(nom_fichier, mode = 'w') as fic:
        nb_lignes = get_nb_lignes(la_matrice)
        nb_colonnes = get_nb_colonnes(la_matrice)
        for ligne in range(nb_lignes):
            ligne_fichier = ""
            for colonne in range(nb_colonnes):
                ligne_fichier += str(get_val(la_matrice, ligne, colonne))
                if colonne < nb_colonnes - 1:
                    ligne_fichier += ","
            ligne_fichier += "\n"
            fic.write(ligne_fichier)