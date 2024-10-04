def transforme_nombre(chaine):
    """transforme une chaîne de caractères en un nombre
    Entrées :
    chaine (str) : les nombres que l'on veut convertir en entiers
    Returns:
        [list]: Renvoie une liste d'entiers correspondant aux nombres présents dans la chaine de caractère
    """    
    liste = []
    for elem in range(len(chaine)):
        if chaine[elem] in "0123456789":
            if (ord(chaine[elem])) == 48:
                liste.append(0)
            elif(ord(chaine[elem])) == 49:
                liste.append(1)
            elif(ord(chaine[elem])) == 50:
                liste.append(2)
            elif(ord(chaine[elem])) == 51:
                liste.append(3)
            elif(ord(chaine[elem])) == 52:
                liste.append(4)
            elif(ord(chaine[elem])) == 53:
                liste.append(5)
            elif(ord(chaine[elem])) == 54:
                liste.append(6)
            elif(ord(chaine[elem]))== 55:
                liste.append(7)
            elif(ord(chaine[elem])) == 56:
                liste.append(8)
            else:
                liste.append(9)
    return liste


def test_transforme_nombre():
    assert(transforme_nombre("434343453")==[4,3,4,3,4,3,4,5,3])
    assert(transforme_nombre("qeffsfs")==[])
    assert(transforme_nombre("")==[])
    assert(transforme_nombre("0123456789")==[0,1,2,3,4,5,6,7,8,9])
    assert(transforme_nombre("6156")==[6,1,5,6])

