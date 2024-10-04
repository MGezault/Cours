def est_croissante(liste):
    """vérifie si une liste est bien triée dans l’ordre croissant.

    Args:
        liste (list): la liste dont vérifie la croissance

    Returns:
        booléen : Oui ou Non si la liste est croissante
    """    
    prec = None
    for elem in liste:
        if (prec is None) or (prec <= elem)  :
            prec = elem
        else:
            return False
    return True

def depasse_seuil(liste,seuil):
    total = 0
    for nombre in liste:
        total += nombre
    return total> seuil

def verifie_email(chaine):
    tournant = None
    nb_aro = 0
    email = False
    if len(chaine)>0:
        if not ((chaine[0]=="@") or (chaine[len(chaine)-1]== ".")):
            for cara in range(len(chaine)):
                if (chaine[cara] == " ") or (nb_aro> 1):
                    return False
                elif chaine [cara] == "@":
                    tournant = False
                    nb_aro +=1
                elif (chaine[cara]==".") and (tournant == False):
                    tournant = True
            if (nb_aro == 1) and (tournant== True):
                email = True
    return email


def test_est_croissante():
    assert(est_croissante([0,1,2,4,5,6,7,8,9])==True)
    assert(est_croissante([12,54,5,48,97])==False)
    assert(est_croissante([])==True)
    assert(est_croissante([-4,-6,5,-7,4,9])==False)

def test_depasse_seuil():
    assert depasse_seuil([0,1,2,4,5,6,7,8,9],25)==True
    assert depasse_seuil([12,54,5,48,-97],50)==False
    assert depasse_seuil([2,1,5],15)==False
    assert depasse_seuil([0,1,-2],0)== False

def test_verifie_email():
    assert (verifie_email("jesuis.une.email@gmail.fr")==True)
    assert(verifie_email("alors quemoi@non.f")==False)
    assert(verifie_email("Quantamoi@nonplus")==False)
    assert(verifie_email("")==False)
    assert(verifie_email("onfinit.surune@vraie.email")==True)
