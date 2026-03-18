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
    
    # Ja spēle ir beigusies, atgriež gala novērtējumu
    if ir_beigas(virsotne):
        if virsotne.p2 > virsotne.p1:
            return 1000 # uzvar dators
        elif virsotne.p2 < virsotne.p1:
            return -1000 # uzvar cilvēks
        return 0 # neizšķirts

    # Pamata novērtējums:
    # punktu starpība starp datoru un cilvēku + daļa no bankas vērtības
    vertiba = (virsotne.p2 - virsotne.p1) + 0.5 * virsotne.banka

    # Ja tagad ir datora gājiens un dators var uzreiz iegūt 2, tad pozīcija kļūst daudz izdevīgāka
    if virsotne.gajiens == 2 and var_sasniegt_2(virsotne.skaitlis):
        vertiba += 20 + virsotne.banka

    # Ja tagad ir cilvēka gājiens un cilvēks var uzreiz iegūt 2, tad pozīcija datoram kļūst bīstamāka
    if virsotne.gajiens == 1 and var_sasniegt_2(virsotne.skaitlis):
        vertiba -= 20 + virsotne.banka

    return vertiba