def annee(untuple):
    """Indique si untuple respecte les conditions d'un tuple

    Args:
        untuple (tuple): Un tuple 

    Returns:
        bool : Renvoie True si untuple respecte les conditions, False s'il ne les respecte pas
    """
    if isinstance(untuple,tuple):
        if len(untuple)==4:
            if (isinstance(untuple[0],str)) and (isinstance(untuple[1],str)) and (isinstance(untuple[3],str)):
                if (len(untuple[1])==10):
                    if (isinstance(untuple[2],float)):
                        return True
    return False

def test_annee():
    assert annee(('Lucas', '2024-09-01', 67.2, 'type3'))
    assert annee(('Lucas', '1999-12-27', 70.08, 'type3'))
    # Nouveaux Asserts
    assert not(annee(('Lucas', '1999-12-27', 70.08)))
    assert not(annee(('Lucas', '5', 70.08,"type2" )))
    assert not(annee(("Sheriff",78)))
    assert annee(('Lucas', '5648-12-27', 70.08, "type1"))
    assert not(annee(()))

test_annee()