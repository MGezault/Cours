def somme_n_entiers(nb):
    """fait la somme des n premiers entiers

    Args:
        nb (int): Le nombre des premiers entiers desquels ont fait la somme
    Sortie:
        res (int) : La valeur de la somme des n premiers entiers
    """
    res = 0
    if (nb == 0) or (type(nb) !=int):
        pass
    else:
        #Pour chaque tour de boucle, res vaut la valeur des entiers rencontrés au tour de boucle correspondant
        for valeur in range (0,nb+1):
            res += valeur
    return res

def test_somme_n_entiers():
    assert(somme_n_entiers(4) ==10)
    assert(somme_n_entiers(0) ==0)
    assert(somme_n_entiers(7) ==28)
    assert(somme_n_entiers(15) ==120)
    assert(somme_n_entiers("qdsqd") ==0)

