def plus_long_plateau(chaine):
    """recherche la longueur du plus grand plateau d'une chaine
    Args:
        chaine (str): une chaine de caractères

    Returns:
        int: la longueur de la plus grande suite de lettres consécutives égales
    """
    lg_max = 0  # longueur du plus grand plateau déjà trouvé
    lg_actuelle = 0  # longueur du plateau actuel
    for lettre in range(len(chaine)):
        if chaine[lettre] == chaine[lettre-1]:  # si la lettre actuelle est égale à la précédente
            lg_actuelle += 1
        else:  # si la lettre actuelle est différente de la précédente
            if lg_actuelle > lg_max:
                lg_max = lg_actuelle
            lg_actuelle = 1
    if lg_actuelle > lg_max:  # cas du dernier plateau
        lg_max = lg_actuelle
    return lg_max

def test_plus_long_plateau():
    assert (plus_long_plateau("")== 0)
    assert (plus_long_plateau("a")== 1)
    assert (plus_long_plateau("fffdsfsdfsf")== 3)
    assert (plus_long_plateau("155444444565")== 6)