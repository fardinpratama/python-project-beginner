import pygame

"""
This class serves to draw the player's and enemy's hand
"""

# hands as player


class Player():
    def __init__(self, screen):
        self.screen = screen
        self.position = (247, 258)

    def draw_player(self, images):
        # load image
        self.image = pygame.image.load(
            r"rock paper scissors game\images\hand"+str(images)+".png")
        # draw hands in screen
        self.screen.blit(self.image, self.position)

# hands as Enemy


class Enemy():
    def __init__(self, screen):
        self.screen = screen
        self.position = (247, 99)

    def draw_enemy(self, num_img):
        # load image
        self.image = pygame.image.load(
            r"rock paper scissors game\images\hand"+str(num_img)+".png")
        self.image = pygame.transform.rotate(self.image, 180)
        # draw hands in screen
        self.screen.blit(self.image, self.position)
