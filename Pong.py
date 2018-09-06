import pygame

class Pong:
    def __init__(self):
        # True = Player 1
        # False = Player 2
        self.winner = True
        
    def play(self, player):
        print("PLAYER", player, "CHALLENGES")
        return self.winner