def tous_true(nb):
    """initialise une liste de nb booléens tous à True sauf les deux premiers.

    Args:
        nb (entier): le nombre de booléen dans la liste

    Returns:
        list: liste de booléens tous à True sauf les deux premiers
    """    
    if nb ==0:
        liste = [False]
    else:
        liste = [False,False]+[True]*(nb-1)
    return liste

def supprime_multiples(liste,nb):
    """ met à False tous les booléens d’indice multiple de x (sauf celui de x lui-même)

    Args:
        liste (list): liste de booléens
        nb (int): l'entier desquels nous allons mettre les multiples à False

    Returns:
        list: Une liste de booléens dont les multiples de nb ont été mis a False
    """    
    if nb != 0 and nb !=1:
        for indice in range(len(liste)):
            if (indice % nb == 0) and indice != nb:
                liste[indice] = False
        return liste
    

def crible(nb):
    """implémente le crible pour les N premiers entiers

    Args:
        nb (int): le nombre qui va servir de limite au crible d'Eratosthène

    Returns:
        list: la liste des premiers entiers jusqu'à nb
    """
    liste= tous_true(nb)
    nb_premiers= []
    for nombres in range(len(liste)):
        supprime_multiples(liste,nombres)
        if (liste[nombres]):
            nb_premiers.append(nombres)
    return nb_premiers

def test_tous_true():
    assert (tous_true(2)==[False,False,True])
    assert(tous_true(1)==[False,False])
    assert (tous_true(5)==[False, False, True, True, True, True])
    assert(tous_true(0)==[False])

def test_supprime_multiples():
    assert supprime_multiples([False, False, True, True, True, True, True],2)== [False, False, True, True, False, True, False]
    assert supprime_multiples([False,False,True,True,True,True,True],3)==[False,False,True,True,True,True,False]
    assert supprime_multiples( [False,False,True,True,False,True,False,False,False,False,True],5)== [False,False,True,True,False,True,False,False,False,False,False]
    
def test_crible():
    assert crible(6)==[2,3,5]
    assert crible(10)==[2,3,5,7]
    assert crible(1) == []

print(crible(5))