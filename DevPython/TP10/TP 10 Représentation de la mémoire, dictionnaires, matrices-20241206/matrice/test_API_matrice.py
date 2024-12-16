""" tests pour les API matrices
    Remarques : tous les tests de ce fichier doivent passer
    quelle que soit l'API utilisée
"""
import API_matrice2 as API
import utilitaires_matrice as um

def matrice1():
    """ définition d'une matrice pour les tests """
    mat1 = API.matrice(3, 4, None)
    API.set_val(mat1, 0, 0, 10)
    API.set_val(mat1, 0, 1, 11)
    API.set_val(mat1, 0, 2, 12)
    API.set_val(mat1, 0, 3, 13)
    API.set_val(mat1, 1, 0, 14)
    API.set_val(mat1, 1, 1, 15)
    API.set_val(mat1, 1, 2, 16)
    API.set_val(mat1, 1, 3, 17)
    API.set_val(mat1, 2, 0, 18)
    API.set_val(mat1, 2, 1, 19)
    API.set_val(mat1, 2, 2, 20)
    API.set_val(mat1, 2, 3, 21)
    return mat1
print(matrice1)

def matrice2():
    """ définition d'une matrice pour les tests """
    mat2 = API.matrice(2, 3, None)
    API.set_val(mat2, 0, 0, 'A')
    API.set_val(mat2, 0, 1, 'B')
    API.set_val(mat2, 0, 2, 'C')
    API.set_val(mat2, 1, 0, 'D')
    API.set_val(mat2, 1, 1, 'E')
    API.set_val(mat2, 1, 2, 'F')
    return mat2

def matrice3():
    """ définition d'une matrice pour les tests """
    mat3 = API.matrice(3, 3, None)
    API.set_val(mat3, 0, 0, 2)
    API.set_val(mat3, 0, 1, 7)
    API.set_val(mat3, 0, 2, 6)
    API.set_val(mat3, 1, 0, 9)
    API.set_val(mat3, 1, 1, 5)
    API.set_val(mat3, 1, 2, 1)
    API.set_val(mat3, 2, 0, 4)
    API.set_val(mat3, 2, 1, 3)
    API.set_val(mat3, 2, 2, 8)
    return mat3

def matrice4():
    mat4 = API.matrice(4, 4, None)
    API.set_val(mat4, 0, 0, 1)
    API.set_val(mat4, 0, 1, 2)
    API.set_val(mat4, 0, 2, 3)
    API.set_val(mat4, 0, 3, 4)
    API.set_val(mat4, 1, 0, 5)
    API.set_val(mat4, 1, 1, 6)
    API.set_val(mat4, 1, 2, 7)
    API.set_val(mat4, 1, 3, 8)
    API.set_val(mat4, 2, 0, 9)
    API.set_val(mat4, 2, 1, 10)
    API.set_val(mat4, 2, 2, 11)
    API.set_val(mat4, 2, 3, 12)
    API.set_val(mat4, 3, 0, 13)
    API.set_val(mat4, 3, 1, 14)
    API.set_val(mat4, 3, 2, 15)
    API.set_val(mat4, 3, 3, 16)
    return mat4

def matrice5():
    """ définition d'une matrice carrée 2x2 pour les tests """
    mat6 = API.matrice(2, 2, None)
    API.set_val(mat6, 0, 0, 3)
    API.set_val(mat6, 0, 1, 5)
    API.set_val(mat6, 1, 0, 7)
    API.set_val(mat6, 1, 1, 9)
    return mat6

def matrice6():
    """ définition d'une matrice pour les tests """
    mat3 = API.matrice(3, 3, None)
    API.set_val(mat3, 0, 0, 2)
    API.set_val(mat3, 0, 1, 0)
    API.set_val(mat3, 0, 2, 0)
    API.set_val(mat3, 1, 0, 9)
    API.set_val(mat3, 1, 1, 5)
    API.set_val(mat3, 1, 2, 0)
    API.set_val(mat3, 2, 0, 4)
    API.set_val(mat3, 2, 1, 3)
    API.set_val(mat3, 2, 2, 8)
    return mat3


def test_get_nb_lignes():
    """ tests get_nb_lignes """
    matrice_1 = matrice1()
    matrice_2 = matrice2()
    matrice_3 = matrice3()
    assert API.get_nb_lignes(matrice_1) == 3
    assert API.get_nb_lignes(matrice_2) == 2
    assert API.get_nb_lignes(matrice_3) == 3

def test_get_nb_colonnes():
    """ tests pour get_nb_colonnes """
    mat_1 = matrice1()
    mat_2 = matrice2()
    mat_3 = matrice3()
    assert API.get_nb_colonnes(mat_1) == 4
    assert API.get_nb_colonnes(mat_2) == 3
    assert API.get_nb_colonnes(mat_3) == 3

def test_get_val():
    """ tests pour get_val """
    matr1 = matrice1()
    matr2 = matrice2()
    matr3 = matrice3()
    assert API.get_val(matr1, 0, 1) == 11
    assert API.get_val(matr1, 2, 1) == 19
    assert API.get_val(matr2, 1, 1) == 'E'
    assert API.get_val(matr2, 0, 2) == 'C'
    assert API.get_val(matr3, 2, 0) == 4
    assert API.get_val(matr3, 1, 0) == 9
'''
def test_sauve_charge_matrice():
    """tests pour sauvegarde et restauration"""
    la_matrice = matrice2()
    API.sauve_matrice(la_matrice, "matrice.csv")
    matrice_bis = API.charge_matrice_str("matrice.csv")
    assert la_matrice == matrice_bis
'''
def test_get_ligne():
    assert um.get_ligne(matrice1(),0) == [10,11,12,13]
    assert um.get_ligne(matrice1(),2) == [18, 19, 20, 21]
    assert not(um.get_ligne(matrice2(),1)==["B","C","D"])
    
def test_get_colonne():
    assert um.get_colonne(matrice1(),2) == [12, 16, 20]
    assert um.get_colonne(matrice2(),2) == ['C', 'F']
    assert not(um.get_colonne(matrice3(),0)==[7, 9, 4])

def test_get_diago_princi():
    assert um.get_diagonale_principale(matrice3()) == [2, 5, 8]
    assert not(um.get_diagonale_principale(matrice4()) == [1, 7, 11, 16])
    assert um.get_diagonale_principale(matrice4()) == [1, 6, 11, 16]
    assert um.get_diagonale_principale(matrice5()) == [3,9]

def test_get_diago_sec():
    assert um.get_diagonale_secondaire(matrice3()) == [4,5,6]
    assert not(um.get_diagonale_secondaire(matrice4()) == [1, 6, 11, 16])
    assert um.get_diagonale_secondaire(matrice4()) == [13,10,7,4]
    assert um.get_diagonale_secondaire(matrice5()) == [7,5]
    assert um.get_diagonale_secondaire([API.matrice(0,0,None)]) == []


def test_transposee():
    assert um.transpose(matrice1()) == [10, 14, 18, 11, 15, 19, 12, 16, 20, 13, 17, 21]
    assert um.transpose(matrice4()) == [1, 5, 9, 13, 2, 6, 10, 14, 3, 7, 11, 15, 4, 8, 12, 16]
    assert um.transpose(matrice2()) == ['A', 'D', 'B', 'E', 'C', 'F']
    assert not(um.transpose(matrice3()) == [2, 9, 4, 7, 5, 3, 6,8,1])
    assert um.transpose(API.matrice(0,0,None)) == []


def test_triangle_inf():
    assert not(um.is_triangle_inferieur(matrice4()))
    assert um.is_triangle_inferieur(API.matrice(0,0,None))
    assert not(um.is_triangle_inferieur(matrice5()))
    assert um.is_triangle_inferieur(matrice6())

def test_bloc():
    assert um.bloc(matrice1(),1,1,2,2) == [15, 16, 19, 20]
    assert um.bloc(matrice4(),1,2,2,3) ==  [7, 8, 9, 11, 12, 13]
    assert um.bloc(matrice5(),0,1,1,2) == [5,7]
    assert not(um.bloc(matrice2(),0,0,1,2)) == ['A','B','C']

test_bloc()

