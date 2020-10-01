import pygame.font


class Button():
    def __init__(self, ai_setting, screen, msg):
        """initialize button attribute"""
        self.screen = screen
        self.screen_rect = screen.get_rect()

        # set the dimension and properties of the button
        self.width, self.height = 150, 30
        self.button_color = (0, 255, 0)
        self.text_color = (255, 255, 255)
        self.font = pygame.font.SysFont(None, 40)

        # build the button's rect object and cetner it
        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.rect.center = self.screen_rect.center

        # the buttton message needs to be prepped only once.
        self.prep_msg(msg)

    def prep_msg(self, msg):
        """turn message into a rendered image and center text on the button."""
        self.msg_image = self.font.render(
            msg, True, self.text_color, self.button_color)
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.center = self.rect.center

    def draw_button(self):
        """draw blank button and then draw a message"""
        self.screen.fill(self.button_color, self.rect)
        self.screen.blit(self.msg_image, self.msg_image_rect)
