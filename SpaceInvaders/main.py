import pygame
import random
import math
from pygame import mixer


# Initialize the pygame
pygame.init()

# Background Music
mixer.music.load('background.wav')
mixer.music.play(-1)

screenwidth = 800
screenheight = 600
# create the screen
screen = pygame.display.set_mode((screenwidth, screenheight))

#  Changing title and icon
pygame.display.set_caption('Space Invaders')
icon = pygame.image.load('icon.png')
pygame.display.set_icon(icon)

# Background
background = pygame.image.load('background.jpg')
# Player
playerImg = pygame.image.load('spaceship.png')
playerX = 370
playerY = 480
playerX_Change = 0
playerY_Change = 0

# bullets
bulletImg = pygame.image.load('bullet.png')
bulletX = 0
bulletY = 480
bulletX_change = 0
bulletY_change = 7
bullet_State = 'ready'

enemyImg = []
enemyX = []
enemyY = []
enemyX_Change = []
enemyY_Change = []
# Enemy
num_of_enemies = 6
for i in range(num_of_enemies):
    enemyImg.append(pygame.image.load('monsters'+str(i)+'.png'))
    enemyX.append(random.randint(0, 736))
    enemyY.append(random.randint(0, 64))
    enemyX_Change.append(5)
    enemyY_Change.append(40)

score_value = 0
scoreX = 10
scoreY = 20

font = pygame.font.Font('Caramel Candy .ttf',32)

def show_score(x, y):
    score = font.render('Score : ' + str(score_value), True, (255,255,255))
    screen.blit(score, (x, y))

def collision(enemyX, enemyY, bulletX, bulletY):
    distance = math.sqrt(pow(bulletX - enemyX,2) + pow(bulletY - enemyY,2))
    if distance < 27:
        return True
    else:
        return False

def player(x, y):
    # blit meaning drawing the player on the screen
    screen.blit(playerImg,(x, y))

def enemy(x,y,i):
    screen.blit(enemyImg[i],(x,y))

def fire_bullet(x,y):
    global bullet_State
    bullet_State = 'fire'
    screen.blit(bulletImg, (x + 16, y + 10))


running = True
while True:
    # changing the screen color and updating the display each time
    screen.fill((0, 0, 0))
    screen.blit(background, (0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                playerX_Change = -5
            if event.key == pygame.K_RIGHT:
                playerX_Change = 5

            if event.key == pygame.K_SPACE:
                if bullet_State is 'ready':
                    bullet_sound = mixer.Sound('laser.wav')
                    bullet_sound.play()
                    bulletX = playerX
                    fire_bullet(bulletX, bulletY)

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT or event.key == pygame.K_LEFT:
                playerX_Change = 0

    # player boundaries restriction
    playerX += playerX_Change

    if playerX <= 0:
        playerX = 0
    elif playerX >= 736:
        playerX = 736

        # enemy boundaries restriction
    for i in range(num_of_enemies):
        enemyX[i] += enemyX_Change[i]
        if enemyX[i] <= 0:
            enemyX_Change[i] = 5
            enemyY[i] += enemyY_Change[i]

        elif enemyX[i] >= 736:
            enemyX_Change[i] = -5
            enemyY[i] += enemyY_Change[i]

        collide = collision(enemyX[i], enemyY[i], bulletX, bulletY)
        if collide:
            bulletY = 480
            bullet_State = 'ready'
            explosion_sound = mixer.Sound('explosion.wav')
            explosion_sound.play()
            score_value += 1
            enemyX[i] = random.randint(0, 735)
            enemyY[i] = random.randint(0, 64)

        enemy(enemyX[i], enemyY[i], i)

    if bulletY <= 0:
        bulletY = 480
        bullet_State = 'ready'

    # bullet movement
    if bullet_State is 'fire':
        fire_bullet(bulletX, bulletY)
        bulletY -= bulletY_change


    playerY += playerY_Change

    show_score(scoreX, scoreY)

    player(playerX, playerY)
    pygame.display.update()


pygame.quit()

