import pygame, sys, time

pygame.init()

windowWidth = 800
windowHeight = 600
gameSideMargin = 0
gameTopMargin = 0
gameBottomMargin = 150
gameBorderWidth = 0


wallTop = gameTopMargin + gameBorderWidth
wallLeft = gameSideMargin + gameBorderWidth
wallRight = windowWidth - gameSideMargin - gameBorderWidth
wallBottom = windowHeight - gameBottomMargin - gameBorderWidth


black = (0,0,0)
white = (255, 255, 255)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (4, 49, 89)

gameDisplay = pygame.display.set_mode((windowWidth, windowHeight))
pygame.display.set_caption('Digimon RPG')

titleFont = pygame.font.SysFont('Pixel Digivolve', 35, False)

clock = pygame.time.Clock()


backgroundImg1 = pygame.image.load("graphics/Meadow.png")
backgroundImg2 = pygame.image.load("graphics/Grassland.png")
playerImg = pygame.image.load("MetalGreymon_individual/MetalGreymon_stand1.png")
enemyImg = pygame.image.load("SkullGreymon_individual/SkullGreymon_stand1.png")
battleFPS = 0

class Cursor():
    def __init__(self, xcor, ycor)
        self.xcor = xcor
        self.ycor = ycor
    def show(self):
        


class Digimon:
    def __init__(self, xcor, ycor, health: int, attack: int, defense: int, image):
        self.xcor = xcor
        self.ycor = ycor
        self.health = health
        self.attack = attack
        self.defense = defense
        self.img = image
        self.width = image.get_width()
        self.height = image.get_height()
    def show(self):
        gameDisplay.blit(self.img, (self.xcor, self.ycor))

class Player(Digimon):
    def __init__(self, xcor, ycor, health: int, attack: int, defense: int, image):
        super().__init__(xcor, ycor, health, attack, defense, image)
        self.level = 1
        self.isAlive = True

    def show(self):
        gameDisplay.blit(playerImg, (self.xcor, self.ycor))

class Enemy(Digimon):
    def __init__(self, xcor, ycor, health: int, attack: int, defense: int, image):
        super().__init__(xcor, ycor, health, attack, defense, image)
        self.level = 1
        self.isAlive = True

    def show(self):
        gameDisplay.blit(enemyImg, (self.xcor, self.ycor))

enemy = Enemy(windowWidth / enemyImg.get_width() * 9, wallBottom - enemyImg.get_height() * 2, 100, 4, 4, enemyImg)
player = Player(windowWidth - playerImg.get_width() * 3, wallBottom - playerImg.get_height() * 2, 100, 5, 3, playerImg)


isRunning = True


# MAIN LOOP
while isRunning:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            isRunning = False

    # LOGIC

    # RENDER GRAPHICS
    gameDisplay.blit(gameDisplay, (0, 0))
    gameWidth = wallRight - wallLeft
    gameHeight = wallBottom - wallTop
    gameDisplay.fill((black))
    pygame.draw.rect(gameDisplay, blue, (gameSideMargin, (gameTopMargin + 450), windowWidth - gameSideMargin * 2, windowHeight - gameBottomMargin - gameTopMargin))

    gameDisplay.blit(backgroundImg1, (wallLeft, wallTop), (0, 0, gameWidth, gameHeight))
    gameDisplay.blit(backgroundImg2, (wallLeft, wallTop), (0, 0, gameWidth, gameHeight))
    titleText1 = titleFont.render('FIGHT', False, white)
    titleText2 = titleFont.render('ITEMS', False, white)
    titleText3 = titleFont.render('FLEE!!', False, white)
    gameDisplay.blit(titleText1, ((gameSideMargin + 675), (gameTopMargin + 455), windowWidth - gameSideMargin * 2, windowHeight - gameBottomMargin - gameTopMargin))
    gameDisplay.blit(titleText2, ((gameSideMargin + 675), (gameTopMargin + 495), windowWidth - gameSideMargin * 2, windowHeight - gameBottomMargin - gameTopMargin))
    gameDisplay.blit(titleText3, ((gameSideMargin + 675), (gameTopMargin + 535), windowWidth - gameSideMargin * 2, windowHeight - gameBottomMargin - gameTopMargin))
    
    # Battle
    if(battleFPS <= 10):
        playerImg = pygame.image.load("MetalGreymon_individual/MetalGreymon_stand1.png")
        enemyImg = pygame.image.load("SkullGreymon_individual/SkullGreymon_stand1.png")
        player.show()
        enemy.show()
        battleFPS += 1
    elif(battleFPS >= 11):
        playerImg = pygame.image.load("MetalGreymon_individual/MetalGreymon_stand2.png")
        enemyImg = pygame.image.load("SkullGreymon_individual/SkullGreymon_stand2.png")
        player.show()
        enemy.show()
        battleFPS += 1
        if(battleFPS == 20):
            battleFPS = 0
    
    clock.tick()
    pygame.display.update()


pygame.quit