#Klase, kas atbilst speles kokam        
class Speles_koks:
    
    # Konstruktors, kas izveido tuksu virsotnu un loku kopu
    def __init__(self):
        self.virsotnu_kopa=[] # saraksts ar visam virsotnem
        self.loku_kopa=dict() # vardnica ar lokiem starp virsotnem
    
    # Pievieno jaunu virsotni kokam
    def pievienot_virsotni(self, Virsotne):
        self.virsotnu_kopa.append(Virsotne)
        
    # Pievieno loku starp divam virsotnem
    def pievienot_loku(self, sakumvirsotne_id, beiguvirsotne_id):
        self.loku_kopa[sakumvirsotne_id]=self.loku_kopa.get(sakumvirsotne_id,[])+[beiguvirsotne_id]