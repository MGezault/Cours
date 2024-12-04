# Codé par Papy Force X, jeune padawan de l'informatique

def dialogue_mot_de_passe():
    login = input("Entrez votre nom : ")
    mot_de_passe_correct = False
    while not mot_de_passe_correct :
        mot_de_passe = input("Entrez votre mot de passe : ")
        if ((longueur_ok(mot_de_passe)) and (chiffre_ok(mot_de_passe)) and (sans_espace(mot_de_passe))):
            mot_de_passe_correct = True

        if not longueur_ok:
            print("Votre mot de passe doit comporter au moins 8 caractères")
    stockfichier(login,mot_de_passe)
    print("Votre mot de passe est correct")
    return mot_de_passe

#La pratique numéro 2 n'est pas respectée
#La pratique numéro 3 n'est pas rspectée
#La pratique numéro 4 n'est pas respectée


def longueur_ok(mdp):
    """Permet de savoir si un mot de passe est composé d'au moins 8 caractères

    Args:
        mdp (str): Le mot de passe que l'on veut tester 

    Returns:
        bool:  Si mdp à une longueur de 8 ou plus
    """
    return len(mdp)>=8

def chiffre_ok(mdp):
    """Permet de savoir s'il y a un chiffre dans le mot de passe donné

    Args:
        mdp (str): Le mot de passe que l'on veut tester 

    Returns:
        bool: S'il y a un chiffre dans mdp 
    """
    #Pour chaque tour de boucle, aucun caractère rencontré n'est un chiffre
    for cara in mdp:
        if cara.isdigit():
            return True
    print("Votre mot de passe doit comporter au moins un chiffre")
    return False

def sans_espace(mdp):
    """Permet de savoir s'il y a un espace dans le mot de passe fourni

    Args:
        mdp (str): Le mot de passe que l'on veut tester 

    Returns:
        bool: False s'il y a un espace dans mdp et True s'il n'y en a pas  
    """
    #Pour chaque tour de boucle, aucun caractère n'est un espace
    for cara in mdp:
        if cara == " ":
            print("Votre mot de passe ne doit pas comporter d'espace")	   
            return False
    return True


def troischiffre_ok(mdp):
    """Permet de savoir s'il y a au moins 3 chiffres dans le mot de passe donné

    Args:
        mdp (str): Le mot de passe que l'on veut tester 

    Returns:
        bool: S'il y a au moins 3 chiffres dans mdp 
    """
    nb_nb=0
    #Pour chaque tour de boucle, parmi tous les caractère rencontrés, il n'y a pas 3 chiffres
    for cara in mdp:
        if cara.isdigit():
            nb_nb+=1      
        if nb_nb == 3:
            return True  
    return False

def chiffre_non_consecutifs_ok(mdp):
    """Permet de savoir si aucun chiffre n'est consécutif à un autre

    Args:
        mdp (str): Le mot de passe que l'on veut tester 

    Returns:
        bool: True si aucun chiffre ne sont consécutifs, False sinon
    """
    #Pour chaque tour de boucle, de l'indice 0 à l'indice indice, il n'y a pas de chiffres consécutifs
    for indice in range(1,len(mdp)):
        if mdp[indice-1].isdigit() and mdp[indice].isdigit():
            return False
    return True


def minimum_unique_ok(mdp):
    """Permet de savoir si le plus petit chiffre est unique

    Args:
        mdp (str): Le mot de passe que l'on veut tester 

    Returns:
        bool: True si le plus petit chiffre est unique, False sinon
    """
    mini = None
    occurence = 0
    #Pour chaque tour de boucle, mini contient le plus petit chiffre rencontré parmi les caractères rencontrés et occurence le nombre de fois que mini a été observé
    for cara in mdp:
        if (cara.isdigit()) and ((mini is None) or  (mini<cara)):
            mini = cara
            occurence = 1
        elif mini == cara:
            occurence +=1
    return not(occurence>=2)
            
def stockfichier(login,motdepasse):
    """Ouvre le fichier mdpUltraSecret.txt et y ajoute le login avec le mot de passe

    Args:
        login (str): Le nom d'utilisateur 
        motdepasse (str): Le mot de passe associé au login
    """
    with open("mdpUltraSecret.txt","a") as fichier:
        if fichier.readline() != "Login, Mot de passe":
            fichier.seek()
            fichier.write("Login, Mot de passe")
        fichier.write(login,motdepasse)
    fichier.close()
 
def modificationfichier(login,mdp):
    """Ajoute le mdp du login seulement si ce login est inconnu, s'il est déjà connu, le mdp associé sera simplement modifié
    Args:
        login (str): Le nom d'utilisateur 
        motdepasse (str): Le mot de passe associé au login
    """
    with open('mdpUltraSecret.txt',"a") as fichier:
        modif= False
        if fichier.readline() != "Login, Mot de passe":
            fichier.seek()
            fichier.write("Login, Mot de passe")
        #Parmi toutes les lignes analysées, aucune n'est composée du login donné
        for ligne in fichier:
            association = ligne.strip().split(',')
            if association[0] == login:
                association[1] = mdp
                modif = True
                break
        if not(modif):
            fichier.write(login,mdp)
    fichier.close()


            