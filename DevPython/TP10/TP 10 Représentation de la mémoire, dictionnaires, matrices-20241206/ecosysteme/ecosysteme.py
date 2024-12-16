"""
Init Dev : TP10
Exercice 2 : Ecosystème
"""

def extinction_immediate(ecosysteme, animal):
    """
    renvoie True si animal s'éteint immédiatement dans l'écosystème faute
    de nourriture
    """
    if ecosysteme[animal] is None:
        return False
    return not(ecosysteme[animal] in ecosysteme)


def en_voie_disparition(ecosysteme, animal):
    """
    renvoie True si animal s'éteint est voué à disparaitre à long terme
    """
    chaine_alimentaire = [animal]
    while (chaine_alimentaire[-1] in ecosysteme) and not(ecosysteme[chaine_alimentaire[-1]] in chaine_alimentaire):
            chaine_alimentaire.append(ecosysteme[chaine_alimentaire[-1]])
    if  (chaine_alimentaire[-1] is None) or (chaine_alimentaire[-1] in ecosysteme):
        return False
    return True
        
        
    


def animaux_en_danger(ecosysteme):
    """ renvoie l'ensemble des animaux qui sont en danger d'extinction immédiate"""
    endanger = set()
    for animaux in ecosysteme:
        if extinction_immediate(ecosysteme,animaux):
            endanger.add(animaux)
    return endanger


def especes_en_voie_disparition(ecosysteme):
    """ renvoie l'ensemble des animaux qui sont en voués à disparaitre à long terme
    """
    endanger = set()
    for animaux in ecosysteme:
        if en_voie_disparition(ecosysteme,animaux):
            endanger.add(animaux)
    return endanger




