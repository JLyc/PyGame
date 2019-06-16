import random
import time

import pygame

pygame.init()
displayWidth = 800
displayHeight = 600

black = (30, 30, 30)
white = (255, 255, 255)
green = (0, 155, 0)
greenDark = (100, 255, 100)

gameDisplay = pygame.display.set_mode((displayWidth, displayHeight))
pygame.display.set_caption("First Game")
clock = pygame.time.Clock()

round = "round"
missile = pygame.image.load("missile.png")
missile = pygame.transform.scale(missile, (10, 20))
explosion = pygame.image.load("explosion.png")
explosion = pygame.transform.scale(explosion, (100, 100))
fighterImgOrg = pygame.image.load("fighter.png")
fighterSizeW = 100
fighterSizeH = 100
fighterImg = pygame.transform.scale(fighterImgOrg, (fighterSizeW, fighterSizeH))

day = green
daytime = 0

bullets = []
objects = []

fighterX = (displayHeight * 0.8)
fighterY = (displayWidth * 0.45)
range = 250

def fire(posX, posY, ammoType):
    bullets.append([posX, posY, ammoType])


def fighter(x, y):
    gameDisplay.blit(fighterImg, (x, y))
    pygame.draw.rect(gameDisplay, (0,0,0), [x + fighterSizeH/2.65, y +((fighterSizeW/2)) - range - fighterSizeH/2.65, (fighterSizeW/4)+2, 2])
    pygame.draw.rect(gameDisplay, (0,0,0), [x+ ((fighterSizeW/2)), y - range, 2, (fighterSizeH/4)+2])


def text_objects(text, font):
    textSurface = font.render(text, True, black)
    return textSurface, textSurface.get_rect()


def message_display(text):
    largeText = pygame.font.Font('freesansbold.ttf', 115)
    TextSurf, TextRect = text_objects(text, largeText)
    TextRect.center = ((displayWidth / 2), (displayHeight / 2))
    gameDisplay.blit(TextSurf, TextRect)

    pygame.display.update()
    time.sleep(2)


def crash():
    message_display("you crashed")


def fly(bullet):
    speedMissile = 10
    speedRound = 20
    if bullet[1] < fighterY+(fighterSizeH/4) - range:
        if bullet[2] == missile:
            gameDisplay.blit(explosion, (bullet[0] - 50, bullet[1]-25))
            objects.append([bullet[0] - 25, bullet[1]-25, "ground", random.randrange(15, 30), random.randrange(20, 30)])
        else:
            objects.append([bullet[0] + random.randrange(-2, 2), bullet[1], "ground", random.randrange(1, 5), random.randrange(1, 5)])
        return True
    else:
        if bullet[2] == missile:
            bullet[1] -= speedMissile
            gameDisplay.blit(missile, (bullet[0], bullet[1]))
        else:
            bullet[1] -= speedRound
            pygame.draw.rect(gameDisplay, black, [bullet[0], bullet[1], 1, 3])
            # gameDisplay.blit(missile, (bullet[0], bullet[1]))
        return False


def spawnObject(objectTerrain):
    preGenX = (displayWidth + 600) - random.randrange(-600, (displayWidth + 600))
    preGenY = int(-600)
    if objectTerrain < 65:
        return [preGenX, preGenY, "tree", random.randrange(15, 30), random.randrange(20, 30)]
    elif objectTerrain < 66:
        return [preGenX, preGenY, "lake", random.randrange(200, 500), random.randrange(200, 500)]
    elif objectTerrain < 68:
        return [preGenX, preGenY, "hause", random.randrange(50, 250), random.randrange(50, 250)]
    elif objectTerrain < 70:
        return [preGenX, preGenY, "rock", random.randrange(20, 50), random.randrange(20, 50)]
    else:
        return False

0
def terrain(chance):
    if chance < 90:
        item = spawnObject(random.randrange(0,100))
        if item:
            objects.append(item)


def drawObject(objectThing):
    fighterSpeedY = int((displayHeight-fighterY)*0.01)
    objectThing[1] += fighterSpeedY
    fighterSpeedX = int((displayWidth/2 - fighterX) * 0.01)
    objectThing[0] += fighterSpeedX
    if objectThing[1] > displayWidth+600:
        return True
    if objectThing[2] == "tree":
        pygame.draw.circle(gameDisplay, (0, 100, 0), [objectThing[0], objectThing[1]],objectThing[3])
    elif objectThing[2] == "lake":
        pygame.draw.ellipse(gameDisplay, (0, 0, 200), [objectThing[0], objectThing[1], objectThing[3], objectThing[4]])
    elif objectThing[2] == "hause":
        pygame.draw.rect(gameDisplay, (100,0,0), [objectThing[0], objectThing[1], objectThing[3], objectThing[4]])
    elif objectThing[2] == "rock":
        pygame.draw.ellipse(gameDisplay, (50, 50, 50), [objectThing[0], objectThing[1], objectThing[3], objectThing[4]])
    elif objectThing[2] == "ground":
        pygame.draw.ellipse(gameDisplay, (126, 72, 15), [objectThing[0], objectThing[1], objectThing[3]*2, objectThing[4]*2])
        pygame.draw.ellipse(gameDisplay, (100, 50, 5), [objectThing[0]+(objectThing[3]/2), objectThing[1]+(objectThing[4]/2), objectThing[3], objectThing[4]])
    else:
        True





def game_loop():
    global fighterImg, day, daytime, fighterX, fighterY, fighterImg

    x_change = 0
    y_change = 0
    speed = 5
    crashed = False
    side = 25
    cannonSpace = 0
    delay = 0

    while not crashed:
        gameDisplay.fill(day)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                crashed = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_a:
                    x_change -= speed
                    fighterImg = pygame.transform.scale(fighterImgOrg, (85, 100))
                    cannonSpace = 13
                if event.key == pygame.K_d:
                    x_change += speed
                    fighterImg = pygame.transform.scale(fighterImgOrg, (85, 100))
                    cannonSpace = 13
                if event.key == pygame.K_w:
                    y_change -= speed
                if event.key == pygame.K_s:
                    y_change += speed
                if event.key == pygame.K_l:
                    if side == 25:
                        side = 65 - cannonSpace
                    else:
                        side = 25
                    pygame.draw.ellipse(gameDisplay, (200, 200, 10),
                                        [fighterX + side, fighterY + 70,
                                         5, 15])
                    fire(fighterX + side, fighterY + 50, missile)
                if event.key == pygame.K_k:
                    delay = 1
                if event.key == pygame.K_j:
                    delay = 2
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_a or event.key == pygame.K_d:
                    fighterImg = pygame.transform.scale(fighterImgOrg, (100, 100))
                    cannonSpace = 0
                    x_change = 0
                if event.key == pygame.K_s or event.key == pygame.K_w:
                    y_change = 0
                if event.key == pygame.K_k:
                    delay = -1
                if event.key == pygame.K_j:
                    delay = 0
        delay = cannon(delay, fighterX, fighterY, cannonSpace)
        terrain(random.randrange(0,1000))
        fighterX += x_change
        fighterY += y_change
        for objectThing in objects:
            if drawObject(objectThing):
                objects.remove(objectThing)
        for bullet in bullets:
            if fly(bullet):
                bullets.remove(bullet)

        if fighterX > displayWidth - 50 or fighterX < 0 or fighterY > displayHeight - 150 or fighterY < -50:
            x_change = 0
            y_change = 0
            # crash()
            continue
        else:
            fighter(fighterX, fighterY)
        pygame.display.update()

        clock.tick(60)


def cannon(delay, x, y, cannonSpace):
    if delay == 1:
        fire(x + 50-cannonSpace/2, y + 20 - random.randrange(0, 30), round)
        pygame.draw.ellipse(gameDisplay, (200, 200, 10),
                            [x-1 + 50-cannonSpace/2, y+2,
                             3, 5])
    elif delay == 2:
        fire(x + 78-cannonSpace, y + 85 - random.randrange(0, 15), round)
        pygame.draw.ellipse(gameDisplay, (200, 200, 10),
                            [x + 78-cannonSpace, y+50,
                             3, 5])
        fire(x + 20, y + 85 - random.randrange(0, 15), round)
        pygame.draw.ellipse(gameDisplay, (200, 200, 10),
                            [x + 20, y+50,
                             3, 5])
    else:
        pass
    return delay


game_loop()
pygame.quit()
quit()
