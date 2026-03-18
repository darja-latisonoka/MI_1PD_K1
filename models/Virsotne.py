#Klase, kas atbilst vienai virsotnei sp?les kok?
class Virsotne:

    # Klases konstruktors, kas izveido sp?les koka virsotni
    def __init__(self, id, skaitlis, p1, p2, banka, limenis, gajiens):
        self.id = id
        self.skaitlis = skaitlis # pa?reiz?jais skaitlis sp?l?
        self.p1 = p1 # pirm? sp?l?t?ja punkti
        self.p2 = p2 # otr? sp?l?t?ja punkti
        self.banka = banka # bankas punktu skaits
        self.limenis = limenis # virsotnes l?menis sp?les kok?
        self.gajiens = gajiens # kur? sp?l?t?js izdara g?jienu (1 vai 2)