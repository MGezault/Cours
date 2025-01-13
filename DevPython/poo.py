class Couple():

    def __init__(self,v1,v2):
        self.valeur1=v1
        self.valeur2=v2

    def get_valeur1(self):
        return self.valeur1
    
    def get_valeur2(self):
        return self.valeur2
    
    def set_valeur1(self,nouvelle_val):
        self.valeur1=nouvelle_val

    def set_valeur2(self,nouvelle_val):
        self.valeur2=nouvelle_val

    def somme_compo(self):
        return self.valeur1()+self.valeur2()
    
    def somme_couples(self,couple2):
        return self.somme_compo() + couple2.somme_compo()