import pygame, sys, time
import random

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
cursorStart_X = 615
cursorStart_Y = 448

black = (0,0,0)
white = (255, 255, 255)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (4, 49, 89)
yellow = (255, 201, 15)

gameDisplay = pygame.display.set_mode((windowWidth, windowHeight))
pygame.display.set_caption('Digimon RPG')

titleFont = pygame.font.Font('Pixel Digivolve.otf', 35)
monsterFont = pygame.font.Font('Pixel Digivolve.otf', 15)

clock = pygame.time.Clock()

cursorImg = pygame.image.load("cursor.png")
backgroundImg1 = pygame.image.load("graphics/Meadow.png")
backgroundImg2 = pygame.image.load("graphics/Grassland.png")
playerImg = pygame.image.load("MetalGreymon_individual/MetalGreymon_stand1.png")
enemyImg = pygame.image.load("SkullGreymon_individual/SkullGreymon_stand1.png")
bulletImg = pygame.image.load("MetalGreymon_individual/projectile.png")
enemyBulletImg = pygame.image.load("SkullGreymon_individual/enemy_projectile.png")
attackSound = pygame.mixer.Sound("se_attack.wav")
pygame.mixer.music.load("Digimon_World_2-Boss_Battle_www.mp3")
pygame.mixer.music.play(-1)
battleFPS = 0

class Cursor():
    def __init__(self, xcor, ycor):
        self.location = 0
        self.xcor = xcor
        self.ycor = ycor
    def show(self):
        gameDisplay.blit(cursorImg, (self.xcor, self.ycor))
    def moveDown(self):
        self.location = 1
    def moveUp(self):
        self.location = -1
        
def isCollision(a, b):
    if a.xcor + a.width > b.xcor and a.xcor < b.xcor + b.width \
    and a.ycor + a.height > b.ycor and a.ycor < b.ycor + b.height:
        return True
    else:
        return False

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
        self.health = 100
        self.isAlive = True

    def show(self):
        gameDisplay.blit(playerImg, (self.xcor, self.ycor))
    def attacking(self):
        attackSound.play()
        newAttack = Attack(self.xcor + self.width / 2 - bulletImg.get_width() / 2, self.ycor, bulletImg, 17)
        attacks.append(newAttack)

class Enemy(Digimon):
    def __init__(self, xcor, ycor, health: int, attack: int, defense: int, image):
        super().__init__(xcor, ycor, health, attack, defense, image)
        self.level = 1
        self.health = 100
        self.isAlive = True

    def show(self):
        gameDisplay.blit(enemyImg, (self.xcor, self.ycor))
    def attacking(self):
        attackSound.play()
        newAttack = Attack(self.xcor + self.width / 2 - enemyBulletImg.get_width() / 2, self.ycor, enemyBulletImg, -17)
        enemyAttacks.append(newAttack)

class Attack:
    def __init__(self, xcor, ycor, image, speed):
        self.xcor = xcor
        self.ycor = ycor
        self.width = image.get_width()
        self.height = image.get_height()
        self.image = image
        self.speed = speed
    def show(self):
        gameDisplay.blit(self.image, (self.xcor, self.ycor))
    def move(self):
        self.xcor -= self.speed

enemy = Enemy(windowWidth / enemyImg.get_width() * 9, wallBottom - enemyImg.get_height() * 2, 100, 38, 14, enemyImg)
player = Player(windowWidth - playerImg.get_width() * 3, wallBottom - playerImg.get_height() * 2, 100, 29, 13, playerImg)

attacks = []
enemyAttacks = []

isRunning = True
isPlayerAttacking = False
menuSelect = False
attackAnimPlayer = False
isEnemyDamaged = False
isPlayerDamaged= False

hp_Disk_Count = 10

# MAIN LOOP
while isRunning:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            isRunning = False

    # Key commands
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_DOWN:
                if(cursorStart_Y == 528):
                    cursorStart_Y -= 80
                else:
                    cursorStart_Y += 40
            elif event.key == pygame.K_UP:
                if(cursorStart_Y == 448):
                    cursorStart_Y += 80
                else:
                    cursorStart_Y -= 40
            elif event.key == pygame.K_SPACE:
                if(cursorStart_Y == 448):
                    player.attacking()
                    cursorStart_Y = 0 
                    menuSelect = True
                    isPlayerAttacking = True
                    attackAnimPlayer = True
                    break
                elif(cursorStart_Y == 488):
                    player.health = 100
                    isPlayerAttacking = True
                    if (enemy.health <= 10):
                        enemy.attacking()
                    break
                else:
                    pass

    for attack in attacks:
        attack.move()

    for attack in attacks:
        if attack.xcor < wallLeft:
            try:
                attacks.remove(attack)
            except ValueError:
                pass
            break
        if isCollision(enemy, attack):
            try:
                enemy.health -= player.attack - enemy.defense
                cursorStart_Y = 448
                isEnemyDamaged = True
                enemy.attacking()
            except ValueError:
                pass
            try:
                attacks.remove(attack)
            except ValueError:
                pass
            break
        elif attack.xcor < wallTop:
            attacks.remove(attack)
            break

    for attack in enemyAttacks:
        attack.move()

    if(isPlayerAttacking == True):
        for attack in enemyAttacks:
            if attack.xcor > wallRight:
                try:
                    enemyAttacks.remove(attack)
                except ValueError:
                    pass
                break
            if isCollision(player, attack):
                try:
                    player.health -= enemy.attack - player.defense
                    cursorStart_Y = 448
                    isPlayerDamaged = True
                    isPlayerAttacking = False
                    menuSelect = False
                except ValueError:
                    pass
                try:
                    enemyAttacks.remove(attack)
                except ValueError:
                    pass
                break
            elif attack.xcor > wallRight:
                enemyAttacks.remove(attack)
                break
        
    # RENDER GRAPHICS
    gameDisplay.blit(gameDisplay, (0, 0))
    gameWidth = wallRight - wallLeft
    gameHeight = wallBottom - wallTop
    gameDisplay.fill((black))
    pygame.draw.rect(gameDisplay, blue, (gameSideMargin, 450, windowWidth, windowHeight - gameBottomMargin))
    damageTotalEnemy = titleFont.render(str(player.attack - enemy.defense), False, white)
    damageTotalPlayer = titleFont.render(str(enemy.attack - player.defense), False, white)

    gameDisplay.blit(backgroundImg1, (wallLeft, wallTop), (0, 0, gameWidth, gameHeight))
    gameDisplay.blit(backgroundImg2, (wallLeft, wallTop), (0, 0, gameWidth, gameHeight))

    if(menuSelect == False):
        titleText1 = titleFont.render('FIGHT', False, white)
        titleText2 = titleFont.render('ITEMS', False, white)
        titleText3 = titleFont.render('FLEE!!', False, white)
        gameDisplay.blit(titleText1, (675, 455, windowWidth, windowHeight - gameBottomMargin))
        gameDisplay.blit(titleText2, (675, 495, windowWidth, windowHeight - gameBottomMargin))
        gameDisplay.blit(titleText3, (675, 535, windowWidth, windowHeight - gameBottomMargin))
    
    # Move cursor
        gameDisplay.blit(cursorImg, (cursorStart_X, cursorStart_Y, windowWidth, windowHeight - gameBottomMargin))

    # Enemy Stats
    enemyHealth = monsterFont.render('SkullGreymon   lv: ' + str(enemy.level), False, white)
    gameDisplay.blit(enemyHealth, (5, 453, windowWidth - gameSideMargin * 2, windowHeight - gameBottomMargin))
    if(enemy.health >= 65):
        pygame.draw.rect(gameDisplay, white, (5, 473, 204, 14))
        pygame.draw.rect(gameDisplay, blue, (7, 475, 200, 10))
        pygame.draw.rect(gameDisplay, green, (7, 475, enemy.health * 2, 10))
    elif(enemy.health < 65 and enemy.health > 25):
        pygame.draw.rect(gameDisplay, white, (5, 473, 204, 14))
        pygame.draw.rect(gameDisplay, blue, (7, 475, 200, 10))
        pygame.draw.rect(gameDisplay, yellow, (7, 475, enemy.health * 2, 10))
    elif(enemy.health > 0 and enemy.health <= 25):
        pygame.draw.rect(gameDisplay, white, (5, 473, 204, 14))
        pygame.draw.rect(gameDisplay, blue, (7,475, 200, 10))
        pygame.draw.rect(gameDisplay, red, (7, 475, enemy.health * 2, 10))
    else:
        pygame.draw.rect(gameDisplay, white, (5, 473, 204, 14))
        pygame.draw.rect(gameDisplay, blue, (7, 475, 200, 10))

    # Player Stats
    playerHealth = monsterFont.render('MetalGreymon   lv: ' + str(player.level), False, white)
    gameDisplay.blit(playerHealth, (305, 453, windowWidth, windowHeight - gameBottomMargin))
    if(player.health >= 65):
        pygame.draw.rect(gameDisplay, white, (305, 473, 204, 14))
        pygame.draw.rect(gameDisplay, blue, (307, 475, 200, 10))
        pygame.draw.rect(gameDisplay, green, (307, 475, player.health * 2, 10))
    elif(player.health < 65 and player.health > 25):
        pygame.draw.rect(gameDisplay, white, (305, 473, 204, 14))
        pygame.draw.rect(gameDisplay, blue, (307, 475, 200, 10))
        pygame.draw.rect(gameDisplay, yellow, (307, 475, player.health * 2, 10))
    elif(player.health >= 0 and player.health <= 25):
        pygame.draw.rect(gameDisplay, white, (305, 473, 204, 14))
        pygame.draw.rect(gameDisplay, blue, (307, 475, 200, 10))
        pygame.draw.rect(gameDisplay, red, (307, 475, player.health * 2, 10))
   
    # Battle Animations
    for attack in attacks:
        attack.show()

    for attack in enemyAttacks:
        attack.show()

    if(battleFPS <= 10):
        if(attackAnimPlayer == True):
            playerImg = pygame.image.load("MetalGreymon_individual/MetalGreymon_attack.png")
        else:
            playerImg = pygame.image.load("MetalGreymon_individual/MetalGreymon_stand1.png")
        if(isPlayerDamaged == True):
            gameDisplay.blit(damageTotalPlayer, (windowWidth / playerImg.get_width() * 49, wallBottom - playerImg.get_height() * 2.75))
            playerImg = pygame.image.load("MetalGreymon_individual/MetalGreymon_damage.png")
        player.show()
    elif(battleFPS >= 11):
        if(attackAnimPlayer == True):
            playerImg = pygame.image.load("MetalGreymon_individual/MetalGreymon_attack.png")
            if(player.health < 30):
                playerImg = pygame.image.load("MetalGreymon_individual/MetalGreymon_damage.png")
            attackAnimPlayer = False
        else:
            if(player.health < 30):
                playerImg = pygame.image.load("MetalGreymon_individual/MetalGreymon_damage.png")
            else:
                playerImg = pygame.image.load("MetalGreymon_individual/MetalGreymon_stand2.png")
        if(isPlayerDamaged == True):
            gameDisplay.blit(damageTotalPlayer, (windowWidth / playerImg.get_width() * 49, wallBottom - playerImg.get_height() * 2.75))
            playerImg = pygame.image.load("MetalGreymon_individual/MetalGreymon_damage.png")
        player.show()

    if(battleFPS <= 10):
        if(enemy.health <= 0):
            enemyImg = pygame.image.load("SkullGreymon_individual/SkullGreymon_damage.png")
            enemy.health = 0
        else:
            enemyImg = pygame.image.load("SkullGreymon_individual/SkullGreymon_stand1.png")
        if(isEnemyDamaged == True): 
            gameDisplay.blit(damageTotalEnemy, (windowWidth / enemyImg.get_width() * 9, wallBottom - enemyImg.get_height() * 2.75))
            enemyImg = pygame.image.load("SkullGreymon_individual/SkullGreymon_damage.png")
        enemy.show()
        battleFPS += 1
    elif(battleFPS >= 11):
        if(enemy.health < 30):
            enemyImg = pygame.image.load("SkullGreymon_individual/SkullGreymon_damage.png")
        else:
            enemyImg = pygame.image.load("SkullGreymon_individual/SkullGreymon_stand2.png")
        if(isEnemyDamaged == True):
            gameDisplay.blit(damageTotalEnemy, (windowWidth / enemyImg.get_width() * 9, wallBottom - enemyImg.get_height() * 2.75))
            enemyImg = pygame.image.load("SkullGreymon_individual/SkullGreymon_damage.png")
        if(battleFPS == 20 and isEnemyDamaged == True):
            enemyImg = pygame.image.load("SkullGreymon_individual/SkullGreymon_stand2.png") 
        enemy.show()
        battleFPS += 1
    if(battleFPS == 20):
        battleFPS = 0
        isEnemyDamaged = False
        isPlayerDamaged = False
    
    clock.tick(30)
    pygame.display.update()

pygame.quit