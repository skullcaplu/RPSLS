from player import Player

class Human(Player):
    def __init__(self,name):
        super(). __init__(name)
        self.name = name
        self.choice = input(f"{self.name}, Would you like to choose rock, paper, scissors, lizard, or spock? ")