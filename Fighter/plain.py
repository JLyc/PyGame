import time

import pygame

pygame.init()
displayWidth = 800
displayHeight = 600

black = (30,30,30)
white = (255,255,255)

gameDisplay = pygame.display.set_mode((displayWidth, displayHeight))
pygame.display.set_caption("First Game")
clock = pygame.time.Clock()

fighterImg = pygame.image.load("fighter.png")
fighterImg = pygame.transform.scale(fighterImg, (50, 150))
# carOffImg = pygame.transform.rotate(carOffImg, 90)
carOnImg = pygame.image.load("carlight.png")
carOnImg = pygame.transform.scale(carOnImg, (50, 150))
# carOnImg = pygame.transform.rotate(carOnImg, 90)
fighterImg = fighterImg
day = white
daytime = 0

bullets = []

def fire(posX, posY):
    bullets.append((posX,posY))

def car(x,y):
    gameDisplay.blit(fighterImg, (x, y))


def text_objects(text, font):
    textSurface = font.render(text, True, black)
    return textSurface, textSurface.get_rect()

def message_display(text):
    largeText = pygame.font.Font('freesansbold.ttf',115)
    TextSurf, TextRect = text_objects(text, largeText)
    TextRect.center = ((displayWidth/2), (displayHeight/2))
    gameDisplay.blit(TextSurf, TextRect)

    pygame.display.update()
    time.sleep(2)

def crash():
    message_display("you crashed")


def game_loop():
    global fighterImg, day, daytime
    x = (displayHeight * 0.8)
    y = (displayWidth * 0.45)
    x_change = 0
    y_change = 0
    speed = 5
    crashed = False
    while not crashed:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                crashed = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_a:
                    x_change -= speed
                if event.key == pygame.K_d:
                    x_change += speed
                if event.key == pygame.K_w:
                    y_change -= speed
                if event.key == pygame.K_s:
                    y_change += speed
                if event.key == pygame.K_l:
                    currentCar = carOnImg
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_a or event.key == pygame.K_d:
                    x_change = 0
                if event.key == pygame.K_s or event.key == pygame.K_w:
                    y_change = 0
                if event.key == pygame.K_l:
                    currentCar = fighterImg

        x += x_change
        y += y_change
        daytime+=1
        if daytime==100:
            daytime = 0
            if day[0] == 255:
                day = black
            else:
                day = white
        gameDisplay.fill(day)
        if x > displayWidth-50 or x<0 or y > displayHeight-150 or y < -50:
            x_change = 0
            y_change = 0
            # crash()

            continue
        else:
            car(x, y)
        pygame.display.update()

        clock.tick(60)


game_loop()
pygame.quit()
quit()