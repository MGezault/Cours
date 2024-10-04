def cpt_syl(mot):
    syllabes = 0
    voyelles ="aeiouy"
    lettre_precedente = mot[0]
    for lettre in mot[1:]:
        if lettre_precedente in voyelles:
            if lettre not in(voyelles):
                syllabes += 1
        lettre_precedente = lettre
    if lettre in voyelles:
        syllabes += 1
    return syllabes

def test_cpt_syl():
    assert (cpt_syl("tableau")==2)
    assert (cpt_syl("ecouteur")== 3)
    assert (cpt_syl("abricot")==3)
    assert(cpt_syl("ananas")==3)


