"""
Permet de modéliser un le_plateau de jeu avec :
    - une matrice qui contient des nombres entiers
    - chaque nombre entier correspond à un item :
      MUR, COULOIR, PERSONNAGE, FANTOME
"""
import matrice

MUR = 1
COULOIR = 0
PERSONNAGE = 2
FANTOME = 3

NORD = 'z'
OUEST = 'q'
SUD = 'w'
EST = 's'


def init(nom_fichier="./labyrinthe1.txt"):
    """Construit le plateau de jeu de la façon suivante :
        - crée une matrice à partir d'un fichier texte qui contient des COULOIR et MUR
        - met le PERSONNAGE en haut à gauche cad à la position (0, 0)
        - place un FANTOME en bas à droite
    Args:
        nom_fichier (str, optional): chemin vers un fichier csv qui contient COULOIR et MUR.
        Defaults to "./labyrinthe1.txt".

    Returns:
        le plateau de jeu avec les MUR, COULOIR, PERSONNAGE et FANTOME
    """
    matrice_lab = matrice.charge_matrice(nom_fichier)
    nb_lignes = matrice.get_nb_lignes(matrice_lab)
    nb_colonnes = matrice.get_nb_colonne(matrice_lab)
    matrice.set_val(matrice_lab,0,0,PERSONNAGE)
    matrice.set_val(matrice_lab,nb_lignes-1,nb_colonnes-1,FANTOME)
    return matrice_lab

def est_sur_le_plateau(le_plateau, position):
    """Indique si la position est bien sur le plateau

    Args:
        le_plateau (plateau): un plateau de jeu
        position (tuple): un tuple de deux entiers de la forme (no_ligne, no_colonne) 

    Returns:
        [boolean]: True si la position est bien sur le plateau
    """
    (no_ligne,no_col)=position
    (max_ligne,max_col)=(matrice.get_nb_lignes(le_plateau),matrice.get_nb_colonne(le_plateau))
    if no_ligne>=0 and no_ligne<=max_ligne and no_col>=0 and no_col <= max_col:
        return True
    return False


def get(le_plateau, position):
    """renvoie la valeur de la case qui se trouve à la position donnée

    Args:
        le_plateau (plateau): un plateau de jeu
        position (tuple): un tuple d'entiers de la forme (no_ligne, no_colonne)

    Returns:
        int: la valeur de la case qui se trouve à la position donnée ou
             None si la position n'est pas sur le plateau
    """
    pos_ok = est_sur_le_plateau(le_plateau,position)
    (no_ligne,no_colonne) = position
    if pos_ok:
        return matrice.get_val(le_plateau,no_ligne,no_colonne)
    return None


def est_un_mur(le_plateau, position):
    """détermine s'il y a un mur à la poistion donnée

    Args:
        le_plateau (plateau): un plateau de jeu
        position (tuple): un tuple d'entiers de la forme (no_ligne, no_colonne)

    Returns:
        bool: True si la case à la position donnée est un MUR, False sinon
    """
    if est_sur_le_plateau(le_plateau,position):
        (ligne,colonne) = position
        return (matrice.get_val(le_plateau,ligne,colonne)==1)
    return False


def contient_fantome(le_plateau, position):
    """Détermine s'il y a un fantôme à la position donnée

    Args:
        le_plateau (plateau): un plateau de jeu
        position (tuple): un tuple de deux entiers de la forme (no_ligne, no_colonne) 

    Returns:
        bool: True si la case à la position donnée est un FANTOME, False sinon
    """
    if est_sur_le_plateau(le_plateau,position):
        (ligne,colonne) = position
        return (matrice.get_val(le_plateau,ligne,colonne)==3)
    return False

def est_la_sortie(le_plateau, position):
    """Détermine si la position donnée est la sortie
       cad la case en bas à droite du labyrinthe

    Args:
        le_plateau (plateau): un plateau de jeu
        position (tuple): un tuple de deux entiers de la forme (no_ligne, no_colonne) 

    Returns:
        bool: True si la case à la position donnée est la sortie, False sinon
    """
    if est_sur_le_plateau(le_plateau,position):
        (max_ligne,max_col)=(matrice.get_nb_lignes(le_plateau),matrice.get_nb_colonne(le_plateau))
        return position== (max_ligne,max_col)
    return False




def deplace_personnage(le_plateau, personnage, direction):
    """déplace le PERSONNAGE sur le plateau si le déplacement est valide
       Le personnage ne peut pas sortir du plateau ni traverser les murs
       Si le déplacement n'est pas valide, le personnage reste sur place

    Args:
        le_plateau (plateau): un plateau de jeu
        personnage (tuple): la position du personnage sur le plateau
        direction (str): la direction de déplacement SUD, EST, NORD, OUEST

    Returns:
        [tuple]: la nouvelle position du personnage
    """
    equivalent = {["NORD"] : (1,0),["SUD"]: (-1,0), ["OUEST"] : (-1,0),["EST"] : (1,0) }
    nouvelle_pos = personnage+equivalent[direction]
    if est_sur_le_plateau(le_plateau,personnage) and est_sur_le_plateau(nouvelle_pos) and not(est_un_mur(nouvelle_pos)) :
        le_plateau[personnage],le_plateau[nouvelle_pos] = 2,0
        return nouvelle_pos
    return personnage

def voisins(le_plateau, position):
    """Renvoie l'ensemble des positions cases voisines accessibles de la position renseignées
       Une case accessible est une case qui est sur le plateau et qui n'est pas un mur
    Args:
        le_plateau (plateau): un plateau de jeu
        position (tuple): un tuple de deux entiers de la forme (no_ligne, no_colonne) 

    Returns:
        set: l'ensemble des positions des cases voisines accessibles
    """
    equivalent = {"NORD" : (1,0),"SUD": (-1,0), "OUEST" : (-1,0),"EST" : (1,0)}
    pos_pos= set()
    if est_sur_le_plateau(le_plateau,position):
        for direction in equivalent:
            if est_sur_le_plateau(le_plateau,((position[0]+equivalent[direction][0]),(position[1]+equivalent[direction][1])):
                pos_pos.add(direction)
    return pos_pos



def fabrique_le_calque(le_plateau, position_depart):
    """fabrique le calque d'un labyrinthe en utilisation le principe de l'inondation :
       
    Args:
        le_plateau (plateau): un plateau de jeu
        position_depart (tuple): un tuple de deux entiers de la forme (no_ligne, no_colonne) 

    Returns:
        matrice: une matrice qui a la taille du plateau dont la case qui se trouve à la
       position_de_depart est à 0 les autres cases contiennent la longueur du
       plus court chemin pour y arriver (les murs et les cases innaccessibles sont à None)
    """
    ...


def fabrique_chemin(le_plateau, position_depart, position_arrivee):
    """Renvoie le plus court chemin entre position_depart position_arrivee

    Args:
        le_plateau (plateau): un plateau de jeu
        position_depart (tuple): un tuple de deux entiers de la forme (no_ligne, no_colonne) 
        position_arrivee (tuple): un tuple de deux entiers de la forme (no_ligne, no_colonne) 

    Returns:
        list: Une liste de positions entre position_arrivee et position_depart
        qui représente un plus court chemin entre les deux positions
    """
    ...


def deplace_fantome(le_plateau, fantome, personnage):
    """déplace le FANTOME sur le plateau vers le personnage en prenant le chemin le plus court

    Args:
        le_plateau (plateau): un plateau de jeu
        fantome (tuple): la position du fantome sur le plateau
        personnage (tuple): la position du personnage sur le plateau

    Returns:
        [tuple]: la nouvelle position du FANTOME
    """
    ...
