def separation_pos_neg(liste):
    """permet de séparer les nombres positifs des nombres négatifs d’une liste de nombres
    Args:
        liste (list): Une liste d'entiers desquelles ont souhaite trier

    Returns:
        list: une chaine d'entiers positifs
        list: une chaine d'entiers négatifs
        """    
    chainepos = []
    chaineneg= []
    if len(liste)!= 0:
        #Pour chaque tour de boucle, elem prendra la valeur d'un element de liste, on viendra trier cet élement 
        # en fonction de son signe
        for elem in liste:
            if elem >= 0 :
                chainepos.append(elem)
            else:
                chaineneg.append(elem)
    return (chainepos,chaineneg) 

def test_separation_pos_neg():
    assert separation_pos_neg([-1,15,0,12,-5,7])==([15,0,12,7],[-1,-5])
    assert separation_pos_neg([48,5,-8,50,-5,0])==([48,5,50,0],[-8,-5])
    assert separation_pos_neg([])==([],[])
    assert separation_pos_neg([5,4,8,7,8,4,9,5])==([5,4,8,7,8,4,9,5],[])
    assert separation_pos_neg([-8,-5,-7,-96,-974,-9])== ([],[-8,-5,-7,-96,-974,-9])

