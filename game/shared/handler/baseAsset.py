import pygame

from game.shared.handler.loadHandler import loadAllSpritesFromDirectory, loadSprite


class BaseAsset:

    def __init__(self):
        self.tick = 0
        self.x = 0
        self.y = 0
        self.indice = 0
        self.sprite = pygame.surface.Surface((0, 0))
        self.sprites = []
        self.vel = 5

    def drawSelf(self, screen):
        # TODO: desenhar a si mesmo com heraça
        return

    def animation(self, screen):
        self.tick += 1
        if self.tick == 60:
            self.tick = 0
        if self.indice == len(self.sprites) - 1:
            self.indice = 0
        elif self.tick % self.vel == 0:
            self.indice += 1
        screen.blit(self.sprites[self.indice], (self.x, self.y))

    def animationOnce(self, screen):
        self.tick += 1
        if self.tick == 60:
            self.tick = 0
        if self.indice == len(self.sprites) - 1:
            if self.sprite != self.sprites[-1]:
                self.sprite = self.sprites[-1]
            self.static(screen)
            return
        elif self.tick % self.vel == 0:
            self.indice += 1
        screen.blit(self.sprites[self.indice], (self.x, self.y))

    def static(self, screen):
        screen.blit(self.sprite, (self.x, self.y))

    def loadStatic(self, filename, filefolder=""):
        self.sprite = loadSprite(file_name=filename, folder_name=filefolder)
    def loadAnimation(self, folder = ""):
        self.sprites = loadAllSpritesFromDirectory(folder)

# TODO: herança para desenhar a si mesmo como estático ou animação