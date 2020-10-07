import pygame
import time

"""
Collection of functions for displaying text
"""


class Img_text:
    def __init__(self, screen):
        # draw text
        self.screen = screen

    def get_start(self, images):
        self.images = images
        self.image = pygame.image.load(
            "rock paper scissors game\\images\\" + self.images+".png")
        self.image_rect = self.image.get_rect()
        self.image_rect.center = self.screen.get_rect().center
        self.image_rect.top = 210

        self.screen.blit(self.image, self.image_rect)

    def play_button(self):
        self.position = (self.image_rect.x, self.image_rect.y)
        self.rect = self.image.get_rect(topleft=self.position)
        return self.rect

    def label_click(self):
        self.font = pygame.font.SysFont("Arial", 14)
        self.text_color = (105, 105, 105)
        label = "click your choice"
        self.img_label = self.font.render(label, True, self.text_color)
        self.label_rect = self.img_label.get_rect()
        self.label_rect.center = self.screen.get_rect().center
        self.label_rect.top = 460

        self.screen.blit(self.img_label, self.label_rect)
