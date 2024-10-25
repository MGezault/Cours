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
    assert (bc.max_emmission([(),(),()])) is None


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


def test_cumul_emmissions():
    assert bc.cumul_emmissions([]) == 0
    assert bc.cumul_emmissions(bc.liste4) == 78

def test_plus_longue_periode_emmissions_decroissantes():
    assert bc.plus_longue_periode_emmissions_decroissantes([]) == 0
    assert bc.plus_longue_periode_emmissions_decroissantes(bc.liste6) == 3
    
def test_est_bien_triee():
    assert bc.est_bien_triee([]) == True
    assert bc.est_bien_triee([('Lucas', '2024-09-01', 67.2, 'type3')]) == True
    assert bc.est_bien_triee([('Lucas', '2024-09-01', 67.2, 'type3'), ('Lucas', '2024-09-02', 70.08, 'type3')]) == True
    assert bc.est_bien_triee([('Lucas', '2024-09-02', 70.08, 'type3'), ('Lucas', '2024-09-01', 67.2, 'type3')]) == False


def test_liste_des_types():
    assert bc.liste_des_types([]) == []
    assert bc.liste_des_types([('Lucas', '2024-09-01', 67.2, 'type3')]) == ['type3']
    assert bc.liste_des_types([('Lucas', '2024-09-01', 67.2, 'type3'), ('Lucas', '2024-09-02', 70.08, 'type3')]) == ['type3']
    assert bc.liste_des_types([('Lucas', '2024-09-01', 67.2, 'type4'), ('Lucas', '2024-09-02', 70.08, 'type3')]) == ['type4', 'type3']


def test_liste_des_personnes():
    assert bc.liste_des_personnes([]) == []
    assert bc.liste_des_personnes([('Lucas', '2024-09-01', 67.2, 'type3')]) == ['Lucas']
    assert bc.liste_des_personnes([('Lucas', '2024-09-01', 67.2, 'type3'), ('Lucas', '2024-09-02', 70.08, 'type3')]) == ['Lucas']
    assert bc.liste_des_personnes([('Lucas', '2024-09-01', 67.2, 'type3'), ('David', '2024-09-02', 70.08, 'type3')]) == ['Lucas', 'David']


def test_fusionner_activites():
    assert bc.fusionner_activites([], []) == []
    assert bc.fusionner_activites([('Lucas', '2024-09-01', 67.2, 'type3')], [('Lucas', '2024-09-02', 70.08, 'type3')]) == [('Lucas', '2024-09-01', 67.2, 'type3'), ('Lucas', '2024-09-02', 70.08, 'type3')]
    assert bc.fusionner_activites([('Lucas', '2024-09-02', 70.08, 'type3')], [('Lucas', '2024-09-01', 67.2, 'type3')]) == [('Lucas', '2024-09-01', 67.2, 'type3'), ('Lucas', '2024-09-02', 70.08, 'type3')]
    assert bc.fusionner_activites([('Lucas', '2024-09-01', 67.2, 'type3'), ('Lucas', '2024-09-02', 70.08, 'type3')], [('Lucas', '2024-09-03', 67.2, 'type3')]) == [('Lucas', '2024-09-01', 67.2, 'type3'), ('Lucas', '2024-09-02', 70.08, 'type3'), ('Lucas', '2024-09-03', 67.2, 'type3')]
    assert bc.fusionner_activites(bc.liste3, bc.liste4) == bc.liste2


def test_premiere_apparition_type():
    assert bc.premiere_apparition_type([], 'type1') == None
    assert bc.premiere_apparition_type([('Lucas', '2024-09-01', 67.2, 'type3')], 'type1') == None
    assert bc.premiere_apparition_type([('Lucas', '2024-09-01', 67.2, 'type3'), ('Lucas', '2024-09-02', 70.08, 'type3')], 'type3') == '2024-09-01'


def test_recherche_activite_dichotomique():
    assert bc.recherche_activite_dichotomique('Lucas', '2024-09-01', 'type3', []) == None
    assert bc.recherche_activite_dichotomique('Lucas', '2024-09-01', 'type3', [('Lucas', '2024-09-01', 67.2, 'type3'), ('Lucas', '2024-09-02', 70.08, 'type3')]) == ('Lucas', '2024-09-01', 67.2, 'type3')

def test_charger_sauver():
    ...

def test_temps_activite():
    assert bc.temps_activite(('Lucas', '2024-09-01', 67.2, 'type3'), bc.co2_minute) == 67.2/0.96
    assert bc.temps_activite(('Lucas', '2024-09-02', 70.08, 'type5'), bc.co2_minute) is None

def test_cumul_temps_activite():
    assert bc.cumul_temps_activite([], bc.co2_minute) == 0
    assert bc.cumul_temps_activite([('Lucas', '2024-09-01', 67.2, 'type3')], bc.co2_minute) == 67.2/0.96

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