import bilan_carbone as bc

# Ici vos fonctions dédiées aux interactions

# ici votre programme principal
def programme_principal():
    toutes_activites= bc.charger_activites("emissions_CO2_septembre_2024.csv")
    unites = dict(kg=0.001,hg=0.01,dag=0.1,g=1,dg=10,cg=100,mg=1000,h=1/60,m=1,s=60)
    umasse = "g"
    utemps= "h"
    fin= False
    while not(fin):
        print("Souhaitez vous faire des recherches ou quitter ?")
        print("Vos unités sont actuellement en",umasse,"pour la masse et en",utemps,"pour le temps. Tapez 'unite' pour les modifier. ")
        choixfinal= input().strip().lower()
        if choixfinal in ("recherches","recherche","r"):

            choix = (input("Sur un individu ou sur un groupe ? ")).strip().lower()
            if choix in  ("invidu","individuel","un individu","une personne","quelqu'un","i"):
                condition= False
                while not(condition) : 
                    prenom= (input("Veuillez insérer le prénom de la personne que vous souhaitez que vous voulez analyser :  ")).strip()
                    if prenom.isalpha():
                        condition= True
                    else:
                        print("Veuillez n'entrer que des lettres s'il vous plait. ")

                print("Voulez-vous faire des recherches sur une période de temps précises ? ")
                ouinon= bc.oui_non()
                if ouinon:
                    condition3 = False
                    while not(condition3):
                        print("Nous allons avoir besoin de la date de début de période et de la date de fin de période : ")
                        debut = input("Quelle est la date de début de période (sous forme YEAR-MM-DD) : ")
                        fin = input("Quelle est la date de fin de période (sous forme YEAR-MM-DD) : ")
                        liste_visee= bc.creer_liste_date(bc.filtre_par_prenom(toutes_activites,prenom),debut,fin)
                        if liste_visee is None:
                            print("")
                            print("Veuillez entrer des dates valides s'il vous plait.")
                        else:
                            condition3= True
                    
                    
                elif ouinon is None:
                    continue
                else:
                    liste_visee= bc.filtre_par_prenom(toutes_activites,prenom)
   

            elif choix in ("groupe","tout le monde","global","tout","g","un groupe"):
                print("Voulez vous créer votre propre groupe (oui) ou analyser la totalité des personnes (non) ?")
                ouinon= bc.oui_non()
                if ouinon:
                    liste_visee= []
                    fingroupe = False
                    gens= []
                    while not(fingroupe):
                        condition= False
                        while not(condition) : 
                            prenom= (input("Veuillez insérer le prénom de la personne que vous souhaitez que vous voulez analyser (ou quitter/fin pour commencer les analyses):  ")).strip().lower()
                            if prenom.isalpha():
                                condition= True
                            else:
                                print("Veuillez n'entrer que des lettres s'il vous plait. ")
                        if prenom in ("quitter","fin",'quit',"q"):
                            fingroupe = True
                        elif prenom not in gens:
                            gens.append(prenom)
                            liste_visee.extend(bc.fusionner_activites(liste_visee,bc.filtre_par_prenom(toutes_activites,prenom)))
                            print("Voici les personnes déjà ajouter au groupe : ",gens,".")     
                        else:
                            print("Cette personne est déjà dans votre groupe.")
                elif ouinon is None:
                    continue
                else:
                    liste_visee = toutes_activites
                
                print("Voulez-vous faire des recherches sur une période de temps précises ? ")
                ouinon=bc.oui_non()
                if ouinon:
                    condition3 = False
                    while not(condition3):
                        print("Nous allons avoir besoin de la date de début de période et de la date de fin de période : ")
                        debut = input("Quelle est la date de début de période (sous forme YEAR-MM-DD) : ")
                        fin = input("Quelle est la date de fin de période (sous forme YEAR-MM-DD) : ")
                        liste_visee= bc.creer_liste_date(toutes_activites,debut,fin)
                        if liste_visee is None:
                            print("")
                            print("Veuillez entrer des dates valides s'il vous plait.")
                        else:
                            condition3= True
                    
                elif ouinon is None:
                    continue
            else:
                print("Il y a une erreur dans votre réponse, veuillez répondre 'invidu' ou 'groupe'. ")
                continue
            finrenseignement= False
            while not(finrenseignement):
                print("Quels renseignements souhaitez vous avoir ? (Entrez 'aide' pour voir la liste des renseignements.) ")
                choixinfo= input("").strip().lower()

                if choixinfo in ("type","types","t"):
                    pourcentagetype=[]
                    typetrouves= bc.liste_des_types(liste_visee)
                    print("Les personnes ciblées dans l'échantillon ont participé aux types d'activités suivants :", end=" ")

                    # Ce bloc me permet d'afficher la liste des types dans la liste des activités demandées et de retrouver le pourcentage de chaque type d'activité dans l'échantillon obtenu 
                    for types in (typetrouves[:-1]):
                        print(types[4],",",end="",sep="")
                        pourcentagetype.append((types,int((len(bc.filtre(liste_visee,3,types))/len(liste_visee))*100)))
                    print(typetrouves[-1][4],".",sep="")
                    pourcentagetype.append((typetrouves[-1],int((len(bc.filtre(liste_visee,3,typetrouves[-1]))/len(liste_visee))*100)))

                    for (letype,pourcentage) in pourcentagetype:
                        print("Dans l'échantillon sélectionné ",pourcentage," % des activités sont de ",letype,".",sep="")
                    
                    print("")
                    #Ce bloc me permet de calculer le pourcentage de pratiquant chacun des types
                    nb_personnes = len(bc.liste_des_personnes(liste_visee))
                    for typ in ("type1","type2","type3","type4"):
                        nb_adepte_type= len(bc.liste_des_personnes(bc.filtre(liste_visee,3,typ)))
                        print("Dans l'échantillon sélectionné, ",int((nb_adepte_type/nb_personnes)*100)," % des personnes sélectionnées pratiquent l'activité de ",typ,".",sep="")

                elif choixinfo in ("noms","nom","n","personne","personnes"):
                    print ("Voici les personnes qui apparaissent dans l'échantillon demandé': ")
                    for nom in (bc.liste_des_personnes(liste_visee)):
                        print("-",nom,";")

                elif choixinfo in ("emission","emissions","e"):
                    totalem = 0
                    totaltemps= 0
                    for typ in ("type1","type2","type3","type4"):
                        listetype=bc.filtre(liste_visee,3,typ)
                        emission = bc.cumul_emmissions(listetype)
                        temps=bc.cumul_temps_activite(listetype,bc.co2_minute)
                        totalem += emission
                        totaltemps += temps
                        print(
                                "Pour le type ", typ[4], ", il y a eu ", round(emission * unites[umasse],2), umasse,  #Je calcule et affiche la masse dans l'unité demandé 
                                " de CO2 émis pour un total de ", round((temps) * unites[utemps],2),utemps, " d'émissions.",sep="" # Je calcule et affiche le temps dans l'unité demandé
                            )
                        
                    print(
                            "Pour un total de ",round(totalem*unites[umasse],2), umasse," de CO2 émis pour un total de " #Je calcule et affiche la masse dans l'unité demandé 
                            ,round((totaltemps)*unites[utemps]),2,utemps," d'émissions.",sep="" # Je calcule et affiche le temps dans l'unité demandé
                            )
                    print("")
                    print("Voulez vous davantages d'informations ? ")
                    if bc.oui_non():
                        condition2= False
                        while not(condition2):
                            if choix in ("groupe","tout le monde","global","tout","g","un groupe"):
                                print ("Souhaitez-vous obtenir des informations sur la moyenne ou les extrémités ? (Ou quitter pour quitter.) ")
                            else:
                                print ("Souhaitez-vous obtenir des informations sur la croissance, la moyenne ou les extrémités ? (Ou quitter pour quitter.) ")
                            choixplus=(input("")).strip().lower()

                            if choixplus in ("croissance","croissances","c") and not( choix in ("groupe","tout le monde","global","tout","g","un groupe")):
                                print("La longueur de la plus longue suite d'emmissions croissantes dans l'échantillon visé est : ",bc.plus_longue_periode_emmissions_croissantes(liste_visee),".",sep="")
                                print("La longueur de la plus longue suite d'emmissions décroissantes dans l'échantillon visé est : ",bc.plus_longue_periode_emmissions_decroissantes(liste_visee),".",sep="")

                            elif choixplus in ("moyenne","moyennes","m"):
                                print("La moyenne des émissions sur l'échantillon demandé est : ", round(((totalem/len(liste_visee))*unites[umasse]),2),umasse,".",sep="")
                            elif choixplus in("extremite","extremites","minimum","minimums","maximum","maximums,","e","extrémités,'extrémité"):

                                mini= bc.min_emmission(liste_visee)
                                maxi=bc.max_emmission(liste_visee)
                                print("L'activité la plus polluante parmi toutes celles analysées est : ", maxi,".",sep="")
                                print("L'activité la moins polluante parmi toutes celles analysées est : ", mini,".",sep="")

                            elif choixplus in ("quitter","quit","q","non"):
                                condition2 = True
                            else:
                                print("Veuillez entrer une valeur parmi :'croissance', 'moyenne', 'extrémités' ou 'quitter'. ")
                            

                elif choixinfo in ("echantillon","echantillons","ec"):
                    print("Voici la liste de toutes les activités qui correspondent aux caractéristiques renseignées : ")
                    for activite in liste_visee:
                        print(activite)
                    print("")

                elif choixinfo in ("quitter","quit","q"):
                    finrenseignement=True

                elif choixinfo.strip().lower() in ("a","aide","aides"):
                    print("Voici la liste des options que vous pouvez entrer pour obtenir des informations : ")
                    print("- nom : Permet de voir les noms de toutes les personnes présentes dans le fichier csv.")
                    print("- type : Permet de voir la liste des types présents dans le fichier csv.")
                    print("- emission: Permet de voir la quantité de CO2 émis et le temps d'émissions de chacun des types d'activités et enfin d'un total de tous.")
                    print("- echantillon : Permet de voir la liste de toutes les activités qui correspondent aux caractéristiques renseignées. ")
                    print("- quitter : Permet de retourner au menu de base.")
                
                else:
                    print("Pour obtenir la liste des options utilisables, entrez 'aide'.")


        elif choixfinal in ("q","quit","quitter"):
            fin = True

        elif choixfinal in ("u","unites","unite"):
            valide = False
            while not(valide):
                umasse= input("Comment voulez-vous que vos données de masse soient analysées ? (Veuillez entrer kg/hg/dag/g/dg/cg/mg.) ")
                utemps=input("Comment voulez-vous que vos données de temps soient analysées ? (Veuillez entrer h/m/s.) ")
                if umasse in ("kg","hg","dag","g","dg","cg","mg") and utemps in ("h","m","s"):
                    valide = True
                else:
                    print("Veuillez entrer des valeurs correctes ! ")

        else:
            print("")
            print("Il y a une erreur dans votre réponse, veuillez répondre 'quitter','recherche', ou 'unite'. ")

programme_principal()