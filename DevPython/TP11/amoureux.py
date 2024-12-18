def amour_reciproque(organisme):
    couples = []
    for (envoyeur,receveur) in organisme:
        if organisme[receveur] == envoyeur:
            couples.append((envoyeur,receveur))
    return couples

def soupirants(organisme,personne):
    rivaux = []
    for (envoyeur,receveur) in organisme:
        if receveur == personne:
            rivaux.append(envoyeur)
    return rivaux
        

ATM={'Armand':'Beatrice','Beatrice':'Cesar','Cesar':'Dalida','Dalida':'Cesar','Etienne':'Beatrice','Firmin':'Henri','Gaston':'Beatrice','Henri':'Firmin'}
