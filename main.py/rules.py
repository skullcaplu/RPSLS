import time
import random

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
                elif self.game_mode == "player vs cpu":
                    print("")
                    time.sleep(.8)
                    self.player1_input = input("Player 1, Would you like to choose rock, paper, scissors, lizard, or spock? ")
                    self.player2_choice = random.choice(self.choices)
                        
                if self.player2_choice == "rock" and self.player1_input == "scissors":
                    self.player2_counter += 1
                    print(f"player2: ", self.player2_counter)
                    print(f"player1: ", self.player1_counter)
                    print("Rock crushes Scissors")

                elif self.player2_choice == "scissors" and self.player1_input == "paper":
                    self.player2_counter += 1
                    print(f"player2: ", self.player2_counter)
                    print(f"player1: ", self.player1_counter)
                    print("Scissors cuts Paper")

                elif self.player2_choice == "paper" and self.player1_input == "rock":
                    self.player2_counter += 1
                    print(f"player2: ", self.player2_counter)
                    print(f"player1: ", self.player1_counter)
                    print("Paper covers Rock")

                elif self.player2_choice == "rock" and self.player1_input == "lizard":
                    self.player2_counter += 1
                    print(f"player2: ", self.player2_counter)
                    print(f"player1: ", self.player1_counter)
                    print("Rock crushes Lizard")

                elif self.player2_choice == "lizard" and self.player1_input == "spock":
                    self.player2_counter += 1
                    print(f"player2: ", self.player2_counter)
                    print(f"player1: ", self.player1_counter)
                    print("Lizard poisons Spock")

                elif self.player2_choice == "spock" and self.player1_input == "scissors":
                    self.player2_counter += 1
                    print(f"player2: ", self.player2_counter)
                    print(f"player1: ", self.player1_counter)
                    print("Spock smashes Scissors")

                elif self.player2_choice == "scissors" and self.player1_input == "lizard":
                    self.player2_counter += 1
                    print(f"player2: ", self.player2_counter)
                    print(f"player1: ", self.player1_counter)
                    print("Scissors decapitates Lizard")

                elif self.player2_choice == "lizard" and self.player1_input == "paper":
                    self.player2_counter += 1
                    print(f"player2: ", self.player2_counter)
                    print(f"player1: ", self.player1_counter)
                    print("Lizard eats Paper")

                elif self.player2_choice == "paper" and self.player1_input == "spock":
                    self.player2_counter += 1
                    print(f"player2: ", self.player2_counter)
                    print(f"player1: ", self.player1_counter)
                    print("Paper disproves Spock")

                elif self.player2_choice == "spock" and self.player1_input == "rock":
                    self.player2_counter += 1
                    print(f"player2: ", self.player2_counter)
                    print(f"player1: ", self.player1_counter)
                    print("Spock vaporizes Rock")



                elif self.player1_input == "rock" and self.player2_choice == "scissors":
                    self.player1_counter += 1
                    print(f"player2: ", self.player2_counter)
                    print(f"player1: ", self.player1_counter)
                    print("Rock crushes Scissors")

                elif self.player1_input == "scissors" and self.player2_choice == "paper":
                    self.player1_counter += 1
                    print(f"player2: ", self.player2_counter)
                    print(f"player1: ", self.player1_counter)
                    print("Scissors cuts Paper")

                elif self.player1_input== "paper" and self.player2_choice == "rock":
                    self.player1_counter += 1
                    print(f"player2: ", self.player2_counter)
                    print(f"player1: ", self.player1_counter)
                    print("Paper covers Rock")

                elif self.player1_input == "rock" and self.player2_choice == "lizard":
                    self.player1_counter += 1
                    print(f"player2: ", self.player2_counter)
                    print(f"player1: ", self.player1_counter)
                    print("Rock crushes Lizard")

                elif self.player1_input == "lizard" and self.player2_choice == "spock":
                    self.player1_counter += 1
                    print(f"player2: ", self.player2_counter)
                    print(f"player1: ", self.player1_counter)
                    print("Lizard poisons Spock")

                elif self.player1_input == "spock" and self.player2_choice == "scissors":
                    self.player1_counter += 1
                    print(f"player2: ", self.player2_counter)
                    print(f"player1: ", self.player1_counter)
                    print("Spock smashes Scissors")

                elif self.player1_input == "scissors" and self.player2_choice == "lizard":
                    self.player1_counter += 1
                    print(f"player2: ", self.player2_counter)
                    print(f"player1: ", self.player1_counter)
                    print("Scissors decapitates Lizard")

                elif self.player1_input == "lizard" and self.player2_choice == "paper":
                    self.player1_counter += 1
                    print(f"player2: ", self.player2_counter)
                    print(f"player1: ", self.player1_counter)
                    print("Lizard eats Paper")

                elif self.player1_input == "paper" and self.player2_choice == "spock":
                    self.player1_counter += 1
                    print(f"player2: ", self.player2_counter)
                    print(f"player1: ", self.player1_counter)
                    print("Paper disproves Spock")

                elif self.player1_input == "spock" and self.player2_choice == "rock":
                    self.player1_counter += 1
                    print(f"player2: ", self.player2_counter)
                    print(f"player1: ", self.player1_counter)
                    print("Spock vaporizes Rock")

                elif self.player1_input == self.player2_choice:
                    print("tie round")
                    print(f"player2: ", self.player2_counter)
                    print(f"player1: ", self.player1_counter)

                else:
                    print("invalid response(s) given, redo round.")
                    print(f"player2: ", self.player2_counter)
                    print(f"player1: ", self.player1_counter)

            while self.valid_response2 == False:
                if self.player1_counter == 2:
                    time.sleep(.8)
                    print("player 1 won")
                    time.sleep(.8)
                    self.closing_message = input("do you want to play again, y/n ")
                    if self.closing_message == "y":
                        self.play_game(self)
                        self.valid_response2 = True
                        
                    elif self.closing_message == "n":
                        print("game complete")
                        self.valid_response2 = True

                elif self.player2_counter == 2:
                    time.sleep(.8)
                    print("player 2 won")
                    time.sleep(.8)
                    self.closing_message = input("do you want to play again, y/n ")
                    time.sleep(.8)
                    if self.closing_message == "y":
                        self.play_game(self)
                        self.valid_response2 = True
                    elif self.closing_message == "n":
                        print("game complete")
                        self.valid_response2 = True
