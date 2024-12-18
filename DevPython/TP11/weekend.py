#Question 1 ) 
#Pierre doit verser 19.0e
#MArion doit recevoir 23.0e
#ANna doit recevoir 21.0e
#Béatrice doit verser 22.0e
#Pierre doit verser 19.0e




def bilan_total(bilan):
    total = 0 
    for valeur in bilan.values():
        total += valeur
    return total

def affiche_bilan_financier (week_end):
    moyenne = bilan_total(week_end) / len(week_end)
    for (nom,depenses) in week_end.items():
        if (depenses - moyenne)>0:
            print(nom, "doit recevoir",(depenses- moyenne),"euros.")
        else:
                print(nom, "doit verser ", -(depenses -moyenne),"euros.")


week_end_mai= {"Pierre":92,"Paul":100,"Marie":15,"Anna":0}
week_end_juin= {"Pierre" : 38,"Marie":54,"Anna":52,"Béatrice":8}
affiche_bilan_financier(week_end_juin)
