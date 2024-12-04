# pylint: disable=missing-function-docstring
"""les tests pour les foctions des exercices 1 et 4 du TP9"""
import petites_betes

# ==================================
# TESTS pour l'exercice 1
# ==================================

def test_toutes_les_familles():
    mon_pokedex = [('Bulbizarre', 'Plante'), ('Aeromite', 'Poison'), ('Abo', 'Poison')]
    assert petites_betes.toutes_les_familles(mon_pokedex) == {'Plante', 'Poison'}
    mon_pokedex2 = [('Pikachu', 'Electrik'), ('Bulbizarre', 'Plante'), ('Salameche', 'Feu'), ('Aeromite', 'Poison')]
    assert petites_betes.toutes_les_familles(mon_pokedex2) == {'Electrik', 'Plante', 'Feu', 'Poison'}
    mon_pokedex3 = [('Bulbizarre', 'Plante'), ('Herbizarre', 'Plante')]
    assert petites_betes.toutes_les_familles(mon_pokedex3) == {'Plante'}
    mon_pokedex4 = []
    assert petites_betes.toutes_les_familles(mon_pokedex4) == set()

def test_nombre_pokemons():
    mon_pokedex = [('Bulbizarre', 'Plante'), ('Aeromite', 'Poison'), ('Abo', 'Poison')]
    assert petites_betes.nombre_pokemons(mon_pokedex, 'Plante') == 1
    assert petites_betes.nombre_pokemons(mon_pokedex, 'Poison') == 2
    assert petites_betes.nombre_pokemons(mon_pokedex, 'Insecte') == 0
    
    mon_pokedex2 = [('Pikachu', 'Electrik'), ('Bulbizarre', 'Plante'), ('Salameche', 'Feu'), ('Aeromite', 'Poison')]
    assert petites_betes.nombre_pokemons(mon_pokedex2, 'Electrik') == 1
    assert petites_betes.nombre_pokemons(mon_pokedex2, 'Feu') == 1
    assert petites_betes.nombre_pokemons(mon_pokedex2, 'Poison') == 1
    assert petites_betes.nombre_pokemons(mon_pokedex2, 'Eau') == 0

def test_frequences_famille():
    mon_pokedex = [('Bulbizarre', 'Plante'), ('Aeromite', 'Poison'), ('Abo', 'Poison')]
    assert petites_betes.frequences_famille(mon_pokedex) == {'Plante': 1, 'Poison': 2}
    mon_pokedex2 = [('Pikachu', 'Electrik'), ('Bulbizarre', 'Plante'), ('Salameche', 'Feu'), ('Aeromite', 'Poison')]
    assert petites_betes.frequences_famille(mon_pokedex2) == {'Electrik': 1, 'Plante': 1, 'Feu': 1, 'Poison': 1}
    mon_pokedex3 = [('Bulbizarre', 'Plante'), ('Herbizarre', 'Plante')]
    assert petites_betes.frequences_famille(mon_pokedex3) == {'Plante': 2}

def test_dico_par_famille():
    mon_pokedex = [('Bulbizarre', 'Plante'), ('Aeromite', 'Poison'), ('Abo', 'Poison')]
    assert petites_betes.dico_par_famille(mon_pokedex) == {
        'Plante': {'Bulbizarre'},
        'Poison': {'Aeromite', 'Abo'}
    }
    mon_pokedex2 = [('Pikachu', 'Electrik'), ('Bulbizarre', 'Plante'), ('Salameche', 'Feu'), ('Aeromite', 'Poison')]
    assert petites_betes.dico_par_famille(mon_pokedex2) == {
        'Electrik': {'Pikachu'},
        'Plante': {'Bulbizarre'},
        'Feu': {'Salameche'},
        'Poison': {'Aeromite'}
    }
    mon_pokedex3 = [('Bulbizarre', 'Plante'), ('Herbizarre', 'Plante')]
    assert petites_betes.dico_par_famille(mon_pokedex3) == {'Plante': {'Bulbizarre', 'Herbizarre'}}

def test_famille_la_plus_representee():
    mon_pokedex = [('Bulbizarre', 'Plante'), ('Aeromite', 'Poison'), ('Abo', 'Poison')]
    assert petites_betes.famille_la_plus_representee(mon_pokedex) == 'Poison'
    mon_pokedex2 = [('Pikachu', 'Electrik'), ('Bulbizarre', 'Plante'), ('Salameche', 'Feu'), ('Aeromite', 'Poison')]
    assert petites_betes.famille_la_plus_representee(mon_pokedex2) in {'Electrik', 'Plante', 'Feu', 'Poison'}
    mon_pokedex3 = [('Bulbizarre', 'Plante'), ('Herbizarre', 'Plante')]
    assert petites_betes.famille_la_plus_representee(mon_pokedex3) == 'Plante'
    mon_pokedex4 = []
    assert petites_betes.famille_la_plus_representee(mon_pokedex4) is None


# ==================================
# TESTS pour l'exercice 4
# ==================================

def test_toutes_les_familles_v2():
    mon_pokedex = {"Bulbizarre":{"Plante", "Poison"},
                   "Aeromite":{"Poison", "Insecte"}, "Abo":{"Poison"}}
    assert petites_betes.toutes_les_familles_v2(mon_pokedex) == {'Plante', 'Insecte', 'Poison'}
    nv_pokedex = {"Giratina" : {"Dragon","Spectre"},"Lucario" :{"Acier","Combat"},"Etouraptor": {"Normal","Vol"},"Sulfura":{"Vol","Feu"}}
    assert petites_betes.toutes_les_familles_v2(nv_pokedex)== {"Dragon","Spectre","Acier","Combat","Normal","Vol","Feu"}

def test_nombre_pokemons_v2():
    mon_pokedex = {"Bulbizarre":{"Plante", "Poison"},
                   "Aeromite":{"Poison", "Insecte"}, "Abo":{"Poison"}}
    assert petites_betes.nombre_pokemons_v2(mon_pokedex, 'Plante') == 1
    assert petites_betes.nombre_pokemons_v2(mon_pokedex, 'Poison') == 3
    assert petites_betes.nombre_pokemons_v2(mon_pokedex, 'Fée') == 0
    nv_pokedex = {"Giratina" : {"Dragon","Spectre"},"Lucario" :{"Acier","Combat"},"Etouraptor": {"Normal","Vol"},"Sulfura":{"Vol","Feu"}}
    assert petites_betes.nombre_pokemons_v2(nv_pokedex, 'Dragon') == 1
    assert petites_betes.nombre_pokemons_v2(nv_pokedex, 'Vol') == 2


def test_frequences_famille_v2():
    mon_pokedex = {"Bulbizarre":{"Plante", "Poison"},
                   "Aeromite":{"Poison", "Insecte"}, "Abo":{"Poison"}}
    assert petites_betes.frequences_famille_v2(mon_pokedex) == {'Plante': 1, 'Poison': 3, 'Insecte':1}
    nv_pokedex = {"Giratina" : {"Dragon","Spectre"},"Lucario" :{"Acier","Combat"},"Etouraptor": {"Normal","Vol"},"Sulfura":{"Vol","Feu"}}
    assert petites_betes.frequences_famille_v2(nv_pokedex) == {"Dragon":1,"Spectre":1,"Acier":1,"Combat":1,"Normal":1,"Vol": 2,"Feu" : 1}


def test_dico_par_famille_v2():
    mon_pokedex = {"Bulbizarre":{"Plante", "Poison"},
                   "Aeromite":{"Poison", "Insecte"}, "Abo":{"Poison"}}
    assert petites_betes.dico_par_famille_v2(mon_pokedex) == {
        'Plante': {'Bulbizarre'},
        'Poison': {'Aeromite', 'Abo', 'Bulbizarre'},
        'Insecte':{'Aeromite'}}
    nv_pokedex = {"Giratina" : {"Dragon","Spectre"},"Lucario" :{"Acier","Combat"},"Etouraptor": {"Normal","Vol"},"Sulfura":{"Vol","Feu"}}
    assert petites_betes.dico_par_famille_v2(nv_pokedex) == {"Dragon":{"Giratina"},"Spectre":{"Giratina"},"Acier":{"Lucario"},"Combat":{"Lucario"},"Normal": {"Etouraptor"},"Vol": {"Etouraptor","Sulfura"},"Feu" : {"Sulfura"}}



def test_famille_la_plus_representee_v2():
    mon_pokedex = {"Bulbizarre":{"Plante", "Poison"},
                   "Aeromite":{"Poison", "Insecte"}, "Abo":{"Poison"}}
    assert petites_betes.famille_la_plus_representee_v2(mon_pokedex) == 'Poison'
    nv_pokedex = {"Giratina" : {"Dragon","Spectre"},"Lucario" :{"Acier","Combat"},"Etouraptor": {"Normal","Vol"},"Sulfura":{"Vol","Feu"}}
    assert petites_betes.famille_la_plus_representee_v2(nv_pokedex) == "Vol"

