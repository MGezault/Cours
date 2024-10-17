def mystere_indice(liste, valeur):
    """Trouve la quatrième valeur de liste égale à valeur

    Args:
        liste ([list]): une liste d'entier dans laquelle on va chercher la valeur
        valeur ([int]): l'entier que nous allons chercher dans liste

    Returns:
        [int]: l'indice de la quatrième occurence de valeur dans la liste
    """
    yyy = 0
    for indice in range (len(liste)):
        #Au début de chaque tour de boucle, y à la valeur du nombre d'élement de la liste égale à la valeur cherchée
        if liste[indice] == valeur:
            yyy += 1
            if yyy > 3:
                #l'instruction est exécutée si on rencontre la 4e valeur de la liste égale à valeur
                return indice
    return None

def premier_nombre(chaine):   
    """retourne l’indice du premier caractère contenant un chiffre dans une
chaîne de caractères.

    Args:
        chaine (str): la chaine de caractère de laquelle on retournera le premier chiffre

    Returns:
        int: l'indice du premier chiffre
    """    
    #Pour chaque tour de boucle, les caractères de chaine de l'index 0 à i-1 ne sont pas des chiffres.
    for indice in range(len(chaine)):
        if "0"<=chaine[indice]<="9":
            return indice
    return None

def trouve_pop(liste_ville,liste_pop,ville):
    """retourne la population de cette ville

    Args:
        liste_ville (list): la liste des villes 
        liste_pop (list): liste des populations des villes dans liste_villes
        ville (ville): la ville de laquelle on souhaite savoir la population

    Returns:
        int: la population de la ville cherchée
    """  
    #Pour chaque tour de boucle, les villes de liste_ville de l'index 0 à i-1 n'ont pas été trouvées égales à ville
    for indice in range(len(liste_ville)):
        if liste_ville[indice] == ville :
            return liste_pop[indice]
    return None


def test_premier_nombre():
    assert (premier_nombre("on est le 30/09/2021" )==10)
    assert (premier_nombre("Eh nan il n'y a pas de nombre dans celle la.")== None)
    assert(premier_nombre("Alors qu'ici : 2")==15 )
    assert(premier_nombre("")==None)

def test_trouve_pop():
    assert trouve_pop(liste_villes,population,"Blois")== 45871
    assert trouve_pop(liste_villes,population,"")== None
    assert trouve_pop(liste_villes,population,"Paris")== None
    assert trouve_pop(liste_villes,population,"Chartres")== 38426
    assert trouve_pop(liste_villes,population,"Tours")== 136463


liste_villes = ["Blois", "Bourges", "Chartres", "Châteauroux", "Dreux",
                "Joué-lès-Tours", "Olivet", "Orléans", "Tours", "Vierzon"]
population = [45871, 64668,  38426, 43442, 30664, 38250, 22168, 116238,
              136463,  25725]



def est_croissante(liste):
    """vérifie si une liste est bien triée dans l’ordre croissant.

    Args:
        liste (list): la liste dont vérifie la croissance

    Returns:
        booléen : Oui ou Non si la liste est croissante
    """    
    prec = None
    #Pour chaque tour de boucle, la boucle est triée dans l'ordre croissante
    for elem in liste:
        if (prec is None) or (prec <= elem)  :
            prec = elem
        else:
            return False
    return True

def depasse_seuil(liste,seuil):
    """Indique si la somme des éléments d’une liste de nombres dépasse un
seuil

    Args:
        liste (list): la liste que l'on veut additionner
        seuil (int): le seuil que l'on veut comparer à la somme d'une liste

    Returns:
        bool: Si la somme des éléments d'une liste dépasse le seuil
    """
    total = 0
    #Pour chaque tour de boucle, total vaudra la somme des i premiers éléments de la liste
    for nombre in liste:
        total += nombre
    return total> seuil

def verifie_email(chaine):
    """Vérifie qu’une chaîne de caractères correspond à une adresse e-mail
potentielle

    Args:
        chaine (str): la chaine que l'on veut analyser

    Returns:
        bool: Si la chaine est une adresse email valide
    """
    tournant = None
    nb_aro = 0
    email = False
    if len(chaine)>0:
        if not ((chaine[0]=="@") or (chaine[len(chaine)-1]== ".")):
            #Pour chaque tour de boucle, nb_aro compte le nombre d'arobases rencontrées jusqu'à l'index correspondante,
            # et tournant indique si un point a été trouvé après un arobase.
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



def meilleur_score_joueur(liste_joueurs,scores,joueur):
     """Retourne le meilleur score d’un joueur

     Args:
         liste_joueurs (list): liste des joueurs
         scores (list): liste des scores associés aux joueurs
         joueur (str): joueur duquel on recherche le score

     Returns:
         int/None: le score du joueur ciblé, s'il n'est pas dans la liste, renvoie None
     """
    #Pour chaque tour de boucle, le joueur ayant réalisé le meilleur score n'a pas été trouvé
     for indice in range(len(liste_joueurs)):
               if liste_joueurs[indice] == joueur:
                    return scores[indice]
     return None

def est_decroissante(liste_score):
     """Vérifie que les meilleurs scores sont bien triés dans l’ordre décroissant

     Args:
         liste_score (list): la liste des scores que l'ont veut analyser

     Returns:
         bool: Si la liste est bien triée
     """
     prec = None
    #A chaque itération de la boucle, la liste est bien triée dans l'ordre décroissante
     for elem in liste_score:
          if (prec is None) or (elem<= prec):
               prec = elem
          else:
               return False
     return True

def apparition_joueur(liste_joueurs,joueur):
     """retourne combien de fois un joueur apparaît dans les meilleurs scores

     Args:
          liste_joueurs (list): liste des joueurs
          joueur (str): joueur duquel on recherche le score
     Returns:
         int: le nombre d'apparitions du joueur
     """
     apparitions = 0
    #Pour chaque tour de boucle, apparitions représente le nombre d'apparitions du joueur dans liste_joueurs
     for players in liste_joueurs:
          if players == joueur:
               apparitions +=1
     return apparitions

def meilleur_classement(liste_score,liste_joueurs,joueur):
     """Retourne le meilleur classement d’un joueur 

     Args:
         liste_joueurs (list): liste des joueurs
         scores (list): liste des scores associés aux joueurs
         joueur (str): joueur duquel on recherche le score

     Returns:
         int/None: La meilleur place d'un joueur dans le classement grâce à son score, ou None s'il n'a pas de score
     """
     score = meilleur_score_joueur(liste_joueurs,liste_score,joueur)
     #Pour chaque tour de boucle, le meilleur score du joueur n'a pas été trouvé
     for indice in range(len(liste_score)):
          if score == liste_score[indice]:
               return (indice+1)
     return None


def insertion_score(liste_score,score):
     """retourne l’indice où le score devra s’insérer si on doit l’ajouter à la liste

     Args:
         scores (list): liste des scores associés aux joueurs
         score (int): le score que l'on cherche à ajouter à la liste

     Returns:
         int: l'indice auquel le score devrait être ajouté
     """
     #Pour chaque tour de boucle, nous n'avons pas encore trouvé l'indice auquel devra s'ajouter le score donné
     for indice in range(len(liste_score)):
          if liste_score[indice] < score:
               return indice
     return len(liste_score)

def insertion_totale(nv_score,nv_joueur,liste_joueurs,liste_score):
     """ajoute le nouveau score au bon endroit dans la liste des scores et le nom du joueur dans liste_joueurs

     Args:
         nv_score (int): le nouveau score
         nv_joueur (str): le joueur ayant effectué le nouveau score
         liste_joueurs (list): la liste de tous les joueurs
         liste_score (list): la liste de tous les records
     """
     indice_vise=insertion_score(liste_score,nv_score)
     liste_joueurs.insert(indice_vise,nv_joueur)
     liste_score.insert(indice_vise,nv_score)
     



def test_meilleur_score_joueur():
     assert (meilleur_score_joueur(joueurs,liste,"Batman")==352100)
     assert (meilleur_score_joueur(joueurs,liste,"Robin")==325410)
     assert (meilleur_score_joueur(joueurs,liste,"Joker")==220199)
     assert (meilleur_score_joueur(joueurs,liste,"") is None)
     assert (meilleur_score_joueur(joueurs,liste,"Mbappe") is None)
    
def test_est_decroissante():
     assert(est_decroissante([100,55,45,24,5]))
     assert not(est_decroissante([54,8,845,84,8965,486,464,0]))
     assert not(est_decroissante([12,23,45,65,78,98,-1]))
     assert(est_decroissante([]))

def test_apparition():
     assert apparition_joueur(joueurs,"Batman")== 3
     assert apparition_joueur(joueurs,"Mbappé")== 0
     assert apparition_joueur([],"Batman")== 0
     assert apparition_joueur(joueurs,"Joker")== 1

def test_meilleur_classement():
     assert meilleur_classement(liste,joueurs,"Batman")==1
     assert meilleur_classement(liste,joueurs,"Joker")==4
     assert meilleur_classement(liste,joueurs,"Mbappé") is None
     assert meilleur_classement([],joueurs,"Batman") is None

def test_insertion_score():
     assert insertion_score(liste,154000)==4
     assert insertion_score(liste,150000000)==0
     assert insertion_score([],154000)==0
     assert insertion_score(liste,4)== 5
     assert insertion_score([17,11,9,1],9)==3

def test_insertion_totale():
     insertion_totale(2541,"Yanis",joueurs,liste)
     assert joueurs == ['Batman', 'Robin', 'Batman', 'Joker', 'Batman', 'Yanis']
     assert liste == [352100, 325410, 312785, 220199, 127853, 2541]
     insertion_totale(69,"Paul",joueurs,liste)
     assert joueurs == ['Batman', 'Robin', 'Batman', 'Joker', 'Batman', 'Yanis',"Paul"]
     assert liste == [352100, 325410, 312785, 220199, 127853, 2541,69]
     insertion_totale(340020,"Nolan",joueurs,liste)
     assert joueurs == ['Batman',"Nolan", 'Robin', 'Batman', 'Joker', 'Batman', 'Yanis',"Paul"]
     assert liste == [352100,340020, 325410, 312785, 220199, 127853, 2541,69]
     insertion_totale(800000,"Arthur",joueurs,liste)
     assert joueurs == ["Arthur",'Batman',"Nolan", 'Robin', 'Batman', 'Joker', 'Batman', 'Yanis',"Paul"]
     assert liste == [800000,352100,340020, 325410, 312785, 220199, 127853, 2541,69]



liste = [352100, 325410, 312785, 220199, 127853]
joueurs= ["Batman", "Robin", "Batman", "Joker", "Batman"]