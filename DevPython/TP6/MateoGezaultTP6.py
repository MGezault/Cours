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
    """calcule le nombre moyen de spécimens observés dans une liste d’observations et renvoie None si la liste est vide

    Args:
        liste_obse (list): la liste des tuples d'une liste d'observation 

    Returns:
        (float) ou (None): Renvoie None si la liste est vide ou alors renvoie la moyenne des spécimens observés pour chaque espèce
    """
    moyenne= 0
    #a chaque tour de boucle, observes vaut le plus grand nombre de spécimens observé
    for oiseaux in liste_obse:
        moyenne += oiseaux[1]
    if len(liste_obse)!=0:
        return (moyenne/len(liste_obse))
    return None

def total_famille(liste_obse,liste_oiseaux,famille):
    """calcule le nombre total de spécimens observés pour une famille d’oiseaux à partir d’une liste d’oiseaux et 
             d’une liste d’observations
    Args:
        liste_obse (list): la liste des tuples d'une liste d'observation 
        liste_oiseaux (list): la liste des tuples contenant des noms d'oiseaux associés à leur famille
        famille(str): Une famille d'oiseau pour laquelle nous allons chercher son nombre occurences


    Returns:
        (int) : le nombre de fois qu'un oiseau de la famille a été observé
    """
    total=0
    familleoiseau= recherche_par_famille(liste_oiseaux,famille)
    #De l'indice 0 à i, familleoiseau[n] contiendra le nom d'un oiseau
    for i in range (len(familleoiseau)):
        familleoiseau[i]= familleoiseau[i][0]
    #a chaque tour de boucle, la variable total contient le nombre total d'observations des oiseaux de la famille spécifiée dans liste_obse 
    for bird in liste_obse:
        if bird[0] in familleoiseau:
            total += bird[1]
    return total

#Exercice 4

def construire_liste_observations(liste_oiseau,liste_comptage):
    """à partir d’une liste d’oiseaux et d’une liste de comptage crée une liste d’observations

    Args:
        liste_oiseau (list): Une liste de noms d'oiseaux
        liste_comptage (list): une liste de comptage

    Returns:
        list: une liste d'observation contenant le nom d'oiseau à l'indice i et le nb de fois qu'il a été compté 
    """
    liste_obse=list()
    #A l'indice i, liste_obse est égal au tuple de liste_oiseau[i] et liste_comptage[i]
    for i in range(len(liste_oiseau)):
        if liste_comptage[i]!=0:
            liste_obse.append((liste_oiseau[i][0],liste_comptage[i]))
    return liste_obse