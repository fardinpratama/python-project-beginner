import pygame

from pygame.sprite import Sprite

class Bullet(Sprite):
    """a class to manage bullets fired from ship"""
    
    def __init__(self, ai_setting, screen, ship):
        """create a bulet object at the ship's current position"""
        super().__init__()
        self.screen = screen

        #create a bullet rect at (0, 0) and then set correct position
        self.rect = pygame.Rect(0, 0, ai_setting.bullet_width, ai_setting.bullet_height)
        self.rect.centerx = ship.rect.centerx
        self.rect.top = ship.rect.top

        #store the bullet's position as a decimal value
        self.y = float(self.rect.y)

        self.color = ai_setting.bullet_color
        self.speed_factor = ai_setting.ship_speed_factor

    def update(self):
        """move the bullet up the screen"""
        #update the decimal position of the bullet
        self.y -= self.speed_factor

        #update rect position
        self.rect.y = self.y

    def draw_bullet(self):
        """draw the bullet to the screen"""
        pygame.draw.rect(self.screen, self.color, self.rect)