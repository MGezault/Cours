# TP8 B - Manipuler des listes, ensembles et dictionnaires


def total_animaux(troupeau):
    """ Calcule le nombre total d'animaux dans un troupeau

    Args:
        troupeau (dict): un dictionnaire modélisant un troupeau {nom_animaux: nombre}

    Returns:
        int: le nombre total d'animaux dans le troupeau
    """
    total = 0
    #A chaque tour de boucle, total contient la globalité de toutes les valeurs des éléments rencontrés 
    for animaux in troupeau.values():
        total += animaux
    return total  
    
def tous_les_animaux(troupeau):
    """ Détermine l'ensemble des animaux dans un troupeau

    Args:
        troupeau (dict): un dictionnaire modélisant un troupeau {nom_animaux: nombre}

    Returns:
        set: l'ensemble des animaux du troupeau
    """
    animaux= set()
    #Tous les animaux rencontrés ont été ajouté à la liste animaux
    for animal in troupeau:
        animaux.add(animal)
    return animaux


def specialise(troupeau):
    """ Vérifie si le troupeau contient 30 individus ou plus d'un même type d'animal 

    Args:
        troupeau (dict): un dictionnaire modélisant un troupeau {nom_animaux: nombre}

    Returns:
        bool: True si le troupeau contient 30 (ou plus) individus d'un même type d'animal,
        False sinon 
    """
    #Parmi tous les élements rencontrés, aucun animal n'a plus de 30 représentant
    for (_,nb) in troupeau.items():
        if nb >=30:
            return True
    return False


def le_plus_represente(troupeau):
    """ Recherche le nom de l'animal qui a le plus d'individus dans le troupeau
    
    Args:
        troupeau (dict): un dictionnaire modélisant un troupeau {nom_animaux: nombre}

    Returns:
        str: le nom de l'animal qui a le plus d'individus  dans le troupeau
        None si le troupeau est vide) 
    
    """
    maxi= None
    maxinom= None
    #A chaque tour de boucle, maxi contient le nom de l'animal le plus représenté associé à son nombre d'individu
    for (nom,nb) in troupeau.items():
        if maxi is None or nb>maxi :
            maxi =nb
            maxinom=nom
    return maxinom

def quantite_suffisante(troupeau):
    """ Vérifie si le troupeau contient au moins 5 individus de chaque type d'animal

    Args:
        troupeau (dict): un dictionnaire modélisant un troupeau {nom_animaux: nombre}

    Returns:
        bool: True si le troupeau contient au moins 5 individus de chaque type d'animal
        False sinon    
    """
    #Pour chaque tour de boucle, tous les élements rencontrés ont plus de 5 individus 
    for nb in troupeau.values():
        if nb<5:
            return False 
    return True

def reunion_troupeaux(troupeau1, troupeau2):
    """ Simule la réunion de deux troupeaux

    Args:
        troupeau1 (dict): un dictionnaire modélisant un premier troupeau {nom_animaux: nombre}
        troupeau2 (dict): un dictionnaire modélisant un deuxième troupeau        

    Returns:
        dict: le dictionnaire modélisant la réunion des deux troupeaux    
    """
    troupeau=troupeau1.copy()
    for (cle,val) in troupeau2.items():
        if cle in troupeau:
            troupeau[cle] += val
        else:
            troupeau[cle]=val
    return troupeau

#Exercice 2)



def intelligence_moyenne(dico):
    """Calcule l'intelligence moyenne d'un dictionnaire de personnages

    Args:
        dico (dict): un dictionnaire de personnages

    Returns:
        float: la statistique d'intelligence moyenne de la liste donnée
    """
    intel_tot=0
    #Pour chaque tour de boucle, intel_tot contient toutes les valeurs d'intelligence rencontrées
    for intel in dico.values():
        intel_tot+=intel[1]
    return intel_tot/len(dico.values())

def kikelplusfort(dico):
    """REnvoie le personnage le plus fort

    Args:
        dico (dict): un dictionnaire de personnages

    Returns:
        str: Le nom du personnage le plus fort
    """
    nomfort=None
    fort=None
    #Parmi tous les élements rencontrés, nomfort est le personnage le plus fort
    for (nom,(force,_,_)) in dico.items():
        if fort is None or fort<force:
            nomfort= nom
            fort= force
    return nomfort

def combiendecretins(dico):
    """Calcule le nombre de personnages étant en dessous de l'intelligence moyenne

    Args:
        dico (dict): un dictionnaire de personnages
    Returns:

    """
    intel=intelligence_moyenne(dico)
    cretins=0
    #Parmi tous les élements rencontrés, il y a crétins personnages en dessous de la moyenne d'intelligence
    for (_,intelligence,_) in dico.values():
        if intelligence<intel:
            cretins+=1
    return cretins
