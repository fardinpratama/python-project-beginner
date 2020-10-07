import pygame
import pygame.font

"""
class to display the score
"""

class Score:
    def __init__(self, screen):
        self.screen = screen
        self.screen_rect = screen.get_rect()
        #set the start of the score
        self.win = 0
        self.draw = 0
        self.loss = 0
        self.font = pygame.font.SysFont("Arial", 14)

    def get_score(self, result):
        if result == "win":
            self.win += 1
        elif result == "draw":
            self.draw += 1
        elif result == "lose":
            self.loss += 1

    def draw_score(self):
        list_score = [self.win, self.draw, self.loss]
        color_label = [(126, 223, 210), (159, 197, 77), (214, 108, 81)]
        label_score = ["Win", "Draw", "Loss"]
        list_position = [-50, 0, 50]

        for i in range(3):
            label = "{}: {}".format(label_score[i], list_score[i])
            self.text_color = color_label[i]
            self.img_score = self.font.render(label, True, self.text_color)
            # self.score_win = self.font.render(label_win, True, self.text_color)
            self.image_rect = self.img_score.get_rect()
            self.image_rect.center = (
                self.screen_rect.center[0] + list_position[i], self.screen_rect.center[1])
            self.image_rect.top = 375
            self.screen.blit(self.img_score, self.image_rect)
