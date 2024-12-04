# ==========================
# La maison qui rend fou
# ==========================

#Question 1)
#On l'obtient d'Astus
#On l'obtient de Saudepus


def quel_guichet(mqrf, guichet):
    """Détermine le nom du guichet qui délivre le formulaire A-38

    Args:
        mqrf (dict): représente une maison qui rend fou
        guichet (str): le nom du guichet de départ qui est le nom d'un guichet de la mqrf

    Returns:
        str: le nom du guichet qui finit par donner le formulaire A-38
    """
    nv_guichet = guichet
    infini = False
    while  not(infini) and not(mqrf[nv_guichet] is None) :
        nv_guichet,guichet_precedent = mqrf[nv_guichet],nv_guichet
        if mqrf[nv_guichet] == guichet_precedent:
            infini = True
            nv_guichet = None
    return nv_guichet


def quel_guichet_v2(mqrf, guichet):
    """Détermine le nom du guichet qui délivre le formulaire A-38
    ainsi que le nombre de guichets visités

    Args:
        mqrf (dict): représente une maison qui rend fou
        guichet (str): le nom du guichet de départ qui est le nom d'un guichet de la mqrf

    Returns:
        tuple: le nom du guichet qui finit par donner le formulaire A-38 et le nombre de
        guichets visités pour y parvenir
    """
    nv_guichet = guichet
    infini = False
    visites = 1
    while  not(infini) and not(mqrf[nv_guichet] is None) :
        nv_guichet,guichet_precedent = mqrf[nv_guichet],nv_guichet
        visites +=1
        if mqrf[nv_guichet] == guichet_precedent:
            infini = True
    if infini : 
        return None
    return (nv_guichet,visites)

#Question 4)
#Cela créé une boucle infinie.


def quel_guichet_v3(mqrf, guichet):
    """Détermine le nom du guichet qui délivre le formulaire A-38
    ainsi que le nombre de guichets visités

    Args:
        mqrf (dict): représente une maison qui rend fou
        guichet (str): le nom du guichet de départ qui est le nom d'un guichet de la mqrf

    Returns:
        tuple: le nom du guichet qui finit par donner le formulaire A-38 et le nombre de
        guichets visités pour y parvenir
        S'il n'est pas possible d'obtenir le formulaire en partant du guichet de depart,
        cette fonction renvoie None
    """
    nv_guichet = guichet
    visites = 1
    while  not(visites> len(mqrf)) and not(mqrf[nv_guichet] is None) :
        nv_guichet = mqrf[nv_guichet]
        visites +=1
    if (visites> len(mqrf)) : 
        return None
    return (nv_guichet,visites)


