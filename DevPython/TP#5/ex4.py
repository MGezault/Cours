def meilleur_score_joueur(liste_joueurs,scores,joueur):
     for indice in range(len(liste_joueurs)):
       if liste_joueurs[indice] == joueur:
            return scores[indice]
     return None

def est_decroissante(liste):
     prec = None
     for elem in liste:
          if (prec is None) or (elem<= prec):
               prec = elem
          else:
               return False
     return True

def apparition_joueur():

def test_meilleur_score_joueur():
     assert (meilleur_score_joueur(joueurs,liste,"Batman")==352100)
     assert (meilleur_score_joueur(joueurs,liste,"Robin")==325410)
     assert (meilleur_score_joueur(joueurs,liste,"Joker")==220199)
     assert (meilleur_score_joueur(joueurs,liste,"")==None)
     assert (meilleur_score_joueur(joueurs,liste,"Mbappe")==None)
    
def test_est_decroissante():
     assert(est_decroissante([100,55,45,24,5])==True)
     assert(est_decroissante([54,8,845,84,8965,486,464,0])==False)
     assert(est_decroissante([12,23,45,65,78,98,-1])==False)
     assert(est_decroissante([])==True)


liste = [352100, 325410, 312785, 220199, 127853]
joueurs= ["Batman", "Robin", "Batman", "Joker", "Batman"]
