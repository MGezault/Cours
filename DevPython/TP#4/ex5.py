def liste_mots(phrase):
    """permet de retrouver la liste des mots de ce texte

    Args:
        phrase (str): la phrase ou la chaine de caractère dont on voit séparer les mots en une liste

    Returns:
        list: la liste des mots séparés sans espace et signes de ponctuation
    """
    chaine = []
    mot= ""
    for cara in phrase:
        if cara.isalpha():
            mot += cara
        else:
            if mot !="":
                chaine.append(mot)
            mot =""
    return chaine

def test_liste_mots():
    assert (liste_mots("Cela fait déjà 28 jours! 28 jours à l’IUT’O! Cool!!")== ["Cela", "fait", "déjà", "jours", "jours", "à", "l", "IUT", "O", "Cool"])
    assert (liste_mots("Hier, j'ai mangé des pâtes, c'était plutôt bon !")==['Hier', 'j', 'ai', 'mangé', 'des', 'pâtes', 'c', 'était', 'plutôt', 'bon'])
    assert (liste_mots("Vraiment, beaucoup de pâtes !")== ['Vraiment', 'beaucoup', 'de', 'pâtes'])
    assert(liste_mots("")==[])