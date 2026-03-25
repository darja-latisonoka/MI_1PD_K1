from models.node import Virsotne
from models.game_tree import Speles_koks

import logic.tree_builder as tbuilder
from logic.minimax import izveleties_labako_gajienu as minimax_move, noteikt_dalitaju
from logic.alpha_beta import izveleties_labako_gajienu as alphabeta_move
from logic.heuristic import nav_gajienu
from logic.Metrics import make_ai_move_with_metrics

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
        self.tree, self.node_dict = tbuilder.rebuild_tree_from_current_node(self.current_node)

        if self.game.algorithm == "alfa-beta":
            move, value = make_ai_move_with_metrics(
                alphabeta_move, 
                self.current_node, 
                self.tree, 
                self.node_dict
            )
        else:
            move, value = make_ai_move_with_metrics(
                minimax_move, 
                self.current_node, 
                self.tree, 
                self.node_dict
            )
        
        self.alterGameState(move)

    def alterGameState(self, move):
        self.game.current_number = move.skaitlis
        self.game.player_score = move.p1
        self.game.ai_score = move.p2
        self.game.bank_score = move.banka
        self.game.switch_turn()
