def plus_peuple(villes,population):
    """Permet de connaitre le nom de la ville la plus peuplée de la liste.

    Args:
        villes (list): la liste donnant l'ordre et les noms des villes visées
        population (list): la liste associée au nombre d'habitants des villes de la liste villes

    Returns:
        peuple: un tuple composé du nom de la ville la plus peuplée de la liste
    """    
    peuple = ()
    for elem in range(len(villes)):
        if (peuple == ()) or (peuple[1]<population[elem]):
            peuple = (villes[elem],population[elem])
    return peuple 


def test_plus_peuple():
    assert(plus_peuple(["Blois", "Bourges", "Chartres", "Châteauroux", "Dreux","Joué-lès-Tours", "Olivet", "Orléans", "Tours", "Vierzon"],[45871, 64668,  38426, 43442, 30664, 38250, 22168, 116238, 136463,25725])== ("Tours",136463))
    assert(plus_peuple(["Apagnaville","Listenbourg","Koikcity","Royan"],[84864,43754,25106,18393] == ('Apagnaville',84864)))