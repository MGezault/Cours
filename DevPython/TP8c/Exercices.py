def trouver_dans_liste(liste,cible):
    indice = 0
    while indice< len(liste):
        if liste[indice] == cible:
            return  True
        indice +=1
    return False

def cumuler_jusqua_seuil(dictionnaire,seuil):
    total = 0
    for cle,valeur in  dictionnaire.items():
        total += valeur
        if total >= seuil:
            break
    return total

#réécriture

def trouver_dans_liste2(liste,cible):
    indice = 0
    while (indice< len(liste)) and not(liste[indice] == cible):
        indice +=1
    return (liste[indice] == cible)

def cumuler_jusqua_seuil2(dictionnaire,seuil):
    total = 0
    ind=0
    valeurs=dictionnaire.values()
    while (ind<len(dictionnaire)) and total < seuil:
        total += valeurs[ind]
        ind+=1
    return total


#exercice 2
#morticia, gomez, mercredi, fétide

course_morticia=["bave de crapaud","oeufs de dragon","lézards","ketchup","sel"]
facture_morticia=[17,157,17,2,1]

def ajout_morticia(course,facture,objet,prix):
    """Ajoute objet et son prix dans la liste de morticia

    Args:
        course (list): La liste des objets achetés par Morticia
        facture (list): La liste des prix des objets de la liste course
        objet (str): Le nom de l'objet à ajouter
        prix (int): le prix de l'objet à ajouter
    """
    course.append(objet)
    facture.append(prix)

def retirer_morticia(course,facture,objet):
    """Retire un élement de la liste de course et retire son prix de la liste des factures

    Args:
        course (list): La liste des objets achetés par Morticia
        facture (list): La liste des prix des objets de la liste course
        objet (str): Le nom de l'objet à supprimer

    Returns:
        None: Renvoie None si l'objet donné n'est pas dans la liste des courses
    """
    ind = 0
    #Parmi tous les élements parcourus, je n'ai pas encor trouvé l'objet dans la liste de course
    while (ind<=len(course)) and (course[ind]!=objet):
        ind +=1
    if ind> len(course):
        return None
    course.remove(objet)
    facture.pop(ind)

def modifie_morticia(course,facture,objet,nvprix):
    """Modifie le prix d'un élément de course

    Args:
        course (list): La liste des objets achetés par Morticia
        facture (list): La liste des prix des objets de la liste course
        objet (str): Le nom de l'objet à supprimer

    Returns:
        None: Renvoie None si l'objet donné n'est pas dans la liste des courses.
    """
    ind = 0
    #Parmi tous les élements parcourus, je n'ai pas encor trouvé l'objet dans la liste de course
    while (ind<=len(course)) and (course[ind]!=objet):
        ind +=1
    if ind> len(course):
        return None
    facture[ind]=nvprix

def total_morticia(course,facture):
    """Calcule la somme des prix des objets de la liste de course

    Args:
        course (list): La liste des objets achetés par Morticia
        facture (list): La liste des prix des objets de la liste course

    Returns:
        int : la somme des prix de tous les élements de facture
    """
    total = 0
    #A chaque tour de boucle, total contient la somme de tous les élements rencontrés
    for article in facture:
        total += article
    return total

def trouve_morticia(course,facture):
    """Trouve l'objet le plus cher de la liste de course 

    Args:
        course (list): La liste des objets achetés par Morticia
        facture (list): La liste des prix des objets de la liste course

    Returns:
        str: Le nom de l'objet le plus de cher de la liste de course
    """
    plus_cher=None
    prixcher=None
    #Entre l'indice 0 et indice, plus_cher est l'objet le plus cher
    for indice in range(len(facture)):
        if prixcher is None or prixcher<facture[indice]:
            plus_cher=course[indice]
            prixcher=facture[indice]
    return plus_cher

course_gomez=["bave de crapaud",17,"oeufs de dragon",157,"lézards",17,"ketchup",2,"sel",1]


def ajout_gomez(course,objet,prix):
    """Ajoute objet et son prix dans la liste de Gomez d'après la modélisation de Gomez

    Args:
        course (list): La liste des objets achetés
        objet (str): Le nom de l'objet à ajouter
        prix (int): le prix de l'objet à ajouter
    """
    course.append(objet)
    course.append(prix)

def retirer_gomez(course,objet):
    """Retire un élement de la liste de course et retire son prix de la liste des factures d'après la modélisation de Gomez

    Args:
        course (list): La liste des objets achetés 
        objet (str): Le nom de l'objet à supprimer

    Returns:
        None: Renvoie None si l'objet donné n'est pas dans la liste des courses
    """
    ind = 0
    #Parmi tous les élements parcourus, je n'ai pas encor trouvé l'objet dans la liste de course
    while (ind<=len(course)) and (course[ind]!=objet):
        ind +=1
    if ind> len(course):
        return None
    course.pop(ind+1)
    course.remove(objet)

def modifie_gomez(course,objet,nvprix):
    """Modifie le prix d'un élément de course d'après la modélisation de Gomez

    Args:
        course (list): La liste des objets achetés
        objet (str): Le nom de l'objet à supprimer

    Returns:
        None: Renvoie None si l'objet donné n'est pas dans la liste des courses.
    """
    ind = 0
    #Parmi tous les élements parcourus, je n'ai pas encor trouvé l'objet dans la liste de course
    while (ind<=len(course)) and (course[ind]!=objet):
        ind +=1
    if ind> len(course):
        return None
    course[ind+1]=nvprix

def total_gomez(course):
    """Calcule la somme des prix des objets de la liste de course d'après la modélisation de Gomez

    Args:
        course (list): La liste des objets achetés par Morticia
        facture (list): La liste des prix des objets de la liste course

    Returns:
        int : la somme des prix de tous les élements de facture
    """
    total = 0
    #A chaque tour de boucle, total contient la somme de tous les élements rencontrés
    for article in course:
        if type(article) == int:
            total += article
    return total

def trouve_gomez(course):
    """Trouve l'objet le plus cher de la liste de course 

    Args:
        course (list): La liste des objets achetés par Morticia
        
    Returns:
        str: Le nom de l'objet le plus de cher de la liste de course
    """
    plus_cher=None
    prixcher=None
    #Entre l'indice 0 et indice, plus_cher est l'objet le plus cher
    for indice in range(0,len(course),2):
        if prixcher is None or prixcher<course[indice]:
            plus_cher=course[indice-1]
            prixcher=course[indice]
    return plus_cher