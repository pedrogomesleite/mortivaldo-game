import pygame

from game.shared.handler.baseAsset import BaseAsset


class MouseObj(BaseAsset):
    def __init__(self, folder):
        super().__init__()
        self.loadAnimation(folder)

    def drawSelf(self, screen):
        self.x, self.y = pygame.mouse.get_pos()
        self.animation(screen)
