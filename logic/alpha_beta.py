from logic.minimax import iegut_bernus
from logic.heuristic import heuristika, ir_beigas
from logic import Metrics

def alphabeta(virsotne, sp, virsotnes_dict, alpha, beta):
Metrics.evaluated_nodes += 1

    if ir_beigas(virsotne):
        return heuristika(virsotne)

    berni = iegut_bernus(virsotne, sp, virsotnes_dict)

    if not berni:
        return heuristika(virsotne)

    # Dators (MAX)
    if virsotne.gajiens == 2:

        vertiba = float('-inf')

        for berns in berni:
            vertiba = max(
                vertiba,
                alphabeta(berns, sp, virsotnes_dict, alpha, beta)
            )

            alpha = max(alpha, vertiba)

            if beta <= alpha:
                break

        return vertiba

    # Cilvēks (MIN)
    else:

        vertiba = float('inf')

        for berns in berni:
            vertiba = min(
                vertiba,
                alphabeta(berns, sp, virsotnes_dict, alpha, beta)
            )

            beta = min(beta, vertiba)

            if beta <= alpha:
                break

        return vertiba


def izveleties_labako_gajienu(sakuma_virsotne, sp, virsotnes_dict):

    berni = iegut_bernus(sakuma_virsotne, sp, virsotnes_dict)

    if not berni:
        return None, None

    labakais_gajiens = None
    labaka_vertiba = float('-inf')

    for berns in berni:

        vertiba = alphabeta(
            berns,
            sp,
            virsotnes_dict,
            float('-inf'),
            float('inf')
        )

        print(f"Gājiens uz {berns.skaitlis} -> vērtība {vertiba}")

        if vertiba > labaka_vertiba:
            labaka_vertiba = vertiba
            labakais_gajiens = berns

    return labakais_gajiens, labaka_vertiba
