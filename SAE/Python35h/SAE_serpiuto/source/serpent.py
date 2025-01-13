# coding: utf-8
"""
            SAE1.02 SERPIUT'O
         BUT1 Informatique 2024-2025

    Module serpent.py
    Ce module implémente l'API permettant de gérer les informations des joueurs (idenfier à leur serpent)
"""
import arene

def Serpent(nom_joueur:str, num_joueur:int,points:int=0,positions:list=None,tps_s:int=0,tps_p:int=0,tps_m:int=0,direction:str='N')->dict:
    """Créer un joueur avec toutes les informations le concernant.

    Args:
        nom_joueur (str): nom du joueur
        num_joueur (int): numero du joueur
        points (int, optional): nombre de points attribués au joueur. Defaults to 0.
        positions (list, optional): la liste des positions occupées par le serpent sur l'arène. Defaults to None.
        tps_s (int, optional): temps restant pour le bonus surpuissance. Defaults to 0.
        tps_p (int, optional): temps restant pour le bonus protection. Defaults to 0.
        tps_m (int, optional): temps restant pour le bonus mange-mur. Defaults to 0.
        direction (str, optional): dernière direction prise par le serpent. Defaults to 'N'.

    Returns:
        dict: une dictionnaire contenant les informations du serpent
    """    
    return {
        "nom" : nom_joueur,
        "numero" :num_joueur,
        "nb_points" :points,
        "positions" :positions,
        "mangemur" :tps_m,
        "surpuissance" :tps_s,
        "protection" :tps_p,
        "direction" :direction
    }

def get_nom(serpent:dict)->str:
    """retourne le nom du joueur associé au serpent

    Args:
        serpent (dict): le serpent considéré

    Returns:
        str: le nom du joueur associé à ce serpent
    """    
    return serpent["nom"]

def get_num_joueur(serpent:dict)->int:
    """retourne le numéro du joueur associé au serpent

    Args:
        serpent (dict): le serpent considéré

    Returns:
        int: le numéro du joueur associé à ce serpent
    """   
    return serpent["numero"]

def get_points(serpent:dict)->int:
    """retourne le nombre de points du joueur associé au serpent

    Args:
        serpent (dict): le serpent considéré

    Returns:
        int: le nombre de points du joueur associé à ce serpent
    """   
    return serpent ["nb_points"]

def get_liste_pos(serpent:dict)->list:
    """retourne la liste des positions occupées par le serpent sur l'arène. La première position étant la tête du serpent

    Args:
        serpent (dict): le serpent considéré

    Returns:
        list: la liste des positions occupées par le serpent
    """
    return serpent["positions"]

def get_queue(serpent:dict)->[int,int]:
    """retourne la position (lig,col) de la queue du serpent dans l'arène

    Args:
        serpent (dict): le serpent considéré

    Returns:
        [int,int]: la position lig,col du la queue du serpent
    """    
    return serpent["positions"][-1]

def get_derniere_direction(serpent:dict)->str:
    """retourne la dernière direction choisie par le joueur pour se déplacer

    Args:
        serpent (dict): le serpent considéré

    Returns:
        str: un des caractère N S E O
    """    
    return serpent["direction"]

def get_bonus(serpent:dict)->list:
    """retourne une liste contenant les bonus obtenus par le joueur
        c'est-à-dire ceux pour lesquels le temps restant est supérieur à 0

    Args:
        serpent (dict): le serpent considéré

    Returns:
        list: la liste des bonus du joueur
    """    
    bonus = []
    if serpent["mangemur"] > 0:
        bonus.append("mangemur")
    if serpent["surpuissance"] > 0:
        bonus.append("surpuissance")
    if serpent["protection"] > 0:
        bonus.append("protection")
    return bonus



def ajouter_points(serpent:dict,nb_points:int):
    """ajoute (ou enlève) des points à un serpent

    Args:
        serpent (dict): le serpent considéré
        nb_points (int): le nombre de points à ajouter (si négatif enlève des points)
    """    
    total_points = serpent["nb_points"] + nb_points
    serpent["nb_points"] = total_points
    return serpent

def set_liste_pos(serpent:dict, tete:list):
    """initialise la liste des positions d'un serpent

    Args:
        serpent (dict): le serpent considéré
        tete (list): la liste des positions occupées par ce serpent
    """    
    serpent["positions"] = tete
    return serpent

def set_derniere_direction(serpent:dict, direction:str):
    """Met à jout la dernière direction utilisée par le serpent (utile pour l'affichage)

    Args:
        serpent (dict): le serpent considéré
        direction (str): un des caractère N S E O
    """    
    serpent["direction"] = direction
    return serpent

def to_str(serpent:dict)->str:
    """produit une chaine de caractères contenant les informations principales d'un serpent sour la forme
    Joueur 1 -> 143 s:0 m:4 p:0
    où Joueur 1 est le nom du joueur, après la flèche se trouve le nombre de point
    puis le temps restant de chaque bonus (supuissante, mange mur et protection)

    Args:
        serpent (dict): le serpent considéré

    Returns:
        str: la chaine de caractères donnant les informations principales d'un serpent 
    """    
    return serpent["nom"]+" -> "+ str(serpent["nb_points"])+" s:"+str(serpent["surpuissance"])+" m:"+str(serpent["mangemur"])+" p:"+str(serpent["protection"])
     
def get_temps_protection(serpent:dict)->int:
    """indique le temps restant pour le bonus protection

    Args:
        serpent (dict): le serpent considéré

    Returns:
        int: le nombre de tours restant pour ce bonus
    """    
    return serpent["protection"]

def get_temps_mange_mur(serpent:dict)->int:
    """indique le temps restant pour le bonus mange mur

    Args:
        serpent (dict): le serpent considéré

    Returns:
        int: le nombre de tours restant pour ce bonus
    """   
    return serpent["mangemur"]

def get_temps_surpuissance(serpent:dict)->int:
    """indique le temps restant pour le bonus surpuissance

    Args:
        serpent (dict): le serpent considéré

    Returns:
        int: le nombre de tours restant pour ce bonus
    """   
    return serpent["surpuissance"]

def ajouter_temps_protection(serpent:dict, temps:int)->int:
    """ajoute du temps supplémentaire pour le bonus protection

    Args:
        serpent (dict): le serpent considéré
        temps (int): le nombre de tours à ajouter

    Returns:
        int: le nombre de tours total restant pour ce bonus
    """    
    total_temps = serpent["protection"] + temps
    serpent["protection"] = total_temps
    return serpent

def ajouter_temps_mange_mur(serpent:dict, temps:int)->int:
    """ajoute du temps supplémentaire pour le bonus mange mur

    Args:
        serpent (dict): le serpent considéré
        temps (int): le nombre de tours à ajouter

    Returns:
        int: le nombre de tours total restant pour ce bonus
    """    
    total_temps = serpent["mangemur"] + temps
    serpent["mangemur"] = total_temps
    return serpent

def ajouter_temps_surpuissance(serpent:dict, temps:int)->int:
    """ajoute du temps supplémentaire pour le bonus surpuissance

    Args:
        serpent (dict): le serpent considéré
        temps (int): le nombre de tours à ajouter

    Returns:
        int: le nombre de tours total restant pour ce bonus
    """    
    total_temps = serpent["surpuissance"] + temps
    serpent["surpuissance"] = total_temps
    return serpent

def maj_temps(serpent:dict):
    """Décrémente les temps restant pour les bonus de ce serpent
    Attention les temps ne peuvent pas être négatif

    Args:
        serpent (dict): le serpent considéré
    """    
    bonus = ["mangemur","surpuissance","protection"]
    for boost in bonus:
        if serpent[boost]>0:
            serpent[boost]-=1
    return serpent

def serpent_2_str(serpent:dict, sep=";")->str:
    """Sérialise un serpent sous la forme d'une chaine de caractères
    contenant 2 lignes.
    nom_j;num_j;nb_points;tps_surpuissance;tps_mange_mur;tps_protection
    lig1;col1;lig2;col2;...
    La première ligne donne les informations autres que la liste des positions du serpent
    la deuxième ligne donné la liste des position du serpent en commençant par la tête
    Args:
        serpent (dict): le serpent considéré
        sep (str, optional): le caractère séparant les informations du serpent. Defaults to ";".

    Returns:
        str: la chaine de caractères contenant les toutes informations du serpent
    """    
    chaine = ""
    for cle,val in serpent.items():
        if cle != "positions":
            chaine+= str(val) + sep
    chaine= chaine[:-1]
    chaine += "\n"
    if serpent["positions"] is not None:
        for pos in serpent["positions"]:
            chaine+= str(pos) + sep
        chaine = chaine[:-1]
    else:
        chaine+= "None"
    return chaine


def serpent_from_str(la_chaine, sep=";")->dict:
    """Reconstruit un serpent à partir d'une chaine de caractères
       telle que celle produite par la fonction précédente

    Args:
        la_chaine (str): la chaine de caractères contenant les informations du serpent
        sep (str, optional): le caractère servant à séparer les informations du serpent. Defaults to ";".

    Returns:
        dict: Le serpent représenté dans la chaine de caractères
    """    
    nouvelle_chaine= la_chaine.replace("\n",";")
    liste_serp=nouvelle_chaine.split(sep)
    print(liste_serp)
    nvserpent = {
        "nom" : liste_serp[0],
        "numero" :liste_serp[1],
        "nb_points":liste_serp[2],
        "positions" : None,
        "mangemur" : liste_serp[3],
        "protection" : liste_serp[4],
        "surpuissance": liste_serp[5],
        "direction" :liste_serp[6],
    }
    if liste_serp[7] != None:
        nvpositions=[]
        for pos in range(7,len(liste_serp),2):
          nvpositions.append((liste_serp[pos],liste_serp[pos+1]))   
        nvserpent["positions"] = nvpositions
    return nvserpent

def copy_serpent(serpent:dict)->dict:
    """fait une copie du serpent passer en paramètres
    Attention à bien faire une copie de la liste des positions
    

    Args:
        serpent (dict): le serpent à recopier

    Returns:
        dict: la copie du serpent passé en paramètres
    """ 
    return {
    "nom" : get_nom(serpent),
    "numero" : get_num_joueur(serpent),
    "nb_points" : get_points(serpent),
    "positions" : get_liste_pos(serpent),
    "direction" : get_derniere_direction(serpent),
    "mangemur" :get_temps_mange_mur(serpent),
    "protection" : get_temps_protection(serpent),
    "surpuissance" : get_temps_surpuissance(serpent),
    }
