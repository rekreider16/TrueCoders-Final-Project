import pygame, sys, time
#import spritesheet
from SpritesheetAnim import SpriteStripAnim

pygame.init()

windowWidth = 800
windowHeight = 600
gameSideMargin = 0
gameTopMargin = 0
gameBottomMargin = 150
gameBorderWidth = 0

AREA = windowWidth * windowHeight


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



CENTER_HANDLE = 0

index = 0


backgroundImg1 = pygame.image.load("graphics/Meadow.png")
backgroundImg2 = pygame.image.load("graphics/Grassland.png")
playerImg = pygame.image.load("MetalGreymon_stand1.png")
menuBorder = pygame.image.load("graphics/menuBorder.gif")
menuBorder = pygame.transform.scale(menuBorder, (800, 150))

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
        self.direction = 0
        self.score = 0
        self.level = 0
        self.isAlive = True

    def show(self):
        gameDisplay.blit(playerImg, (self.xcor, self.ycor))

class spritesheet:
    def __init__(self, filename, cols, rows):
        self.sheet = pygame.image.load(filename)

        self.cols = cols
        self.rows = rows
        self.totalCellCount = cols*rows

        self.rect = self.sheet.get_rect()
        w = self.cellWidth = self.rect.width / cols
        h = self.cellHeight = self.rect.height / rows
        hw, hh = self.cellCenter = (w / 2, h / 2)

        self.cells = list([(index % cols * w, index / cols * h)for index in range(self.totalCellCount)])
        self.handle = list([(0, 0), (-hw, 0), (-w, 0), (0, -hh), (-hw, -hh), (-w, -hh), (0, -h), (-hw, -h), (-w, -h)])

    def draw(self, surface, cellIndex, x, y, handle = 0):
        surface.blit(self.sheet, (x + self.handle[handle][0], y + self.handle[handle][1]))
ss = spritesheet('MetalGreymon_sheet.png',4,1)
player = Digimon(windowWidth / 2 - playerImg.get_width() / 2, wallBottom - playerImg.get_height(), playerImg)

isRunning = True


# MAIN LOOP
while isRunning:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            isRunning = False

    #LOGIC

    # RENDER GRAPHICS
    gameDisplay.blit(gameDisplay, (0, 0))
    gameWidth = wallRight - wallLeft
    gameHeight = wallBottom - wallTop
    gameDisplay.fill((black))
    pygame.draw.rect(gameDisplay, blue, (gameSideMargin, (gameTopMargin + 450), windowWidth - gameSideMargin * 2, windowHeight - gameBottomMargin - gameTopMargin))

    gameDisplay.blit(backgroundImg1, (wallLeft, wallTop), (0, 0, gameWidth, gameHeight))
    gameDisplay.blit(backgroundImg2, (wallLeft, wallTop), (0, 0, gameWidth, gameHeight))
    gameDisplay.blit(menuBorder, (wallLeft, wallTop + 450), (0, 0, gameWidth, gameHeight))

    # animate sprites
    ss.draw(gameDisplay, index % ss.totalCellCount, windowWidth / 2, windowHeight / 2, CENTER_HANDLE)
    index += 1

    pygame.draw.circle(gameDisplay, white, ((windowWidth // 2), (windowHeight // 2)), 2, 0)

    
    clock.tick()
    pygame.display.update()


pygame.quit