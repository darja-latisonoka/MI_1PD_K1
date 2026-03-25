import random
from models.node import Virsotne
from models.game_tree import Speles_koks


MAX_LIMENIS = 6

def gajiena_parbaude(gajiena_tips, generetas_virsotnes, pasreizeja_virsotne, sp): # gajiena_tips: '2' vai '3' (dalītājs)
    # ja 2 vai 3 spēle beidzas
    if pasreizeja_virsotne.skaitlis == 2 or pasreizeja_virsotne.skaitlis == 3:
        return
    
    # ja sasniegts maksimālais dziļums, tālāk koku neveido
    if pasreizeja_virsotne.limenis >= MAX_LIMENIS:
        return

    dalitajs = int(gajiena_tips)
    skaitlis = pasreizeja_virsotne.skaitlis

    # Pārbaude: vai var dalīt bez atlikuma
    if skaitlis % dalitajs != 0:
        return

    global j
    id_new = 'A' + str(j)
    j += 1

    # Jaunais skaitlis pēc dalīšanas
    jaunais_skaitlis = skaitlis // dalitajs

    # Pašreizējie punkti un banka
    p1_new = pasreizeja_virsotne.p1
    p2_new = pasreizeja_virsotne.p2
    banka_new = pasreizeja_virsotne.banka

    # Kurš izdara gājienu
    gajiens = pasreizeja_virsotne.gajiens

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

    limenis_new = pasreizeja_virsotne.limenis + 1

    # Nākamais gājiens (mainās spēlētājs)
    if gajiens == 1:
        gajiens_new = 2
    else:
        gajiens_new = 1

    jauna_virsotne = Virsotne(
        id_new,
        jaunais_skaitlis,
        p1_new,
        p2_new,
        banka_new,
        limenis_new,
        gajiens_new
    )

    # Pārbaude vai tāda virsotne jau eksistē
    parbaude = False
    i = 0
    while (not parbaude) and (i < len(sp.virsotnu_kopa)):
        v = sp.virsotnu_kopa[i]
        if (
            v.skaitlis == jauna_virsotne.skaitlis and
            v.p1 == jauna_virsotne.p1 and
            v.p2 == jauna_virsotne.p2 and
            v.banka == jauna_virsotne.banka and
            v.limenis == jauna_virsotne.limenis and
            v.gajiens == jauna_virsotne.gajiens
        ):
            parbaude = True
        else:
            i += 1

    if not parbaude:
        sp.pievienot_virsotni(jauna_virsotne)
        generetas_virsotnes.append(jauna_virsotne)
        sp.pievienot_loku(pasreizeja_virsotne.id, id_new)
    else:
        j -= 1
        sp.pievienot_loku(pasreizeja_virsotne.id, sp.virsotnu_kopa[i].id)


def uzgeneret_koku_no_virsotnes(sp, sakuma_virsotne):

    # saraksts ar virsotnēm
    generetas_virsotnes = []

    sp.pievienot_virsotni(sakuma_virsotne)
    generetas_virsotnes.append(sakuma_virsotne)

    global j
    j = 2

    # ģenerē koku
    while len(generetas_virsotnes) > 0:

        pasreizeja_virsotne = generetas_virsotnes[0]

        # gājiens: dalīt ar 2
        gajiena_parbaude('2', generetas_virsotnes, pasreizeja_virsotne, sp)

        # gājiens: dalīt ar 3
        gajiena_parbaude('3', generetas_virsotnes, pasreizeja_virsotne, sp)

        generetas_virsotnes.pop(0)
    
def rebuild_tree_from_current_node(current_node):
    sp = Speles_koks()

    uzgeneret_koku_no_virsotnes(sp, current_node)
    virsotnes_dict = {v.id: v for v in sp.virsotnu_kopa}

    return sp, virsotnes_dict