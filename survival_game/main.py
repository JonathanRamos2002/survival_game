import pygame

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

# player
player_img = pygame.image.load('survival_game/player_ship.png')
playerX = 370 
playerY = 480
playerX_change = 0
playerY_change = 0 

def player(x, y):
    SCREEN.blit(player_img, (x, y))


is_running = True
while is_running:
    SCREEN.fill(BLACK)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            is_running = False

        # movement
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                playerX_change = -0.2
            if event.key == pygame.K_RIGHT:
                playerX_change = 0.2
            if event.key == pygame.K_UP:
                playerY_change = -0.2
            if event.key == pygame.K_DOWN:
                playerY_change = 0.2
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                playerX_change = 0
            if event.key == pygame.K_DOWN or event.key == pygame.K_UP:
                playerY_change = 0
            
    
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

    player(playerX, playerY)
    pygame.display.update()

pygame.quit()