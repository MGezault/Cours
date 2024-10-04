def derniere_voyelle(phrase):
    """retourne la dernière voyelle d’une chaîne de caractères

    Args:
        phrase (str): une phrase ou un mot auquel on recherche a retourner la dernière voyelle

    Returns:
        voyelle : dernière voyelle d’une chaîne de caractères ou None s'il n'y a pas de voyelle
    """    
    #Pour chaque tour de boucle, voyelle vaut la dernière voyelle rencontrée
    voyelle = None
    for cara in phrase:
        if cara in "aeiouy":
            voyelle=cara
    return voyelle

def test_derniere_voyelle():
    assert(derniere_voyelle("bonjour")=="u")
    assert(derniere_voyelle("fgkushioazhdafhzieoufbziufbaiufbaif")=="i")
    assert(derniere_voyelle("aqsdfghjklmlkjhgfdsqsdfghjkl")=="a")
    assert(derniere_voyelle("aeiouieaoiueoiueoiaeuaoieuaoiyyeyuaioyyyeuoiu")=="u")
    assert(derniere_voyelle("qsdfghjkklmnbvcxqsdfghjk")is None)

