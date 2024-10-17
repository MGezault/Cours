#Exercice1
#Le probleme vient du fait qu'on essaye de comparer un tuple avec None

oiseaux = [("Merle", "Turtidé"), ("Moineau", "Passereau"), ("Mésange", "Passereau"),
           ("Pic vert", "Picidae"), ("Pie", "Corvidé"), ("Pinson", "Passereau"),
           ("Rouge-gorge", "Passereau"), ("Tourterelle", "Colombidé")] 

def oiseau_le_plus_observe(liste_observations):
    """ recherche le nom de l'oiseau le plus observé de la liste
        (si il y en a plusieur on donne le 1er trouve)

    Args:
        liste_observations (list): une liste de tuples (nom_oiseau, nb_observes)

    Returns:
        str: l'oiseau le plus observé (None si la liste est vide)
    """
    oiseau_max = None
    for indice in range(len(liste_observations)):
        if (oiseau_max is None) or (liste_observations[indice][1] > oiseau_max[1]):
            oiseau_max = liste_observations[indice]
    try:
        return oiseau_max[0]
    except:
        return None

    
#Exercice 2 

def recherche_oiseau (liste_oiseau,oiseau):
    """permet de retrouver les caractéristiques (nom,famille) d’un oiseau dans
une liste d’oiseaux à partir de son nom

    Args:
        liste_oiseau (list): liste de tuple contenant l'oiseau recherché
        oiseau(str): le nom de l'oiseau

    Returns:
        tuple: Le nom et la famille de l'oiseau
    """
    #A chaque itération de la boucle, le nom de l'oiseau n'a pas encore été trouvé
    for ioiseau in liste_oiseau:
        if ioiseau[0]== oiseau:
           return ioiseau
    return None

def recherche_par_famille(liste_oiseau,famille):
    """permet de retrouver tous les oiseaux d’une même famille dans une liste d’oiseaux

    Args:
        liste_oiseau (list): liste de tuple parmi lesquels on va chercher tous les oiseaux de la famille
        famille (str): La famille de laquelle on cherche a connaitre tous les oiseaux 

    Returns:
        list: la liste de tous les oiseaux de la famille donnée
    """
    meme_famille=[]
    #Meme_famille contient tous les oiseaux de la famille donnée de l'indice 0 à l'indice correspondant
    for oiseaux in liste_oiseau:
        if oiseaux[1]== famille:
            meme_famille.append(oiseaux)
    return meme_famille



#Exercice 3

def est_liste_observations(liste_obse):
    """vérifie qu’une liste est bien une liste d’observations

    Args:
        liste_obse (list): la liste des tuples d'une liste d'observation

    Returns:
        bool: est une liste d'observation ou non
    """
    dernierelettre="a"
    #A chaque occurence de la boucle, la valeur de liste_obse est une valeur correcte d'une liste d'observation
    for tuples in liste_obse:
        try:
            if not((type(tuples[0]) == str)and (type(tuples[1])== int)and (tuples[1]>0) and (tuples[0][0]<=dernierelettre)):
                return False
        except:
            return False
    return True


def max_observations(list_observations):
    """Donne le plus grand nombre de spécimens observés dans une liste
d’observations

    Args:
        list_observations (list): la liste des tuples d'une liste d'observation

    Returns:
        int : le plus grand nombre d'observation d'un meme spécimen
    """
    observes = 0
    #a chaque tour de boucle, observes vaut le plus grand nombre de spécimens observé
    for oiseaux in list_observations:
        if oiseaux[1] > observes:
            observes = oiseaux[1]
    return observes

def moyenne_oiseaux_observes(liste_obse):
        
    somme= 0
    #a chaque tour de boucle, observes vaut le plus grand nombre de spécimens observé
    for oiseaux in liste_obse:
        somme += oiseaux[1]
    if len(liste_obse!=0):
        return (somme/len(liste_obse))
    return None
