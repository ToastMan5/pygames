from importlib.util import source_hash
from traceback import format_list

import pygame

pygame.init()

SCREEN_WIDTH = 1600
SCREEN_HEIGHT = 1200
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

rectangleThing = pygame.Rect((300, 250, 50, 50)) # x coord, y coord, width, height

class Player:
    def __init__(self, health: int, lvl: int, xp: float):
        self.health = health
        self.lvl = lvl
        self.xp = xp

mario = Player(10,1,0)

print(f"{1 + 1 = }  ")


run = False
while run: #  GAME LOOP
    screen.fill((0,0,0))

    pygame.draw.rect(screen, (255, 0, 0), rectangleThing)

    key = pygame.key.get_pressed()
    if key[pygame.K_a]: # format is K_<KEY>
        rectangleThing.move_ip(-1, 0) # move in place (left)
    elif key[pygame.K_d]:
        rectangleThing.move_ip(1, 0) # move right
    elif key[pygame.K_w]:
        rectangleThing.move_ip(0, -1) # move up
    elif key[pygame.K_s]:
        rectangleThing.move_ip(0, 1) # move down


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    pygame.display.update()
pygame.quit()

