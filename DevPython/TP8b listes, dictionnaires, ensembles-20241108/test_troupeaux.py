import troupeaux


def test_total_animaux():
    troupeau_de_jean = {'vache':12, 'cochon':17, 'veau':3}
    troupeau_vide = dict()
    troupeau_de_perrette = {'veau':14, 'vache':7, 'poule':42}
    mon_troupeau = {"Ornithorynque": 15,"Iguane": 45,"Drattak" : 2, "Flamby" : 2}
    assert troupeaux.total_animaux(troupeau_de_perrette) == 63
    assert troupeaux.total_animaux(troupeau_de_jean) == 32
    assert troupeaux.total_animaux(troupeau_vide) == 0
    assert troupeaux.total_animaux(mon_troupeau) == 64



def test_tous_les_animaux():
    jean = {'vache':12, 'cochon':17, 'veau':3}
    vide = dict()
    perrette = {'veau':14, 'vache':7, 'poule':42}
    mon_troupeau = {"Ornithorynque": 15,"Iguane": 45,"Drattak" : 2, "Flamby" : 2}
    assert troupeaux.tous_les_animaux(perrette) == {'veau', 'vache', 'poule'}
    assert troupeaux.tous_les_animaux(jean) == {'veau', 'vache', 'cochon'}
    assert troupeaux.tous_les_animaux(vide) == set()
    assert troupeaux.tous_les_animaux(mon_troupeau) == {"Ornithorynque","Iguane","Drattak" , "Flamby"}


def test_specialise():
    troupeau_de_jean = {'vache':12, 'cochon':17, 'veau':3}
    troupeau_vide = dict()
    troupeau_de_perrette = {'veau':14, 'vache':7, 'poule':42}
    mon_troupeau = {"Ornithorynque": 15,"Iguane": 45,"Drattak" : 2, "Flamby" : 2}
    assert troupeaux.specialise(troupeau_de_perrette)
    assert not troupeaux.specialise(troupeau_de_jean)
    assert not troupeaux.specialise(troupeau_vide)
    assert troupeaux.specialise(mon_troupeau)


def test_quantite_suffisante():
    troupeau_de_jean = {'vache':12, 'cochon':17, 'veau':3}
    troupeau_vide = dict()
    troupeau_de_perrette = {'veau':14, 'vache':7, 'poule':42}
    mon_troupeau = ...    
    assert troupeaux.quantite_suffisante(troupeau_de_perrette)
    assert not troupeaux.quantite_suffisante(troupeau_de_jean)
    assert troupeaux.quantite_suffisante(troupeau_vide)
    assert troupeaux.quantite_suffisante(troupeau_vide)

def test_le_plus_represente():
    troupeau_de_jean = {'vache':12, 'cochon':17, 'veau':3}
    troupeau_vide = dict()
    troupeau_de_perrette = {'veau':14, 'vache':7, 'poule':42}
    mon_troupeau = {"Ornithorynque": 15,"Iguane": 45,"Drattak" : 2, "Flamby" : 2}
    assert troupeaux.le_plus_represente(troupeau_de_perrette) == 'poule'
    assert troupeaux.le_plus_represente(troupeau_de_jean) == "cochon"
    assert troupeaux.le_plus_represente(troupeau_vide) is None
    assert troupeaux.le_plus_represente(mon_troupeau) == "Iguane"


def test_reunion_troupeaux():
    troupeau_de_jean = {'vache':12, 'cochon':17, 'veau':3}
    troupeau_de_perrette = {'veau':14, 'vache':7, 'poule':42}
    troupeau_vide = dict()    
    mon_troupeau = {"Ornithorynque": 15,"Iguane": 45,"Drattak" : 2, "Flamby" : 2}
    assert troupeaux.reunion_troupeaux(troupeau_de_perrette, troupeau_vide) == troupeau_de_perrette
    assert troupeaux.reunion_troupeaux(troupeau_vide, troupeau_de_jean) == troupeau_de_jean
    assert troupeaux.reunion_troupeaux(troupeau_de_perrette, troupeau_de_jean) == {'vache':12+7, 'cochon':17, 'veau':3+14, 'poule':42}
    assert troupeau_de_jean == {'vache':12, 'cochon':17, 'veau':3}
    assert troupeau_de_perrette == {'veau':14, 'vache':7, 'poule':42}
    assert troupeaux.reunion_troupeaux(troupeau_de_perrette, mon_troupeau) == {'veau':14, 'vache':7, 'poule':42,"Ornithorynque": 15,"Iguane": 45,"Drattak" : 2, "Flamby" : 2}
    assert troupeaux.reunion_troupeaux(mon_troupeau, troupeau_de_jean) == {"Ornithorynque": 15,"Iguane": 45,"Drattak" : 2, "Flamby" : 2,'vache':12, 'cochon':17, 'veau':3}
    assert troupeau_de_jean == {'vache':12, 'cochon':17, 'veau':3}
    assert troupeau_de_perrette == {'veau':14, 'vache':7, 'poule':42}


avengers = {
    'Spiderman ': (5 , 5 , 'araignée a quatre pattes') ,
    'Hulk': (7 , 4 , "Grand homme vert" ) ,
    'Agent 13': (2 , 3 , 'agent 13') ,
    'M Melin': (2 , 6 , 'expert en archi') , 
}

def test_intelligence_moyenne():
    assert troupeaux.intelligence_moyenne({'a ' :(1 , 1 , 'a ') , 'b ' :(3 , 9 , 'b ') , 'c ' :(7 , 2 , 'c ')})== 12/3
    assert troupeaux.intelligence_moyenne({ 'a ' :(1 , 1 , 'a ') , 'b ' :(3 , 9 , 'b ') , 'd ' :(4 , 4 , 'd ')})==14/3
    assert troupeaux.intelligence_moyenne({"a": (4,12,"a"),"b":(1,0,"b"),"c":(1,4,"c"),"d":(0,7,"d")})==23/4
    assert troupeaux.intelligence_moyenne(avengers)==4.5

def test_kikelplusfort():
    assert troupeaux.kikelplusfort({'a' :(1 , 1 , 'a '),'b ' :(3 , 9 , 'b ') , 'c' :(7 , 2 , 'c ')})== 'c'
    assert troupeaux.kikelplusfort({ 'a' :(1 , 1 , 'a ') , 'b' :(3 , 9 , 'b ') , 'd' :(4 , 4 , 'd ')})=="d"
    assert troupeaux.kikelplusfort({"a": (4,12,"a"),"b":(1,0,"b"),"c":(1,4,"c"),"d":(0,7,"d")})=="a"
    assert troupeaux.kikelplusfort(avengers)=="Hulk"

def test_cbdecretins():
    assert troupeaux.combiendecretins({'a ' :(1 , 1 , 'a ') , 'b ' :(3 , 9 , 'b ') , 'c ' :(7 , 2 , 'c ')})== 2
    assert troupeaux.combiendecretins({ 'a ' :(1 , 1 , 'a ') , 'b ' :(3 , 1 , 'b ') , 'd ' :(4 , 1 , 'd ')})==0
    assert troupeaux.combiendecretins({"a": (4,12,"a"),"b":(1,0,"b"),"c":(1,4,"c"),"d":(0,7,"d")})==2
    assert troupeaux.combiendecretins(avengers)==2


