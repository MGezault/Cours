def suite_syracuse(val_init,nb):
    """Permet de calculer le terme Un d’une suite de Syracuse

    Args:
        val_init (int): La valeur à laquelle on veut commencer la suite de syracuse
        nb (int): le nombre de répétitions de la suite de Syracuse
    Sortie:
        total(float): la valeur finale de la suite 
    """
    total = val_init
    #Pour chaque valeur de boucle, total vaut la valeur de la suite de Syracuse au n-ième terme de la suite
    for n in range(1,nb+1):
        if total %2 == 0:
            total //=2
        else:
            total =3*total +1   
    return total

def test_suite_syracuse():
    assert (suite_syracuse(6,2)==10.0)
    assert (suite_syracuse(6,1)==3.0)
    assert (suite_syracuse(15,0)==15)
    assert (suite_syracuse(6,4)==16.0)
