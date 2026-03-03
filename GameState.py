# visam gan jau vajag validāciju

class GameState:
    random_numbers_list: list[int] = []
    selected_number: int = 0
    current_number: int = 0

    player_score: int = 0
    ai_score: int = 0
    bank_score: int = 0

    algorithm: str = "alfa-beta" # vai nu "alfa-beta", vai "minmax"
    turn: str = "player" # "player" vai "ai"

    def start_new_round(self):
        self.random_numbers_list = [1000001, 1000002, 1000003, 1000004, 1000005] # vajadzīga funkcija
        self.selected_number = 0
        self.current_number = 0
        self.player_score = 0
        self.ai_score = 0
    
    def select_number(self, number):
        self.selected_number = number

    def choose_number(self, number):
        self.current_number = number
    
    def switch_algorithm(self):
        self.algorithm = "minmax" if self.algorithm == "alfa-beta" else "alfa-beta"
    
    def switch_turn(self):
        self.turn = "ai" if self.turn == "player" else "player"