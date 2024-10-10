def meilleur_score_joueur(liste_joueurs,scores,joueur):
     """Retourne le meilleur score d’un joueur

     Args:
         liste_joueurs (list): liste des joueurs
         scores (list): liste des scores associés aux joueurs
         joueur (str): joueur duquel on recherche le score

     Returns:
         int/None: le score du joueur ciblé, s'il n'est pas dans la liste, renvoie None
     """
    #Pour chaque tour de boucle, nous utiliserons indice afin de trouver le meilleur score d'un joueur à partir de son nom
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
    #Pour chaque tour de boucle, prec vaudra la valeur précédente rencontrée dans la liste afin de la comparé à la nouvelle
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
    #Pour chaque tour de boucle, apparitions vaudra le nombre de fois que le joueur recherché à été rencontré 
    # au tour de boucle correspondant
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
     #Pour chaque tour de boucle, nous utilisons indice afin de trouver la place dans le classement d'un joueur grâce 
     #à son meilleur score
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
     #Pour chaque tour de boucle, nous utilisons indice pour comparer la valeur de la liste_score au tour de boucle correspondant
     # puis nous le comparons au score donné pour savoir s'il est inférieur ou supérieur
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