# Pārbauda vai vairs nav iespējams izdarīt gājienu
def nav_gajienu(virsotne):
    return virsotne.skaitlis % 2 != 0 and virsotne.skaitlis % 3 != 0


# Pārbauda vai spēle ir beigusies
def ir_beigas(virsotne):
    return virsotne.skaitlis == 2 or virsotne.skaitlis == 3 or nav_gajienu(virsotne)


# Pārbauda vai no dotā skaitļa vienā gājienā var iegūt skaitli 2
def var_sasniegt_2(skaitlis):
    return (skaitlis % 2 == 0 and skaitlis // 2 == 2) or \
           (skaitlis % 3 == 0 and skaitlis // 3 == 2)


def iespejamie_gajieni(skaitlis):
    gajieni = 0
    if skaitlis % 2 == 0:
        gajieni += 1
    if skaitlis % 3 == 0:
        gajieni += 1
    return gajieni


# Heiristiskā novērtējuma funkcija
def heuristika(virsotne):
    # Ja spēle beigusies, ņemam gala rezultātu
    if ir_beigas(virsotne):
        return 10 * (virsotne.p2 - virsotne.p1)

    # Pamata novērtējums:
    vertiba = virsotne.p2 - virsotne.p1

    # Neliels bankas svars
    vertiba += 0.5 * virsotne.banka

    # Ja dators var uzreiz iegūt 2, tas ir labi
    if var_sasniegt_2(virsotne.skaitlis):
        if virsotne.gajiens == 2:
            vertiba += virsotne.banka
        else:
            vertiba -= virsotne.banka

    # Jo vairāk iespējamo gājienu, jo elastīgāka pozīcija
    gajienu_skaits = iespejamie_gajieni(virsotne.skaitlis)

    if virsotne.gajiens == 2:
        vertiba += 0.5 * gajienu_skaits
    else:
        vertiba -= 0.5 * gajienu_skaits

    return vertiba