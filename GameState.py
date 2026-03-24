import math
import random

from models.AI import AI

NUMBERCOUNT = 5

class GameState:
    random_numbers_list: list[int] = []
    selected_number: int = 0
    current_number: int = 0

    player_score: int = 0
    ai_score: int = 0
    bank_score: int = 0

    algorithm: str = "alfa-beta" # vai nu "alfa-beta", vai "minmax"
    turn: str = "player" # "player" vai "ai"
    gameHasEnded: bool = False

    def start_new_round(self):
        self.random_numbers_list = self.generateRandomNumbers()
        self.selected_number = 0
        self.current_number = 0
        self.player_score = 0
        self.ai_score = 0
        self.gameHasEnded = False
    
    def divideByNumber(self, number):
        self.current_number = int(self.current_number / number)

        if self.current_number % 2 != 0 and self.current_number % 3 != 0:
            self.gameHasEnded = True

        # punktu pieskaitīšana (vai atņemšana)
        if self.current_number % 2 == 0:
            self.player_score += 1
        else:
            self.player_score -= 1
        if self.current_number % 5 == 0:
            self.bank_score += 1
        self.switch_turn()

        # bankas punktu pārlikšana, spēles beigās
        if self.gameHasEnded:
            if self.turn == "player":
                self.player_score += self.bank_score
            else:
                self.ai_score += self.bank_score

    def runTheAI(self):
       AI.runTheAI(self, self)

    def select_number(self, number):
        self.selected_number = number

    def choose_number(self, number):
        self.current_number = number
    
    def switch_algorithm(self):
        self.algorithm = "minmax" if self.algorithm == "alfa-beta" else "alfa-beta"
    
    def switch_turn(self):
        self.turn = "ai" if self.turn == "player" else "player"

    def generateRandomNumbers(self):
        skaitli = []
        intervals = [1000000, 5000000]
        lowerLimit = math.ceil(intervals[0]/216) # 1 000 000 / 216 = 4630
        upperLimit = math.floor(intervals[1]/216) # 5 000 000 / 216 = 23148
        while len(skaitli) < NUMBERCOUNT:
            x = random.randint(lowerLimit, upperLimit)
            skaitli.append(216 * x)
        return sorted(skaitli)