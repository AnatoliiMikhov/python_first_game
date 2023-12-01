# main.py
import pygame
from pygame.constants import QUIT

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

# pygame set mode
main_display = pygame.display.set_mode((WIDTH, HEIGHT))

# create player
player_size = (20, 20)

player = pygame.Surface(player_size)
player.fill(COLOR_WHITE)

player_rect = player.get_rect()
player_speed = [1, 1]
# --------------------------------------------------------------------------- #

# set active flag
playing = True

while playing:
    for event in pygame.event.get():
        FPS.tick(120)

        if event.type == QUIT:
            playing = False

    if player_rect.bottom >= HEIGHT:
        player_speed[1] = -player_speed[1]
        player.fill(COLOR_RED)

    if player_rect.right >= WIDTH:
        player_speed[0] = -player_speed[0]
        player.fill(COLOR_ORANGE)

    if player_rect.top < 0:
        player_speed[1] = -player_speed[1]
        player.fill(COLOR_GREEN)

    if player_rect.left < 0:
        player_speed[0] = -player_speed[0]
        player.fill(COLOR_VIOLET)

    # fill display to main color
    main_display.fill(DISPLAY_COLOR)

    # to put the image on the screen
    main_display.blit(player, player_rect)

    # the player starts
    player_rect = player_rect.move(player_speed)

    # update display
    pygame.display.flip()
