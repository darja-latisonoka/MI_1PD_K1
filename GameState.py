# visam gan jau vajag validāciju

class GameState:
    random_numbers_choice: list[int] = []
    current_number: int = 0

    player_score: int = 0
    ai_score: int = 0
    bank_score: int = 0

    algorithm: str = "alfa-beta" # vai nu "alfa-beta", vai "minmax"
    turn: str = "player" # "player" vai "ai"

    def new_round(self):
        self.random_numbers_choice = [1000001, 1000002, 1000003, 1000004, 1000005] # vajadzīga funkcija
        self.current_number = 0
        self.player_score = 0
        self.ai_score = 0
    
    def choose_number(self, number):
        self.current_number = number
    
    def change_algorithm(self):
        if self.algorithm == "alfa-beta":
            self.algorithm = "minmax"
        else:
            self.algorithm = "alfa-beta"
    
    def change_starting_turn(self):
        if self.turn == "player":
            self.turn = "ai"
        else:
            self.turn = "player"