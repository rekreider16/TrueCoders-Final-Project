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

titleFont = pygame.font.SysFont('Pixel Digivolve', 25, False)

clock = pygame.time.Clock()


index = 0


backgroundImg1 = pygame.image.load("graphics/Meadow.png")
backgroundImg2 = pygame.image.load("graphics/Grassland.png")
playerImg = pygame.image.load("MetalGreymon_sheet.png")

class GameObject:
    def __init__(self, xcor, ycor, image):
        self.xcor = xcor
        self.ycor = ycor
        self.img = image
        self.width = image.get_width()
        self.height = image.get_height()
    def show(self):
        gameDisplay.blit(self.img, (self.xcor, self.ycor))

class Digimon(GameObject):
    def __init__(self, xcor, ycor, image):
        super().__init__(xcor, ycor, image)
        self.level = 0
        self.isAlive = True

    def show(self):
        gameDisplay.blit(playerImg, (self.xcor, self.ycor))

class obj_Spritesheet:
    def __init__(self, file_name):
        self.sprite_sheet = pygame.image.load(file_name).conver()
        self.tiledicts = {'a': 1, 'b': 2, 'c': 3, 'd': 4}

    def get_image(self, column, row, width = 64, height = 64, scale = None):
        image = pygame.surface([width, height]).conver()
        image.blit(self.sprite_sheet, (0, 0), (self.tiledict[column]*width, row*height, width, height))
        
    

#ss = spritesheet('MetalGreymon_sheet.png',4,1)
player = Digimon(windowWidth / 2 - playerImg.get_width() / 2, wallBottom - playerImg.get_height(), playerImg)

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
    
    player.show()
    # animate sprites
    
    
    clock.tick()
    pygame.display.update()


pygame.quit