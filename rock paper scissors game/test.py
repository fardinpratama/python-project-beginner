import sys
import pygame
from random import choice
from hands import (Player, Enemy)
from button import (Rock, Paper, Scissors)
from game_function import Test
import time
from text import Img_text
from score import Score


# initilize game
pygame.init()

bg = pygame.image.load(r"rock paper scissors game\images\bg.jpg")


screen = pygame.display.set_mode(
    (600, 500))
pygame.display.set_caption("Rock Paper Scissors Game ")
choice_player = 0
choice_enemy = 0
game_active = 0
text_play = "start"

score = Score(screen)
player = Player(screen)
enemy = Enemy(screen)
img_text = Img_text(screen)
b_rock = Rock(screen)
b_paper = Paper(screen)
b_scissors = Scissors(screen)
# start the main loop for the game
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                game_active = 1
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            if not game_active:
                if img_text.play_button().collidepoint(mouse_x, mouse_y):
                    game_active = 1
            else:
                if b_rock.rect.collidepoint(mouse_x, mouse_y):
                    choice_player = 1
                elif b_paper.rect.collidepoint(mouse_x, mouse_y):
                    choice_player = 2
                elif b_scissors.rect.collidepoint(mouse_x, mouse_y):
                    choice_player = 3

    screen.blit(bg, [0, 0])

    # start to test
    if game_active:
        if not choice_player:
            choice_enemy = choice([1, 2, 3])
            time.sleep(.05)
        else:
            choice_enemy = choice_enemy
            test = Test(screen, choice_player, choice_enemy)
            text_play = test.get_result()
            score.get_score(text_play)
            img_text.get_start(text_play, 1)

        player.draw_player(choice_player)
        enemy.draw_enemy(choice_enemy)
    else:
        player.draw_player(choice_player)
        enemy.draw_enemy(choice_enemy)
        img_text.get_start(text_play)

    # draw button
    b_rock.draw_rock()
    b_paper.draw_paper()
    b_scissors.draw_scissors()

    score.draw_score()
    pygame.display.flip()

    if text_play != "start" and text_play != "again":
        time.sleep(1.5)
        text_play = "again"
        game_active = 0
        choice_player = 0
