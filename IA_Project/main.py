import algorithm
import objects
import pygame

# initialize the pygame
pygame.init()

# create the screen
icon = pygame.image.load('images/menu.png')
screen = pygame.display.set_mode((420, 420))

# Title and Icon
pygame.display.set_caption("8 puzzles")
pygame.display.set_icon(icon)

arr = []
for i in range(9):
    arr.append(i)

imagenes = []
posY = 0
posX = 0

for i in range(9):
    if i < 3:
        posY = 0
        posX += 140
    elif i < 6:
        posY = 140
        posX += 140
    else:
        posY = 280
        posX += 140

    if i == 0 or i == 3 or i == 6:
        posX = 0

    obj = objects.Img()
    obj.setPos(posX, posY)
    obj.setName(arr[i])
    imagenes.append(obj)

#ejemplo screen.blit(squareImg, (imgX, imgY))

# GAME LOOP --> makes game function properly
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    # Background
    screen.fill((155, 155, 155))
    for i in range(9):
        screen.blit(imagenes[i].getImg(), imagenes[i].getPos())
    # aqui se pone el proceso de dibujado
    pygame.display.update()