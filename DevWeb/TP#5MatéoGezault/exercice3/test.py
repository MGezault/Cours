
DIRECTIONS={"N":(-1,0),"E":(0,1),"S":(1,0),"O":(0,-1)}

def coordonnees_boussole(coordonnees,direction):
    return (coordonnees[0]+DIRECTIONS[direction][0],coordonnees[1]+DIRECTIONS[direction][1])

def inondation(calque,depart):
    """Le calque doit etre rempli à None

    Args:
        calque (dict): _description_
        depart (tuple): 
    """
    calque[depart][1] = 0
    ligne,colonne = depart
    modif = False
    while not modif:
        for case in calque:
            modif = True
            if case != depart:
                if calque[case][1] != None :
                    break
                ligne,colonne = case
                for dire in "NOSE":
                    ligne2,colonne2= coordonnees_boussole((ligne,colonne),dire)
                    if (ligne2,colonne2) in calque:
                        if not (calque[(ligne2,colonne2)][0] is  None) and not (calque[(ligne2,colonne2)][1] is None): 
                            calque[ligne,colonne][1]= calque[(ligne2,colonne2)][1]+1
                            modif = False
    return calque
