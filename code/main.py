from random import randint

import pygame

# general setip
pygame.init()
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600
display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
running = True
title = 'MyGame'
pygame.display.set_caption(title)

# surface
surf = pygame.Surface((100, 200))
surf.fill('green')
player_x = 100
player_y = 100

# Load player imag
player_surf = pygame.image.load('../resources/space shooter/images/player.png').convert_alpha()

#Load 20 star randomly
#generate a list with 20 random tuples
star_surf = pygame.image.load('../resources/space shooter/images/star.png').convert_alpha()
randomStarPositions = [(randint(0, WINDOW_WIDTH), randint(0, WINDOW_HEIGHT)) for i in range(20)]


while running:
    # event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # draw the game
    display_surface.fill('darkgrey')
    #draw stars
    for pos in randomStarPositions:
        display_surface.blit(star_surf, pos)
    # draw player
    display_surface.blit(player_surf, (player_x, player_y))

    pygame.display.update()

pygame.quit()