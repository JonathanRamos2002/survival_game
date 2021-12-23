import pygame
import random

pygame.init()

# global variables for width, height, and creating the window
WIDTH = 800
HEIGHT = 600
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))

# rgb color options
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 255)

# caption and icon
pygame.display.set_caption('Survival Game Attempt')
icon = pygame.image.load('survival_game/ufo.png')
pygame.display.set_icon(icon)

# background
background = pygame.image.load('survival_game/starry-night-sky.jpg')

# player ship
player_img = pygame.image.load('survival_game/player_ship.png')
playerX = 370 
playerY = 480
playerX_change = 0
playerY_change = 0 

# enemy ship
enemy_img = pygame.image.load('survival_game/enemy_ship.png')
enemy_img = pygame.transform.smoothscale(enemy_img, (44, 44))
enemy_img = pygame.transform.rotate(enemy_img, 180)
enemyX = random.randint(0, 756)
enemyY = random.randint(25, 150)
enemyX_change = 2
enemyY_change = 20


def player(x, y):
    SCREEN.blit(player_img, (x, y))


def enemy(x, y):
    SCREEN.blit(enemy_img, (x, y))


is_running = True
while is_running:
    SCREEN.fill(BLACK)
    SCREEN.blit(background, (0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            is_running = False

        # movement
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                playerX_change = -3
            if event.key == pygame.K_RIGHT:
                playerX_change = 3
            if event.key == pygame.K_UP:
                playerY_change = -3
            if event.key == pygame.K_DOWN:
                playerY_change = 3
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                playerX_change = 0
            if event.key == pygame.K_DOWN or event.key == pygame.K_UP:
                playerY_change = 0
            
    # player movment
    playerX += playerX_change
    playerY += playerY_change

    # horizontal borders (left and right)
    if playerX <= 0:
        playerX = 0 
    elif playerX >= 736:
        playerX = 736

    # vertical borders (up and down)
    if playerY <= 0:
        playerY = 0
    elif playerY >= 536:
        playerY = 536

    # enemy movement
    enemyX += enemyX_change
    
    # horizontal borders and change movement
    if enemyX <= 0:
        enemyX_change = 2 
        enemyY += enemyY_change
    elif enemyX >= 756:
        enemyX_change = -2
        enemyY += enemyY_change


    player(playerX, playerY)
    enemy(enemyX, enemyY)
    pygame.display.update()

pygame.quit()