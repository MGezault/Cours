def somme_pairs(liste):
    """Retourne la somme des nombres pairs d’une liste d’entiers

    Args:
        liste (list): liste de nombres entiers

    Returns:
        somme: entier representant le total des nombres pairs dans la liste
    """    
    somme = 0
    #Pour chaque tour de boucle, somme vaut la somme de tous les éléments pairs de la liste rencontrés 
    for nb in liste:
        if nb %2 == 0:
            somme += nb
    return somme

def test_somme_pairs():
    assert (somme_pairs([12,13,6,5,7]) == 18)
    assert (somme_pairs([41,-2,8,4,15,7,6,5,-5]) == 16)
    assert (somme_pairs([5,4,8,1,8,48,4,8,84]) == 164)
    assert (somme_pairs([]) == 0)
    assert (somme_pairs([5,9,7,123,67,5,9]) == 0)
