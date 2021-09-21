import algorithm
import pygame

# initialize the pygame
pygame.init()

# create the screen
icon = pygame.image.load('images/menu.png')
screen = pygame.display.set_mode((800, 600))

# Title and Icon
pygame.display.set_caption("8 puzzles")
pygame.display.set_icon(icon)



# GAME LOOP --> makes game function properly
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    # Background
    screen.fill((0, 155, 0))
    pygame.display.update()