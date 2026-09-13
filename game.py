import pygame

class Player: #player class for storing coordinates
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def move(self, direction: str, amount: int):
        """
        :param direction: ("up"/"down"/"left"/"right")
        :param amount: any integer value to move the object by
        :return: object with modified x/y values depending on it's direction and amount to move
        :Example:
        >>> player = Player(50,50)
        >>> player.move('up', 5)
        player.x = 50
        player.y = 55
        """

        match direction:
            case "up":
                if self.y - amount > 2 * screen.get_height()/65: # prevents ball from going past the edge
                    self.y -= amount #moves the player
            case "down":
                if self.y + amount < screen.get_height()/1.032:
                    self.y += amount
            case "left":
                if self.x - amount > 2 * screen.get_width()/65:
                    self.x -= amount
            case "right":
                if self.x + amount < screen.get_width()/1.032:
                    self.x += amount

pygame.init() #initialises pygame
screen = pygame.display.set_mode((1200, 1200)) #sets the screen to be 900x900px, code should adapt to different resolutions
running = True # initialises the game to start
clock = pygame.time.Clock() #creates a time object
dt=0
player = Player((screen.get_width()/2), (screen.get_height()/2))
box = (screen.get_width()/3.3,screen.get_height()/1.25,400,40)
rect1 = pygame.Rect(box)
while running:

    screen.fill("grey") #fill grey/clear others
    pygame.draw.circle(screen, "red", (player.x, player.y), 40) 
    pygame.draw.rect(screen, "black", box)
    #rect1 = pygame.Rect.inflate(2,2)

    for event in pygame.event.get():
        if event.type == pygame.QUIT: #user pressed the x button
            running = False #stop the game loop

    keys = pygame.key.get_pressed() #gets an object containing all keys and whether they are pressed or not (True / False)
    if keys[pygame.K_w]:
        player.move("up", 5)
    if keys[pygame.K_s]:
        player.move("down", 5)
    if keys[pygame.K_a]:
        player.move("left", 5)
    if keys[pygame.K_d]:
        player.move("right", 5)
    pygame.display.flip() # updates the screen

    dt = clock.tick(60) / 1000 #prevents visual tearing/sets an FPS limit to 60 - this game loop only executes 60 times a second
    print(f"{player.x=}, {player.y=}") # debugging

pygame.quit()
