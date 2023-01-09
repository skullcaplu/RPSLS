

class Rules:
    def __init__(self):
        self.choices = ['rock', 'paper', 'scissors', 'lizard', 'spock']
        self.player2_counter = 0
        self.player1_counter = 0
        self.game_mode = input("would you like to play 'player vs player' or 'player vs cpu'?")
        self.player2_choice = input("Player 2, Would you like to choose rock, paper, scissors, lizard, or spock? ")