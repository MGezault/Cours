import bilan_carbone as bc
fingroupe = False
while not(fingroupe):
    gens= []
    condition= False
    while not(condition) : 
        prenom= (input("Veuillez insérer le prénom de la personne que vous souhaitez que vous voulez analyser (ou quitter/fin pour commencer les analyses):  ")).strip()
        if prenom.isalpha():
            condition= True
        else:
            print("Veuillez n'entrer que des lettres s'il vous plait. ")
        if prenom in ("quitter","fin",'quit',"q"):
            fingroupe = True
        elif prenom not in gens:
            gens.append(prenom)
            print("Voici les personnes déjà ajouter au groupe : ",gens,".")     
        else:
            print("Cette personne est déjà dans votre groupe.")