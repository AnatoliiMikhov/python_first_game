# main.py
import random
import pygame
from pygame.constants import QUIT, K_DOWN, K_LEFT, K_UP, K_RIGHT

#
pygame.init()
# -------------------------------- CONSTANTS -------------------------------- #
# FPS = pygame.time.Clock()

# Display sizes
HEIGHT = 800
WIDTH = 1200

# colors
COLOR_WHITE = (255, 255, 255)
COLOR_BLACK = (0, 0, 0)
COLOR_RED = (231, 12, 12)
COLOR_ORANGE = (245, 166, 30)
COLOR_GREEN = (37, 204, 13)
COLOR_VIOLET = (17, 13, 204)
COLOR_CHARCOAL_GREY = (54, 69, 79)

COLOR_OF_DISPLAY = COLOR_CHARCOAL_GREY
COLOR_OF_PLAYER = COLOR_GREEN
COLOR_OF_ENEMY = COLOR_RED
COLOR_OF_BONUS = COLOR_ORANGE
# --------------------------------------------------------------------------- #

# create the main display
main_display = pygame.display.set_mode((WIDTH, HEIGHT))
# --------------------------------------------------------------------------- #

# ---------------------------- Create characters ---------------------------- #
# create a player
player_size = (20, 20)
player = pygame.Surface(player_size)
player_rect = player.get_rect()
player.fill(COLOR_GREEN)

# the direction of movement of the player
player_move_down = [0, 1]
player_move_right = [1, 0]
player_move_up = [0, -1]
player_move_left = [-1, 0]


# create an enemy
def create_enemy():
    enemy_size = (20, 20)
    enemy = pygame.Surface(enemy_size)
    enemy.fill(COLOR_OF_ENEMY)
    enemy_rect = pygame.Rect(WIDTH, random.randint(0, HEIGHT), *enemy_size)
    enemy_move = [random.randint(-6, -1), 0]
    return [enemy, enemy_rect, enemy_move]


# create a bonus
def create_bonus():
    bonus_size = (20, 20)
    bonus = pygame.Surface(bonus_size)
    bonus.fill(COLOR_OF_BONUS)
    bonus_rect = pygame.Rect(random.randint(0, WIDTH), 0, *bonus_size)
    bonus_move = [0, random.randint(1, 6)]
    return [bonus, bonus_rect, bonus_move]


# Creating User Events
CREATE_ENEMY = pygame.USEREVENT + 1
pygame.time.set_timer(CREATE_ENEMY, 1500)

CREATE_BONUS = pygame.USEREVENT + 2
pygame.time.set_timer(CREATE_BONUS, 1500)

# Creating lists
enemies = []
bonuses = []
# -------------------------- END Create Characters -------------------------- #

# set active flag
playing = True

while playing:
    for event in pygame.event.get():
        # FPS.tick(120)

        if event.type == QUIT:
            playing = False

        if event.type == CREATE_ENEMY:
            enemies.append(create_enemy())

        if event.type == CREATE_BONUS:
            bonuses.append(create_bonus())

    # fill display to main color
    main_display.fill(COLOR_OF_DISPLAY)

    keys = pygame.key.get_pressed()

    # movement of player when pressing keys
    if keys[K_DOWN] and player_rect.bottom < HEIGHT:
        player_rect = player_rect.move(player_move_down)

    if keys[K_RIGHT] and player_rect.right < WIDTH:
        player_rect = player_rect.move(player_move_right)

    if keys[K_UP] and player_rect.top > 0:
        player_rect = player_rect.move(player_move_up)

    if keys[K_LEFT] and player_rect.left > 0:
        player_rect = player_rect.move(player_move_left)

    # to move enemies
    for enemy in enemies:
        enemy[1] = enemy[1].move(enemy[2])
        main_display.blit(enemy[0], enemy[1])

    # to move bonuses
    for bonus in bonuses:
        bonus[1] = bonus[1].move(bonus[2])
        main_display.blit(bonus[0], bonus[1])

    # to put the player on the screen
    main_display.blit(player, player_rect)

    # update display
    pygame.display.flip()

    # --------------------------------- Removing -------------------------------- #
    # removing enemies
    for enemy in enemies:
        if enemy[1].left < 0:
            enemies.pop(enemies.index(enemy))

    # removing bonuses
    for bonus in bonuses:
        if bonus[1].bottom >= HEIGHT:
            bonuses.pop(bonuses.index(bonus))
