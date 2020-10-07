import pygame

"""
This class serves to draw the hand selection button for the player
"""


class Rock:
    def __init__(self, screen):
        self.screen = screen
        self.position = (187, 392)
        # load image
        self.image = pygame.image.load(
            r"rock paper scissors game\images\b1.png")
        self.rect = self.image.get_rect(topleft=self.position)

    def draw_rock(self):
        # draw hands in screen
        self.screen.blit(self.image, self.position)


class Paper:
    def __init__(self, screen):
        self.screen = screen
        self.position = (267, 392)
        # load image
        self.image = pygame.image.load(
            r"rock paper scissors game\images\b2.png")
        self.rect = self.image.get_rect(topleft=self.position)

    def draw_paper(self):
        # draw hands in screen
        self.screen.blit(self.image, self.position)


class Scissors:
    def __init__(self, screen):
        self.screen = screen
        self.position = (347, 392)
        # load image
        self.image = pygame.image.load(
            r"rock paper scissors game\images\b3.png")
        self.rect = self.image.get_rect(topleft=self.position)

    def draw_scissors(self):
        # draw hands in screen
        self.screen.blit(self.image, self.position)
