import pygame

class Img:
    posX = 0
    posY = 0
    name = 0
    imgRoute = "images/"

    def setPos(self, posX, posY):
        self.posY = posY
        self.posX = posX

    def getPos(self):
        return (self.posX, self.posY)

    def setName(self, name):
        self.name = name

    def getImg(self):
        return pygame.image.load(self.imgRoute + str(self.name) + '.png')




