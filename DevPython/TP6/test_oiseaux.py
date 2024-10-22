import oiseaux
import MateoGezaultTP6 as mg
# --------------------------------------
# FONCTIONS
# --------------------------------------

def test_recherche_oiseau():
    assert mg.recherche_oiseau(oiseaux.oiseaux,"Moineau")==("Moineau", "Passereau")
    assert mg.recherche_oiseau([],"Oiseauquivole") == None
    assert mg.recherche_oiseau(oiseaux.oiseaux,"Pic vert")==("Pic vert", "Picidae")
    assert mg.recherche_oiseau(oiseaux.oiseaux,"Tourterelle")==("Tourterelle", "Colombidé")

def test_recherche_par_famille():
    assert mg.recherche_par_famille(oiseaux.oiseaux,"Passereau")==[("Moineau", "Passereau"),("Mésange", "Passereau"),("Pinson", "Passereau"),
           ("Rouge-gorge", "Passereau")]
    assert mg.recherche_par_famille([],"Oiseauquivole") == []
    assert mg.recherche_par_famille(oiseaux.oiseaux,"Picidae")==[("Pic vert", "Picidae")]
    assert mg.recherche_par_famille(oiseaux.oiseaux,"Colombidé")==[("Tourterelle", "Colombidé")]

def test_oiseau_le_plus_observe():
    assert mg.oiseau_le_plus_observe(oiseaux.observations1)=="Moineau"
    assert mg.oiseau_le_plus_observe(oiseaux.observations2)=="Tourterelle"
    assert mg.oiseau_le_plus_observe(oiseaux.observations3)=="Mésange"
    assert mg.oiseau_le_plus_observe([]) is None

def test_est_liste_observations():
    assert mg.est_liste_observations(oiseaux.observations1)
    assert not(mg.est_liste_observations([("mes",4),("pic",7),("oui")]))
    assert mg.est_liste_observations(oiseaux.observations3)
    assert mg.est_liste_observations([])

def test_max_observations():
    assert mg.max_observations(oiseaux.observations1)==5
    assert mg.max_observations(oiseaux.observations3)==4
    assert mg.max_observations(oiseaux.observations2)==5
    assert mg.max_observations([])==0



def test_moyenne_oiseaux_observes():
    assert mg.moyenne_oiseaux_observes([])==None
    assert mg.moyenne_oiseaux_observes(oiseaux.observations1)==3.0
    assert mg.moyenne_oiseaux_observes(oiseaux.observations2)==2.5
    assert mg.moyenne_oiseaux_observes(oiseaux.observations3)==8/3


def test_total_famille():
    assert mg.total_famille([],[],"Picidae")==0
    assert mg.total_famille(oiseaux.observations2,oiseaux.oiseaux,"Batmobile")==0
    assert mg.total_famille(oiseaux.observations2,oiseaux.oiseaux,"Passereau")==8
    assert mg.total_famille(oiseaux.observations3,oiseaux.oiseaux,"Colombidé")==4



def test_construire_liste_observations():
    assert mg.construire_liste_observations(oiseaux.oiseaux,oiseaux.comptage1)==oiseaux.observations1
    assert mg.construire_liste_observations(oiseaux.oiseaux,oiseaux.comptage2)==oiseaux.observations2
    assert mg.construire_liste_observations(oiseaux.oiseaux,oiseaux.comptage3)==oiseaux.observations3
    assert mg.construire_liste_observations([],[])==[]


def test_creer_ligne_sup():
    assert oiseaux.creer_ligne_sup(...)==...

def test_creer_ligne_noms_oiseaux():
    assert oiseaux.creer_ligne_noms_oiseaux(...)==...

assert mg.construire_liste_observations(oiseaux.oiseaux,oiseaux.comptage2)==oiseaux.observations2
