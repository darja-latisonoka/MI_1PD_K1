# Pārbauda vai vairs nav iespējams izdarīt gājienu
def nav_gajienu(virsotne):
    return virsotne.skaitlis % 2 != 0 and virsotne.skaitlis % 3 != 0


# Pārbauda vai spēle ir beigusies
# Spēle beidzas, ja iegūts 2 vai 3 vai nav iespējamu gājienu
def ir_beigas(virsotne):
    return virsotne.skaitlis == 2 or virsotne.skaitlis == 3 or nav_gajienu(virsotne)


# Pārbauda vai no dotā skaitļa vienā gājienā var iegūt skaitli 2
def var_sasniegt_2(skaitlis):
    return (skaitlis % 2 == 0 and skaitlis // 2 == 2) or \
           (skaitlis % 3 == 0 and skaitlis // 3 == 2)


# Heiristiskā novērtējuma funkcija
def heuristika(virsotne):

    # Pamata novērtējums:
    vertiba = virsotne.p2 - virsotne.p1

    # Ja dators var uzreiz iegūt 2, tad var arī saņemt banku
    if virsotne.gajiens == 2 and var_sasniegt_2(virsotne.skaitlis):
        vertiba += virsotne.banka

    # Ja cilvēks var uzreiz iegūt 2, tas ir bīstami
    elif virsotne.gajiens == 1 and var_sasniegt_2(virsotne.skaitlis):
        vertiba -= virsotne.banka

    # Banka pati par sevi ir neliels bonuss, bet ne pārāk liels
    else:
        vertiba += 0.1 * virsotne.banka

    return vertiba