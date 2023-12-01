# main.py
import random
import pygame
from pygame.constants import QUIT, K_DOWN, K_LEFT, K_UP, K_RIGHT

#
pygame.init()
# -------------------------------- CONSTANTS -------------------------------- #
FPS = pygame.time.Clock()

# Display sizes
HEIGHT = 800
WIDTH = 1200

# colors
COLOR_WHITE = (255, 255, 255)
COLOR_BLACK = (0, 0, 0)
COLOR_CHARCOAL_GREY = (54, 69, 79)
COLOR_RED = (231, 12, 12)
COLOR_ORANGE = (245, 166, 30)
COLOR_GREEN = (37, 204, 13)
COLOR_VIOLET = (17, 13, 204)

DISPLAY_COLOR = COLOR_CHARCOAL_GREY
# --------------------------------------------------------------------------- #

# create the main display
main_display = pygame.display.set_mode((WIDTH, HEIGHT))
# --------------------------------------------------------------------------- #

# create player
player_size = (20, 20)
player = pygame.Surface(player_size)
player_rect = player.get_rect()
player.fill(COLOR_GREEN)
# --------------------------------------------------------------------------- #

# the direction of movement of the player
player_move_down = [0, 1]
player_move_right = [1, 0]
player_move_up = [0, -1]
player_move_left = [-1, 0]
# --------------------------------------------------------------------------- #

# set active flag
playing = True

while playing:
    for event in pygame.event.get():
        FPS.tick(120)

        if event.type == QUIT:
            playing = False

    # fill display to main color
    main_display.fill(DISPLAY_COLOR)

    keys = pygame.key.get_pressed()

    if keys[K_DOWN] and player_rect.bottom < HEIGHT:
        player_rect = player_rect.move(player_move_down)

    if keys[K_RIGHT] and player_rect.right < WIDTH:
        player_rect = player_rect.move(player_move_right)

    if keys[K_UP] and player_rect.top > 0:
        player_rect = player_rect.move(player_move_up)

    if keys[K_LEFT] and player_rect.left > 0:
        player_rect = player_rect.move(player_move_left)

    # to put the image on the screen
    main_display.blit(player, player_rect)

    # update display
    pygame.display.flip()
