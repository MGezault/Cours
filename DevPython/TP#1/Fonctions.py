def fonction1(a,b,c,d):
    """renvoie le nombre le plus petit parmis les 4 selectionnés

    Args:
        a (entier): un nombre entier quelconque
        b (entier): _desun nombre entier quelconquecription_
        c (entier): un nombre entier quelconque
        d (entier): un nombre entier quelconque

    Returns:
        res: le plus petit entier parmis a,b,c ou d
    """
    if a < b : 
        res = a
    else : 
        res = b
    if c < res : 
        res = c
    if d < res : 
        res = d
    return res



def fonction2(m):
    """La fonction renvoie True s'il y'a plus de voyelles que de consonne dans le mot donné et False s'il y'en a autant ou moins.

    Args:
        m (string): un mot quelconque

    Returns:
        Un booléen : True si res > 0 et False sinon
    """
    res = 0
    for lettre in m:
        if lettre in 'aeiouy':
            res +=1
        else:
            res -=1
    return (res>0)
    

def test_f1():
    assert fonction1(7,5,4,80) == 4
    assert fonction1(1,1,1,0) == 0
    assert fonction1(1,1,1,1) == 1
    assert fonction1(-5,0,1,2) ==-5
    assert fonction1(654,52,46521,425) == 52

def test_f2():
    assert fonction2("pouet") == True
    assert fonction2('accordéon') == False
    assert fonction2("paon") == False
    assert fonction2("pluie") ==True

