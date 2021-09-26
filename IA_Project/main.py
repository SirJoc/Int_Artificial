#import algorithm
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

arr = [[1,2,3],[4,5,6],[7,8,0]]
DIRECTIONS = {"U" : (-1, 0), "D": [1, 0], "L": [0, -1], "R": [0, 1]}
imagenes = [[], [], []]
def generarImg():
    posY = 0
    posX = 0
    for i in range(3):
        if i == 1:
            posY = 140
        elif i == 2:
            posY = 280

        for j in range(3):
            if j == 0:
                posX = 0
            elif j == 1:
                posX = 140
            elif j == 2:
                posX = 280

            obj = objects.Img()
            obj.setPos(posX, posY)

            obj.setName(arr[i][j])
            imagenes[i].append(obj)



#ejemplo screen.blit(squareImg, (imgX, imgY))

# GAME LOOP --> makes game function properly
running = True
generarImg()
print(imagenes)
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    # Background
    screen.fill((155, 155, 155))
    for i in range(3):
        for j in range(3):
            # para hacer el swap, solo se debe cambiar el name --> imagenes[i].setName(1)
            screen.blit(imagenes[i][j].getImg(), imagenes[i][j].getPos())

    # aqui se pone el proceso de dibujado
    pygame.display.update()