from logic import Metrics
from logic.heuristic import heuristika, ir_beigas

def iegut_bernus(virsotne, sp, virsotnes_dict):
    bernu_id = sp.loku_kopa.get(virsotne.id, [])
    return [virsotnes_dict[vid] for vid in bernu_id]


def minimax(virsotne, sp, virsotnes_dict):
    Metrics.evaluated_nodes += 1
    
    if ir_beigas(virsotne):
        return heuristika(virsotne)

    berni = iegut_bernus(virsotne, sp, virsotnes_dict)

    if not berni:
        return heuristika(virsotne)

    # Datora gājiens -> MAX
    if virsotne.gajiens == 2:
        labaka_vertiba = float('-inf')
        for berns in berni:
            vertiba = minimax(berns, sp, virsotnes_dict)
            labaka_vertiba = max(labaka_vertiba, vertiba)
        return labaka_vertiba

    # Cilvēka gājiens -> MIN
    else:
        labaka_vertiba = float('inf')
        for berns in berni:
            vertiba = minimax(berns, sp, virsotnes_dict)
            labaka_vertiba = min(labaka_vertiba, vertiba)
        return labaka_vertiba


def izveleties_labako_gajienu(sakuma_virsotne, sp, virsotnes_dict):
    if ir_beigas(sakuma_virsotne):
        return None, None
    
    berni = iegut_bernus(sakuma_virsotne, sp, virsotnes_dict)

    if not berni:
        return None, None

    labakais_gajiens = None
    labaka_vertiba = float('-inf')

    for berns in berni:
        vertiba = minimax(berns, sp, virsotnes_dict)
        print(f"Gājiens uz {berns.skaitlis} -> vērtība {vertiba}")

        if vertiba > labaka_vertiba:
            labaka_vertiba = vertiba
            labakais_gajiens = berns

    return labakais_gajiens, labaka_vertiba


def noteikt_dalitaju(pasreizeja_virsotne, nakama_virsotne):
    if pasreizeja_virsotne.skaitlis % 2 == 0 and pasreizeja_virsotne.skaitlis // 2 == nakama_virsotne.skaitlis:
        return 2
    elif pasreizeja_virsotne.skaitlis % 3 == 0 and pasreizeja_virsotne.skaitlis // 3 == nakama_virsotne.skaitlis:
        return 3
    return None
