
import random

skaitli = []

while len(skaitli) < 5:
    x = random.randint(1000000, 5000000)
    if x % 216 == 0:
        skaitli.append(x)

print(skaitli)

#Klase, kas atbilst vienai virsotnei spēles kokā
class Virsotne:

    # Klases konstruktors, kas izveido spēles koka virsotni
    def __init__(self, id, skaitlis, p1, p2, banka, limenis, gajiens):
        self.id = id
        self.skaitlis = skaitlis # pašreizējais skaitlis spēlē
        self.p1 = p1 # pirmā spēlētāja punkti
        self.p2 = p2 # otrā spēlētāja punkti
        self.banka = banka # bankas punktu skaits
        self.limenis = limenis # virsotnes līmenis spēles kokā
        self.gajiens = gajiens # kurš spēlētājs izdara gājienu (1 vai 2)
               
#Klase, kas atbilst spēles kokam        
class Speles_koks:
    
    # Konstruktors, kas izveido tukšu virsotņu un loku kopu
    def __init__(self):
        self.virsotnu_kopa=[] # saraksts ar visām virsotnēm
        self.loku_kopa=dict() # vārdnīca ar lokiem starp virsotnēm
    
    # Pievieno jaunu virsotni kokam
    def pievienot_virsotni(self, Virsotne):
        self.virsotnu_kopa.append(Virsotne)
        
    # Pievieno loku starp divām virsotnēm
    def pievienot_loku(self, sakumvirsotne_id, beiguvirsotne_id):
        self.loku_kopa[sakumvirsotne_id]=self.loku_kopa.get(sakumvirsotne_id,[])+[beiguvirsotne_id]


def gajiena_parbaude(gajiena_tips, generetas_virsotnes, pasreizeja_virsotne):
    # ja 2 vai 3 spēle beidzas
    if pasreizeja_virsotne[1] == 2 or pasreizeja_virsotne[1] == 3:
        return

    # gajiena_tips: '2' vai '3' (dalītājs)

    dalitajs = int(gajiena_tips)
    skaitlis = pasreizeja_virsotne[1]

    # Pārbaude: vai var dalīt bez atlikuma
    if skaitlis % dalitajs != 0:
        return

    global j
    id_new = 'A' + str(j)
    j += 1

    # Jaunais skaitlis pēc dalīšanas
    jaunais_skaitlis = skaitlis // dalitajs

    # Pašreizējie punkti un banka
    p1_new = pasreizeja_virsotne[2]
    p2_new = pasreizeja_virsotne[3]
    banka_new = pasreizeja_virsotne[4]

    # Kurš izdara gājienu
    gajiens = pasreizeja_virsotne[6]

    # Punkti par pāra/nepāra rezultātu
    if (jaunais_skaitlis % 2) == 0:
        result = 1   # ja pāra tad +1
    else:
        result = -1  # ja nepāra tad -1

    if gajiens == 1:
        p1_new = p1_new + result
    else:
        p2_new = p2_new + result

    # Banka: ja skaitlis beidzas ar 0 vai 5
    if (jaunais_skaitlis % 10) == 0 or (jaunais_skaitlis % 10) == 5:
        banka_new = banka_new + 1

    # Spēles beigas: ja iegūst 2 vai 3
    if jaunais_skaitlis == 2:
        if gajiens == 1:
            p1_new = p1_new + banka_new
        else:
            p2_new = p2_new + banka_new
        banka_new = 0

    limenis_new = pasreizeja_virsotne[5] + 1

    # Nākamais gājiens (mainās spēlētājs)
    if gajiens == 1:
        gajiens_new = 2
    else:
        gajiens_new = 1

    jauna_virsotne = Virsotne(id_new, jaunais_skaitlis, p1_new, p2_new, banka_new, limenis_new, gajiens_new)

    # Pārbaude vai tāda virsotne jau eksistē
    parbaude = False
    i = 0
    while (not parbaude) and (i <= len(sp.virsotnu_kopa)-1):
        v = sp.virsotnu_kopa[i]
        if (v.skaitlis == jauna_virsotne.skaitlis) and (v.p1 == jauna_virsotne.p1) and (v.p2 == jauna_virsotne.p2) and (v.banka == jauna_virsotne.banka) and (v.limenis == jauna_virsotne.limenis) and (v.gajiens == jauna_virsotne.gajiens):
            parbaude = True
        else:
            i += 1

    if not parbaude:
        sp.pievienot_virsotni(jauna_virsotne)
        generetas_virsotnes.append([id_new, jaunais_skaitlis, p1_new, p2_new, banka_new, limenis_new, gajiens_new])
        sp.pievienot_loku(pasreizeja_virsotne[0], id_new)
    else:
        j -= 1
        sp.pievienot_loku(pasreizeja_virsotne[0], sp.virsotnu_kopa[i].id)
     
# izveido tukšu spēles koku
sp = Speles_koks()

# saraksts ar virsotnēm
generetas_virsotnes = []

# sākuma virsotne, punkti 0, banka 0, līmenis 1, sāk p1
sp.pievienot_virsotni(Virsotne('A1', skaitli[0], 0, 0, 0, 1, 1))
generetas_virsotnes.append(['A1', skaitli[0], 0, 0, 0, 1, 1])

# virsotņu skaitītājs
j = 2

# ģenerē koku
while len(generetas_virsotnes) > 0:
    pasreizeja_virsotne = generetas_virsotnes[0]

    # gājiens: dalīt ar 2
    gajiena_parbaude('2', generetas_virsotnes, pasreizeja_virsotne)

    # gājiens: dalīt ar 3
    gajiena_parbaude('3', generetas_virsotnes, pasreizeja_virsotne)

    # izņem apstrādāto virsotni
    generetas_virsotnes.pop(0)

# izvada virsotnes
for x in sp.virsotnu_kopa:
    print(x.id, x.skaitlis, x.p1, x.p2, x.banka, x.limenis, x.gajiens)

# izvada lokus
for x, y in sp.loku_kopa.items():
    print(x, y)