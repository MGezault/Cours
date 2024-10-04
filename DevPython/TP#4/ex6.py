from ex5 import liste_mots
from ex4 import premiere_lettre
def trouve_mots(chaine,lettre):
    """permet de retrouver tous les mots qui commencent par une certaine lettre dans un texte

    Args:
        chaine (str): la liste des mots que l'on veut analyser
        lettre (str): la lettre que l'on veut trouver
    Returns:
        list: la liste des mots commencant par la lettre
    """
    return(premiere_lettre(liste_mots(chaine),lettre))

def test_trouve_mots():
    assert (trouve_mots("Cela fait déjà 28 jours! 28 jours à l’IUT’O! Cool!!",'C')==['Cela', 'Cool'])
    assert (trouve_mots("Hier, j'ai mangé des pâtes, c'était plutôt bon !","m") == ['mangé'])
    assert (trouve_mots("Vraiment, beaucoup de pâtes !","x")==[])
    assert(trouve_mots("","z")==[])