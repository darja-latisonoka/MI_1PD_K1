#Klase, kas atbilst sp?les kokam        
class Speles_koks:
    
    # Konstruktors, kas izveido tuk?u virsot?u un loku kopu
    def __init__(self):
        self.virsotnu_kopa=[] # saraksts ar vis?m virsotn?m
        self.loku_kopa=dict() # v?rdn?ca ar lokiem starp virsotn?m
    
    # Pievieno jaunu virsotni kokam
    def pievienot_virsotni(self, Virsotne):
        self.virsotnu_kopa.append(Virsotne)
        
    # Pievieno loku starp div?m virsotn?m
    def pievienot_loku(self, sakumvirsotne_id, beiguvirsotne_id):
        self.loku_kopa[sakumvirsotne_id]=self.loku_kopa.get(sakumvirsotne_id,[])+[beiguvirsotne_id]