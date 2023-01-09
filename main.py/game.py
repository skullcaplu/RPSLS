import random
from ai import AI
from human import Human
from player import Player
from rules import Rules

rules = Rules
human = Human
cpu = AI("Bowser")

class Game(Rules):
    def __init__ (self):
        super(). __init__()
        self.player1 = Human("Mario")
        self.player2 = Human("Luigi")
        self.player3 = AI("Bowser")
        self.choices = ['rock', 'paper', 'scissors', 'lizard', 'spock']

    def play_game(self):
        super().play_game(self)
       