def premiere_lettre(liste,lettre):
    """retrouve les mots qui commencent par une certaine lettre dans une liste de mots

    Args:
        liste (list): la liste des mots que l'on veut analyser
        lettre (str): la lettre que l'on veut trouver

    Returns:
        list: la liste des mots commencant par la lettre
    """
    chaine = []
    for mots in liste:
        try:
            if mots[0]== lettre:
                chaine.append(mots)
        except IndexError:
            pass
    return chaine

def test_premiere_lettre():
    assert (premiere_lettre(["salut","hello","hallo","ciao","hola"],"h")==['hello', 'hallo', 'hola'])
    assert (premiere_lettre(["salut","hello","hallo","ciao","hola"],"a")==[])
    assert (premiere_lettre(["manger","goinfrer","grailler","déguster","consommer","diner","déjeuner","gouter"],"g")==["goinfrer","grailler","gouter"])
    assert (premiere_lettre(["manger","goinfrer","grailler","déguster","consommer","diner","déjeuner","gouter"],"m")==["manger"])

