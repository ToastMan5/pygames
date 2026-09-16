from typing import reveal_type

import pygame # allows the pygame program to be used
pygame.init() # starts pygame
screen = pygame.display.set_mode((750,750)) # sets the size of the game screen
posX = 375 # sets x position of rectangle
posY = 375 # sets y position of rectangle
On = True
clock = pygame.time.Clock()
dt = 0 # =allows the frames of the screen to be set


def move(direction, magnitude, pos):
    if direction == "^":
        if pos - magnitude > 0:
            return pos - magnitude # only allows the rectangle to move up if not going through edge of screen
        else:
            return pos
    if direction == "v":
        if pos + magnitude < 650:
            return pos + magnitude # only allows the rectangle to move down if not going through edge of screen
        else:
            return pos
    if direction == "<":
        if pos - magnitude > 0:
            return pos - magnitude # only allows the rectangle to move left if not going through edge of screen
        else:
            return pos
    if direction == ">":
        if pos + magnitude < 650:
            return pos + magnitude # only allows the rectangle to move right if not going through edge of screen
        else:
            return pos


while On:
    screen.fill("blue") #sets the screen colour as blue to be the sea
    pygame.draw.rect(screen, "yellow", (000,550,750,200)) #background sand
    pygame.draw.rect(screen, "red", (500,600,50,50)) # background gem
    pygame.draw.rect(screen, "cyan", (300,650,40,30)) # background gem
    pygame.draw.rect(screen, "cyan", (400,670,40,30)) # background gem
    pygame.draw.rect(screen, "green", (100,600,70,50)) # background gem
    pygame.draw.rect(screen, "purple", (600,680,90,40)) # background gem
    pygame.draw.rect(screen, "white", (50,50,150,50)) # background cloud
    pygame.draw.rect(screen, "white", (250,50,150,50)) # background cloud
    pygame.draw.rect(screen, "white", (460,50,80,40)) # background cloud
    pygame.draw.rect(screen, "white", (600,60,90,50)) # background cloud
    pygame.draw.rect(screen, "orange", (posX,posY,80,80)) # creates the movable rectangle object, sets the colour to red and determines its size and position
    keys = pygame.key.get_pressed() # allows the keyboard to be used
    for event in pygame.event.get():
        if event.type == pygame.QUIT: # allows the user to quit the game
            On = False
    keys = pygame.key.get_pressed() # allows the keyboard to be used
    if keys[pygame.K_w] == True: # sets the w key to be used
        posY = move("^", 4, posY)
    if keys[pygame.K_s] == True: # sets the s key to be used
        posY = move("v", 4, posY)
    if keys[pygame.K_a] == True: # sets the a key to be used
        posX = move("<", 4, posX)
    if keys[pygame.K_d] == True: # sets the d key to be used
        posX = move(">", 4, posX)
    pygame.display.flip() # allows the screen to be seen
    dt = clock.tick(60) / 1000 #sets the framerate at 60 so that the rectangle's movement is smoother
pygame.quit() # closes pygame

