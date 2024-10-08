def meilleur_score_joueur(liste_joueurs,scores,joueur):
     """Retourne le meilleur score d’un joueur

     Args:
         liste_joueurs (list): liste des joueurs
         scores (list): liste des scores associés aux joueurs
         joueur (str): joueur duquel on recherche le score

     Returns:
         int/None: le score du joueur ciblé, s'il n'est pas dans la liste, renvoie None
     """
     for indice in range(len(liste_joueurs)):
       if liste_joueurs[indice] == joueur:
            try:
               return scores[indice]
            except:
                 pass
     return None

def est_decroissante(liste_score):
     """Vérifie que les meilleurs scores sont bien triés dans l’ordre décroissant

     Args:
         liste_score (list): la liste des scores que l'ont veut analyser

     Returns:
         bool: Si la liste est bien triée
     """
     prec = None
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
     for indice in range(len(liste_score)):
          if liste_score[indice] < score:
               return indice
     return len(liste_score)

def insertion_totale(nv_score,nv_joueur,liste_joueurs,liste_score):
     indice_vise=insertion_score(liste_score,nv_score)
     liste_score.append(nv_score)
     liste_joueurs.append(nv_joueur)
     for indice in range(len(liste_score),indice_vise):
          liste_joueurs[indice],liste_joueurs[indice+1]=liste_joueurs[indice+1],liste_joueurs[indice]
          liste_score[indice],liste_score[indice+1]=liste_score[indice+1],liste_score[indice]
     



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




liste = [352100, 325410, 312785, 220199, 127853]
joueurs= ["Batman", "Robin", "Batman", "Joker", "Batman"]

insertion_totale(5000000,"Bord",joueurs,liste)
print(liste)