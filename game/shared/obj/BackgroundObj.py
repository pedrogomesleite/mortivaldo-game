import pygame

from game.shared.handler.baseAsset import BaseAsset
from game.shared.settings import SETTINGS


class BackgroundObj(BaseAsset):
    def __init__(self, filename, folder):
        super().__init__()
        self.loadStatic(filename, folder)

    def drawSelf(self, screen):
        self.static(screen)

    def transform(self, screen):
        pygame.transform.scale_by(self.sprite, 1.1, self.sprite)
