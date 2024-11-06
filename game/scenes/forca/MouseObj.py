import pygame

from game.shared.handler.baseAsset import BaseAsset


class MouseObj(BaseAsset):
    def __init__(self):
        self.indice = 0
        self.x = None
        self.y = None

    def drawSelf(self, screen):
        self.x, self.y = pygame.mouse.get_pos()

        tamanho_quadrado = 30

        pygame.draw.rect(screen, (255, 0, 0), (
        self.x - tamanho_quadrado // 2, self.y - tamanho_quadrado // 2, tamanho_quadrado, tamanho_quadrado))
