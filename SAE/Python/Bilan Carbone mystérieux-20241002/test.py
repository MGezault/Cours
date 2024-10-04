def annee(activite):
    """
    Retourne l'année d'une activité
    Args:
        activite (tuple): une activité

    Returns:
        str: l'année de l'activité
    """
    res = ""
    for chiffre in range (4):
        res+= activite[1][chiffre]
    return res

