def premier_nombre(chaine):   
    """retourne l’indice du premier caractère contenant un chiffre dans une
chaîne de caractères.

    Args:
        chaine (str): la chaine de caractère de laquelle on retournera le premier chiffre

    Returns:
        int: l'indice du premier chiffre
    """    
    #Pour chaque tour de boucle, indice vaudra le caractère de chaine au tour de boucle correspondant
    for indice in range(len(chaine)):
        if chaine[indice].isnumeric():
            return indice
    return None

def trouve_pop(liste_ville,liste_pop,ville):
    """retourne la population de cette ville

    Args:
        liste_ville (list): la liste des villes 
        liste_pop (list): liste des populations des villes dans liste_villes
        ville (ville): la ville de laquelle on souhaite savoir la population

    Returns:
        int: la population de la ville cherchée
    """    
    #Pour chaque tour de boucle, indice vaudra l'indice du tour de boucle correspondant 
    #liste_villes[indice] vaudra le caractère de chaine au tour de boucle correspondant
    for indice in range(len(liste_ville)):
        if liste_ville[indice] == ville :
            return liste_pop[indice]
    return None


def test_premier_nombre():
    assert (premier_nombre("on est le 30/09/2021" )==10)
    assert (premier_nombre("Eh nan il n'y a pas de nombre dans celle la.")== None)
    assert(premier_nombre("Alors qu'ici : 2")==15 )
    assert(premier_nombre("")==None)

def test_trouve_pop():
    assert trouve_pop(liste_villes,population,"Blois")== 45871
    assert trouve_pop(liste_villes,population,"")== None
    assert trouve_pop(liste_villes,population,"Paris")== None
    assert trouve_pop(liste_villes,population,"Chartres")== 38426
    assert trouve_pop(liste_villes,population,"Tours")== 136463


liste_villes = ["Blois", "Bourges", "Chartres", "Châteauroux", "Dreux",
                "Joué-lès-Tours", "Olivet", "Orléans", "Tours", "Vierzon"]
population = [45871, 64668,  38426, 43442, 30664, 38250, 22168, 116238,
              136463,  25725]

