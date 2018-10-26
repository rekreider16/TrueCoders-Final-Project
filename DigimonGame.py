import pygame, sys


windowWidth = 650
windowHeight = 500
gameSideMargin = 1
gameTopMargin = 30
gameBottomMargin = 25
gameBorderWidth = 3

wallTop = gameTopMargin + gameBorderWidth
wallLeft = gameSideMargin + gameBorderWidth
wallRight = windowWidth - gameSideMargin - gameBorderWidth
wallBottom = windowHeight - gameBottomMargin - gameBorderWidth

black = (0,0,0)
white = (255, 255, 255)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)

pygame.init()

gameDisplay = pygame.display.set_mode((windowWidth, windowHeight))
pygame.display.set_caption('Digimon RPG')

titleFont = pygame.font.SysFont('Pixel Digivolve', 25, False)

clock = pygame.time.Clock()

playerImg = pygame.image.load("MetalGreymon_stand1.png")

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

player = Digimon(windowWidth / 2 - playerImg.get_width() / 2, wallBottom - playerImg.get_height(), playerImg)

while player.isAlive:

    titleText = titleFont.render('DIGIMON RPG', False, white)
    gameDisplay.blit(titleText, (windowWidth / 2 - titleText.get_width() / 2, 0))

    player.show()
    
    pygame.display.update()

    clock.tick(60)


pygame.quit