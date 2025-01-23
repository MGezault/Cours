# coding: utf-8
"""
            SAE1.02 SERPIUT'O
         BUT1 Informatique 2024-2025

    Module IA.py
    Ce module implémente toutes les fonctions ainsi que l'IA de votre serpent
"""

import matrice
import partie
import argparse
import client
import random
import arene 
import serpent
import case
direction_prec='X' # variable indiquant la décision précédente prise par le joueur. A mettre à jour soi-même

#=========================================================================================================
#liste_boites_1 = [arene.BOITE1, arene.BOITE2]
#liste_boites_2 = [arene.AJOUTE, arene.MULTIPLIE, arene.SURPUISSANCE, arene.MANGE_MUR, arene.PROTECTION]
#=========================================================================================================

####################################################################
### A partir d'ici, implémenter toutes les fonctions qui vous seront 
### utiles pour prendre vos décisions
### Toutes vos fonctions devront être documentées
####################################################################

def directions_possibles(l_arene:dict,num_joueur:int)->str:
    """Indique les directions possible pour le joueur num_joueur
        c'est à dire les directions qu'il peut prendre sans se cogner dans
        un mur, sortir de l'arène ou se cogner sur une boîte trop grosse pour sa tête

    Args:
        l_arene (dict): l'arène considérée
        num_joueur (int): le numéro du joueur

    Returns:
        str: une chaine composée de NOSE qui indique les directions
            pouvant être prise par le joueur. Attention il est possible
            qu'aucune direction ne soit possible donc la fonction peut retourner la chaine vide
    """    
    res=''
    mat=l_arene["matrice"]
    nb_lig=matrice.get_nb_lignes(mat)
    nb_col=matrice.get_nb_colonnes(mat)
    lig_dep,col_dep=serpent.get_liste_pos(l_arene["serpents"][num_joueur-1])[0]
    for dir in 'NOSE':
        delta_lig,delta_col=arene.DIRECTIONS[dir]
        lig_arr=lig_dep+delta_lig
        col_arr=col_dep+delta_col
        if lig_arr<0 or lig_arr>=nb_lig or col_arr<0 or col_arr>=nb_col:
            continue
        if case.est_mur(matrice.get_val(mat,lig_arr,col_arr)):
            continue
        if case.get_proprietaire(matrice.get_val(mat,lig_arr,col_arr))==num_joueur:
            continue
        res+=dir
    return res    

def objets_voisinage(l_arene:dict, num_joueur:int, dist_max:int):
    """Retourne un dictionnaire indiquant pour chaque direction possibles, 
        les objets ou boites pouvant être mangés par le serpent du joueur et
        se trouvant dans voisinage de la tête du serpent 

    Args:
        l_arene (dict): l'arène considérée
        num_joueur (int): le numéro du joueur considéré
        dist_max (int): le nombre de cases maximum qu'on s'autorise à partir du point de départ

    Returns:
        dict: un dictionnaire dont les clés sont des directions  et les valeurs une liste de triplets
            (coordonnees,val_objet,prop) où coordonnees indique les coordonnees de la case jusqu'à l'objet et id_objet
            val_obj indique la valeur de l'objet ou de la boite et prop indique le propriétaire de la boite
    """
    directions = {"N":[], "S":[], "E":[], "O":[]}
    nb = 0
    voisins = dict()
    coords_tete = arene.get_serpent(l_arene,num_joueur)[0] # le dictionnaire du sserpent
    coords_voisinage = {coords_tete}
    cases_tot = {coords_tete}
    while nb+1 < dist_max:
        for nb in range(dist_max):
            for case in coords_voisinage:
                if (get_serpent(l_arene,num_joueur))["tps_m"] == 0 or nb > (get_serpent(l_arene,num_joueur))["tps_m"] :
                    for direc in directions_possibles_depuis_coords(l_arene,num_joueur,case[0],case[1]):                 
                        cases_tot.add(coordonnees_boussole(case,direc))
                else:
                    cases_tot.add(coordonnees_boussole(case,direc))
            coords_voisinage = cases_tot.copy()
    for case in coords_voisinage:
        val_boite = arene.get_val_boite(l_arene,case[0],case[1])
        if case[0] < coords_tete[0] and case[1] == coords_tete[1]:
            directions["N"].append((case, val_boite, num_joueur))
        if case[0] > coords_tete[0] and case[1] == coords_tete[1]:
            directions["S"].append((case, val_boite, num_joueur))
        if case[1] < coords_tete[1] and case[0] == coords_tete[0]:
            directions["O"].append((case, val_boite, num_joueur))
        if case[1] > coords_tete[1] and case[0] == coords_tete[0]:
            directions["E"].append((case, val_boite, num_joueur))
    return directions


#================================ calques et valeurs ================================

def calque_arene(arene: dict):
    """Fonction qui créé un calque de l'arene vide sous forme de dictionnaire
       avec toutes les coordonnées de l'arene en clé et 0 en valeur

    Args:
        arene (dict): L'arene de jeux

    Returns:
        dict: Un dictionnaire avec les coordonées de chaque case de l'arene en 
              clé et 0 en valeur
    """
    calc_co = dict()
    mat_claque = []
    liste_ligne = []
    for x in range(arene["matrice"]["nb_lig"]):
        for y in range(arene["matrice"]["nb_col"]):
            liste_ligne.append(0)
        mat_claque.append(liste_ligne)
        liste_ligne = []

    mat_coordonee = []
    liste_coordonee = []
    for x in range(arene["matrice"]["nb_lig"]):
        for y in range(arene["matrice"]["nb_col"]):  
            liste_coordonee.append((x, y))
        mat_coordonee.append(liste_coordonee)
        liste_coordonee = []

    for i in range(len(mat_coordonee)):
        for j in range(len(mat_coordonee[i])):
            calc_co[mat_coordonee[i][j]] = mat_claque[i][j]

    return calc_co

def calque_serpent(position:list): 
    """Fonction qui créé un calque autour du serpent sous forme de dictionnaire
       avec comme clé des coordonnées et comme valeur des informations relative 
       au serpent

    Args:
        position (list): La position de la tete du serpent sous forme de coordonnées (x, y)
    Returns:
        dict: Un dictionnaire avec les coordonées sous forme de tuple (x, y) de 
              chaque case du calque pour clé et qui a pour valeur une liste sous 
              la forme [valeur_case, innondation], avec valeur_case qui represente 
              la valeur de la case aux dites coordonnées et innondation qui est un
              espace libre pour pouvoir effectuer la future innondation dans les 
              allentours du serpent
    """
    calc_co = dict()
    mat_claque = []
    liste_ligne = []
    for x in range(11):
        for y in range(11):
            liste_ligne.append([None, None])
        mat_claque.append(liste_ligne)
        liste_ligne = []

    mat_coordonee = []
    liste_coordonee = []
    for x in range(11):
        for y in range(11):  
            liste_coordonee.append((x+position[0]-5, y+position[1]-5))
        mat_coordonee.append(liste_coordonee)
        liste_coordonee = []
    
    for i in range(len(mat_coordonee)):
        for j in range(len(mat_coordonee[i])):
            calc_co[mat_coordonee[i][j]] = mat_claque[i][j]
    
    return calc_co
 
def valeur_calque_arene(calque_arene:dict, partie:dict):
    """Fonction qui applique les differentes valeurs de l'arene directement sur
       un claque vide

    Args:
        calque_arene (dict): Calque de l'arene sous forme de dictionnaire
        partie (dict): Structure qui contient la partie en cours

    Returns:
        dict: Un dictionnaire qui reprend calque_arene passé en parametre avec 
              les valeurs de chaque case de l'arene associé a chaque coordonné 
              de cette derniere
    """
    dim = arene.get_dim(partie["arene"])
    for co in calque_arene.keys():
        for x in range(dim[0]):
            for y in range(dim[1]):
                calque_arene[(x,y)] = matrice.get_val(partie["arene"]['matrice'], x, y)["valeur"]
    return calque_arene

def valeur_calque_serpent(calque_arene:dict, calque_serpent:dict):
    """Fonction qui applique les differentes valeurs aux allentours de serpent
       directement sur un claque vide en fonctions des valeurs du calque_arene

    Args:
        calque_arene (dict): Calque de l'arene sous forme de dictionnaire
        calque_serpent (dict): Claque du serpent avec les valeur des positions
        dans un certain rayon de 5 cases autour de lui

    Returns:
        dict: Un dictionnaire qui reprend calque_serpent passé en parametre avec 
              les valeurs de chaque cases considére par ce dernier qui sont appliqué 
              en fonction de claque_arene sur l'indice [0] des valeurs des listes. 
              L'indice [1] étant réservé pour l'innondation
    """
    for co in calque_serpent.keys():
        if co in calque_arene.keys():
            calque_serpent[co][0] = calque_arene[co]
    return calque_serpent


#====================================== chemin ======================================
def get_temps_restant(arene:dict,lig:int,col:int)-> int:
    """Fonction qui retourne le temps restant d'une case contenant une boite

    Args:
        arene (dict): L'arène considérée
        lig (int): La ligne de la case souhaité
        col (int): La colone de la case souhaité

    Returns:
        int: Un nombre qui corespond au nombres de tours restant a la boite 
        avant de disparaitre
    """
    return case.get_temps_restant(matrice.get_val(arene["matrice"],lig,col))

def coordonnees_boussole(coordonnees:tuple,direction:str):
    """Fonction qui retourne les coordonnées suivante dans une direction donnée

    Args:
        coordonnees (tuple): Les coordonnées innitials
        direction (str): La directions souhaité

    Returns:
        tuple: Un tuple qui correspond au coordonées choisis
    """
    return (coordonnees[0]+arene.DIRECTIONS[direction][0],coordonnees[1]+arene.DIRECTIONS[direction][1])

def get_serpent(l_arene:dict,num_serpent:int): #================================= docstring
    """Renvoie le nom d'un joueur grace a son numero de serpent ainsi qu'a 
       l'arene dans laquel il evolue

    Args:
        l_arene (dict): L'arene concernée
        num_serpent (int): Le numéro du serpent souhaité

    Returns:
        dict: Le serpent concerné par le num joueur
    """
    for joueur in l_arene["serpents"]:
        if joueur["num_joueur"] == num_serpent:
            return joueur
    return False

def directions_possibles_depuis_coords(l_arene:dict,num_joueur:int,lig_dep:int,col_dep:int)->str:
    """Indique les directions possible pour le joueur num_joueur
        c'est à dire les directions qu'il peut prendre sans se cogner dans
        un mur, sortir de l'arène ou se cogner sur une boîte trop grosse pour sa tête

    Args:
        l_arene (dict): L'arène considérée
        num_joueur (int): Le numéro du joueur
        lig_dep (int): La ligne de départ
        col_dep (int): La colonne de départ

    Returns:
        str: une chaine composée de NOSE qui indique les directions
            pouvant être prise par le joueur.
    """    
    res=''
    mat=l_arene["matrice"]
    nb_lig=matrice.get_nb_lignes(mat)
    nb_col=matrice.get_nb_colonnes(mat)
    for dir in 'NOSE':
        delta_lig,delta_col=arene.DIRECTIONS[dir]
        lig_arr=lig_dep+delta_lig
        col_arr=col_dep+delta_col
        if lig_arr<0 or lig_arr>=nb_lig or col_arr<0 or col_arr>=nb_col:
            continue
        if case.est_mur(matrice.get_val(mat,lig_arr,col_arr)):
            if (get_serpent(l_arene,num_joueur))["tps_m"] ==0:
              continue
            else:
                red+=dir
        if case.get_proprietaire(matrice.get_val(mat,lig_arr,col_arr))==num_joueur:
            continue
        res+=dir
    return res

def meilleure_route(calque:dict,routes:list,priorite:int):
    """Fonction qui détermine la meilleur route possible dans le calque du 
       serpent en fonction de la valeur de priorite

    Args:
        calque (dict): Le calque du serpent
        routes (list): Liste des bonus sur la route
        priorite (int): La valeur de l'objet que l'on souhaite chercher (1 pour 
        une boite de 1 point, -1 pour une boite d'adition etc...)

    Returns:
        liste: Une liste qui contient le chemin que le serpent devra effectuer 
               lors de ce tour
    """
    total_route = {}
    pt = 1
    cpt = 1
    for bonus in routes: # routes => [[()]] ,,,,,,,, bonus => [()]
        for co in bonus: # bonus => [()] ,,,,,,,, co => () (coordonnées)
            if calque[co][0] > 0:
                pt += calque[co][0]
            elif calque[co][0] in (-1,-2):
                cpt += 1
                if priorite in (-1,-2):
                    cpt += 1
            else:
                if priorite < -2:
                    if priorite == calque[co][0]:
                        cpt += 2
                        if priorite == -5:
                            cpt += 2
        if priorite > 0:
            pt = 2
        total_route[1] = [pt,cpt]
    ratio = None
    route = None
    for cle,val in total_route.items():
        distance = val / calque[cle[0]][1]
        if ratio is None or distance >ratio:
            ratio =val / distance
            route = cle
    return route

def inondation(calque:dict,depart:tuple):
    """Fonction qui fait l'innondation du calque du serpent

    Args:
        calque (dict): Claque du serpent avec les valeur des positions
        dans un certain rayon de 5 cases autour de lui
        depart (tuple): La position de départ pour commencer l'inondation 
        du calque
    
    Returns:
        Dict: Un dictionnaire qui reprend calque_serpent passé en parametre avec 
              les valeurs de chaque cases considére par ce dernier qui sont appliqué 
              en fonction de depart, en suivant le principe de l'inondation, sur 
              l'indice libre [1] des valeurs
    """
    calque[(depart[0],depart[1])][1] = 0
    ligne,colonne = depart
    modif = False
    while not modif:
        for case in calque:
            modif = True
            if case != depart:
                if calque[case][1] != None:
                    break
                ligne,colonne = case
                for dire in "NOSE":
                    ligne2,colonne2 = coordonnees_boussole((ligne,colonne),dire)
                    if (ligne2,colonne2) in calque:
                        if not (calque[(ligne2,colonne2)][0] is  None) and not (calque[(ligne2,colonne2)][1] is None): 
                            calque[ligne,colonne][1] = calque[(ligne2,colonne2)][1]+1
                            modif = False
    return calque

def genere_combinaisons(calque:dict,objets:dict,depart:tuple,coups_max:int,num_joueur:int):
    """Fonction qui renvoie la liste de toutes les combinaisons possibles d'objets parmis une liste d'objets voisins

    Args:
        calque (dict): Le calque du serpent avec l'inondation
        objets (dict): Un dictionaire avec les objets aux alentours
        depart (tuple): Position de départ sous la forme (x, y)
        coups_max (int): Le nombre de coup max
    
    Returns:
        liste: Renvois une liste de liste avec toutes les combinaisons possible pour le serpent 
    """
    combinaisons = []
    inondation(calque, depart)  
    for direction, liste_objets in objets.items():
        for case, _, _ in liste_objets:
            total = calque[case][1]
            ligne, colonne = case
            if calque[(ligne, colonne)][1] is not None and calque[(ligne, colonne)][1] <= coups_max:
                combinaison = [case] 
                route = determine_route(depart,combinaison,calque)
                for obj,_,_ in liste_objets:
                    route = determine_route(depart,combinaison,calque)
                    if obj in route or (abs(case[0]-obj[0])+abs(case[1]-obj[1])) <=coups_max:
                        combinaison.append(obj)
                combinaisons.append(combinaison) 
    return combinaisons

def determine_route(point_de_depart:list,chemin:list,calque:dict):
    """Fonction qui determine la route du serpent

    Args:
        point_de_depart (list): Position de départ du serpent
        chemin (list): Liste des positions que le serpent empruntera
        pour se déplacer
        calque (dict): Le calque du serpent

    Returns:
        str: Retourne la direction vers laquel le serpent se déplace 
    """
    arrivee= chemin[0]
    chemin = [arrivee]
    for nb in range(calque[arrivee][1]):
        mini = None
        diremini = None
        for dire in "NOSE":
            if mini == None or calque[coordonnees_boussole(chemin[-1],dire)][1] == None:
                mini = calque[coordonnees_boussole(chemin[-1],dire)][1]
                diremini = dire
            elif calque[coordonnees_boussole(chemin[-1],dire)][1] < mini:
                mini = calque[coordonnees_boussole(chemin[-1],dire)][1]
                diremini = dire
            chemin.append(coordonnees_boussole(chemin[-1],dire))
    return chemin

#======================================= sep =======================================

def mon_IA2(num_joueur:int, la_partie:dict)->str:
    """Programme principal de l'IA serpent

    Args:
        num_joueur (int): Le numero du joueur
        la_partie (dict): Structure qui contient la partie en cours

    Returns:
        str: Retourne la direction vers laquel le serpent doit se déplacer
    """
    try: 
        priorite = 1
        if la_partie["temps_restant"] >= 148:
            return mon_IA(num_joueur, la_partie)
        else:
            aren = partie.get_arene(la_partie)
            dir_pos=arene.directions_possibles(aren,num_joueur)
            tete_serp = arene.get_serpent(aren,num_joueur)[0]
            calque_are = calque_arene(aren)
            calque_serp =calque_serpent(tete_serp)
            calque_are = valeur_calque_arene(calque_are,la_partie)
            calque_serp= valeur_calque_serpent(calque_are,calque_serp)
            inonde= inondation(calque_serp,tete_serp)
            liste_objets= objets_voisinage(aren,num_joueur,6)

            if liste_objets is None: 
                return mon_IA(num_joueur, la_partie)
            combi= genere_combinaisons(inonde,liste_objets,tete_serp,5,num_joueur)
            if combi == [] or combi is None:
                return mon_IA(num_joueur,la_partie)

            route= meilleure_route(calque_serp,combi,priorite)
            direction= determine_route(tete_serp,route,calque_serp)

            taille_serpent = len(arene.get_serpent(aren,num_joueur))

            if calque_serp[tete_serp][0] == 1:
                priorite = 1
                route = meilleure_route(calque_serp,combi,priorite)
                direction = determine_route(tete_serp,route,calque_serp)[-1]

            elif calque_serp[tete_serp][0] >= 8 and taille_serpent == 1:
                priorite = -2
                route = meilleure_route(calque_serp,combi,priorite)
                direction = determine_route(tete_serp,route,calque_serp)[-1]

            elif taille_serpent >= 1 and taille_serpent <= 3 and calque_serpent(arene.get_serpent(aren,num_joueur)[1]):
                priorite = -1
                route = meilleure_route(calque_serp,combi,priorite)
                direction = determine_route(tete_serp,route,calque_serp)[-1]

            elif taille_serpent >= 5:
                priorite = -5
                route = meilleure_route(calque_serp,combi,priorite)
                direction = determine_route(tete_serp,route,calque_serp)[-1]

            else:
                priorite = 2
                route = meilleure_route(calque_serp,combi,priorite)
                direction = determine_route(tete_serp,route,calque_serp)[-1]

            return direction
    except:
        return mon_IA(num_joueur,la_partie)

def mon_IA(num_joueur:int, la_partie:dict)->str:
    """Fonction qui va prendre la decision du prochain coup pour le joueur de numéro ma_couleur

    Args:
        num_joueur (int): un entier désignant le numero du joueur qui doit prendre la décision
        la_partie (dict): structure qui contient la partie en cours

    Returns:
        str: une des lettres 'N', 'S', 'E' ou 'O' indiquant la direction que prend la tête du serpent du joueur
    """
    direction=random.choice("NSEO")
    direction_prec=direction #La décision prise sera la direction précédente le prochain tour
    dir_pos=arene.directions_possibles(partie.get_arene(la_partie),num_joueur)
    if dir_pos=='':
        direction=random.choice('NOSE')
    else:
        direction=random.choice(dir_pos)
    return direction

if __name__=="__main__":
    parser = argparse.ArgumentParser()  
    parser.add_argument("--equipe", dest="nom_equipe", help="nom de l'équipe", type=str, default='Non fournie')
    parser.add_argument("--serveur", dest="serveur", help="serveur de jeu", type=str, default='localhost')
    parser.add_argument("--port", dest="port", help="port de connexion", type=int, default=1111)
    
    args = parser.parse_args()
    le_client=client.ClientCyber()
    le_client.creer_socket(args.serveur,args.port)
    le_client.enregistrement(args.nom_equipe,"joueur")
    ok=True
    while ok:
        ok,id_joueur,le_jeu,_=le_client.prochaine_commande()
        if ok:
            la_partie=partie.partie_from_str(le_jeu)
            actions_joueur=mon_IA2(int(id_joueur),la_partie)
            le_client.envoyer_commande_client(actions_joueur)
    le_client.afficher_msg("terminé")