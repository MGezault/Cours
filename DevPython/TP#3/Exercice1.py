# exercice 1
def plus_pairs(entree):
    """Compte le nombres de nombres pairs et de nombres impairs dans une liste

    Args:
        entree (liste): une liste de nombres entiers

    Returns:
        pairs(int): le nombre de nombres pairs dans la liste
        impairs (int): le nombre de nombres impairs dans la liste
    """
    pairs = 0
    impairs = 0
    # au début de chaque tour de boucle, pairs vaut le nombre de nombre pairs dans la liste et impairs vaut le nombre de nombre impairs
    for nb in entree:
        if nb % 2 == 0:
            pairs += 1
        else:
            impairs += 1
    return pairs >= impairs

def test_plus_pairs():
    assert(plus_pairs([1,4,6,-2,-5,3,10])==True)
    assert(plus_pairs([-4,5,-11,-56,5,-11])==False)
    assert(plus_pairs([0,2,-1,-53,5,-20])==True)
    assert(plus_pairs([-3,5,-11,-51,5,-11])==False)

