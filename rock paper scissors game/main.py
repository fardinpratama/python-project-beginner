import sys
import pygame
from random import choice
import time

# import my class
from hands import (Player, Enemy)
from button import (Rock, Paper, Scissors)
from game_function import Test
from text import Img_text
from score import Score


# initilize game
pygame.init()

# create bacgkround
bg = pygame.image.load(r"rock paper scissors game\images\bg.jpg")


screen = pygame.display.set_mode(
    (600, 500))
pygame.display.set_caption("Rock Paper Scissors Game ")


choice_player = 2
choice_enemy = 1
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
        # key to start
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                game_active = 1
                choice_player = 0

        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            # key to start
            if not game_active:
                if img_text.play_button().collidepoint(mouse_x, mouse_y):
                    game_active = 1
                    choice_player = 0
            else:
                # if button on click
                if b_rock.rect.collidepoint(mouse_x, mouse_y):
                    choice_player = 1
                elif b_paper.rect.collidepoint(mouse_x, mouse_y):
                    choice_player = 2
                elif b_scissors.rect.collidepoint(mouse_x, mouse_y):
                    choice_player = 3

    # start to test
    if game_active:
        if not choice_player:
            #randomly draw enemy hands
            enemy_hand = choice([1, 2, 3])
            choice_enemy = enemy_hand
            time.sleep(.05)
        else:
            #makes the enemy unselect based on the previous image
            choice_enemy = choice([1, 2, 3])
            test = Test(screen, choice_player, choice_enemy)
            text_play = test.get_result()
            score.get_score(text_play)
            img_text.get_start(text_play)

        player.draw_player(choice_player)
        enemy.draw_enemy(choice_enemy)
    else:
        # draw hands default
        player.draw_player(choice_player)
        enemy.draw_enemy(choice_enemy)
        img_text.get_start(text_play)

    # draw button
    b_rock.draw_rock()
    b_paper.draw_paper()
    b_scissors.draw_scissors()

    # draw label and score
    img_text.label_click()
    score.draw_score()
    pygame.display.flip()

    # reset image
    if text_play != "start" and text_play != "again":
        time.sleep(1.5)
        text_play = "again"
        game_active = 0
        choice_player = 0

    screen.blit(bg, [0, 0])
