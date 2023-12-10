# main.py
import random
import os
import pygame

from pygame.constants import QUIT, K_DOWN, K_LEFT, K_UP, K_RIGHT, K_a, K_w, K_s, K_d

#
pygame.init()
# -------------------------------- CONSTANTS -------------------------------- #
FPS = pygame.time.Clock()

# Display sizes
HEIGHT = 800
WIDTH = 1200

# font
FONT = pygame.font.SysFont("Verdana", 24)

# colors
COLOR_WHITE = (255, 255, 255)
COLOR_BLACK = (0, 0, 0)
COLOR_RED = (231, 12, 12)
COLOR_ORANGE = (245, 166, 30)
COLOR_GREEN = (37, 204, 13)
COLOR_VIOLET = (17, 13, 204)
COLOR_CHARCOAL_GREY = (54, 69, 79)

COLOR_OF_DISPLAY = COLOR_CHARCOAL_GREY
COLOR_OF_PLAYER = COLOR_BLACK
COLOR_OF_ENEMY = COLOR_RED
COLOR_OF_BONUS = COLOR_GREEN
COLOR_OF_SCORE = COLOR_BLACK

# images
IMAGE_PATH = "img/goose"
PLAYER_IMAGES = os.listdir(IMAGE_PATH)
# ------------------------------ END CONSTANTS ------------------------------ #

# create the main display
main_display = pygame.display.set_mode((WIDTH, HEIGHT))
# --------------------------------------------------------------------------- #

# set background image
bg = pygame.transform.scale(pygame.image.load("img/background.png"), (WIDTH, HEIGHT))
bg_X1 = 0
bg_X2 = bg.get_width()
bg_move = 3

# ---------------------------- Create characters ---------------------------- #
# create a player
player = pygame.image.load("img/player.png").convert_alpha()
player_size = player.get_size()
player_rect = pygame.Rect(0, HEIGHT / 2, *player_size)

# the direction of movement of the player
player_move_down = [0, 4]
player_move_right = [4, 0]
player_move_up = [0, -4]
player_move_left = [-4, 0]


# create an enemy
def create_enemy():
    enemy = pygame.image.load("img/enemy.png").convert_alpha()
    enemy_size = enemy.get_size()
    enemy_rect = pygame.Rect(WIDTH, random.randint(60, HEIGHT - 60), *enemy_size)
    enemy_move = [random.randint(-8, -4), 0]
    return [enemy, enemy_rect, enemy_move]


# create a bonus
def create_bonus():
    bonus = pygame.image.load("img/bonus.png").convert_alpha()
    bonus_size = bonus.get_size()
    bonus_rect = pygame.Rect(random.randint(60, WIDTH - 60), 0, *bonus_size)
    bonus_move = [0, random.randint(4, 8)]
    return [bonus, bonus_rect, bonus_move]


# Creating User Events
CREATE_ENEMY = pygame.USEREVENT + 1
pygame.time.set_timer(CREATE_ENEMY, 1500)

CREATE_BONUS = pygame.USEREVENT + 2
pygame.time.set_timer(CREATE_BONUS, 1500)

CHANGE_IMAGE = pygame.USEREVENT + 3
pygame.time.set_timer(CHANGE_IMAGE, 200)

# Creating lists
enemies = []
bonuses = []
# -------------------------- END Create Characters -------------------------- #

score = 0
image_index = 0
# set active flag
playing = True

while playing:
    for event in pygame.event.get():
        FPS.tick(120)

        if event.type == QUIT:
            playing = False

        if event.type == CREATE_ENEMY:
            enemies.append(create_enemy())

        if event.type == CREATE_BONUS:
            bonuses.append(create_bonus())

        if event.type == CHANGE_IMAGE:
            player = pygame.image.load(
                os.path.join(IMAGE_PATH, PLAYER_IMAGES[image_index])
            )
            image_index += 1
            if image_index >= len(PLAYER_IMAGES):
                image_index = 0

    # background settings
    bg_X1 -= bg_move
    bg_X2 -= bg_move

    if bg_X1 < -bg.get_width():
        bg_X1 = bg.get_width()

    if bg_X2 < -bg.get_width():
        bg_X2 = bg.get_width()

    main_display.blit(bg, (bg_X1, 0))
    main_display.blit(bg, (bg_X2, 0))

    # movement of player when pressing keys
    keys = pygame.key.get_pressed()

    if (keys[K_DOWN] or keys[K_s]) and player_rect.bottom < HEIGHT:
        player_rect = player_rect.move(player_move_down)

    if (keys[K_RIGHT] or keys[K_d]) and player_rect.right < WIDTH:
        player_rect = player_rect.move(player_move_right)

    if (keys[K_UP] or keys[K_w]) and player_rect.top > 0:
        player_rect = player_rect.move(player_move_up)

    if (keys[K_LEFT] or keys[K_a]) and player_rect.left > 0:
        player_rect = player_rect.move(player_move_left)

    # to move enemies
    for enemy in enemies:
        enemy[1] = enemy[1].move(enemy[2])
        main_display.blit(enemy[0], enemy[1])

        if player_rect.colliderect(enemy[1]):
            print(f"We scored {score} points")
            playing = False

    # to move bonuses
    for bonus in bonuses:
        bonus[1] = bonus[1].move(bonus[2])
        main_display.blit(bonus[0], bonus[1])

        if player_rect.colliderect(bonus[1]):
            score += 1
            bonuses.pop(bonuses.index(bonus))

    # to put the objects on the screen
    main_display.blit(player, player_rect)
    main_display.blit(FONT.render(str(score), True, COLOR_OF_SCORE), (WIDTH - 50, 20))

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
