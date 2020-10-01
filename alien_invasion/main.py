import pygame
from pygame.sprite import Group

from setting import Setting
from ship import Ship
import game_functions as gf
from game_stat import GameStats
from button import Button
from scoreboard import Scoreboard


def run_game():
    # initialize game and create a screen object
    pygame.init()
    ai_setting = Setting()
    screen = pygame.display.set_mode(
        (ai_setting.screen_width, ai_setting.screen_height))
    pygame.display.set_caption("Alien Invasion")

    # make the play button.
    play_button = Button(ai_setting, screen, "Play")

    # create an instance to store game statictics and create a scoreboard
    stats = GameStats(ai_setting)
    sb = Scoreboard(ai_setting, screen, stats)
    # make a ship
    ship = Ship(ai_setting, screen)

    # make a group to store bullets and alien in.
    bullets = Group()
    aliens = Group()

    # create the fleet of aliens
    gf.create_fleet(ai_setting, screen, ship, aliens)

    # start the main loop for the game
    while True:

        # watch for keyboard and mouse events.
        gf.check_events(ai_setting, screen, stats, sb,
                        play_button, ship, aliens, bullets)
        if stats.game_active:
            ship.update()
            gf.update_bullets(ai_setting, screen, stats,
                              sb, ship, aliens, bullets)
            gf.update_aliens(ai_setting, screen, stats,
                             sb, ship, aliens, bullets)
        gf.update_screen(ai_setting, screen, stats, sb, ship,
                         aliens, bullets, play_button)


run_game()
