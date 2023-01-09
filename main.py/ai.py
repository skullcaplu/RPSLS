from player import Player
import random

class AI(Player):
    def __init__ (self, name):
        super(). __init__(name)
        self.name = "Bowser"
        self.choices = ['rock', 'paper', 'scissors', 'lizard', 'spock']
        self.choice = random.choice(self.choices)