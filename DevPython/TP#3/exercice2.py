# exercice 2
def min_sup(liste_nombres, valeur):
    """trouve le plus petit nombre d'une liste supérieur à une certaine valeur

    Args:
        liste_nombres (list): la liste de nombres
        valeur (int ou float): la valeur limite du minimum recherché

    Returns:
        int ou float: le plus petit nombre de la liste supérieur à valeur
    """
    res = None
    # Pour chaque tour de boucle, res faut le plus petit nombre d'une liste supérieur à valeur rencontré 
    for elem in liste_nombres:
        if (res == None) or (valeur < elem < res):
            res = elem
    return res


def test_min_sup():
    assert min_sup([8, 12, 7, 3, 9, 2, 1, 4, 9], 5) == 7
    assert min_sup([-2, -5, 2, 9.8, -8.1, 7], 0) == 2
    assert min_sup([5, 7, 6, 5, 7, 3], 10) is None,"3"
    assert min_sup([], 5) is None
