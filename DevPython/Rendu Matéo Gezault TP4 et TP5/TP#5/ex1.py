def mystere_indice(liste, valeur):
    """Trouve la quatrième valeur de liste égale à valeur

    Args:
        liste ([list]): une liste d'entier dans laquelle on va chercher la valeur
        valeur ([int]): l'entier que nous allons chercher dans liste

    Returns:
        [int]: l'indice de la quatrième occurence de valeur dans la liste
    """
    yyy = 0
    for indice in range (len(liste)):
        #Au début de chaque tour de boucle, y à la valeur du nombre d'élement de la liste égale à la valeur cherchée
        if liste[indice] == valeur:
            yyy += 1
            if yyy > 3:
                #l'instruction est exécutée si on rencontre la 4e valeur de la liste égale à valeur
                return indice
    return None