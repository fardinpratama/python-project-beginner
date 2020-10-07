import pygame
import time

"""
This class contains functions for obtaining the results 
by converting suit shapes into numbers during the analysis process :
    rock = 1
    paper = 2
    scissors = 3
"""
class Test:
    def __init__(self, screen, player, enemy):
        self.screen = screen
        self.player = player
        self.enemy = enemy
        # self.position = (244, 190)

    def get_result(self):
        self.check = self.player - self.enemy
        if self.check == 1 or self.check == -2:
            self.result = "win"
        elif self.check == 0:
            self.result = "draw"
        else:
            self.result = "lose"

        return self.result