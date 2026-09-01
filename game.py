from importlib.util import source_hash
from traceback import format_list

import pygame

pygame.init()

SCREEN_WIDTH = 1600
SCREEN_HEIGHT = 1200
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

player = pygame.Rect((300, 250, 50, 50)) # x coord, y coord, width, height



run = True
while run: #  GAME LOOP
    pygame.draw.rect(screen, (255, 0, 0), player)

    key = pygame.key.get_pressed()
    if key[pygame.K_a]: # format is K_<KEY>
        player.move_ip(-1, 0) # move in place
    elif key[pygame.K_d]: # format is K_<KEY>
        player.move_ip(1, 0) # move in place
    elif key[pygame.K_w]: # format is K_<KEY>
        player.move_ip(0, -1) # move in place
    elif key[pygame.K_s]: # format is K_<KEY>
        player.move_ip(0, 1) # move in place

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    pygame.display.update()
pygame.quit()

