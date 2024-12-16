"""Init Dev : TP10"""

# =====================================================================
# Exercice 1 : Choix de modélisation et complexité
# =====================================================================
# Modélisation n°1
#pokedex_modelisation_1_romain = {("Maraiste", "Eau"),("Maraiste","Sol"),("Racaillou","Sol"),("Racaillou","Roche")}
#pokedex_modelisation_2_romain = {"Maraiste":{"Eau","Sol"},"Racaillou" : {"Sol","Roche"}
#pokedex_modelisation_3_romain = {"Sol" : {"Maraiste","Racaillou"}, "Eau": {"Maraiste"}, "Roche" : {"Racaillou"}}
# =====================================================================

# Penser à completer la fonction exemples_pokedex_v1 dans le fichier de tests

def appartient_v1(pokemon, pokedex): 
    """ 
    Renvoie True si pokemon (str) est présent dans le pokedex 
    Complexité de O(N)
    """
    for (nom,_) in pokedex:
        if pokemon == nom:
            return True
    return False


def toutes_les_attaques_v1(pokemon, pokedex): 
    """
    param: un pokedex et le nom d'un pokemon (str) qui appartient au pokedex
    resultat: renvoie l'ensemble des types d'attaque du pokemon passé en paramètre
    """
    attaques = set()
    for (nom,typeattk) in pokedex:
        if nom == pokemon:
            attaques.add(typeattk)
    return attaques


def nombre_de_v1(attaque, pokedex): 
    """
    param: un pokedex et un type d'attaque (str)
    resultat: renvoie le nombre de pokemons de ce type d'attaque
    dans le pokedex
    Complexité de O(N)
    """
    nb = 0
    for (_,typeattk) in pokedex:
        if attaque == typeattk :
            nb +=1
    return nb


def attaque_preferee_v1(pokedex):
    """
    Renvoie le nom du type d'attaque qui est la plus fréquente dans le pokedex
    Complexité de O(N)
    """
    dico_freq = dict()
    for (_,typeattk) in pokedex:
        if typeattk not in dico_freq :
            dico_freq[typeattk] = 0
        dico_freq[typeattk] +=1
    maxi = None
    for types in dico_freq:
        if maxi is None or dico_freq[types]> dico_freq[maxi]:
            maxi=types
    return maxi


# =====================================================================
# Modélisation n°2
# =====================================================================

# Penser à completer la fonction exemples_pokedex_v2 dans le fichier de tests

def appartient_v2(pokemon, pokedex):
    """ renvoie True si pokemon (str) est présent dans le pokedex 
    Complexité : O(N)"""
    for nom in pokedex:
        if pokemon == nom:
            return True
    return False


def toutes_les_attaques_v2(pokemon, pokedex):
    """
    param: un pokedex et le nom d'un pokemon (str) qui appartient au pokedex
    resultat: renvoie l'ensemble des types d'attaque du pokemon passé en paramètre
    Complexité : O(N carré)
    """
    attaques = set()
    for (nom,typeattk) in pokedex.items():
        if nom == pokemon:
            for types in typeattk:
                attaques.add(types)
    return attaques


def nombre_de_v2(attaque, pokedex):
    """
    param: un pokedex et un type d'attaque (str)
    resultat: renvoie le nombre de pokemons de ce type d'attaque
    dans le pokedex
    Complexité : O(N carré)
    """
    nb = 0
    for typeattk in pokedex.values():
        for types in typeattk:
            if attaque == types :
                nb +=1
    return nb


def attaque_preferee_v2(pokedex):
    """
    Renvoie le nom du type d'attaque qui est la plus fréquente dans le pokedex
    Complexité : O(N carré)
    """
    dico_freq = dict()
    for typeattk in pokedex.values():
        for types in typeattk:
            if types not in dico_freq :
                dico_freq[types] = 0
            dico_freq[types] +=1
    maxi = None
    for types in dico_freq:
        if maxi is None or dico_freq[types]> dico_freq[maxi]:
            maxi=types
    return maxi

# =====================================================================
# Modélisation n°3
# =====================================================================

# Penser à completer la fonction exemples_pokedex_v3 dans le fichier de tests


def appartient_v3(pokemon, pokedex):
    """ renvoie True si pokemon (str) est présent dans le pokedex 
    Complexité : O(N)"""
    for pkmn in pokedex.values():
        if pokemon in pkmn:
            return True
    return False


def toutes_les_attaques_v3(pokemon, pokedex):
    """
    param: un pokedex et le nom d'un pokemon (str) qui appartient au pokedex
    resultat: renvoie l'ensemble des types d'attaque du pokemon passé en paramètre
    Complexité : O(N)
    """
    attaques = set()
    for (typeattk,noms) in pokedex.items():
        if pokemon in noms:
            attaques.add(typeattk)
    return attaques


def nombre_de_v3(attaque, pokedex):
    """
    param: un pokedex et un type d'attaque (str)
    resultat: renvoie le nombre de pokemons de ce type d'attaque
    dans le pokedex
    Complexité : O(N)
    """
    if attaque in pokedex :
        return len(pokedex[attaque])
    return 0


def attaque_preferee_v3(pokedex):
    """
    Renvoie le nom du type d'attaque qui est la plus fréquente dans le pokedex
    Complexité : O(N)
    """
    dico_freq = dict()
    for typeattk in pokedex:
        dico_freq[typeattk] = len(pokedex[typeattk])
    maxi = None
    for types in dico_freq:
        if maxi is None or dico_freq[types]> dico_freq[maxi]:
            maxi=types
    return maxi

# =====================================================================
# Transformations
# =====================================================================

# Version 1 ==> Version 2

def v1_to_v2(pokedex_v1):
    """
    param: prend en paramètre un pokedex version 1
    renvoie le même pokedex mais en version 2
    """
    dico = dict()
    for (nom,typepk) in pokedex_v1:
        if nom not in dico:
            dico[nom]= set()
        dico[nom].add(typepk)
    return dico


# Version 1 ==> Version 2

def v2_to_v3(pokedex_v2):
    """
    param: prend en paramètre un pokedex version2
    renvoie le même pokedex mais en version3
    """
    dico = dict()
    for (nom,typepk) in pokedex_v2.items():
        for types in typepk:
            if types not in dico:
                dico[types]= set()
            dico[types].add(nom)
    return dico
