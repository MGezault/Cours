def decision(sexe,tps_record_100m,nb_course_remp,champion):
    """
    Permet de savoir si un atlèthe est éligible à participer aux JOs.

    Args:
        sexe (str): homme ou femme 
        tps_record_100m (float): Le nombre de secondes que l'atlèthe a mit sur son record pour faire 100 mètres
        nb_course_remp (int): Le nombre de cours remportés par l'atlèthe 
        champion (bool): Si l'atlèthe est champion du monde

    Returns:
        eligible(bool): , True si l'atlèthe est éligible à participer aux JOs
    """    
    eligible = False
    if champion == True :
        eligible = True
    if (sexe == "homme") or (sexe== "Homme") or (sexe=="Masculin"):
        if tps_record_100m <= 12:
            if nb_course_remp >=3:
                eligible = True
    else:
        if tps_record_100m <= 15:
            if nb_course_remp >=3:
                eligible = True
    return (eligible)

def decision_tests():
    """ 
    Teste la fonction decision et vérifie qu'elle renvoie les bons résultats.
    Ne renvoie rien.
    """    
    assert decision("homme",15,5,False) ==False
    assert decision("femme",15,5,False) ==True
    assert decision("homme",54,1,True) ==True
    assert decision("femme",16,5,False) ==False


def sanction (km_depassement,limite_sur_zone,recidive):
    """
    Permet de calculer les peines encourus selon les paramêtres de l'exces de vitesse.

    Args:
        km_depassement (int): Le nombre de kilomètre/heure lors de l'exces
        limite_sur_zone (int): La limite de kilomètre/heure sur la zone où l'exces a eu lieu
        recidive (bool, optional): Si récidive il y a, de base sur Non.

    Returns:
        sanctions (tuple): Renvoie trois entiers, le premier representant l'amende en euro à payer, le second le nombre de points qu'il sera retiré et le dernier,
        le nombre d'années de retrait de permis
    """    
    exces = limite_sur_zone - km_depassement
    cpt = 0
    while exces > 0 :
        exces -= 10
        cpt +=1
    if cpt == 2:
        if limite_sur_zone > 50:
            sanctions = (68,1,0)
        else:
            sanctions = (135,1,0)
    elif cpt==3:
        sanctions = (135,2,0)
    elif cpt ==4:
        sanctions = (135,3,3)
    elif cpt == 5:
        sanctions = (135,4,3)
    elif cpt >5:
        if recidive== True:
            sanctions = (3750,6,3)
        else:
            sanctions = (1500,6,3)
    else:
        sanctions = (0, 0, 0)
    return sanctions

    
def sanction_tests():
    """ 
    Teste la fonction sanction et vérifie qu'elle renvoie les bons résultats.
    Ne renvoie rien.
    """    
    assert(sanction(20,50)==(135,1,0))
    assert(sanction(60,20)==(1500,6,3))
    assert(sanction(34,64)==(135,3,3))
    assert(sanction(54,124,True)==(3750,6,3))

