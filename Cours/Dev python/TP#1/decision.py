def decision(sexe,record,course,champion):
    """Permet de simuler l'enregistrement du participant au championnat du monde d'atléthisme.

    Args:
        sexe (str): homme ou femme
        record (float): un nombre representant le nombre de secondes 
        course (_type_): _description_
        champion (_type_): _description_

    Returns:
        _type_: _description_
    """
    if sexe == "homme" and ((champion = True)or (record<12 and course >= 3)):
        return ("Le participant peut être inscrit dans la catégorie homme.")
    elif sexe == "femme" and ((champion = True)or (record<15 and course >= 3)):
        return ("Le participant peut être inscrit dans la catégorie femme.")
    else :
        return ("Le participant ne peut pas être inscrit.")