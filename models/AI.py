from models.node import Virsotne
from models.game_tree import Speles_koks

from logic.tree_builder import uzgeneret_koku_no_virsotnes
from logic.minimax import izveleties_labako_gajienu as minimax_move, noteikt_dalitaju
from logic.alpha_beta import izveleties_labako_gajienu as alphabeta_move
from logic.heuristic import nav_gajienu

class AI:
    def __init__(self, gameState):
        self.game = gameState
        self.tree = Speles_koks()
        self.node_dict = dict()
    def runTheAI(self):

        self.current_node = Virsotne(
            "A1",
            skaitlis=self.game.current_number,
            p1=self.game.player_score,
            p2=self.game.ai_score,
            banka=self.game.bank_score,
            limenis=1,
            gajiens=self.game.turn
        )
        self.tree, self.node_dict = self.rebuild_tree_from_current_node(self.current_node)

        if self.game.algorithm == "alfa-beta":
            move, value = alphabeta_move(self.current_node, self.tree, self.node_dict)
        else:
            move, value = minimax_move(self.current_node, self.tree, self.node_dict)
        
        print(move, "separator", value)

        self.game.switch_turn()

    def rebuild_tree_from_current_node(self, current_node):
        sp = Speles_koks()

        uzgeneret_koku_no_virsotnes(sp, current_node)
        virsotnes_dict = {v.id: v for v in sp.virsotnu_kopa}

        return sp, virsotnes_dict