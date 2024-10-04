def portion_negatif(liste):
    """Donne la proportion de nombres strictement négatifs dans une liste

    Args:
        liste (liste): liste de nombres entiers de laquelle on veut connaitre la portion de nombres négatifs

    Returns:
        portion: un nombre entre 0 et 1 donnant la part de nombres négatifs dans la liste, si la liste est vide, le résultat est None
    """    
    portion=0
    if liste==[]:
        portion = None
    else:
        #Pour chaque tour de boucle, portion vaut le nombre de nombres négatifs rencontrés 
        for nb in liste:
            if nb <0:
                portion +=1
        portion /= len(liste)
    return portion

def test_portion_negatif():
    assert(portion_negatif([4,-2,8,2,-2,-7]) == 0.5)
    assert(portion_negatif([]) == None)
    assert(portion_negatif([5,4,89,5,8,8,4,6,4,8,4,8,4]) == 0)
    assert(portion_negatif([-5,-8,-5,-87,-96,-3,-2,-7]) == 1)
