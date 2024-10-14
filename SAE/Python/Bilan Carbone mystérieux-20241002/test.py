import bilan_carbone as bc  

def test_cumul_emmissions():
    assert bc.cumul_emmissions([]) == 0
    assert bc.cumul_emmissions(bc.liste4) == 78

test_cumul_emmissions()
p=bc.cumul_emmissions(bc.liste3)
print(p)