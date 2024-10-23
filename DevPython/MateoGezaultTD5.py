#Exercice1
def points(sportif,bareme):
    """Retourne les résultats d'un sportif en fonction du bareme donné et des places qu'il a obtenu lors d'épreuves

    Args:
        sportif ([tuple]): contenant le nom et prénom du sportif ainsi que ses places aux épreuves
        bareme ([list]): le bareme des points des différentes épreuves

    Returns:
        [int]: le total des points obtenues lors des épreuves
    """
    total = 0
    placements=[]
    #Pour chaque tour de boucle, on stocke les placements du sportif dans une liste
    for epreuves in sportif[2:]:
        placements.append(epreuves)
    #Pour chaque tour de boucle, total vaut le nombre de points obtenues du sportif  
    for places in placements:
        total += bareme[places-1]
    return total

def test_points():
    bareme = [100, 80, 60, 40, 20]
    assert points(("Pinturault", "Alexis", 1, 4, 3), bareme) == 200
    assert points(("Shiffrin", "Michaela", 2, 1), bareme) == 180
    assert points(("Hirscher", "Marcel"), bareme) == 0
    assert points(("Vonn", "Lindsey", 4, 1, 2), bareme) == 220

def resultats(sportifs,bareme):
    """renvoie une liste de la forme nom,prenom,points à partir d'une liste non calculée et d'un barème
    Args:
        sportifs ([list]): liste de tuples représentants les sportifs et leurs classements aux différentes épreuves
        bareme ([list]): le barème des points

    Returns:
        [list]: la liste des tuples des sportifs en ayant calculé leurs points
    """
    liste=list()
    for sportif in sportifs:
        liste.append((sportif[0],sportif[1],points(sportif,bareme)))
    return liste

def test_resultats():
    bareme = [100, 80, 60, 50, 45,40,36,32]
    assert resultats([("Odermatt","Marco",3,2,8),("Schwarz","Marco",5,8,4),("Pinturault", "Alexis", 1, 4, 3)], bareme) == [("Odermatt","Marco",172),("Schwarz","Marco",127),("Pinturault", "Alexis", 210)]
    assert resultats([("Shiffrin", "Michaela", 1, 1, 1), ("Vlhova", "Petra", 2, 3, 4)],bareme)== [("Shiffrin", "Michaela", 300), ("Vlhova", "Petra", 190)]
    assert resultats([("Kilde", "Aleksander", 1, 2), ("Feuz", "Beat", 4, 3)],bareme) == [("Kilde", "Aleksander", 180), ("Feuz", "Beat", 110)]
    assert resultats([],bareme)==[]

