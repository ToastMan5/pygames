import pygame


pygame.init() #initialises pygame
screen = pygame.display.set_mode((900, 900))
running = True
clock = pygame.time.Clock()
dt=0

player_pos = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)
box = (screen.get_width()/3.3,screen.get_height()/1.25,400,40)
while running:

    screen.fill("grey") #fill white/clear others
    pygame.draw.circle(screen, "red", player_pos, 40)
    pygame.draw.rect(screen, "black", box)


    for event in pygame.event.get():
        if event.type == pygame.QUIT: #user pressed the x button
            running = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        if player_pos.y - 5 < pygame.Vector2(screen.get_width(), screen.get_height())[1] * 0.04:
            pass
        else:
            player_pos.y -= 5
    if keys[pygame.K_s]:
        if player_pos.y + 5 > pygame.Vector2(screen.get_width(), screen.get_height())[1] * 0.935:
            pass
        else:
            player_pos.y += 5
    if keys[pygame.K_a]:
        if player_pos.x - 5 < pygame.Vector2(screen.get_width(), screen.get_height())[0] * 0.05:
            pass
        else:
            player_pos.x -= 5
    if keys[pygame.K_d]:
        if player_pos.x + 5 > pygame.Vector2(screen.get_width(), screen.get_height())[0] * 0.95:
            pass
        else:
            player_pos.x += 5
    pygame.display.flip() # flip() the display to put your work on screen

    dt = clock.tick(60) / 1000
    print(f"X{player_pos.y=}")
    print(f"y{player_pos.x=}")


pygame.quit()
