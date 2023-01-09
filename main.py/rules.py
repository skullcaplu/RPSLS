import time

class Rules:
    def __init__(self):
        self.choices = ['rock', 'paper', 'scissors', 'lizard', 'spock']
        self.player2_counter = 0
        self.player1_counter = 0
        self.game_mode = input("would you like to play 'player vs player' or 'player vs cpu'?")
        self.player2_choice = input("Player 2, Would you like to choose rock, paper, scissors, lizard, or spock? ")


        def play_game (self):
        
            self.choices = ['rock', 'paper', 'scissors', 'lizard', 'spock']
            self.player1_counter = 0
            self.player2_counter = 0
            self.valid_response = False
            self.valid_response2 = False
            while self.valid_response == False:
                self.game_mode = input("would you like to play 'player vs player' or 'player vs cpu'? ")
                if self.game_mode == "player vs player":
                    self.valid_response = True
                elif self.game_mode == "player vs cpu":
                    self.valid_response = True
                print("")
            while self.player2_counter < 2 and self.player1_counter < 2:
                if self.game_mode == "player vs player":
                    print("")
                    time.sleep(.8)
                    self.player1_input = input("Player 1, Would you like to choose rock, paper, scissors, lizard, or spock? ")
                    self.player2_choice = input("Player 2, Would you like to choose rock, paper, scissors, lizard, or spock? ")