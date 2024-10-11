#Exercice 2)
def somme_totale(liste_art):
    """renvoie la somme totale des prix des articles d’une liste d’articles.
        Paramètre :
        articles (type: liste de tuples) : Une liste d'articles où chaque article est un tuple.
        Résultat :
        (type: float) : La somme des prix de tous les articles dans la liste.
    """
    total = 0
    for elem in liste_art:
        total += elem[2]
    return total

def test_somme_totale():
    assert somme_totale([(152, "Chaussures", 37.5), (145, "Veste", 87.2), (147, "T-shirt", 25.3), (165, "Bonnet", 11.0)]) ==161.0
    assert somme_totale([(152, "Chaussures", 10.0), (145, "Veste", 10.0), (147, "T-shirt", 10.0), (165, "Bonnet", 11.0)]) == 41.0
    assert somme_totale([]) == 0
    assert somme_totale([(152, "Chaussures", 102.0), (145, "Veste", 10.5), (147, "T-shirt", 10.0), (165, "Bonnet", 11.0)])==133.5


def plus_cher(liste_art):
    """ Renvoiel’article le plus cher d’une liste d’articles. Si il y en a plusieurs on veut le premier trouvé.
    Paramètres :
    articles (type: liste de tuples) : Une liste d'articles où chaque article est un tuple.
    Résultat :
    (type: tuple ou None) : L'article avec le prix le plus élevé. None si liste vide
    """ 
    le_plus_cher= None
    for elem in liste_art:
        if le_plus_cher is None or le_plus_cher[2]<elem[2]:
            le_plus_cher= elem
    return le_plus_cher

def test_plus_cher():
    assert plus_cher([(152, "Chaussures", 37.5), (145, "Veste", 87.2), (147, "T-shirt", 25.3), (165, "Bonnet", 11.0)]) ==(145, "Veste", 87.2)
    assert plus_cher([(152, "Chaussures", 122.0), (145, "Veste", 122.0), (147, "T-shirt", 10.0), (165, "Bonnet", 11.0)]) == (152, "Chaussures", 122.0)
    assert plus_cher([]) == None
    assert plus_cher([(152, "Chaussures",-122.0), (145, "Veste", 122.0), (147, "T-shirt", 10.0), (165, "Bonnet", 11.0)])==(145, "Veste", 122.0)
