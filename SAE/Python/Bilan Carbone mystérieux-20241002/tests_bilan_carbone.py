# fichier de tests de la SAE 1.01 partie 1
# bilan carbone d'activités mystères en septembre 2024

# on importe toutes les fonctions et données définies dans le fichier bilan_carbone
# l'appel de ces fonctions et données doit être préfixé par bc. 
import bilan_carbone as bc  

# ---------------------------------------------------------------------------------------------
# Exemples de tests à compléter impérativement
# ---------------------------------------------------------------------------------------------

def test_est_avant():
    assert bc.est_avant(('Lucas', '2024-09-01', 67.2, 'type3'), ('Lucas', '2024-09-01', 67.2, 'type4')) == True
    assert bc.est_avant(('Lucas', '2024-09-01', 67.2, 'type4'), ('Lucas', '2024-09-01', 67.2, 'type3')) == False
    # Nouveaux Asserts
    assert (bc.est_avant((),())) is None
    assert (bc.est_avant((),('Lucas', '2024-09-01', 67.2, 'type3')))is None
    assert not(bc.est_avant(('Lucas', '2024-01-02', 6.0, 'type3'),('Lucas', '2024-01-02', 6.0, 'type3')))
    assert (bc.est_avant(("Sheriff",78),('Lucas', '2024-01-02', 6.0, 'type3'))) is None
    assert not(bc.est_avant(('Lucas', '2024-09-01', 67.2, 'type3'),('Lucas', '2024-01-02', 6.0, 'type3')))

def test_annee():
    assert bc.annee(('Lucas', '2024-09-01', 67.2, 'type3')) == '2024'
    assert bc.annee(('Lucas', '1999-12-27', 70.08, 'type3')) == '1999'
    # Nouveaux Asserts
    assert (bc.annee(('Lucas', '1999-12-27', 70.08))) is None
    assert (bc.annee(('Lucas', '5', 70.08,"type2" )))==None
    assert (bc.annee(("Sheriff",78))) is None
    assert (bc.annee(('Lucas', '5648-12-27', 70.08, "type1"))) == "5648"
    assert (bc.annee(())) is None

def test_annee_mois():
    assert bc.annee_mois(('Lucas', '2024-10-01', 67.2, 'type3')) == '2024-10'
    assert bc.annee_mois(('Lucas', '2023-09-01', 67.2, 'type3')) == '2023-09'
    #Nouveaux Asserts
    assert (bc.annee_mois(('Lucas', '1999-12-27', 70.08))) is None
    assert (bc.annee_mois(('Lucas', 20240527, 70.08,"type2" ))) is None
    assert (bc.annee_mois(("Sheriff",78))) is None
    assert (bc.annee_mois(('Lucas', '5648-12-27', 70.08, "type1"))) == "5648-12"
    assert (bc.annee_mois(())) is None


def test_max_emmission():
    assert bc.max_emmission([]) == None
    assert bc.max_emmission(bc.liste1) == ('David', '2024-09-29', 23, 'type4')
    #Nouveaux Asserts
    assert (bc.max_emmission((bc.liste5)))==('Erika', '2024-09-28', 240.5, 'type2')
    assert (bc.max_emmission([('Lucas', '2024-10-01', 67, 'type3'),('Lucas', '2024-10-01', 6.2, 'type3')]))== ('Lucas', '2024-10-01', 67, 'type3')
    assert (bc.max_emmission([('Lucas', '2024-10-01', 67, 'type3'),('Lucas', '2024-10-01', 6.2, 'type3'),('Lucas', '2024-10-01', "6.2", 'type3')])) is None


def test_filtre_par_prenom():
    assert bc.filtre_par_prenom([], 'Lucas') == []
    assert bc.filtre_par_prenom([('Lucas', '2024-09-01', 67.2, 'type3'), ('David', '2024-09-02', 70.08, 'type3')], 'Lucas') == [('Lucas', '2024-09-01', 67.2, 'type3')]
    assert bc.filtre_par_prenom(bc.liste1, 'David') == [('David', '2024-09-26', 18, 'type1'), ('David', '2024-09-27', 21, 'type2'), ('David', '2024-09-28', 17, 'type3'), ('David', '2024-09-29', 23, 'type4')]
    #Nouveaux Asserts
    assert bc.filtre_par_prenom(bc.liste1,"Matéo")== []
    assert bc.filtre_par_prenom(bc.liste2,"Guillaume") == [('Guillaume', '2024-09-26', 17, 'type1'), ('Guillaume', '2024-09-27', 20, 'type2'), ('Guillaume', '2024-09-28', 16, 'type3'), ('Guillaume', '2024-09-29', 22, 'type4')]
    assert bc.filtre_par_prenom([("Maria","2024-05-21",54,"type1"),("Marios","2023-13-31",12.6,"type3")],"Mario")==[]
    assert bc.filtre_par_prenom(bc.liste5,"")==[]

def test_filtre():
    assert bc.filtre([], 3, 'type1') == []
    assert bc.filtre(bc.liste3, 1, '2024-09-29') == [('David', '2024-09-29', 23, 'type4'), ('Guillaume', '2024-09-29', 22, 'type4')]
    #Nouveaux Asserts
    assert bc.filtre([('Lucas', '2024-09-01', 67.2, 'type3'),('David', '2024-09-02', 70.08, 'type3')],4,"type2") == []
    assert bc.filtre(bc.liste1,1,"2024-09-27")== [('Christophe', '2024-09-27', 19, 'type2'), ('David', '2024-09-27', 21, 'type2'), ('Guillaume', '2024-09-27', 20, 'type2')]
    assert bc.filtre((4,5,78,45),1,"2024-09-27") == []
    assert bc.filtre(bc.liste2,3,(4,5,8,7)) ==[]


def test_cumul_emmissions():
    assert bc.cumul_emmissions([]) == 0
    assert bc.cumul_emmissions(bc.liste4) == 78
    #Nouveaux Asserts
    assert bc.cumul_emmissions([('Lucas', '2024-10-01', 67, 'type3'),('Lucas', '2024-10-01', -6.2, 'type3'),('Lucas', '2024-10-01', 15.2, 'type3')]) ==82.2
    assert bc.cumul_emmissions(bc.liste3) == 144
    assert bc.cumul_emmissions([('David', '2024-09-26', 18, 'type1'), ('David', '2024-09-27', 1.585, 'type2'), ('David', '2024-09-28', 17.2, 'type3'), ('David', '2024-09-29', 0, 'type4')]) == 36.785
    assert bc.cumul_emmissions([('Lucas', '2024-10-01', 0, 'type3'),('Lucas', '2024-10-01', 0, 'type3'),('Lucas', '2024-10-01', 0, 'type3')]) ==0


def test_plus_longue_periode_emmissions_decroissantes():
    assert bc.plus_longue_periode_emmissions_decroissantes([]) == 0
    assert bc.plus_longue_periode_emmissions_decroissantes(bc.liste6) == 3
    #Nouveaux Asserts
    assert bc.plus_longue_periode_emmissions_decroissantes([('Lucas', '2024-10-01', 67, 'type3'),('Lucas', '2024-10-01', 6.2, 'type3'),('Lucas', '2024-10-01', 6, 'type3')])==2
    assert bc.plus_longue_periode_emmissions_decroissantes(bc.liste2)==2
    assert bc.plus_longue_periode_emmissions_decroissantes([('Lucas', '2024-10-01', 67, 'type3'),('Lucas', '2024-10-01', 6.2, 'type3'),('Lucas', '2024-10-01', 6, 'type3'),('Lucas', '2024-10-01', 5.2, 'type3'),('Lucas', 6.2, 'type3')])==3



def test_est_bien_triee():
    assert bc.est_bien_triee([]) == True
    assert bc.est_bien_triee([('Lucas', '2024-09-01', 67.2, 'type3')]) == True
    assert bc.est_bien_triee([('Lucas', '2024-09-01', 67.2, 'type3'), ('Lucas', '2024-09-02', 70.08, 'type3')]) == True
    assert bc.est_bien_triee([('Lucas', '2024-09-02', 70.08, 'type3'), ('Lucas', '2024-09-01', 67.2, 'type3')]) == False
    #Nouveaux Asserts
    assert bc.est_bien_triee([('Lucas', '2024-09-01', 70.08, 'type3'), ('Lucas', '2024-09-01', 67.2, 'type3'), ('Lucas', '2024-09-01', 627.2, 'type1'), ('Antoine', '2024-09-01', 7.2, 'type1')])
    assert not(bc.est_bien_triee([('Lucas', '2024-09-01', 70.08, 'type3'), ('Lucas', '2024-08-02', 67.2, 'type3'), ('Lucas', '2024-09-06', 627.2, 'type1')]))
    assert bc.est_bien_triee([('Lucas', '2024-08-04', 70.08, 'type3'), ('Lucas', '2024-09-02', 67.2, 'type3'), ('Antoine', '2024-10-01', 7.2, 'type1')])

def test_liste_des_types():
    assert bc.liste_des_types([]) == []
    assert bc.liste_des_types([('Lucas', '2024-09-01', 67.2, 'type3')]) == ['type3']
    assert bc.liste_des_types([('Lucas', '2024-09-01', 67.2, 'type3'), ('Lucas', '2024-09-02', 70.08, 'type3')]) == ['type3']
    assert bc.liste_des_types([('Lucas', '2024-09-01', 67.2, 'type4'), ('Lucas', '2024-09-02', 70.08, 'type3')]) == ['type4', 'type3']
    #Nouveaux Asserts
    assert bc.liste_des_types(["Sheriff",78]) == []
    assert bc.liste_des_types([("Sheriff",78),('Lucas', '2024-09-01', 67.2, 'type3')]) == []
    assert bc.liste_des_types([('Lucas', '2024-09-01', 67.2, 'type4'), ('Lucas', '2024-09-02', 70.08, 'type3'),('Lucas', '2024-09-02', 70.08, 'type1'),('Lucas', '2024-09-02', 70.08, 'type2'),('Lucas', '2024-09-01', 67.2, 'type4'), ('Lucas', '2024-09-02', 70.08, 'type3')]) ==['type4', 'type3',"type1","type2"] 



def test_liste_des_personnes():
    assert bc.liste_des_personnes([]) == []
    assert bc.liste_des_personnes([('Lucas', '2024-09-01', 67.2, 'type3')]) == ['Lucas']
    assert bc.liste_des_personnes([('Lucas', '2024-09-01', 67.2, 'type3'), ('Lucas', '2024-09-02', 70.08, 'type3')]) == ['Lucas']
    assert bc.liste_des_personnes([('Lucas', '2024-09-01', 67.2, 'type3'), ('David', '2024-09-02', 70.08, 'type3')]) == ['Lucas', 'David']
    #Nouveaux Asserts
    assert bc.liste_des_personnes([("Sheriff",78)]) == []
    assert bc.liste_des_personnes([("Sheriff",78),('Lucas', '2024-09-01', 67.2, 'type3')]) == []
    assert bc.liste_des_personnes([('Lucas', '2024-09-01', 67.2, 'type3'), ('Kayn', '2024-09-02', 70.08, 'type3'),('Lucas', '2024-09-02', 70.08, 'type3')]) == ["Lucas","Kayn"]

def test_fusionner_activites():
    assert bc.fusionner_activites([], []) == []
    assert bc.fusionner_activites([('Lucas', '2024-09-01', 67.2, 'type3')], [('Lucas', '2024-09-02', 70.08, 'type3')]) == [('Lucas', '2024-09-01', 67.2, 'type3'), ('Lucas', '2024-09-02', 70.08, 'type3')]
    assert bc.fusionner_activites([('Lucas', '2024-09-02', 70.08, 'type3')], [('Lucas', '2024-09-01', 67.2, 'type3')]) == [('Lucas', '2024-09-01', 67.2, 'type3'), ('Lucas', '2024-09-02', 70.08, 'type3')]
    assert bc.fusionner_activites([('Lucas', '2024-09-01', 67.2, 'type3'), ('Lucas', '2024-09-02', 70.08, 'type3')], [('Lucas', '2024-09-03', 67.2, 'type3')]) == [('Lucas', '2024-09-01', 67.2, 'type3'), ('Lucas', '2024-09-02', 70.08, 'type3'), ('Lucas', '2024-09-03', 67.2, 'type3')]
    assert bc.fusionner_activites(bc.liste3, bc.liste4) == bc.liste2
    #Nouveaux Asserts
    assert bc.fusionner_activites([("Bucheron","Cuisinier","Policier","Banquier")], [('Lucas', '2024-09-01', 67.2, 'type3')]) is None
    assert bc.fusionner_activites([], [('Lucas', '2024-09-01', 67.2, 'type3')]) == [('Lucas', '2024-09-01', 67.2, 'type3')]
    assert bc.fusionner_activites([("Ouistiti",12)], [('Lucas', '2024-09-01', 67.2, 'type3'), ('Lucas', '2024-09-02', 70.08, 'type3')]) is None


def test_premiere_apparition_type():
    assert bc.premiere_apparition_type([], 'type1') == None
    assert bc.premiere_apparition_type([('Lucas', '2024-09-01', 67.2, 'type3')], 'type1') == None
    assert bc.premiere_apparition_type([('Lucas', '2024-09-01', 67.2, 'type3'), ('Lucas', '2024-09-02', 70.08, 'type3')], 'type3') == '2024-09-01'
    #Nouveaux Asserts
    assert bc.premiere_apparition_type([('Lucas', '2024-09-01', 67.2, 'type3')], '') == None
    assert bc.premiere_apparition_type([('Lucas', '2024-08-02', 67.2, 'type1'), ('Lucas', '2024-09-01', 70.08, 'type1')], 'type1') == '2024-08-02'
    assert bc.premiere_apparition_type([('Lucas', '2024-08-02', 67.2, 'type3')], 'type') == None


def test_recherche_activite_dichotomique():
    assert bc.recherche_activite_dichotomique('Lucas', '2024-09-01', 'type3', []) == None
    assert bc.recherche_activite_dichotomique('Lucas', '2024-09-01', 'type3', [('Lucas', '2024-09-01', 67.2, 'type3'), ('Lucas', '2024-09-02', 70.08, 'type3')]) == ('Lucas', '2024-09-01', 67.2, 'type3')
    #Nouveaux Asserts
    assert bc.recherche_activite_dichotomique('Lucas', '2024-09-01', 'type7', bc.liste2) is None
    assert bc.recherche_activite_dichotomique('Florian', '2024-09-26', 'type2', bc.liste6) ==('Florian', '2024-09-26', 74.1, 'type2')
    assert bc.recherche_activite_dichotomique('Lucas', '2024-09-01', 'type1', {7,8,78,8}) is None



def test_charger_sauver():
    bc.sauver_activites("fichier_test.csv",[('Lucas', '2024-08-02', 67.2, 'type1'), ('Lucas', '2024-09-01', 70.08, 'type1')])
    bc.charger_sauver("fichier_test.csv",[("Maria","2024-05-21",54,"type1"),("Marios","2023-13-31",12.6,"type3")])
    assert bc.charger_activites("fichier_test.csv") == [('Lucas', '2024-08-02', '67.2', 'type1'), ('Lucas', '2024-09-01', '70.08', 'type1'), ('Maria', '2024-05-21', '54', 'type1'), ('Marios', '2023-13-31', '12.6', 'type3')]

    bc.sauver_activites("fichier_test.csv",[])
    bc.charger_sauver("fichier_test.csv",[])
    assert bc.charger_activites("fichier_test.csv") == []



def test_temps_activite():
    assert bc.temps_activite(('Lucas', '2024-09-01', 67.2, 'type3'), bc.co2_minute) == 67.2/0.96
    assert bc.temps_activite(('Lucas', '2024-09-02', 70.08, 'type5'), bc.co2_minute) is None
    #Nouveaux Asserts
    assert bc.temps_activite(('Lucas', '2024-09-02', "70.08", 'type2'), bc.co2_minute) is None
    assert bc.temps_activite(('Lucas', '2024-09-02',124.5 , 'type2'), bc.co2_minute) == 124.5/0.65
    assert bc.temps_activite(('Lucas', '2024-09-02', 'type2'), bc.co2_minute) is None
    assert bc.temps_activite([], bc.co2_minute) is None


def test_cumul_temps_activite():
    assert bc.cumul_temps_activite([], bc.co2_minute) == 0
    assert bc.cumul_temps_activite([('Lucas', '2024-09-01', 67.2, 'type3')], bc.co2_minute) == 67.2/0.96
    #Nouveaux Asserts
    assert bc.cumul_temps_activite(bc.liste2, bc.co2_minute) == 301.91189318344493
    assert bc.temps_activite([('Lucas', '2024-09-02',124.5 , 'type2'),('Lucas', '2024-09-02', 'type2')], bc.co2_minute) is None
    assert bc.cumul_temps_activite(('Lucas', '2024-09-02',124.5 , 'type5'), bc.co2_minute) is None

# ---------------------------------------------------------------------------------------------
# Ajoutez ici les tests manquants (vos propres fonctions le cas échéant)
# ---------------------------------------------------------------------------------------------
def test_est_activite():
    assert bc.est_activite(('Lucas', '2024-09-01', 67.2, 'type3'))
    assert not(bc.est_activite(('Lucas', '2024-09-1', 67.2, 'type3')))
    assert not(bc.est_activite(()))
    assert not(bc.est_activite(('2024-09-01','Matthieu', 67.2, 'type3')))
    assert bc.est_activite(('Lucas', '2024-09-01', 67, 'type3'))
    assert not(bc.est_activite(('Lucas', '2024-09-01', 'type3')))

def test_creer_liste_date(): 
    assert bc.creer_liste_date(bc.liste4,"2023-09-12","2024-08-12") == []
    assert bc.creer_liste_date([('Lucas', '2024-09-01', 'type3'),('Antoine', '2024-09-11', 'type3'),('Pierre', '2024-09-16', 'type3')],"2024-09-09","2024-09-13") == [('Antoine', '2024-09-11', 'type3')]
    assert bc.creer_liste_date(bc.liste4,"2024-09-12","2024-09-11") is None
    assert bc.creer_liste_date([],"2024-09-12","2024-09-21") == []
    assert bc.creer_liste_date(bc.liste1,"sdfgsdfosdfi","2024-08-12") is None

def test_plus_longue_periode_emmissions_croissantes():
    assert bc.plus_longue_periode_emmissions_croissantes([]) == 0
    assert bc.plus_longue_periode_emmissions_croissantes(bc.liste6) == 4
    #Nouveaux Asserts
    assert bc.plus_longue_periode_emmissions_croissantes([('Lucas', '2024-10-01', 67, 'type3'),('Lucas', '2024-10-01', 6.2, 'type3'),('Lucas', '2024-10-01', 6, 'type3')])==0
    assert bc.plus_longue_periode_emmissions_croissantes(bc.liste2)==2
    assert bc.plus_longue_periode_emmissions_croissantes([('Lucas', '2024-10-01', 67, 'type3'),('Lucas', '2024-10-01', 6.2, 'type3'),('Lucas', '2024-10-01', 6, 'type3'),('Lucas', '2024-10-01', 5.2, 'type3'),('Lucas', 6.2, 'type3')])==0


def test_min_emmission():
    assert bc.min_emmission([]) == None
    assert bc.min_emmission(bc.liste1) == ('Christophe', '2024-09-28', 14, 'type3')
    #Nouveaux Asserts
    assert (bc.min_emmission((bc.liste5)))==('Anaëlle', '2024-09-03', 0.0, 'type1')
    assert (bc.min_emmission([('Lucas', '2024-10-01', 67, 'type3'),('Lucas', '2024-10-01', 6.2, 'type3')]))== ('Lucas', '2024-10-01', 6.2, 'type3')
    assert (bc.min_emmission([('Lucas', '2024-10-01', 67, 'type3'),('Lucas', '2024-10-01', 6.2, 'type3'),('Lucas', '2024-10-01', "6.2", 'type3')])) is None
    
