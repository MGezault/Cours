import motdepasse

# --------------------------------------
# FONCTIONS
# --------------------------------------

def test_longueur_ok():
    assert motdepasse.longueur_ok("choubouilli") # longueur ok
    assert not motdepasse.longueur_ok("chou") # longueur pas ok
    assert not motdepasse.longueur_ok("") # chaine vide


def test_chiffre_ok():
    assert motdepasse.chiffre_ok("chou9bouilli")  # chiffre au milieu
    assert motdepasse.chiffre_ok("7choubouilli")  # chiffre au début
    assert motdepasse.chiffre_ok("choubouilli5")  # chiffre à la fin
    assert motdepasse.chiffre_ok("chou3boui8lli")  # deux chiffres    
    assert not motdepasse.chiffre_ok("chou")       # pas de chiffres
    assert not motdepasse.chiffre_ok("un deux trois") # pas de chiffres



def test_sans_espace():
    assert motdepasse.sans_espace("choubouilli") # sans espace ok
    assert not motdepasse.sans_espace("chou bouilli") # espace au milieu
    assert not motdepasse.sans_espace(" choubouilli") # espace au début
    assert not motdepasse.sans_espace("choubouilli ") # espace à la fin
    assert motdepasse.sans_espace("") # chaine vide


def test_troischiffre_ok():
    assert motdepasse.troischiffre_ok("chou9bou3illi7")
    assert not motdepasse.troischiffre_ok("abc7def")
    assert motdepasse.troischiffre_ok("123abc")

def test_chiffre_non_consecutifs_ok():
    assert motdepasse.chiffre_non_consecutifs_ok("chou7b7ouilli")    
    assert not motdepasse.chiffre_non_consecutifs_ok("abc77def")
    assert not(motdepasse.chiffre_non_consecutifs_ok("hello123"))

def test_minimum_unique_ok():
    assert not(motdepasse.minimum_unique_ok("chou7bou7illi"))
    assert not(motdepasse.minimum_unique_ok("abc777xyz"))
    assert motdepasse.minimum_unique_ok("hello9world")


