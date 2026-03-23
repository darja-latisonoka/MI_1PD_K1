#Klase, kas atbilst vienai virsotnei speles koka
class Virsotne:

    # Klases konstruktors, kas izveido speles koka virsotni
    def __init__(self, id, skaitlis, p1, p2, banka, limenis, gajiens):
        self.id = id
        self.skaitlis = skaitlis # pasreizejais skaitlis spele
        self.p1 = p1 # pirma speletaja punkti
        self.p2 = p2 # otra speletaja punkti
        self.banka = banka # bankas punktu skaits
        self.limenis = limenis # virsotnes limenis speles koka
        self.gajiens = gajiens # kurs speletajs izdara gajienu (1 vai 2)