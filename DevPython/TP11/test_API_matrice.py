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

def matricebloc1():
    mab1=API.matrice(2,2,15)
    API.set_val(mab1, 1, 0, 16)
    API.set_val(mab1, 0, 1, 19)
    API.set_val(mab1, 1, 1, 20)


def matricebloc1():
    mab1=API.matrice(2,2,15)
    API.set_val(mab1, 1, 0, 16)
    API.set_val(mab1, 0, 1, 19)
    API.set_val(mab1, 1, 1, 20)

def test_bloc():
    assert um.bloc(matrice1(),1,1,2,2) == mab1
    assert um.bloc(matrice4(),1,2,2,3) ==  [7, 8, 9, 11, 12, 13]
    assert um.bloc(matrice5(),0,1,1,2) == [5,7]
    assert not(um.bloc(matrice2(),0,0,1,2)) == ['A','B','C']


test_bloc()