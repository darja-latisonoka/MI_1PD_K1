from models.AI import AI
import logic.utilities as util

NUMBERCOUNT = 5

class GameState:
    random_numbers_list: list[int] = []
    selected_number: int = 0
    current_number: int = 0

    player_score: int = 0
    ai_score: int = 0
    bank_score: int = 0

    algorithm: str = "alfa-beta" # vai nu "alfa-beta", vai "minimax"
    turn: str = "cilvēks" # "cilvēks" vai "ai"
    game_has_ended: bool = False

    ai = None

    def start_new_round(self):
        self.random_numbers_list = util.generateRandomNumbers(NUMBERCOUNT)
        self.selected_number = 0
        self.current_number = 0
        self.player_score = 0
        self.ai_score = 0
        self.game_has_ended = False
        self.ai = AI(self)
    
    def divideByNumber(self, number):
        self.current_number = int(self.current_number / number)

        if self.current_number % 2 != 0 and self.current_number % 3 != 0:
            self.game_has_ended = True

        # punktu pieskaitīšana (vai atņemšana)
        if self.current_number % 2 == 0:
            self.player_score += 1
        else:
            self.player_score -= 1
        if self.current_number % 5 == 0:
            self.bank_score += 1
        self.switch_turn()

        # bankas punktu pārlikšana, spēles beigās
        if self.game_has_ended:
            if self.turn == "player":
                self.player_score += self.bank_score
            else:
                self.ai_score += self.bank_score

    def runTheAI(self):
       self.ai.runTheAI()

    def select_number(self, number):
        self.selected_number = number

    def choose_number(self, number):
        self.current_number = number
    
    def switch_algorithm(self):
        self.algorithm = "minimax" if self.algorithm == "alfa-beta" else "alfa-beta"
    
    def switch_turn(self):
        self.turn = "ai" if self.turn == "cilvēks" else "cilvēks"
