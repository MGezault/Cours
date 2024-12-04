"""Init Dev : TP9"""


# ==========================
# Petites bêtes
# ==========================

def toutes_les_familles(pokedex):
    """détermine l'ensemble des familles représentées dans le pokedex
    Complexité de O(n)

    Args:
        pokedex (list): liste de pokemon, chaque pokemon est modélisé par
        un couple de str (nom, famille)

    Returns:
        set: l'ensemble des familles représentées dans le pokedex
    """
    types=set()
    #Tous les types des pokémons rencontrés sont stockés dans types
    for (_,typepoke) in pokedex:
        if typepoke not in types :
            types.add(typepoke)
    return types

def nombre_pokemons(pokedex, famille):
    """calcule le nombre de pokemons d'une certaine famille dans un pokedex
        Complexité de O(n)

    Args:
        pokedex (list): liste de pokemon, chaque pokemon est modélisé par
        un couple de str (nom, famille)
        famille (str): le nom de la famille concernée

    Returns:
        int: le nombre de pokemons d'une certaine famille dans un pokedex
    """
    occ= 0
    #Parmi tous les élements rencontrés, il y a occ pokémons du type famille
    for (_,typepoke) in pokedex:
        if typepoke == famille:
            occ+=1
    return occ
    

def frequences_famille(pokedex):
    """Construit le dictionnaire de fréqeunces des familles d'un pokedex
        Complexité de O(n carré)


    Args:
        pokedex (list): liste de pokemon, chaque pokemon est modélisé par
        un couple de str (nom, famille)

    Returns:
        dict: un dictionnaire dont les clés sont le nom de familles (str)
        et la valeur associée est le nombre de représentants de la famille (int)
    """
    types = dict()
    #A chaque tour de boucle, tous les types rencontrés ont été stockés dans types
    for (_,typepoke) in pokedex:
        if typepoke not in types:
            types[typepoke] = nombre_pokemons(pokedex,typepoke)
    return types

def dico_par_famille(pokedex):
    """Construit un dictionnaire dont les les clés sont le nom de familles (str)
    et la valeur associée est l'ensemble (set) des noms des pokemons de cette
    famille dans le pokedex
        Complexité de O(n)

    Args:
        pokedex (list): liste de pokemon, chaque pokemon est modélisé par
        un couple de str (nom, famille)

    Returns:
        dict: un dictionnaire dont les clés sont le nom de familles (str) et la valeur associée est
        l'ensemble (set) des noms des pokemons de cette famille dans le pokedex
    """
    dico= dict()
    #A chaque tour de boucle, tous les pokémons rencontrés sont stockés en fonction de leur type dans dico
    for (nom,types) in pokedex:
        if types in dico:
            dico[types].add(nom)
        else:
            dico[types]= set()
            dico[types].add(nom)
    return dico

def famille_la_plus_representee(pokedex):
    """détermine le nom de la famille la plus représentée dans le pokedex
        Complexité de O(n)


    Args:
        pokedex (list): liste de pokemon, chaque pokemon est modélisé par
        un couple de str (nom, famille)

    Returns:
        str: le nom de la famille la plus représentée dans le pokedex
    """
    frequence = frequences_famille(pokedex)
    maxi = None
    nom= None
    #Parmi tous les types rencontrés, le type le plus représenté est le type maxi
    for (nomtype,nb_pkmn) in frequence.items():
        if maxi is None or maxi < nb_pkmn:
            maxi = nb_pkmn
            nom=nomtype
    return nom


# ==========================
# Petites bêtes (la suite)
# ==========================


def toutes_les_familles_v2(pokedex):
    """détermine l'ensemble des familles représentées dans le pokedex

    Args:
        pokedex (dict): un dictionnaire dont les clés sont les noms de pokemons et la
        valeur associée l'ensemble (set) de ses familles (str)

    Returns:
        set: l'ensemble des familles représentées dans le pokedex
    """
    types=set()
    #Tous les types des pokémons rencontrés sont stockés dans types
    for typepoke in pokedex.values():
        if typepoke not in types:
            for typediff in typepoke:
                types.add(typediff)
    return types


def nombre_pokemons_v2(pokedex, famille):
    """calcule le nombre de pokemons d'une certaine famille dans un pokedex

    Args:
        pokedex (dict): un dictionnaire dont les clés sont les noms de pokemons et la
        valeur associée l'ensemble (set) de ses familles (str)
        famille (str): le nom de la famille concernée

    Returns:
        int: le nombre de pokemons d'une certaine famille dans un pokedex
    """
    occ= 0
    #Parmi tous les élements rencontrés, il y a occ pokémons du type famille
    for typespoke in pokedex.values():
        if famille in typespoke:
            occ+=1
    return occ

def frequences_famille_v2(pokedex):
    """Construit le dictionnaire de fréqeunces des familles d'un pokedex

    Args:
        pokedex (dict): un dictionnaire dont les clés sont les noms de pokemons et la
        valeur associée l'ensemble (set) de ses familles (str)

    Returns:
        dict: un dictionnaire dont les clés sont le nom de familles (str) et la valeur
        associée est le nombre de représentants de la famille (int)
    """
    dictypes = dict()
    #A chaque tour de boucle, tous les types rencontrés ont été stockés dans types
    for typespoke in pokedex.values():
        for types in typespoke:
            if types not in dictypes:
                dictypes[types] = nombre_pokemons_v2(pokedex,types)
    return dictypes

def dico_par_famille_v2(pokedex):
    """Construit un dictionnaire dont les les clés sont le nom de familles (str)
    et la valeur associée est l'ensemble (set) des noms des pokemons de
    cette famille dans le pokedex

    Args:
        pokedex (dict): un dictionnaire dont les clés sont les noms de pokemons et la
        valeur associée l'ensemble (set) de ses familles (str)

    Returns:
        dict: un dictionnaire dont les clés sont le nom de familles (str) et la valeur associée est
        l'ensemble (set) des noms des pokemons de cette famille dans le pokedex
    """
    dico= dict()
    #A chaque tour de boucle, tous les pokémons rencontrés sont stockés en fonction de leur type dans dico
    for (nom,typespoke) in pokedex.items():
        for types in typespoke:
            if types not in dico:
                dico[types]= set()
            dico[types].add(nom)
    return dico


def famille_la_plus_representee_v2(pokedex):
    """détermine le nom de la famille la plus représentée dans le pokedex

    Args:
        pokedex (dict): un dictionnaire dont les clés sont les noms de pokemons et la
        valeur associée l'ensemble (set) de ses familles (str)

    Returns:
        str: le nom de la famille la plus représentée dans le pokedex
    """
    frequence = frequences_famille_v2(pokedex)
    maxi = None
    nom= None
    #Parmi tous les types rencontrés, le type le plus représenté est le type maxi
    for (nomtype,nb_pkmn) in frequence.items():
        if maxi is None or maxi < nb_pkmn:
            maxi = nb_pkmn
            nom=nomtype
    return nom
